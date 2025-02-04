from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

enter = "u'\ue007'"
parse_start = "courseData="
parse_end = "&utm_source"

print("Paste URL")
user_url = "https://umcp.bncollege.com/course-material-listing-page?utm_campaign=storeId=15551_langId=-1_courseData=CMSC_216_0401_202501%7CCMSC_250_0303_202501%7CHIST_187_0102_202501%7CMATH_240_0332_202501&utm_source=wcs&utm_medium=registration_integration"
#user_url = input()

parsed_url = user_url[user_url.index(parse_start) + len(parse_start) : user_url.index(parse_end)]
classes = parsed_url.split("%7C")
class_array = []

for c in classes:
    split_class = c.split("_")
    split_class.remove(split_class[3])
    class_array.append(split_class)

driver = webdriver.Firefox()
driver.get("https://umcp.bncollege.com/course-material/course-finder")
driver.set_window_size(1920, 1500) # large y axis stops bugs with trying to interact with buttons offscreen
driver.execute_script("document.body.style.transform='scale(.5)';") # keeps all buttons on screen better
sleep(.5)

# add another course button
for i in range(len(class_array) - 4):
    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[3]/div[1]/a[1]").click()

for i in range(len(class_array)):
    index = i + 2

    # term
    css_sel = f"div.bned-register-section:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2) > span:nth-child(1) > span:nth-child(1)" 
    driver.find_element(By.CSS_SELECTOR, css_sel).send_keys(enter)
    driver.find_element(By.CSS_SELECTOR, css_sel).send_keys(enter)

    # department
    sleep(.3)
    css_sel = f"div.bned-register-section:nth-child({index}) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2) > span:nth-child(1) > span:nth-child(1) > span:nth-child(2)"
    char_array = list(class_array[i][0])
    driver.find_element(By.CSS_SELECTOR, css_sel).click()
    sleep(.1)
    textbox = driver.find_element(By.CSS_SELECTOR, ".select2-search__field")
    textbox.send_keys(char_array[0]) 
    textbox.send_keys(char_array[1])
    textbox.send_keys(char_array[2])
    textbox.send_keys(char_array[3])
    driver.find_element(By.CSS_SELECTOR, css_sel).send_keys(enter)

    # course number
    sleep(.3)
    css_sel = f"div.bned-register-section:nth-child({index}) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2) > span:nth-child(1) > span:nth-child(1)"
    driver.find_element(By.CSS_SELECTOR, css_sel).click()
    sleep(.1)
    textbox = driver.find_element(By.CSS_SELECTOR, ".select2-search__field")
    char_array = list(class_array[i][1])
    textbox.send_keys(char_array[0]) 
    textbox.send_keys(char_array[1])
    textbox.send_keys(char_array[2])
    driver.find_element(By.CSS_SELECTOR, css_sel).send_keys(enter)

    # section
    sleep(.3)
    css_sel = f"div.bned-register-section:nth-child({index}) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2) > span:nth-child(1) > span:nth-child(1) > span:nth-child(2)"
    driver.find_element(By.CSS_SELECTOR, css_sel).click()
    sleep(.1)
    textbox = driver.find_element(By.CSS_SELECTOR, ".select2-search__field")
    char_array = list(class_array[i][2])
    textbox.send_keys(char_array[0]) 
    textbox.send_keys(char_array[1])
    textbox.send_keys(char_array[2])
    textbox.send_keys(char_array[3])
    driver.find_element(By.CSS_SELECTOR, css_sel).send_keys(enter)

# retrieve materials button
driver.find_element(By.CSS_SELECTOR, "div.bned-campus-form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > a:nth-child(1)").click()

##################

