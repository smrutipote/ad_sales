from flask import Flask, request, jsonify, render_template
from app_file.utils import AdSales
import config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_sales', methods = ['POST'])
def prediction_sale():
    data = request.form
    tv = float(data['tv'])
    radio = float(data['radio'])
    social_media = float(data['social_media'])
    influencer = data['influencer']
    
    obj = AdSales(tv,radio,social_media,influencer)
    predict = obj.get_prediction()
    
    return jsonify({"The sales prediction due to advertisements is": predict})

if __name__ == "__main__":
    app.run(host = '0.0.0.0' , port = config.PORT_NUMBER,debug = False )