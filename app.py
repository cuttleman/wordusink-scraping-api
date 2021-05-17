from flask import Flask, jsonify
from scrapper import get_image_with_bs,get_image_with_selenium
from threading import Thread
from multiprocessing import Pool
from itertools import chain
import time

app = Flask(__name__)

@app.route("/api/<term>/<start>", methods=['GET'])
def get_images(term, start):
  # 멀티 프로세싱 with 셀레니움
  start_time = time.time()
  # pool = Pool(processes=6)
  # from_googles = pool.starmap(get_image_with_selenium,[(term,int(start)),(term,int(start)+1),(term,int(start)+2),(term,int(start)+3),(term,int(start)+4),(term,int(start)+5)])
  from_googles = get_image_with_bs(term, int(start))
  print("--- %s seconds ---" % (time.time() - start_time))
  # return jsonify(list(chain.from_iterable(from_googles)))
  return jsonify(from_googles)

@app.route("/")
def index():
  return "<h1>Do you wanna get Google Image? 🤔<h1>"
  
if __name__ == "__main__":
  app.run(port=3000, host="0.0.0.0")
  # host="172.30.59.85"
