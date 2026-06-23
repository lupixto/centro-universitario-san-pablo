from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def save_webp(source: Path) -> None:
    with Image.open(source) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        full_output = source.with_suffix(".webp")
        image.save(full_output, "WEBP", quality=84, method=6)

        if image.width > 640:
            mobile = image.copy()
            mobile.thumbnail((640, 6400), Image.Resampling.LANCZOS)
            mobile.save(
                source.with_name(f"{source.stem}-640.webp"),
                "WEBP",
                quality=82,
                method=6,
            )

        print(f"{source.name}: {image.width}x{image.height}")


for image_path in sorted(ASSETS.glob("*.jpg")):
    save_webp(image_path)

logo_path = ASSETS / "logo-san-pablo-nuevo.png"
with Image.open(logo_path) as logo:
    logo = ImageOps.exif_transpose(logo).convert("RGBA")
    web_logo = ImageOps.contain(logo, (320, 320), Image.Resampling.LANCZOS)
    web_logo.save(ASSETS / "logo-san-pablo-320.webp", "WEBP", quality=90, method=6)
    for size, filename in ((64, "favicon.png"), (180, "apple-touch-icon.png")):
        icon = ImageOps.contain(logo, (size, size), Image.Resampling.LANCZOS)
        canvas = Image.new("RGBA", (size, size), "white")
        canvas.alpha_composite(icon, ((size - icon.width) // 2, (size - icon.height) // 2))
        canvas.convert("RGB").save(ASSETS / filename, "PNG", optimize=True)
