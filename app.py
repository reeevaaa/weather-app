from flask import Flask,render_template,request
from weather import main as get_weather

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        city_name = request.form['city_name']
        state_name = request.form['state_name']
        country_name = request.form['country_name']
        
        print(get_weather(city_name, state_name, country_name))
        
        return render_template('index.html', weather=get_weather(city_name, state_name, country_name))
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True,use_reloader=False)
