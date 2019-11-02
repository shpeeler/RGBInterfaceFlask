from raspi.raspiutil import RaspiUtil
from flask import Flask, render_template, request
from jinja2 import Template
import jinja2

# flask setup

app = Flask(__name__, static_folder='./static')

# jinja setup
templateLoader = jinja2.FileSystemLoader(searchpath="/templates/")
templateEnv = jinja2.Environment(loader=templateLoader)

# rapsi setup

raspiutil = RaspiUtil()
RGBInterface = raspiutil.get_rgbinterface()

# routes

@app.route('/')
def hello():
    return 

@app.route('/rgb', methods = ['POST', 'GET'])
def rgb():
    
    if(request.method == 'POST'):
        r = request.form['r']
        g = request.form['g']
        b = request.form['b']
        l = request.form['l']
        # position = request.form['p']

        RGBInterface.send_values(0, r, g, b, l)

    return render_template('rgb.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)