from flask import render_template, current_app as app, request, redirect
from werkzeug.utils import secure_filename
import json
import os, glob




with open("config.json", "r") as file:
    params = json.load(file)['params']

app.config['Upload_folder'] = params["uploadPath"]


# clear Data
def clearDara():
    for file in glob.glob('.//File//*.csv'):
        if not (file.endswith("normal.csv")):
            os.remove(file)



# Creating routes
@app.route('/')
def index():
    clearDara()
    return render_template('home.html')


@app.route('/test')
def test():
    clearDara()
    return render_template('test.html')


@app.route('/saveData', methods = ['POST'])
def model():
    ecg_file = request.files['ecg']

    if not ecg_file.filename.endswith('.csv'):
        return redirect('/error')
    
    data_path = f"{app.config['Upload_folder']}//{secure_filename(ecg_file.filename)}"
    ecg_file.save(data_path)
    print(f'[INFO] File is Saved by Name @ {data_path}')
    return redirect('/analysis/')
    

@app.errorhandler(500)
@app.errorhandler(404)
@app.errorhandler(409)
@app.route("/error")
def error(e):
    print("ERROR")
    return render_template("error.html"), 404

