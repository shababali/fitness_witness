from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():

    # get food data
    with open("foods.json") as f:
        data = json.load(f)
    food_names_array = [e["name"] for category in data.values() for e in category]

    if request.method == 'POST':

        if 'submit' in request.form:
            # Logic based on the submit button value
            return f"submit"
        elif 'reset' in request.form:
            # Logic for reset button
            return "reset"

    return render_template('form_template.html', food_names_array=food_names_array)
