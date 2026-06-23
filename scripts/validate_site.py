import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.fragment_links = []
        self.local_resources = []
        self.images = []
        self.faq_count = 0
        self.in_faq = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.append(attributes["id"])
        href = attributes.get("href", "")
        if href.startswith("#"):
            self.fragment_links.append(href[1:])
        if tag in {"img", "script", "link"}:
            resource = attributes.get("src") or attributes.get("href")
            if resource and not resource.startswith(("http://", "https://", "data:")):
                self.local_resources.append(resource)
        if tag == "img":
            self.images.append(attributes)
            for item in attributes.get("srcset", "").split(","):
                source = item.strip().split(" ")[0]
                if source:
                    self.local_resources.append(source)
        if tag == "section" and attributes.get("id") == "preguntas":
            self.in_faq = True
        if tag == "details" and self.in_faq:
            self.faq_count += 1

    def handle_endtag(self, tag):
        if tag == "section" and self.in_faq:
            self.in_faq = False


def require(condition, message, failures):
    if not condition:
        failures.append(message)


html = (ROOT / "index.html").read_text(encoding="utf-8")
css = (ROOT / "styles.css").read_text(encoding="utf-8")
script = (ROOT / "script.js").read_text(encoding="utf-8")
parser = SiteParser()
parser.feed(html)
failures = []

require(len(parser.ids) == len(set(parser.ids)), "Hay identificadores HTML duplicados.", failures)
require(not (set(parser.fragment_links) - set(parser.ids)), "Hay enlaces internos sin destino.", failures)
require(parser.faq_count == 10, "La sección FAQ no contiene diez preguntas.", failures)

missing_resources = [resource for resource in parser.local_resources if not (ROOT / resource).exists()]
require(not missing_resources, f"Faltan recursos locales: {missing_resources}", failures)

images_without_dimensions = [image.get("src", "") for image in parser.images if not image.get("width") or not image.get("height")]
require(not images_without_dimensions, f"Imágenes sin width/height: {images_without_dimensions}", failures)

json_ld_blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
require(bool(json_ld_blocks), "No existe JSON-LD.", failures)
for block in json_ld_blocks:
    json.loads(block)

ET.parse(ROOT / "sitemap.xml")
robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
require("sitemap.xml" in robots.lower(), "robots.txt no referencia el sitemap.", failures)
require(css.count("{") == css.count("}"), "Las llaves de styles.css no están balanceadas.", failures)

for field_id in ("name", "phone", "program", "campus", "privacy-consent"):
    require(f'id="{field_id}"' in html and "required" in html[html.index(f'id="{field_id}"'):html.index(f'id="{field_id}"') + 260], f"El campo {field_id} no está marcado como obligatorio.", failures)

require("524777134804" in script and "524772659137" in script, "Faltan los WhatsApp de los planteles en script.js.", failures)
require("encodeURIComponent(whatsappMessage)" in script, "El mensaje de WhatsApp no se codifica.", failures)
require("GA4_MEASUREMENT_ID" in (ROOT / "analytics.js").read_text(encoding="utf-8"), "Falta el campo configurable de GA4.", failures)

if failures:
    print("VALIDATION_FAILED")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("VALIDATION_OK")
print(f"IDs: {len(parser.ids)}")
print(f"Internal links: {len(parser.fragment_links)}")
print(f"Images: {len(parser.images)}")
print(f"Local resources: {len(set(parser.local_resources))}")
print(f"FAQ items: {parser.faq_count}")
