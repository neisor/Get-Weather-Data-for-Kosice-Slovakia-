# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:37:00 2019

@author: Antonio Raffaele Iannaccone
"""

import requests
import re
from bs4 import BeautifulSoup

#Get the HTML of the main Microsoft website with a button to download
url = "https://www.foreca.com/Slovakia/Kosice"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

"""
HERE STARTS THE SEARCHING VIA BEAUTIFULSOUP4
"""

#Find the temperature text on a website
soup_temperature = soup.find('span', attrs={'class':'warm txt-xxlarge'})

#Find the feels like text on a website
soup_general_weather_data = soup.find('div', attrs={'class':'right txt-tight'})
#print(soup_general_weather_data)

"""
HERE STARTS THE SEARCHING AND FINDING FOR THE ELEMENTS
"""

#Find the temperature text (strip it via RegEx)
soup_temperature_text = re.findall('strong>(.*)</strong>', str(soup_temperature))

#Find the temperature text (strip it via RegEx)
soup_feelslike_text = re.findall('Feels Like: <strong>(.*)</strong>', str(soup_general_weather_data))

#Find the general weather text (strip it via RegEx)
soup_weather_text = re.findall('<div class=\"right txt-tight\">\r\n(.*)<br\/>', str(soup_general_weather_data), re.MULTILINE)

#Find the humidity text (strip it via RegEx)
soup_humidity_text = re.findall('Humidity:   <strong>(.*)<\/strong>', str(soup_general_weather_data), re.MULTILINE)

#Find the visibility text (strip it via RegEx)
soup_visibility_text = re.findall('Visibility: <strong>(.*)<\/strong>', str(soup_general_weather_data), re.MULTILINE)

"""
HERE STARTS THE REGEXING OF THE FOUND ELEMENTS AND STRIPPING THEM FROM THE UNNEEDED CHARACTERS
"""

#Convert the regexed temperature text from a list to a string
soup_temperature_text_string = ''.join(soup_temperature_text)

#Convert the regexed temperature text from a list to a string
soup_feelslike_text_string = ''.join(soup_feelslike_text)

#Convert the regexed temperature text from a list to a string
soup_weather_text_string = ''.join(soup_weather_text)
soup_weather_text_string = re.sub("(\t)", "", soup_weather_text_string)
soup_weather_text_string = re.sub("( )", "", soup_weather_text_string)

#Convert the regexed temperature text from a list to a string
soup_humidity_text_string = ''.join(soup_humidity_text)

#Convert the regexed visibility text from a list to a string
soup_visibility_text_string = ''.join(soup_visibility_text)

print('Temperature: ' + soup_temperature_text_string + "°C")
print('Feels like: ' + soup_feelslike_text_string + "C")
print('Weather: ' + soup_weather_text_string)
print('Humidity: ' + soup_humidity_text_string)
print('Visibility: ' + soup_visibility_text_string)