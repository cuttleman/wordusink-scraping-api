  
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

import requests
from bs4 import BeautifulSoup

def get_image_with_selenium(term, start_num):    
  chromeOptions = webdriver.ChromeOptions()
  # chromeOptions.add_argument("--headless")
  chromeOptions.add_argument("--no-sandbox")
  chromeOptions.add_argument("--disable-dev-shm-usage")
  chromeOptions.add_argument("--proxy-server=socks5://127.0.0.1:9150")
  chromeOptions.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Whale/2.9.115.16 Safari/537.36"')
  # chromeOptions.add_argument("--remote-debugging-port=9222")
  driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chromeOptions)

  crawled_images = []
  limit_count = 0

  try:
    driver.get(f"https://www.google.com/search?q={term}&tbm=isch&tbs=itp:photo")
    images = driver.find_elements_by_css_selector(".wXeWr.islib.nfEiy.mM5pbd")

    for idx,image in enumerate(images):
      # limit num = 18
      if( limit_count >= 1):
        break
      else:
        if (idx >= start_num):
          image.click()
          time.sleep(3)
          image_url = driver.find_element_by_css_selector(".tvh9oe.BIB1wf .n3VNCb").get_attribute("src")
          crawled_images.append(image_url)
          print(f"Success scrapped image - term: {term}, index: {start_num + limit_count}")
          limit_count = limit_count + 1
  except:
    pass
  
  driver.quit()

  return crawled_images


def get_image_with_bs(term, start_num):
  total = []
  request = requests.get(f"https://www.google.com/search?q={term}&tbm=isch&tbs=isz:lt,islt:qsvga&num=18&start={start_num}&imgtype=photo")
  soup = BeautifulSoup(request.text, "html.parser")
  images = soup.find_all("img",{"class":"t0fcAb"})
  for image in images:
    total.append(image["src"])
  print(f"Success scrapped raw_images - term: {term}, index: {start_num}")
  return total