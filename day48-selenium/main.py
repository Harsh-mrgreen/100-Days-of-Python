from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/msi/chromedriver.exe" 
driver = webdriver.Chrome(executable_path= chrome_driver_path)
driver.get(url="https://www.flipkart.com/acer-21-5-inch-full-hd-ips-panel-white-colour-monitor-ha220q/p/itmfdfdjxg7gdzpf?pid=MONFDFDJVFMGY9NV&lid=LSTMONFDFDJVFMGY9NVV7ABPJ&marketplace=FLIPKART&store=6bo%2Fg0i%2F9no&srno=b_1_6&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&fm=organic&iid=3a1cecaf-11aa-4c56-bd5a-4640f84bcf71.MONFDFDJVFMGY9NV.SEARCH&ppt=hp&ppn=homepage&ssid=4jmmkrvh1c0000001649145083369")
prices = driver.find_elements(by= By.CLASS_NAME, value= "_30jeq3 _16Jk6d")
print(prices)
# for price in prices:
#     print(price.text)
driver.close() # this will close the partuclar tab
#driver.quit() this will close the entire browser

