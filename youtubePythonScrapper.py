
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data=[]
with Chrome() as driver:
    wait = WebDriverWait(driver,5)
    driver.get("https://www.youtube.com/watch?v=kuhhT_cBtFU&t=2s")
for item in range(200): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME,"body"))).send_keys(Keys.END)
        time.sleep(10)
for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
        data.append(comment.text)


import pandas as pd   
df = pd.DataFrame(data, columns=['comment'])
df.head()
