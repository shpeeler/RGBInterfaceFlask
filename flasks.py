from raspi.raspiutil import RaspiUtil
from raspi.sched.action import Action
from raspi.sched.day import Day
from raspi.sched.place import Place
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

        if request.form.get('living'):
            RGBInterface.send_values(0, r, g, b, l)
        if request.form.get('pc'):
            RGBInterface.send_values(1, r, g, b, l)
        if request.form.get('bed'):
            RGBInterface.send_values(2, r, g, b, l)

    return render_template('rgb.html')

@app.route('/sched', methods = ['POST', 'GET'])
def sched():

    if(request.method == 'POST'):
        action = None
        time = None
        days = list()
        places = list()

        # determine time 
        time = request.form['task']
        
        # determine action make this a dropdown
        if request.form.get('led_on'):
            action = Action.LED_ON

        if request.form.get('led_off'):
            action = Action.LED_OFF

        # determine days
        if request.form.get('mon'):
            days.append(Day.MONDAY)

        if request.form.get('tu'):
            days.append(Day.TUESDAY)

        if request.form.get('wed'):
            days.append(Day.WEDNESDAY)

        if request.form.get('th'):
            days.append(Day.THURSDAY)

        if request.form.get('fr'):
            days.append(Day.FRIDAY)

        if request.form.get('sat'):
            days.append(Day.SATURDAY)

        if request.form.get('sun'):
            days.append(Day.SUNDAY)

        # determine place
        if request.form.get('living'):
            places.append(Place.LIV)

        if request.form.get('pc'):
            places.append(Place.PC)

        if request.form.get('bed'):
            places.append(Place.BED)

        print("{} {} {} {}".format(action, time, days, places))
        
        raspiutil.sched(action, time, days, places)
        tasks = raspiutil.tasks # TODO: add  this to new render temp 

        print(len(tasks))

    return  render_template('sched.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
