from raspi.rgbinterface import RGBInterface
from flask import Flask, render_template, request
from jinja2 import Template
import jinja2

app = Flask(__name__)

#
templateLoader = jinja2.FileSystemLoader(searchpath="/templates/")
templateEnv = jinja2.Environment(loader=templateLoader)

ri = RGBInterface()

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
        p = request.form['p']

        ri.update_colors(r, g, b, l, p)

    return render_template('rgb.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)