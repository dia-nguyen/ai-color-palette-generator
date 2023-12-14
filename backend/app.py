import openai
import json
from flask import Flask, render_template, request
from dotenv import dotenv_values

config = dotenv_values('.env')
openai.api_key = config["OPENAI_API_KEY"]

app = Flask(__name__,
    template_folder="templates",
    static_url_path = '',
    static_folder = 'static',
)

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
    prompt = f"""
        You are a color palette generating assistant that responds to text prompts for color palettes
        You should generate color palettes that fit the theme, mood, or instructions in the prompt.
        The palette should be between 2 and 6 colors.

        Desired format: JSON array of hex color codes

        Text: {msg}

        Response:
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )

    return json.loads(response["choices"][0]["text"])

if __name__ == "__main__":
    app.run(debug=True)