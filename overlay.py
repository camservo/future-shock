import textwrap

from PIL import Image, ImageDraw, ImageFont


class ImageTextRenderer:
    def __init__(self, image_path, font_path="/Library/Fonts/Arial Unicode.ttf"):
        self.image = Image.open(image_path)
        self.draw = ImageDraw.Draw(self.image)
        self.font_path = font_path
        self.colors = {
            "title": "black",
            "category": "black",
            "rating": "black",
            "starring": "black",
            "synopsis": "black",
        }
        self.font_sizes = {
            "title": 10,
            "category": 10,
            "rating": 10,
            "starring": 10,
            "synopsis": 10,
        }
        self.positions = {
            "title": (100, 135),
            "category": (157, 148),
            "rating": (141, 159),
            "starring": (152, 182),
            "synopsis": (105, 220),
        }

    def add_text(self, text_type, text):
        font = ImageFont.truetype(self.font_path, self.font_sizes[text_type])
        color = self.colors[text_type]
        position = self.positions[text_type]
        if text_type == "synopsis":
            self._wrap_text(text, font, color, position)
        else:
            self.draw.text(position, text, font=font, fill=color)

    def _wrap_text(self, text, font, color, position):
        current_y = position[1]
        for line in textwrap.wrap(text, width=40):
            self.draw.text((position[0], current_y), line, font=font, fill=color)
            # Measure the height of the line
            text_height = font.getmetrics()[0]
            current_y += text_height + 5  # Adding a little padding between lines

    def save_image(self, output_path):
        self.image.save(output_path)


# Example usage
renderer = ImageTextRenderer("Future Shock Video Box BLANK TEMPLATE.jpg")
renderer.add_text("title", "Awesome Movie Title")
renderer.add_text("category", "Sci-Fi")
renderer.add_text("rating", "PG-13")
renderer.add_text("starring", "Jane Doe, John Smith")
renderer.add_text(
    "synopsis",
    "This is an example of a movie description that could span multiple lines. It includes details about the plot, characters, and more.",
)
renderer.save_image("output_image.jpg")
