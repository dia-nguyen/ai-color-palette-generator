from openai import OpenAI
import json
from flask import Flask, render_template, request
import os


app = Flask(__name__,
    template_folder="templates",
    static_url_path = '',
    static_folder = 'static',
)

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

@app.route("/")
def index():
    """Home page to render index page"""
    return render_template("index.html")

@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    """Route for posting query for color palette"""
    query = request.form.get("query")
    colors = get_colors(query)
    return {"colors": colors}


def get_colors(msg):
    """Makes a request to open ai to return list of color palette"""

    messages = [
        {"role": "system", "content": "You are a color palette generating assistant that responds to text prompts for color palettes. You should generate color palettes that fit the theme, mood, or instructions in the prompt. The palette should be between 3 and 6 colors."},
        {"role": "user", "content": "Convert the following verbal description of a color palette into a list of colors: sage, nature, earth"},
        {"role": "assistant", "content": '["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]'},
        {"role": "user", "content": f"Convert the following verbal description of a color palette into a list of colors: {msg}"}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200,
    )

    return json.loads(response.choices[0].message.content)

if __name__ == "__main__":
    app.run(debug=True)