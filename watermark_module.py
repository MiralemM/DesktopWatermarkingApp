from PIL import Image, ImageTk, ImageOps, ImageDraw, ImageFont
from tkinter import filedialog


class Marker:

    def __init__(self):
        self.base_image = None
        self.resized_image = None
        self.watermark_text = None
        self.watermark_color = None
        self.location_mark = None
        self.base_image_rgba = None

    def pick_image(self):
        filename = filedialog.askopenfilename(title="Select Image")
        self.base_image = Image.open(filename)
        self.base_image_rgba = self.base_image.convert("RGBA")
        self.base_image_rgba = ImageOps.exif_transpose(self.base_image_rgba)

    def resize_image_to_window(self):
        max_height = 680
        max_width = 750
        s = self.base_image.size
        if s[0] > s[1]:
            ratio = float(s[0] / max_width)
        elif s[0] < s[1]:
            ratio = float(s[1] / max_height)
        img = self.base_image.resize((int(s[0] / ratio), int(s[1] / ratio)), Image.ANTIALIAS)
        self.resized_image = ImageTk.PhotoImage(img)

    def get_text(self, text):
        self.watermark_text = text

    def get_location(self, location):
        self.location_mark = location

    def set_watermark_location(self, image_width, image_height, watermark_width, watermark_height):
        margin = 20
        if self.location_mark == "Top-Left":
            x = margin
            y = margin
        elif self.location_mark == "Top-Right":
            x = image_width - watermark_width - margin
            y = margin
        elif self.location_mark == "Center":
            x = (image_width / 2) - (watermark_width / 2)
            y = (image_height / 2) - (watermark_height / 2)
        elif self.location_mark == "Bottom-Left":
            x = margin
            y = image_height - watermark_height - margin
        elif self.location_mark == "Bottom-Right":
            x = image_width - watermark_width - margin
            y = image_height - watermark_height - margin
        return int(x), int(y)

    def set_color(self, color):
        if color == "Black Text":
            self.watermark_color = (0, 0, 0, 64)
        elif color == "White Text":
            self.watermark_color = (255, 255, 255, 64)

    def watermarking_image(self):
        image_width, image_height = self.base_image_rgba.size
        overlay_image = Image.new("RGBA", (image_width, image_height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay_image)
        text = self.watermark_text
        font_size = int(((image_width + image_height) / 2) // 12)
        font = ImageFont.truetype("segoeui.ttf", font_size)
        watermark_width, watermark_height = draw.textsize(text, font)
        x, y = self.set_watermark_location(image_width, image_height, watermark_width, watermark_height)
        draw.text((x, y), text, font=font, fill=self.watermark_color)
        watermarked_image = Image.alpha_composite(self.base_image_rgba, overlay_image)
        watermarked_image.show()
