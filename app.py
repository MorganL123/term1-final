from flask import Flask, render_template, request
from sense_hat import SenseHat 
#Copy and paste imports

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
    temperature = round(temperature, 1)
    temperature = ((temperature/5)*9)+32
    print(temperature)
    return temperature

def get_humidity():
    humidity = sense.get_humidity()
    pressure = round(humidity, 1)
    print(humidity)
    return humidity

def get_pressure():
    pressure = sense.get_pressure()
    pressure = round(pressure, 1)
    print(pressure)
    return pressure

@app.route('/weather', methods=['POST'])

def weather():
    weather = request.form['dropdown']
    if weather == 'temperature':
        temperature = get_temperature()
        print(temperature)
        display = f'The temperature is {temperature}°F'
        sense.show_message(display, text_colour=[0, 0, 255])
        
    elif weather == 'humidity':
        humidity = get_humidity()
        print(humidity)
        display = f'The humidity is {humidity}'
        sense.show_message(display, text_colour=[0, 0, 255])
        
    elif weather == 'pressure':
        pressure = get_pressure()
        print(pressure)
        display = f'The pressure is {pressure}'
        sense.show_message(display, text_colour=[0, 0, 255])
        

    return render_template('weather.html')





#Accepts post request
    

    #display = f'{message}  Love, {name}'
    #sense.show_message(display, text_colour=[0, 0, 255])
    
    
    
    #returing received.html
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')