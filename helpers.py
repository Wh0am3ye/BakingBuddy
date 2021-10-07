import re

def insert_str(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]


def servings(recipe, iniServe, finalServe):
    # Split each line of the ingredients list
    ingredients = recipe.splitlines()
    # Create empty list to return to the programme
    edit_ingr = []
    # Iterate each line
    for item in ingredients:
        # Split each line where there's a space
        item = item.split(" ")
        if not item[0].isnumeric():
            count = 0
            for c in item[0]:
                if c.isdigit():
                    count += 1
                    continue
                elif c == ".":
                    count += 1
                    continue
                else:
                    measure = insert_str(item[0], " ", count)
                    measureList = []
                    measureList = measure.split(" ")
                    item[0] = measureList[0]
                    item.insert(1, measureList[1])
                    break
        # Float item[0] and calculate new value using user provided servings
        item[0] = (float(item[0]) / iniServe) * finalServe
        # format output of item[0] to display max 2 decimal places
        if not item[0].is_integer():
           item[0] = format(item[0], ".2f")
        else:
            item[0] = int(item[0])
        # Convert item[0] back to a string
        item[0] = str(item[0])
        s = " "
        # Add items together including a space inbetween each word and append to edit_ingr
        item = s.join(item)
        edit_ingr.append(item)
    return edit_ingr


