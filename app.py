#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request, redirect, url_for
from preprocessing import preprocess_input
import pandas as pd
import pickle

# Initiate Flask
app = Flask(__name__)

# Load trained model
with open('final_model.pkl', 'rb') as file:
    final_model = pickle.load(file)

# Homepage route
@app.route('/')
def home():
        return render_template('home.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get data inserted by the user
        size = float(request.form['size'])
        rooms = int(request.form['rooms'])
        bathrooms = int(request.form['bathrooms'])
        hasFurniture = bool(request.form.get('hasFurniture'))
        municipality = request.form['municipality']
        hasBalcony = bool(request.form.get('hasBalcony'))
        hasMetro = bool(request.form.get('hasMetro'))
        hasLift = bool(request.form.get('hasLift'))
        hasGarage = bool(request.form.get('hasGarage'))
        isLuxury = bool(request.form.get('isLuxury'))
        propertyType = request.form['propertyType']

        # Preprocessing inserted data
        input_data = preprocess_input(size, rooms, bathrooms, hasFurniture, municipality, hasBalcony, hasMetro, hasLift,                                      hasGarage, isLuxury, propertyType)

        # Predict
        final_prediction = final_model.predict(input_data)
        final_prediction_rounded = round(final_prediction[0])

        # Return prediction value to page
        return render_template('home.html',final_prediction=final_prediction_rounded)

# Run app
if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




