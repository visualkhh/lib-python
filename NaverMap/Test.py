
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

"""
 from pywinauto import application
from pywinauto.findwindows import find_windows
from cThread import cThread
"""

import time
import os




#caps = DesiredCapabilities.INTERNETEXPLORER
#caps['ignoreProtectedModeSettings'] = True
'''
browser = webdriver.Chrome()
'''

caps = DesiredCapabilities.INTERNETEXPLORER
caps['ignoreProtectedModeSettings'] = True
browser = webdriver.Ie(capabilities=caps)
'''
'''
browser.get("http://map.naver.com/?menu=route&mapMode=3&lat=37.5891133&lng=127.036109&dlevel=7&slng=127.0424375&slat=37.6628154&sdid=p18624897&elng=126.9964383&elat=37.5154772&edid=s18764688&pathType=2&dtPathType=0&sText=67Cp7ZWZ7IKs6rGw66as&eText=67CY7Y%2Bs64yA6rWQ&enc=b64")

print browser.title;


time.sleep(4);

'''
print browser.find_element_by_id("loginframe")
'''
'''
browser.switch_to_frame(browser.find_element_by_id("loginframe"));
element = browser.find_element_by_id("id")
element.send_keys("bunker09")
element = browser.find_element_by_id("pw")
element.send_keys("pwd")
element.send_keys(Keys.RETURN)
time.sleep(2);
'''
#browser.switch_to_frame(browser.find_element_by_id("minime"));
#element = browser.find_element_by_id("mail_count_profile");
element = browser.find_element_by_css_selector("#panel > div.panel_content.nano.has-scrollbar > div.scroll_pane.content > div.panel_content_flexible > div.fw_list.fwb_list > ul")
elementList = element.find_elements_by_tag_name("li");
for e in elementList:
    webdriver.ActionChains(browser).move_to_element(e).click(e).perform()
    #e.click();
    #print e.get_attribute('innerHTML'); 
#print 'MAIL COUNT: ' + element.get_attribute('innerHTML') 

