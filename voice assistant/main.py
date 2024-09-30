import subprocess
import wolframalpha
import json
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import ctypes
import time
import requests
from ecapture import ecapture as ec

from urllib.request import urlopen
from command import speak, wishMe, username, takeCommand

if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Kavish.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:

            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Kavish. further It's a secret")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Kavish")

        elif 'reason for you' in query:
            speak("I was created as a Internship project by Mister Kavish ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")


        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org/v1/articles?source = the-times-of-india&sortBy = top&apiKey =\\times 
                    of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))


        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "jarvis" in query:

            wishMe()
            speak("Jarvis 1 point o in your service Mister")
            speak(assname)

        elif "weather" in query:
            api_key = "a611d1d1ffafdd662242db723143ef81"
            base_url = "http://api.openweathermap.org/data/2.5/weather?q="
            speak("Please tell me the city name.")
            print("City name: ")

            city_name = takeCommand()  # Assumes takeCommand() is a function to get user input
            complete_url = base_url + city_name + "&appid=" + api_key

            try:
                # Request weather data from the API
                response = requests.get(complete_url)
                x = response.json()

                # Safely checking if 'cod' key exists and its value is not "404" (correct key for the response code is "cod")
                if x.get("cod") != "404":
                    # Access nested data safely
                    y = x.get("main", {})
                    current_temperature = y.get("temp", "N/A")
                    current_pressure = y.get("pressure", "N/A")
                    current_humidity = y.get("humidity", "N/A")
                    # Access weather description
                    z = x.get("weather", [{}])
                    weather_description = z[0].get("description", "No description available")
                    # Display weather information
                    print(
                        f"Temperature (in kelvin unit) = {current_temperature}\n"

                        f"Atmospheric pressure (in hPa unit) = {current_pressure}\n"
                        
                        f"Humidity (in percentage) = {current_humidity}\n"
                        
                        f"Description = {weather_description}"
                    )
                    # Optional: Speak out the weather details if your system supports it
                    speak(f"The current temperature is {current_temperature} kelvin, "
                          f"atmospheric pressure is {current_pressure} hPa, "
                          f"humidity is {current_humidity} percent, "
                          f"and the weather is described as {weather_description}.")
                else:
                    # City not found error handling
                    speak("City not found. Please check the city name and try again.")
            except requests.exceptions.RequestException as e:
                # Handle exceptions related to network or request issues
                print(f"Error fetching data: {e}")
                speak("There was an error fetching the weather data. Please try again later.")

        elif "wikipedia" in query:
            search_term = query.replace("wikipedia", "").strip()

            if search_term:
                # Try to handle the Wikipedia search using the wikipedia library
                try:
                    page = wikipedia.page(search_term)
                    print(page.summary)
                except wikipedia.exceptions.DisambiguationError as e:
                    print(f"Ambiguous search term. Automatically selecting the first result: {e.options[0]}")
                    # Automatically pick the first disambiguation option
                    page = wikipedia.page(e.options[0])
                    print(page.summary)

                # Open the search term on Wikipedia in the browser
                url = f"https://en.wikipedia.org/wiki/{search_term.replace(' ', '_')}"
                webbrowser.open(url)
            else:
                # If no search term is provided, open the Wikipedia homepage
                webbrowser.open("https://www.wikipedia.org/")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(assname)

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "what is" in query or "who is" in query:

            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

    # elif "" in query:
    # Command go here
    # For adding more commands
