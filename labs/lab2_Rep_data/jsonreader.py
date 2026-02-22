# Program : jsonreader.py
# This program prints json to the console
# Author: Hewa Orang

import requests

URL = "https://www.gov.uk/bank-holidays.json"
response = requests.get(URL)
data = response.json()
print(data['northern-ireland']['events'][0])
