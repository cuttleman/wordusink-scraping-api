from flask import Flask, jsonify
from crawling import get_image_with_bs,get_image_with_selenium
from threading import Thread
from multiprocessing import Pool
from itertools import chain

app = Flask(__name__)

@app.route("/api/<term>/<start>", methods=['GET'])
def get_images(term, start):
  pool = Pool(processes=3)
  from_googles = pool.starmap(get_image_with_selenium,[(term,int(start)),(term,int(start)+3),(term,int(start)+6)])
  return jsonify(list(chain.from_iterable(from_googles)))

@app.route("/")
def index():
  return "<h1>Do you wanna get Google Image? 🤔<h1>"
  
if __name__ == "__main__":
  app.run(port=3000, host="0.0.0.0")
  # host="172.30.59.85"
