# Meme JSON

A schema and implementation examples for a method of generating meme images from a JSON structure.

Try out the HTML/JS implementation here: https://red5d.github.io/memejson/

Files:
* meme-schema.json - JSON Schema for defining image elements
* example.json - Example JSON structure that implements the schema
* index.html - Web UI for building or viewing images defined by the JSON structure
* meme.py - Python Flask implementation that receives a JSON structure via HTTP POST and returns the corresponding image.

Features:
* Images can be created using a source image url or base64 data uri for the background
* Top/Bottom text can be set along with the font/color/size and top/bottom padding for the text
* Free text can be added which can be placed anywhere on the background image using specified XY coordinates.
* Meme "images" distributed in this JSON format can be easily modified and the background or text swapped out by changing a value
* The "images" can also be easily analyzed programmically since it's just JSON data.