def conversion(measure_value, fr_unit, to_unit, ingredients):
    ingredient_weight_dict = {
        "flour": 120,
        "castor-sugar": 190,
        "brown-sugar": 213,
        "granulated-sugar": 198,
        "demerara-sugar": 220,
        "butter": 226,
        "chocolate": 170,
        "cocoa": 84,
        "ground-almonds": 96,
        "milk": 227,
        "water": 227,
        "oats": 99,
        "raisins": 149,
        "oil": 198
    }
    measures_dict = {
        "grams-ounces": 28.3495,
        "milliliters-floz": 29.5735,
        "grams-pounds": 453.592,
        "milliliters-cups": 240,
        "pounds-ounces": 16,
        "floz-cups": 8.32674
    }
    units_dict = {
        "to-grams": "grams",
        "to-milliliters": "milliliters",
        "to-pounds": "pounds",
        "to-ounces": "ounces",
        "to-fluid-ounces": "fluid ounces",
        "to-cups": "cups"
    }
    ingredient_dict = {
        "flour": "flour",
        "castor-sugar": "castor sugar",
        "brown-sugar": "brown sugar",
        "granulated-sugar": "granulated sugar",
        "demerara-sugar": "demerara sugar",
        "butter": "butter",
        "chocolate": "chocolate",
        "cocoa": "cocoa",
        "ground-almonds": "ground almonds",
        "milk": "milk",
        "water": "water",
        "oats": "oats",
        "raisins": "raisins",
        "oil": "oil"
    }

    # Convert from pounds
    if fr_unit == "fr-pounds" and to_unit == "to-grams":
        new_measure = measure_value * measures_dict["grams-pounds"]
    elif fr_unit == "fr-pounds" and to_unit == "to-milliliters":
        return "Error"
    elif fr_unit == "fr-pounds" and to_unit == "to-pounds":
        new_measure = measure_value
    elif fr_unit == "fr-pounds" and to_unit == "to-ounces":
        new_measure = measure_value * measures_dict["pounds-ounces"]
    elif fr_unit == "fr-pounds" and to_unit == "to-fluid-ounces":
        return "Error"
    elif fr_unit == "fr-pounds" and to_unit == "to-cups":
        new_measure = (measure_value * measures_dict["grams-pounds"]) / ingredient_weight_dict[ingredients]
    # Convert from ounces
    elif fr_unit == "fr-ounces" and to_unit == "to-grams":
        new_measure = measure_value * measures_dict["grams-ounces"]
    elif fr_unit == "fr-ounces" and to_unit == "to-milliliters":
        return "Error"
    elif fr_unit == "fr-ounces" and to_unit == "to-pounds":
        new_measure = measure_value / measures_dict["pounds-ounces"]
    elif fr_unit == "fr-ounces" and to_unit == "to-ounces":
        new_measure = measure_value
    elif fr_unit == "fr-ounces" and to_unit == "to-fluid-ounces":
        return "Error"
    elif fr_unit == "fr-ounces" and to_unit == "to-cups":
        new_measure = (measure_value * measures_dict["grams-ounces"]) / ingredient_weight_dict[ingredients]
    # Convert from cups
    elif fr_unit == "fr-cups" and to_unit == "to-grams":
        new_measure = measure_value * ingredient_weight_dict[ingredients]
    elif fr_unit == "fr-cups" and to_unit == "to-milliliters":
        new_measure = measure_value * measures_dict["milliliters-cups"]
    elif fr_unit == "fr-cups" and to_unit == "to-pounds":
        new_measure = (measure_value * ingredient_weight_dict[ingredients]) / measures_dict["grams-pounds"]
    elif fr_unit == "fr-cups" and to_unit == "to-ounces":
        new_measure = (measure_value * ingredient_weight_dict[ingredients]) / measures_dict["grams-ounces"]
    elif fr_unit == "fr-cups" and to_unit == "to-fluid-ounces":
        new_measure = measure_value * measures_dict["floz-cups"]
    elif fr_unit == "fr-cups" and to_unit == "to-cups":
        new_measure = measure_value
    # Convert from fluid ounces
    elif fr_unit == "fr-fluid-ounces" and to_unit == "to-grams":
        return "Error"
    elif fr_unit == "fr-fluid-ounces" and to_unit == "to-milliliters":
        new_measure = measure_value * measures_dict["milliliters-floz"]
    elif fr_unit == "fr-fluid-ounces" and to_unit == "to-pounds":
        return "Error"
    elif fr_unit == "fr-fluid-ounces" and to_unit == "to-ounces":
        return "Error"
    elif fr_unit == "fr-fluid-ounces" and to_unit == "to-fluid-ounces":
        new_measure = measure_value
    elif fr_unit == "fr-fluid-ounces" and to_unit == "to-cups":
        new_measure = measure_value / measures_dict["floz-cups"]
    # Convert from grams
    elif fr_unit == "fr-grams" and to_unit == "to-grams":
        new_measure = measure_value
    elif fr_unit == "fr-grams" and to_unit == "to-milliliters":
        return "Error"
    elif fr_unit == "fr-grams" and to_unit == "to-pounds":
        new_measure = measure_value / measures_dict["grams-pounds"]
    elif fr_unit == "fr-grams" and to_unit == "to-ounces":
        new_measure = measure_value / measures_dict["grams-ounces"]
    elif fr_unit == "fr-grams" and to_unit == "to-fluid-ounces":
        return "Error"
    elif fr_unit == "fr-grams" and to_unit == "to-cups":
        new_measure = measure_value / ingredient_weight_dict[ingredients]
    # Convert from milliliters
    elif fr_unit == "fr-milliliters" and to_unit == "to-grams":
        return "Error"
    elif fr_unit == "fr-milliliters" and to_unit == "to-milliliters":
        new_measure = measure_value
    elif fr_unit == "fr-milliliters" and to_unit == "to-pounds":
        return "Error"
    elif fr_unit == "fr-milliliters" and to_unit == "to-ounces":
        return "Error"
    elif fr_unit == "fr-milliliters" and to_unit == "to-fluid-ounces":
        new_measure = measure_value / measures_dict["milliliters-floz"]
    elif fr_unit == "fr-milliliters" and to_unit == "to-cups":
        new_measure = measure_value / measures_dict["milliliters-cups"]
    else:
        return "Unexp_Error"
    if not new_measure.is_integer():
        new_measure = format(new_measure, ".2f")
    else:
        new_measure = int(new_measure)
    result = str(str(new_measure) + " " + units_dict[to_unit] + " " + ingredient_dict[ingredients])
    return (result)