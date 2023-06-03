from utils import *
from constants import *

# Importing necessary libraries for Flask Application
from flask import Flask,render_template,request
from flask_cors import cross_origin

# Other libraries for loading,preprocessing the data
import pickle

# Initialising flask app
app = Flask(__name__)

# Loading the model
predictor = pickle.load(open(model, "rb"))

@app.route('/')
@cross_origin()
def home():
    return render_template('home.html')

@app.route('/predict',methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == 'POST':
        if DepArrDateCheck() == True:
            if SourceDestCheck() == False:
                transformed_data = OneHotEncode()
                prediction=predictor.predict(transformed_data)
                output=round(prediction[0],2)
                return render_template('home.html',prediction_text="Your flight fare would be around {} Rs . Have a great Journey!!".format(output))
            else:
                return render_template('home.html',prediction_text="OOPS!! Please select different source and destination")
        else:
            return render_template('home.html',prediction_text="Departure DateTime and Arrival DateTime cannot be same!!!")


if __name__ == '__main__':
    app.run(debug=True)