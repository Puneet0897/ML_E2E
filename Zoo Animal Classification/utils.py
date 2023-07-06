from constants import *
from flask import request
from main import *

def OHE():

    hair = request.form['Hair']
    if hair == "Yes":
        hair = 1
    else : 
        hair = 0

    feathers = request.form['Feathers']
    if feathers == "Yes":
        feathers = 1
    else : 
        feathers = 0

    eggs = request.form['Eggs']
    if eggs == "Yes":
        eggs = 1
    else : 
        eggs = 0

    milk = request.form['Milk']
    if milk == "Yes":
        milk = 1
    else : 
        milk = 0

    airborne = request.form['Airborne']
    if airborne == "Yes":
        airborne = 1
    else : 
        airborne = 0

    aquatic = request.form['Aquatic']
    if aquatic == "Yes":
        aquatic = 1
    else : 
        aquatic = 0

    predator = request.form['Predator']
    if predator == "Yes":
        predator = 1
    else : 
        predator = 0

    toothed = request.form['Toothed']
    if toothed == "Yes":
        toothed = 1
    else : 
        toothed = 0

    backbone = request.form['Backbone']
    if backbone == "Yes":
        backbone = 1
    else : 
        backbone = 0

    breathes = request.form['Breathes']
    if breathes == "Yes":
        breathes = 1
    else : 
        breathes = 0

    ven = request.form['Venomous']
    if ven == "Yes":
        ven = 1
    else : 
        ven = 0

    fins = request.form['Fins']
    if fins == "Yes":
        fins = 1
    else : 
        fins = 0

    legs = request.form['Legs']

    tail = request.form['Tail']
    if tail == "Yes":
        tail = 1
    else : 
        tail = 0

    dom = request.form['Domestic']
    if dom == "Yes":
        dom = 1
    else : 
        dom = 0

    catsz = request.form['Catsize']
    if catsz == "Yes":
        catsz = 1
    else : 
        catsz = 0

    OHE_array = [[hair,feathers,eggs,milk,airborne,aquatic,predator,toothed,backbone,breathes,ven,fins,legs,tail,dom,catsz]]

    return OHE_array

def class_determine(pred):
    
    animal_class = class_dict[pred]
    return animal_class

def animals_list(animal_class):
    if animal_class == "Mammal":
        return Mammal
    elif animal_class == "Bird":
        return Bird
    elif animal_class == "Reptile":
        return Reptile
    elif animal_class == "Fish":
        return Fish
    elif animal_class == "Amphibian":
        return Amphibian
    elif animal_class == "Bug":
        return Bug
    else:
        return Invertebrate
