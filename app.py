from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/api/<term>/<start>", methods=['GET'])
def get_images(term, start):
  print(term, start)
  total = []
  request = requests.get(f"https://www.google.com/search?q={term}&tbm=isch&tbs=isz:lt,islt:qsvga&num=18&start={start}&imgtype=photo")
  soup = BeautifulSoup(request.text, "html.parser")
  images = soup.find_all("img",{"class":"t0fcAb"})
  for image in images:
    total.append(image["src"])
  return jsonify(total)

@app.route("/")
def index():
  return "<h1>Do you wanna Google Image? 🤔<h1>"
  
if __name__ == "__main__":
  app.run(threaded=True, port=3000,host="172.30.60.103")
