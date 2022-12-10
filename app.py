from flask import Flask, render_template, request
from sense_hat import SenseHat 
#Copy and paste imports

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)
z = (50, 50, 50)

rmon3 = [w, w, w, c, w, w, w, w,
         c, w, w, c, w, w, c, w,             
         w, c, w, c, w, c, w, w,
         w, w, c, c, c, w, w, w,
         c, c, c, c, c, c, c, w,
         w, w, w, c, w, w, w, w,
         w, w, c, c, c, w, w, w,
         w, c, w, c, w, c, w, w]

rmon4 = [w, w, w, w, w, w, w, w,
         w, w, w, w, w, w, w, w,             
         w, w, y, r, y, w, w, w,
         w, y, o, o, o, r, y, w,
         y, r, o, o, o, o, y, w,
         y, r, o, o, o, o, y, w,
         y, r, w, w, w, r, y, w,
         y, r, w, r, w, r, y, w]

rmon5 = [w, w, w, w, w, w, w, w,
         w, w, d, d, w, d, w, w,             
         w, d, d, d, d, d, d, w,
         w, d, d, d, d, d, d, w,
         w, d, d, d, d, d, d, w,
         w, w, d, d, d, d, w, w,
         w, w, w, d, d, w, w, w,
         w, w, w, w, w, w, w, w]

rmon6 = [w, w, w, w, w, w, w, w,
         r, w, w, c, w, w, w, w,             
         w, r, c, c, c, w, w, w,
         w, c, r, c, c, c, w, w,
         w, c, c, r, c, c, w, w,
         w, c, c, c, r, c, w, w,
         w, w, c, c, c, r, w, w,
         w, w, w, w, w, w, r, w]

rmon7 = [w, w, w, w, w, w, w, w,
         w, w, w, c, w, w, w, w,             
         w, c, c, c, c, w, w, w,
         w, c, c, c, c, c, w, w,
         w, c, c, c, c, c, w, w,
         w, c, c, c, c, c, w, w,
         w, w, c, c, c, c, w, w,
         w, w, w, w, w, w, w, w]

rmon8 = [w, w, w, w, w, w, w, w,
         w, w, w, b, w, w, w, w,             
         w, w, w, b, w, w, w, w,
         w, w, w, b, w, w, w, w,
         w, b, b, b, b, b, w, w,
         w, w, b, b, b, w, w, w,
         w, w, w, b, w, w, w, w,
         w, w, w, w, w, w, w, w]

rmon9 = [w, w, w, r, w, w, w, w,
         w, w, r, r, r, w, w, w,             
         w, r, r, r, r, r, w, w,
         w, w, w, r, w, w, w, w,
         w, w, w, r, w, w, w, w,
         w, w, w, r, w, w, w, w,
         w, w, w, r, w, w, w, w,
         w, w, w, w, w, w, w, w]

rmon10 = [w, w, w, w, w, w, w, w,
         w, w, w, w, w, w, w, w,             
         w, w, y, w, w, y, w, w,
         w, w, y, w, w, y, w, w, 
         y, w, w, w, w, w, w, y,
         w, y, w, w, w, w, y, w,
         w, w, y, y, y, y, w, w,
         w, w, w, w, w, w, w, w]


sense = SenseHat()
sense.clear()

app = Flask(__name__)
#/ means home page of the host/


@app.route('/')
#Decorator receives request
def index():
    return render_template('index.html')
    
@app.route('/about')
#app captured request and gives the template index.html
def about():
    return render_template('about.html')

def get_temperature():
    temperature = sense.get_temperature()
    temperature = round(temperature)
    temperature = ((temperature/5)*9)+32
    print(temperature)
    return temperature

def get_humidity():
    humidity = sense.get_humidity()
    pressure = round(humidity)
    print(humidity)
    return humidity

def get_pressure():
    pressure = sense.get_pressure()
    pressure = round(pressure)
    print(pressure)
    return pressure



@app.route('/weather', methods=['POST'])

def weather():

    
    weather = request.form['dropdown']
    if weather == 'temperature':
        temperature = get_temperature()
        print(temperature)
        display = f'Temperature is {(str(round(temperature,2)))}°F'
        sense.show_message(display, text_colour=[0, 0, 255])
        if temperature < 0:
            sense.set_pixels(rmon3)
        elif temperature > 0 and temperature < 75:
            sense.set_pixels(rmon5)
        else:
            sense.set_pixels(rmon4)
        
    elif weather == 'humidity':
        humidity = get_humidity()
        print(humidity)
        display = f'Humidity is {(str(round(humidity,2)))}'
        sense.show_message(display, text_colour=[0, 0, 255])
        if humidity > 60:
            sense.set_pixels(rmon7)
        elif humidity < 30:
            sense.set_pixels(rmon6)
   
        
    elif weather == 'pressure':
        pressure = get_pressure()
        print(pressure)
        display = f'Pressure is {(str(round(pressure,2)))} mb'
        sense.show_message(display, text_colour=[0, 0, 255])
        if pressure < 900:
            sense.set_pixels(rmon8)
        elif pressure > 1000 and pressure > 1022:
            sense.set_pixels(rmon10)
        elif pressure > 1030:
            sense.set_pixels(rmon9)
    
 
    return render_template('weather.html')

  





#Accepts post request
    

    #display = f'{message}  Love, {name}'
    #sense.show_message(display, text_colour=[0, 0, 255])
    
    
    
    #returing received.html
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')