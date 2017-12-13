from flask import Flask, render_template, request, jsonify
import weather

app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')

@app.route("/show_forecast")
def showForecast():
    loc = request.args.get('inputLoc', 0, type=str)
    print('In showForecast')
    print(weather.getForecast(loc))
    return jsonify(result=weather.getForecast(loc))

if __name__ == "__main__":
    app.run()
    
