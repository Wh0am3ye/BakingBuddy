from flask import Flask, render_template, request, redirect
from helpers import servings, conversion

# Configure application
app = Flask(__name__)
converted_values = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/servings")
def serving_calc():
    return render_template("servings.html")

@app.route("/recipe", methods=["GET", "POST"])
def recipe():
    if request.method == "POST":
        try:
            recipe = request.form["recipe"]
        except:
            return render_template("servings_error.html")
        try:
            iniServe = int(request.form["ini-serve"])
        except:
            return render_template("servings_error.html")
        try:
            finalServe = int(request.form["final-serve"])
        except:
            return render_template("servings_error.html")
        edit_ingr = servings(recipe, iniServe, finalServe)
        return render_template("recipe.html", ingredients=edit_ingr)
    else:
        return redirect("index.html")

@app.route("/conversions")
def conversions():
    converted_values.clear()
    return render_template("conversions.html")

@app.route("/converted", methods=["GET", "POST"])
def converted():
    if request.method == "POST":
        try: 
            measure_value = float(request.form["measure-value"])
        except:
            return render_template("converted_unexp_error.html", converted_values=converted_values)
        fr_unit = request.form["fr-unit"]
        to_unit = request.form["to-unit"]
        ingredients = request.form["ingredients"]
        result = conversion(measure_value, fr_unit, to_unit, ingredients)
        if result == "Error":
            return render_template("converted_error.html", converted_values=converted_values)
        elif result == "Unexp_Error":
            return render_template("converted_unexp_error.html", converted_values=converted_values)
        else:
            converted_values.append(result)
            return render_template("converted.html", converted_values=converted_values)
    else:
        return "Error: Unknown command."

@app.route("/tools")
def tools():
    return render_template("tools.html")