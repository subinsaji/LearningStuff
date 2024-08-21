import requests
import time

start_time = time.time()

def fetch(url):
    return requests.get(url).text

page_1 = fetch("https://www.monzo.com")
page_2 = fetch("http://www.linkedin.com")

print(f"Done in {time.time() - start_time} seconds")

