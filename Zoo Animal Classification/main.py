from pyexpat import model
from utils import *

# Importing necessary libraries for app building
from flask import Flask,render_template,request

# importing library to load the model
import pickle

app = Flask(__name__)

#Loading model
classifier = pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
def predict():
    prediction = classifier.predict(OHE())
    animal_class = class_determine(prediction[0])
    pred_text_1 = "The animal is of class " + str(animal_class) + " . The list of " + str(animal_class) + " present in the zoo are : "
    return render_template('result.html',prediction_text_1 = pred_text_1, prediction_text_2 = animals_list(animal_class))


if __name__ == '__main__':
    app.run(debug=True)