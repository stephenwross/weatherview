import urllib.request
import json
import sys
import configparser

def main():
    config = configparser.ConfigParser()
    config.read("weather.cfg")
    rloc=config.get("Defaults", "DefaultLoc")
    rkey=config.get("Defaults",  "Key")
    print(rloc)
    if len(sys.argv)>1:
        rloc=sys.argv[1]
    getForecast(rloc,  rkey)

def getForecast(loc,  key):
    f = urllib.request.urlopen('http://api.wunderground.com/api/'+key+'/geolookup/forecast10day/q/'+loc+'.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']+', '+parsed_json['location']['state']
    print("10-Day forecast for "+location+":")
    for x in range(0, 9):
        print(
        parsed_json['forecast']['simpleforecast']['forecastday'][x]['date']['weekday_short']+': '+
        parsed_json['forecast']['simpleforecast']['forecastday'][x]['high']['fahrenheit']+'/'+
        parsed_json['forecast']['simpleforecast']['forecastday'][x]['low']['fahrenheit']+ ' -- '+
        parsed_json['forecast']['simpleforecast']['forecastday'][x]['conditions']
        )
    f.close()

if __name__ == "__main__":
    main()
