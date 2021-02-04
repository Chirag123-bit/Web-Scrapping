import pandas as pd
from bs4 import BeautifulSoup
import requests,datetime

website = requests.get("https://weather.com/weather/tenday/l/Kathmandu+Bagmati+Nepal?canonicalCityId=e6cced0f84834b544d382606d1d3944e60b6f1ef46782d49dfe5015f3a8d16d3")
contents = website.content
soup = BeautifulSoup(contents, "html.parser")
#print(soup.prettify())
weather_container = soup.find(class_ = "DaypartDetails--Content--XQooU DaypartDetails--contentGrid--3cYKg")
current_weather = (weather_container.find(class_ ="DailyContent--temp--_8DL5")).get_text()
current_time = (weather_container.find(class_ ="DailyContent--daypartDate--3MM0J")).get_text()
current_narrative = (weather_container.find(class_ ="DailyContent--narrative--3AcXd")).get_text()
"""print(current_time)
print(current_weather)"""

tms = soup.findAll(class_ = "Disclosure--themeList--uBa5q")
#weat = soup.findAll(class_ = "DetailsSummary--highTempValue--3x6cL")
#narra = soup.findAll(class_ = "DetailsSummary--extendedData--aaFeV")
time_weather = []
temp_weather = []
temp_low = []
summ_weather = []
for item in tms:
    try:
        time_weather.append(item.find(class_="DetailsSummary--daypartName--1Mebr").get_text())
        temp_weather.append(item.find(class_="DetailsSummary--highTempValue--3x6cL").get_text())
        temp_low.append(item.find(class_="DetailsSummary--lowTempValue--1DlJK").get_text())
        summ_weather.append(item.find(class_="DetailsSummary--extendedData--aaFeV").get_text())
    except:
        pass
temp_weather.pop(0)
temp_weather.insert(0,weather_container.find(class_ ="DailyContent--temp--_8DL5").get_text())


weather_db = pd.DataFrame({
                                "Date":time_weather,
                                "Temperature(High)":temp_weather,
                                "Temperature(Low)": temp_low,
                                "Prediction":summ_weather
                          })

weather_db.style.set_properties(**{'text-align': 'center'})

tim = datetime.datetime.now()
print("\t","\t" f"Weather Update for Kathmandu On: {tim.strftime('%x')}" ,"\t", "\t")
print("\n")
print(weather_db)