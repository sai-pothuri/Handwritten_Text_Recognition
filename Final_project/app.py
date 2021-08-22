from flask import Flask, request, render_template
from predict_model import predict_model
import os
from werkzeug.utils import secure_filename

app= Flask(__name__)

model_path="Handwriting.model"

    
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        
        f = request.files['file']

        
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        
        preds = predict_model(file_path, model_path)
        result=preds
        return result
    return None

if (__name__=='__main__'):
    app.run(debug=True)