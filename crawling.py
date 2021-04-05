from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

import requests
from bs4 import BeautifulSoup

def get_image_with_selenium(term, start_num):    
  fireFoxOptions = webdriver.FirefoxOptions()
  # fireFoxOptions.add_argument("--headless")
  fireFoxOptions.add_argument("--no-sandbox")
  fireFoxOptions.add_argument("--disable-dev-shm-usage")
  fireFoxOptions.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Whale/2.9.115.16 Safari/537.36"')
  # fireFoxOptions.add_argument("--remote-debugging-port=9222")

  driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=fireFoxOptions)

  driver.get(f"https://www.google.com/search?q={term}&tbm=isch&tbs=itp:photo")
  images = driver.find_elements_by_css_selector(".wXeWr.islib.nfEiy.mM5pbd")

  crawled_images = []
  limit_count = 0

  for idx,image in enumerate(images):
    if( limit_count >= 18):
      break
    else:
      if (idx >= start_num):
        image.click()
        time.sleep(1.5)
        image_url = driver.find_element_by_css_selector(".tvh9oe.BIB1wf .n3VNCb").get_attribute("src")
        crawled_images.append(image_url)
        limit_count = limit_count + 1
  
  driver.close()

  return crawled_images

def get_image_with_bs(term, start_num):
  total = []
  request = requests.get(f"https://www.google.com/search?q={term}&tbm=isch&tbs=isz:lt,islt:qsvga&num=18&start={start_num}&imgtype=photo")
  soup = BeautifulSoup(request.text, "html.parser")
  images = soup.find_all("img",{"class":"t0fcAb"})
  for image in images:
    total.append(image["src"])
  return total