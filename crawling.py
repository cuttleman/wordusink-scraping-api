from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

def get_image(term, start_num):    
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Whale/2.9.115.16 Safari/537.36"')
  # chrome_options.add_argument("--remote-debugging-port=9222")

  driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
  driver.get(f"https://www.google.com/search?q={term}&tbm=isch&tbs=itp:photo")
  images = driver.find_elements_by_css_selector(".wXeWr.islib.nfEiy.mM5pbd")

  crawled_images = []
  limit_count = 0

  for idx,image in enumerate(images):
    if( limit_count > 18):
      break
    else:
      if (idx >= start_num):
        image.click()
        time.sleep(1)
        image_url = driver.find_element_by_css_selector(".tvh9oe.BIB1wf .n3VNCb").get_attribute("src")
        pattern = "^(data:image|https://encrypted-tbn0).*"
        result = re.match(pattern, image_url)
        if result:
          continue
        else:
          crawled_images.append(image_url)
          limit_count = limit_count + 1

  return crawled_images