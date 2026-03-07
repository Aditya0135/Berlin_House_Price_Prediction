from flask import Flask, render_template, request
import pandas as pd
import os
from Berlin_House_Price_Prediction.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homePage():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    area = float(request.form['area'])
    rooms = float(request.form['rooms'])
    zipcode = float(request.form['zipcode'])
    heating = request.form['heating']
    energy = request.form['energy']

    data = pd.DataFrame({
        "area":[area],
        "rooms":[rooms],
        "zipcode":[zipcode],
        "heating":[heating],
        "energy":[energy]
    })

    predict_pipeline = PredictionPipeline()


    prediction = predict_pipeline.predict(data)

    return render_template("index.html", prediction=round(prediction[0],2))

@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successful!!"


if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8080,debug=True)
    app.run(host="0.0.0.0", port=8080)