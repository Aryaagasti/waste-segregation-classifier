from flask import render_template, request
from app import app
from app.classifier import classify_waste, get_tips

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    material_type = request.form['material_type']
    decomposition_time = int(request.form['decomposition_time'])
    source = request.form['source']

    classification = classify_waste(material_type, decomposition_time, source)
    tips = get_tips(classification)

    return render_template('result.html', classification=classification, tips=tips)

@app.route('/tree')
def tree():
    return render_template('tree.html')