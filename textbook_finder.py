from selenium import webdriver
from selenium.webdriver.common.by import By

print("Paste URL")

parse_start = "courseData="
parse_end = "&utm_source"
#user_url = input()
user_url = "https://umcp.bncollege.com/course-material-listing-page?utm_campaign=storeId=15551_langId=-1_courseData=CMSC_216_0401_202501%7CCMSC_250_0303_202501%7CHIST_187_0102_202501%7CMATH_240_0332_202501&utm_source=wcs&utm_medium=registration_integration"
parsed_url = user_url[user_url.index(parse_start) + len(parse_start) : user_url.index(parse_end)]
classes = parsed_url.split("%7C")
class_array = []

for c in classes:
    split_class = c.split("_")
    split_class.remove(split_class[3])
    class_array.append(split_class)

driver = webdriver.Firefox()
driver.get("https://umcp.bncollege.com/course-material/course-finder")
driver.set_window_size(1920, 1500)
driver.execute_script("document.body.style.transform='scale(.6)';")

for i in range(10):
    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[3]/div[1]/a[1]").click()

driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[1]/div/div/span[1]/span[1]/span").send_keys(u'\ue007')
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[1]/div/div/span[1]/span[1]/span").send_keys(u'\ue007')