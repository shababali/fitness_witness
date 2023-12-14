import json

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader, select_autoescape


app = FastAPI()

# Jinja environment setup
templates = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(['html', 'xml'])
)

@app.get("/")
@app.post("/")
async def root():
    # # get food data
    with open("foods.json") as f:
        data = json.load(f)

    # return data
    food_names_array = [e["name"] for category in data.values() for e in category]
    #
    template = templates.get_template("form_template.html")
    html_content = template.render(food_names_array=food_names_array)  # You can pass context variables as arguments if needed
    #
    return HTMLResponse(content=html_content)
