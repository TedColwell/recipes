import json
import csv


def get_leaves(item, key=None):
    if isinstance(item, dict):
        leaves = {}
        for i in item.keys():
            leaves.update(get_leaves(item[i], i))
        return leaves
    elif isinstance(item, list):
        leaves = {}
        for i in item:
            leaves.update(get_leaves(i, key))
        return leaves
    else:
        return {key : item}


with open('randomrecipies.txt') as f_input:
    json_data = '{"recipes":[{"vegetarian":false,"vegan":false,"glutenFree":false,"dairyFree":true,' \
                '"veryHealthy":false,"cheap":false,"veryPopular":false,"sustainable":false,' \
                '"weightWatcherSmartPoints":11,"gaps":"no","lowFodmap":false,"ketogenic":false,"whole30":false,' \
                '"sourceUrl":"https://www.foodista.com/recipe/RJZY48Q2/creamy-chicken-orzo-soup",' \
                '"spoonacularSourceUrl":"https://spoonacular.com/creamy-chicken-orzo-soup-640619","aggregateLikes":7,' \
                '"spoonacularScore":50.0,"healthScore":10.0,"creditsText":"Foodista.com – The Cooking Encyclopedia ' \
                'Everyone Can Edit","license":"CC BY 3.0","sourceName":"Foodista","pricePerServing":164.92,' \
                '"extendedIngredients":[{"id":4053,"aisle":"Oil, Vinegar, Salad Dressing","image":"olive-oil.jpg",' \
                '"consitency":"liquid","name":"olive oil","original":"2 tablespoons olive oil","originalString":"2 ' \
                'tablespoons olive oil","originalName":"olive oil","amount":2.0,"unit":"tablespoons","meta":[],' \
                '"metaInformation":[],"measures":{"us":{"amount":2.0,"unitShort":"Tbsps","unitLong":"Tbsps"},' \
                '"metric":{"amount":2.0,"unitShort":"Tbsps","unitLong":"Tbsps"}}},{"id":11143,"aisle":"Produce",' \
                '"image":"celery.jpg","consitency":"solid","name":"celery","original":"1 cup celery, thinly sliced",' \
                '"originalString":"1 cup celery, thinly sliced","originalName":"celery, thinly sliced","amount":1.0,' \
                '"unit":"cup","meta":["thinly sliced"],"metaInformation":["thinly sliced"],"measures":{"us":{' \
                '"amount":1.0,"unitShort":"cup","unitLong":"cup"},"metric":{"amount":236.588,"unitShort":"ml",' \
                '"unitLong":"milliliters"}}},{"id":11960,"aisle":"Produce","image":"baby-carrots.jpg",' \
                '"consitency":"solid","name":"baby carrots","original":"1 cup baby carrots, thinly sliced",' \
                '"originalString":"1 cup baby carrots, thinly sliced","originalName":"baby carrots, thinly sliced",' \
                '"amount":1.0,"unit":"cup","meta":["thinly sliced"],"metaInformation":["thinly sliced"],"measures":{' \
                '"us":{"amount":1.0,"unitShort":"cup","unitLong":"cup"},"metric":{"amount":236.588,"unitShort":"ml",' \
                '"unitLong":"milliliters"}}},{"id":11282,"aisle":"Produce","image":"brown-onion.png",' \
                '"consitency":"solid","name":"onion","original":"1 small onion, chopped","originalString":"1 small ' \
                'onion, chopped","originalName":"onion, chopped","amount":1.0,"unit":"small","meta":["chopped"],' \
                '"metaInformation":["chopped"],"measures":{"us":{"amount":1.0,"unitShort":"small",' \
                '"unitLong":"small"},"metric":{"amount":1.0,"unitShort":"small","unitLong":"small"}}},{"id":1082047,' \
                '"aisle":"Spices and Seasonings","image":"salt.jpg","consitency":"solid","name":"kosher salt",' \
                '"original":"1 teaspoon kosher salt","originalString":"1 teaspoon kosher salt","originalName":"kosher ' \
                'salt","amount":1.0,"unit":"teaspoon","meta":[],"metaInformation":[],"measures":{"us":{"amount":1.0,' \
                '"unitShort":"tsp","unitLong":"teaspoon"},"metric":{"amount":1.0,"unitShort":"tsp",' \
                '"unitLong":"teaspoon"}}},{"id":1002030,"aisle":"Spices and Seasonings","image":"pepper.jpg",' \
                '"consitency":"solid","name":"ground pepper","original":"1 teaspoon fresh ground black pepper",' \
                '"originalString":"1 teaspoon fresh ground black pepper","originalName":"fresh ground black pepper",' \
                '"amount":1.0,"unit":"teaspoon","meta":["fresh","black"],"metaInformation":["fresh","black"],' \
                '"measures":{"us":{"amount":1.0,"unitShort":"tsp","unitLong":"teaspoon"},"metric":{"amount":1.0,' \
                '"unitShort":"tsp","unitLong":"teaspoon"}}},{"id":5006,"aisle":"Meat","image":"whole-chicken.jpg",' \
                '"consitency":"solid","name":"chicken","original":"1 12.5 oz can Swanson Premium Chunk Chicken, ' \
                'drained","originalString":"1 12.5 oz can Swanson Premium Chunk Chicken, drained",' \
                '"originalName":"Swanson Premium Chunk Chicken, drained","amount":12.5,"unit":"oz","meta":["chunk",' \
                '"drained","canned"],"metaInformation":["chunk","drained","canned"],"measures":{"us":{"amount":12.5,' \
                '"unitShort":"oz","unitLong":"ounces"},"metric":{"amount":354.369,"unitShort":"g",' \
                '"unitLong":"grams"}}},{"id":6194,"aisle":"Canned and Jarred","image":"chicken-broth.png",' \
                '"consitency":"liquid","name":"chicken broth","original":"2 14.5 oz cans Swanson Chicken broth + 2 ' \
                'cans water","originalString":"2 14.5 oz cans Swanson Chicken broth + 2 cans water",' \
                '"originalName":"Swanson Chicken broth + 2 cans water","amount":29.0,"unit":"oz","meta":["canned"],' \
                '"metaInformation":["canned"],"measures":{"us":{"amount":29.0,"unitShort":"oz","unitLong":"ounces"},' \
                '"metric":{"amount":822.136,"unitShort":"g","unitLong":"grams"}}},{"id":2034,"aisle":"Spices and ' \
                'Seasonings","image":"seasoning.jpg","consitency":"solid","name":"poultry seasoning","original":"1/8 ' \
                'teaspoon poultry seasoning","originalString":"1/8 teaspoon poultry seasoning",' \
                '"originalName":"poultry seasoning","amount":0.125,"unit":"teaspoon","meta":[],"metaInformation":[],' \
                '"measures":{"us":{"amount":0.125,"unitShort":"tsps","unitLong":"teaspoons"},"metric":{' \
                '"amount":0.125,"unitShort":"tsps","unitLong":"teaspoons"}}},{"id":10920420,"aisle":"Pasta and Rice",' \
                '"image":"orzo.jpg","consitency":"solid","name":"orzo","original":"1 cup Orzo, uncooked",' \
                '"originalString":"1 cup Orzo, uncooked","originalName":"Orzo, uncooked","amount":1.0,"unit":"cup",' \
                '"meta":["uncooked"],"metaInformation":["uncooked"],"measures":{"us":{"amount":1.0,"unitShort":"cup",' \
                '"unitLong":"cup"},"metric":{"amount":236.588,"unitShort":"ml","unitLong":"milliliters"}}},' \
                '{"id":6016,"aisle":"Canned and Jarred","image":"cream-of-chicken-soup.jpg","consitency":"liquid",' \
                '"name":"condensed cream of chicken soup","original":"1 cup cream of chicken condensed soup",' \
                '"originalString":"1 cup cream of chicken condensed soup","originalName":"cream of chicken condensed ' \
                'soup","amount":1.0,"unit":"cup","meta":[],"metaInformation":[],"measures":{"us":{"amount":1.0,' \
                '"unitShort":"cup","unitLong":"cup"},"metric":{"amount":236.588,"unitShort":"ml",' \
                '"unitLong":"milliliters"}}}],"id":640619,"title":"Creamy Chicken Orzo Soup","readyInMinutes":45,' \
                '"servings":4,"image":"https://spoonacular.com/recipeImages/640619-556x370.jpg","imageType":"jpg",' \
                '"cuisines":[],"dishTypes":["lunch","soup","main course","main dish","dinner"],"diets":["dairy ' \
                'free"],"occasions":["fall","winter"],"winePairing":{"pairedWines":[],"pairingText":"No one wine will ' \
                'suit every pasta dish. Pasta in a tomato-based sauce will usually work well with a medium-bodied ' \
                'red, such as a montepulciano or chianti. Pasta with seafood or pesto will fare better with a ' \
                'light-bodied white, such as a pinot grigio. Cheese-heavy pasta can pair well with red or white - you ' \
                'might try a sangiovese wine for hard cheeses and a chardonnay for soft cheeses. We may be able to ' \
                'make a better recommendation if you ask again with a specific pasta dish.","productMatches":[]},' \
                '"instructions":"In a large pot over medium heat, saute the vegetables in olive oil for about 10 ' \
                'minutes, until vegetables are tender.\nAdd the drained can of chicken and stir.\nSeason the chicken ' \
                'and vegetables with salt and pepper. Stir.\nIncrease the heat to medium-high and add the chicken ' \
                'broth plus 2 cans of warm water and stir.\nAllow the soup to simmer for 15 minutes then add the ' \
                'uncooked pasta and seasoning. Stir.\nLet the soup simmer for 20 minutes, stirring occasionally.\nAdd ' \
                'the condensed soup, stir until the broth is creamy and serve.","analyzedInstructions":[{"name":"",' \
                '"steps":[{"number":1,"step":"In a large pot over medium heat, saute the vegetables in olive oil for ' \
                'about 10 minutes, until vegetables are tender.","ingredients":[{"id":4053,"name":"olive oil",' \
                '"image":"olive-oil.jpg"}],"equipment":[{"id":404752,"name":"pot","image":"stock-pot.jpg"}],' \
                '"length":{"number":10,"unit":"minutes"}},{"number":2,"step":"Add the drained can of chicken and ' \
                'stir.","ingredients":[],"equipment":[]},{"number":3,"step":"Season the chicken and vegetables with ' \
                'salt and pepper. Stir.","ingredients":[{"id":1102047,"name":"salt and pepper",' \
                '"image":"salt-and-pepper.jpg"}],"equipment":[]},{"number":4,"step":"Increase the heat to medium-high ' \
                'and add the chicken broth plus 2 cans of warm water and stir.","ingredients":[{"id":6194,' \
                '"name":"chicken broth","image":"chicken-broth.png"}],"equipment":[]},{"number":5,"step":"Allow the ' \
                'soup to simmer for 15 minutes then add the uncooked pasta and seasoning. Stir.","ingredients":[{' \
                '"id":20420,"name":"pasta","image":"fusilli.jpg"}],"equipment":[],"length":{"number":15,' \
                '"unit":"minutes"}},{"number":6,"step":"Let the soup simmer for 20 minutes, stirring occasionally.",' \
                '"ingredients":[],"equipment":[],"length":{"number":20,"unit":"minutes"}},{"number":7,"step":"Add the ' \
                'condensed soup, stir until the broth is creamy and serve.","ingredients":[],"equipment":[]}]}]}]} '
# First parse all entries to get the complete fieldname list
fieldnames = set()

for entry in json_data:
    fieldnames.update(get_leaves(entry).keys())

with open('output.csv', 'w', newline='') as f_output:
    csv_output = csv.DictWriter(f_output, fieldnames=sorted(fieldnames))
    csv_output.writeheader()
    csv_output.writerows(get_leaves(entry) for entry in json_data)