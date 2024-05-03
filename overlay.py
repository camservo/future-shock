import textwrap

from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(image_path, output_path, title, date, description):
    # Load the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Define fonts (the path might need to be adjusted for your system)
    title_font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 40)
    date_font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 30)
    description_font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 20)

    # Define text colors
    title_color = "yellow"
    date_color = "white"
    description_color = "lightgray"

    # Position for the title, date, and description
    title_position = (50, 30)
    date_position = (50, 80)
    description_position = (50, 120)

    # Add text to image
    draw.text(title_position, title, font=title_font, fill=title_color)
    draw.text(date_position, date, font=date_font, fill=date_color)

    current_y = description_position[1]
    print(type(description))
    for line in textwrap.wrap(description, width=40):
        draw.text(
            (description_position[0], current_y),
            line,
            font=description_font,
            fill=description_color,
        )
        # Correct method to get text size
        text_height = description_font.getmetrics()[0]
        current_y += text_height + 5  # Move to the next line with a small padding

    # Save the modified image
    image.save(output_path)


# Example usage
add_text_to_image(
    "Future Shock Video Box BLANK TEMPLATE.jpg",  # Input image file path
    "output_image.jpg",  # Output image file path
    "Awesome Movie Title",  # Title
    "Created: 2024",  # Date
    "This is an example of a movie description that could span multiple lines.  It includes details about the plot, characters, and more.",  # Description
)
