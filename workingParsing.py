import csv
import json
rawJson =open("randomrecipies.json","r")
realJson =json.loads(rawJson.read())
rCount = len(realJson["recipes"])
with open('recipes.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile, delimiter=',')
    recipeTitles = []
    uniqueIngredients = []
    uniqueIngredientsNames = []
    uniqueIngredientsNames.append('')
    for i in range(rCount):
        recipe = realJson["recipes"][i]
        recipeTitles.append(recipe["title"])
        for j in range(len(recipe["extendedIngredients"])):
            ingredient = recipe["extendedIngredients"][j]
            unique = True
            for k in range(len(uniqueIngredients)):
                if uniqueIngredients[k]["name"] == ingredient["name"]:
                    #Not unique
                    unique = False
            if unique:
                uniqueIngredients.append(ingredient)
                uniqueIngredientsNames.append(ingredient['name'])
    writer.writerow(uniqueIngredientsNames)
    for i in range(rCount):
        recipe = realJson["recipes"][i]
        row = []
        print(recipe['title'])
        row.append(recipe['title'])
        for k in range(len(uniqueIngredients) + 1):
            row.append('0')
        for j in range(len(recipe["extendedIngredients"])):
            ingredient = recipe["extendedIngredients"][j]
            for k in range(len(uniqueIngredients)):
                if uniqueIngredients[k]["name"] == ingredient["name"]:
                    row[k+1] = '1'
        writer.writerow(row)