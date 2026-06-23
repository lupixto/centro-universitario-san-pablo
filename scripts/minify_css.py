import re
from pathlib import Path


root = Path(__file__).resolve().parents[1]
source = (root / "styles.css").read_text(encoding="utf-8")
minified = re.sub(r"/\*.*?\*/", "", source, flags=re.S)
minified = re.sub(r"\s+", " ", minified)
minified = re.sub(r"\s*([{}:;,])\s*", r"\1", minified)
minified = minified.replace(";}", "}").strip()
(root / "styles.min.css").write_text(minified, encoding="utf-8")

print(f"styles.css: {len(source.encode('utf-8'))} bytes")
print(f"styles.min.css: {len(minified.encode('utf-8'))} bytes")
