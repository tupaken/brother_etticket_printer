from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------
# Auto-Fit Funktion
# ---------------------------------------
def fit_text_one_line(draw, text, font_path, max_width, start_size=80, min_size=8):
    size = start_size
    while size >= min_size:
        font = ImageFont.truetype(font_path, size=size)

        bbox = draw.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]

        if w <= max_width:
            return font
        size -= 1

    return ImageFont.truetype(font_path, min_size)

# ---------------------------------------
# Einstellungen
# ---------------------------------------
comment = "Ein kurzes text"    # <-- Dein Kommentar

# ---------------------------------------
# Bild erstellen (566×165 px → richtig für 17x54)
# ---------------------------------------
img = Image.new("RGB", (566, 165), "white")
draw = ImageDraw.Draw(img)

# Oberer Text
font_big = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size=50)
draw.text((40, 20), "200-20", fill="black", font=font_big)

# ---------------------------------------
# Kommentar automatisch skalieren
# ---------------------------------------
max_width = 566 - 80        # links + rechts 40px Abstand
font_comment = fit_text_one_line(draw, comment, "C:/Windows/Fonts/arial.ttf", max_width)

draw.text((40, 90), comment, fill="black", font=font_comment)

img.show()
