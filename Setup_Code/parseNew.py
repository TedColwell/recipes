import csv
import json
rawJson =open("BigCleanRecipies.json","r",encoding="utf8")
realJson =json.loads(rawJson.read())
rCount = len(realJson["recipes"]) # length of recipe
with open('BigCleanRecipes.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile, delimiter=',')
    recipeTitles = []
    uniqueIngredients = []
    uniqueIngredientsNames = []
    uniqueIngredientsNames.append('') # moves column over by one to to reserve column one for recipe names
    for i in range(rCount):  # finds unique ingredient list
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
    writer.writerow(uniqueIngredientsNames) # top row (headers)
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