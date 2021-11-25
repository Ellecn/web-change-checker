from urllib.request import urlopen
import datetime
import time

url = "https://www.example-shop.de/"
needle = "Auf Lager: 0".encode()

while True:
  print(datetime.datetime.now().strftime('%d.%m.%Y %H:%M') + ": Checking " + url + " ...")
  html = urlopen(url).read()
  if needle in html:
    print("No news")
  else:
    print("!!! NEWS !!!")
    break
  time.sleep(600)
