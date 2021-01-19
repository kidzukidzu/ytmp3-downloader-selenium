import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

currentDirectory = os.getcwd()
directory = "mp3"
path = os.path.join(currentDirectory, directory) 
if not os.path.isdir(path):
    print('Membuat folder mp3')
    os.mkdir(path)

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--headless")
prefs = {"download.default_directory" : path}
chromeOptions.add_experimental_option("prefs",prefs)

url = input("Masukkan url youtube: ")
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get("https://ytmp3.cc/en13/")
input = driver.find_element_by_id("input")
input.send_keys(url)
input.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
driver.find_element_by_link_text("Download").click()
print("Tunggu sampai file crdownload berubah menjadi file mp3 di folder mp3")