from flask import Flask, jsonify, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io, requests

app = Flask(__name__)

@app.route('/generate_image', methods=['POST'])
def generate_image():
    json_data = request.get_json()

    # Extract information from the JSON object
    background_url = json_data.get('background_url')
    top_text = json_data.get('top_text')
    bottom_text = json_data.get('bottom_text')
    free_text = json_data.get('free_text')
    formatting = json_data.get('formatting')

    # Load the background image
    background_image = Image.open(requests.get(background_url, stream=True).raw)

    # Create a new image with the same size as the background image
    image = Image.new('RGB', background_image.size)
    draw = ImageDraw.Draw(image)

    # Set the font and text alignment for the text overlays
    # font = ImageFont.truetype(formatting.get('font').lower()+'.ttf', formatting.get('font_size'))
    font = ImageFont.load_default()
    text_alignment = 'center'

    # Add the top text overlay
    top_text_position = (image.width // 2, formatting.get('top_padding'))
    draw.text(top_text_position, top_text, fill=formatting.get('font_color'), font=font, align=text_alignment)

    # Add the bottom text overlay
    bottom_text_position = (image.width // 2, image.height - formatting.get('bottom_padding'))
    draw.text(bottom_text_position, bottom_text, fill=formatting.get('font_color'), font=font, align=text_alignment)

    # Add the free text overlays
    for text_data in free_text:
        text = text_data.get('text')
        position = (text_data.get('position').get('x'), text_data.get('position').get('y'))
        draw.text(position, text, fill=formatting.get('font_color'), font=font, align=text_alignment)

    # Save the generated image to a BytesIO object
    image_io = io.BytesIO()
    image.save(image_io, format='PNG')
    image_io.seek(0)

    return send_file(image_io, mimetype='image/png')

if __name__ == '__main__':
    app.run()
