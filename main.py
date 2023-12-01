import time
import requests
import selectorlib
from datetime import datetime

URL = "https://programmer100.pythonanywhere.com"

def scrape(url):
    request = requests.get(url)
    source = request.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("temp.yaml")
    value = extractor.extract(source)["temp"]
    return value

def store(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open("data.txt", "a") as file:
        content = f"{now},{extracted}"
        file.write(content + "\n")

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        store(extracted)
        print("Temperature recorded")
        time.sleep(2)