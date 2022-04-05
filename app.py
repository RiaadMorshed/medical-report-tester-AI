from flask import Flask, render_template, request
import pickle
import numpy as np

# load models
diabetesModel = pickle.load(
    open('./models/diabetes-prediction-rfc-model.pkl', 'rb'))
heartModel = pickle.load(open('./models/heartdisease.pkl', 'rb'))
liverModel = pickle.load(open('./models/liverdisease.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/diabetes', methods=['POST', 'GET'])
def Diabetes():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])

        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        my_prediction = diabetesModel.predict(data)
        if my_prediction == 1:
            output = "You have diabetes" + str(preg)
        else:
            output = "You don't have diabetes"
        return render_template('diabetes.html', prediction=output)
    else:
        return render_template('diabetes.html')


@app.route("/heart", methods=['POST', 'GET'])
def Heart():
    if request.method == 'POST':
        Age = int(request.form['age'])
        if request.form['sex'] == "Male":
            Gender = int(1)
        else:
            Gender = 0
        ChestPain = int(request.form['cp'])
        BloodPressure = int(request.form['bp'])
        ElectrocardiographicResults = int(request.form['restecg'])
        MaxHeartRate = int(request.form['mxheartrate'])
        ExerciseInducedAngina = int(request.form['exang'])
        STdepression = float(request.form['stdepression'])
        ExercisePeakSlope = int(request.form['slope'])
        MajorVesselsNo = int(request.form['ca'])
        Thalassemia = int(request.form['thal'])
        prediction = heartModel.predict([[Age, Gender, ChestPain, BloodPressure, ElectrocardiographicResults,
                                        MaxHeartRate, ExerciseInducedAngina, STdepression, ExercisePeakSlope, MajorVesselsNo, Thalassemia]])

        if prediction == 1:
            return render_template('heart.html', prediction_text="Oops!The person seems to have Heart Disease.")
        else:
            return render_template('heart.html', prediction_text="The person does not have any Heart Disease.")
    else:
        return render_template('heart.html')


@app.route("/liver", methods=['POST', 'GET'])
def Liver():
    if request.method == 'POST':
        Age = int(request.form['age'])
        if request.form['sex'] == "Male":
            Gender = int(1)
        else:
            Gender = 0
        Total_Bilirubin = float(request.form['tb'])
        Direct_Bilirubin = float(request.form['db'])
        Alkaline_Phosphotase = int(request.form['ap'])
        Alamine_Aminotransferase = int(request.form['aa'])
        Aspartate_Aminotransferase = int(request.form['aspartate'])
        Total_Protiens = float(request.form['protines'])
        Albumin = float(request.form['albamin'])
        Albumin_and_Globulin_Ratio = float(request.form['ag'])
        prediction = liverModel.predict([[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase,
                                        Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])

        if prediction == 1:
            return render_template('liver.html', prediction_text="You have liver Problem")
        else:
            return render_template('liver.html', prediction_text="You don't have liver Problem")
    else:
        return render_template('liver.html')


if __name__ == '__main__':
    app.run(debug=True)
