import urllib.request
import json
import sys
import configparser

def main():
    if len(sys.argv)>1:
        loc=sys.argv[1]
        print(getForecast(loc))
    else:
        print(getForecast())

def getForecast(loc=""):
    config = configparser.ConfigParser()
    config.read("weather.cfg")
    key = config.get("Defaults","Key")
    if loc == "": loc = config.get("Defaults","DefaultLoc")
    f = urllib.request.urlopen('http://api.wunderground.com/api/'+key+'/geolookup/forecast10day/q/'+loc+'.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    try:
        location = parsed_json['location']['city']+', '+parsed_json['location']['state']
    except:
        return "I don't know where "+loc+" is!"
    forecast = '10-Day forecast for ' + location + ':\n'
    for x in range(0, 9):
        forecast += (
        parsed_json['forecast']['simpleforecast']['forecastday'][x]['date']['weekday_short']+': '+
        parsed_json['forecast']['simpleforecast']['forecastday'][x]['high']['fahrenheit']+'/'+
        parsed_json['forecast']['simpleforecast']['forecastday'][x]['low']['fahrenheit']+ ' -- '+
        parsed_json['forecast']['simpleforecast']['forecastday'][x]['conditions']+'\n')
    return forecast
    f.close()

if __name__ == "__main__":
    main()
