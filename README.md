# Energy Prediction Using Prophet

This project aims to forecast energy consumption using the Prophet library. The model is trained on hourly energy consumption data over one year 2015-2016 and can be accessed via a RESTful API.

## Table of Contents
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)


## Installation

To set up this project on your Unix computer, follow these steps:

   git clone https://github.com/hanachaari/energy-prediction-using-prophet.git
   cd energy-prediction-using-prophet
   pip install -r requirements.txt
   python app.py

## API Endpoints
As I used prophet library for the model, the input woould be N
Endpoint: /predict_consumption
Method: GET

## Testing
 using postman : GET "http://127.0.0.1:5000/predict?N=8"

### Notes
Feel free to ask if you need further modifications or additional sections!