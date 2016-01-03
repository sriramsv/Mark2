import requests
import json,os
import speech
weather_data={}
from commands import RegexCommand
from config import coordinates
from utils.tts import speak

class WeatherCommand(RegexCommand):
    def __init__(self):
        """
        Build the basic regex command. Generate the regex without the help
        of regexcommand's init, since it combines polite and standalone sentences
        """
        regex="weather"
        super(WeatherCommand, self).__init__(regex,False)

    def on_event(self,event,sender):
        print event
        if self.match(event):
            req='http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}'.format(coordinates['LAT'],coordinates['LONG'])
            weather=requests.get(req,timeout=5)
            if weather.status_code==200:
                wdata=json.loads(weather.text)
                condition=wdata["weather"][0]["description"]
                temp=wdata["main"]["temp_max"]-273
                location=wdata["name"]
                print '{1} in {0} with temperature of {2} degree celcius'.format(location,condition,int(temp))
                # speech.say('{1} in {0} with temperature of {2} degree celcius'.format(location,condition,int(temp)))
                weather_data["location"]=location
                weather_data["condition"]=condition
                weather_data["temp"]=int(temp)
                speak('{1} in {0} with temperature of {2} degree celcius'.format(location,condition,int(temp)))
            else:
                speak('Could not fetch weather')
                return 'Could not fetch weather'
            return True