# -*- coding: utf-8 -*-
""" based on Bird Chirping Example

"""

from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np
import random as random

# load dataset
dataframe = read_csv("Data/RecipiesCleanNoIndexHalfRealHalfRandomRandomStartsLine4780LabelsInColCUZ.csv", header=None)
dataset = dataframe.values

# split into input (X) and output (Y) variables
X = dataset[:, 0:2599].astype(float)
Y = dataset[:, 2599]
# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

# smaller model
def create_smaller():
    # create model
    model = Sequential()
    model.add(Dense(30, input_dim=2599, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

Y = [1 if y == 'R' else 0 for y in Y]
model = create_smaller()
results = model.fit(X, Y, batch_size=5, epochs=2)


# Creates Good recipes
numberOfRecipes = 5
AproxNumberOfIngredients = 12
scoreLimit = .9 #between 0 and 1
j=0
while j < numberOfRecipes:
    score = 0
    recipe = np.zeros(2599)

    while score < scoreLimit:
        i = 0
        while i < 2599:

            rand = random.randrange(0, 2599)
            if rand > AproxNumberOfIngredients:
                recipe[i] = 0
            else:
                recipe[i] = 1
            i+=1

        score = model.predict(np.asarray([recipe]))


    #print(recipe)
    labels = np.loadtxt("Data/BigCleanRecipesNoHashtagLabelsOnly.csv", skiprows=0, dtype=object, delimiter=",")
    labelsAndRecipes = np.stack((recipe,labels))
    filtered = labelsAndRecipes[:, labelsAndRecipes[0] != 0]
    print(filtered[1])
    print(score)
    j += 1


