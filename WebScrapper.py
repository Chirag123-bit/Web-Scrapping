from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=36.37410569300005&lon=-119.27022999999997")
content = page.content
soup = BeautifulSoup(content, "html.parser")
#print(soup)
week = soup.find_all(class_ = "tombstone-container")
#print(week)

#print(week[1].find(class_ = "period-name").get_text())
#print(week[0].find(class_ = "short-desc").get_text())
#print(week[0].find(class_ = "temp").get_text())

period_names = [item.find(class_="period-name").get_text() for item in week]
short_descs = [item.find(class_="short-desc").get_text() for item in week]
temps = [item.find(class_="temp").get_text() for item in week]

#print(period_names, "\n",short_descs,"\n" ,temps)

weather = pd.DataFrame({
                            "Periods":period_names,
                            "Short Description": short_descs,
                            "Temperature":temps
                        })
tim = datetime.datetime.now()
print("\t","\t" f"Weather Update for: {tim.strftime('%x')}" ,"\t", "\t")
print("\n")
print(weather)

