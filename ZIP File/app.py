import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) 
model = pickle.load(open('model.pkl', 'rb')) 

@app.route('/') 
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'POST':
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Fuel_Type = int(request.form['Fuel_Type'])
        Age_of_the_car = int(request.form['Age_of_the_car'])
        Seller_Type = int(request.form['Seller_Type'])
        Transmission = int(request.form['Transmission'])
        prediction = model.predict(
            [[Present_Price, Kms_Driven, Owner, Fuel_Type, Age_of_the_car, Seller_Type, Transmission]])
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text="You can sell your car at {} lakhs".format(output))

if __name__ == "__main__":
    app.run(debug=True)