# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:18:43 2019

testsuite with several tests
testing eggtimer 
1 - testing main function: entering user input time, eggtimer start, expected result?
2 - browser compatibility in firefox, ie, chrome -> run same test on different browsers
3 - testing for input of negative numbers
4 - testing for input of only letters
5 - minimizing / maximizing window size
6 - checking windows size

Firefox integration test1 

test steps:
call eggtimer in firefox - type in textfield 3 seconds - press go-Button.
Proof of successful eggtimer is shown with screenshots. This can be improved with ExpectedCondition-commands.
In general the timer could be substituted by ExpectedCondition-commands.

Firefox integration test2

test steps:
call eggtimer in firefox - type in textfield 30 seconds - press go-Button.
checks on minimising and maximising the browser and setting own window size and if the text is still properly shown
Proof of successful eggtimer is shown with screenshots. This can be improved with ExpectedCondition-commands.
In general the timer could be substituted by ExpectedCondition-commands.


Internet explorer integration test

test steps:
call eggtimer in internetxplorer - type in textfield "Minutes" - press go-Button.
Purpose to check compatibility in internetexplorer & string values (letters). -> If it does not work, it should bring an error message.
Due to the timer (rendering purpose) it is to be seen that it is possible to type in only letters, but the timer is 
instantly expired.
Proof of successful eggtimer is shown with screenshots. This can be improved with ExpectedCondition-commands.
In general the timer could be substituted by ExpectedCondition-commands.
Note that the time is submitted with the enter key not with click on GO-Button.
For testing the internet explorer make sure the internet safety settings are set all in the same zone.

chrome integration test
test steps:
call eggtimer in chrome - type in textfield "-30 Minutes" - press go-Button.
Purpose to check compatibility in chrome & Negative Values. -> If it does not work, it should bring an error message.
Due to the timer (rendering purpose) it is to be seen that it is possible to type in negative values, but the timer is 
instantly expired.
Proof of successful test is shown with screenshots. This can be improved with ExpectedCondition-commands.
In general the timer could be substituted by ExpectedCondition-commands.
Problems with the chromedriver occured while writing the code. The chromedriver needs to be set up correctly so it
works with the systems chrome browser (which was not the case while testautomation writing).

In general this exercise (creating unittests) should be coded object orientated. With importing unittest, more tests could
be performed and a test report with how many test cases etc. could be printed. 

Currently I am working on Embedded System testing. We are starting the automation work and setting up framework using OOP.
Next weeks I will be reviewing and verifying the code at my current job. 

@author: christian spindler
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


input_Time1 = "3 seconds"
input_Time2 = "30 seconds"
input_Minutes = "-10 Minutes"
input_Letters = "Minutes"
screenshot_Link = "C:\\Users\\chris\\Documents\\xingguthubchallenge" #type in the patch where pictures shall be saved


######################
###MOZILLA FIREFOX1###
######################
        
driver = webdriver.Firefox(executable_path="E:\Programme\Geckodriver\geckodriver-v0.24.0-win64\geckodriver") #define remote server
driver.get("http://e.ggtimer.com")    # opens browser with url

time.sleep(5)   #delay to load browser

driver.get_screenshot_as_file(screenshot_Link + "\\callFirefox1.png") #screenshot start browser Firefox

driver.find_element_by_id("start_a_timer").clear() #removes any values from text input field
time.sleep(5)   #delay
driver.find_element_by_id("start_a_timer").send_keys(input_Time1) #defined user input time
#driver.find_element_by_id("start_a_timer").send_keys(Keys.ENTER)    #hits enter buton
driver.get_screenshot_as_file(screenshot_Link + "\\inputTime_firefox1.png") #screenshot with inputtime
driver.find_element_by_id("timergo").click()    #mouseclick

time.sleep(6)       #delay until time is definitely up -> improved testing with expectedconditions + function that controls the real time!
driver.get_screenshot_as_file(screenshot_Link + "\\firefox_expired1.png") #screenshot with expired clock

time.sleep(3)   #wait for screenshot and close driver
#driver.send_keys(Keys.ENTER)

driver.quit()

print ("first test case done")

######################
###MOZILLA FIREFOX2###
######################
        
driver = webdriver.Firefox(executable_path="E:\Programme\Geckodriver\geckodriver-v0.24.0-win64\geckodriver") #define remote server
driver.get("http://e.ggtimer.com")    # opens browser with url

time.sleep(5)   #delay to load browser

driver.get_screenshot_as_file(screenshot_Link + "\\callFirefox2.png") #screenshot start browser Firefox

driver.find_element_by_id("start_a_timer").clear() #removes any values from text input field
time.sleep(5)   #delay
driver.find_element_by_id("start_a_timer").send_keys(input_Time2) #defined user input time
#driver.find_element_by_id("start_a_timer").send_keys(Keys.ENTER)    #hits enter buton
driver.get_screenshot_as_file(screenshot_Link + \\inputTime_firefox2.png") #screenshot with inputtime
driver.find_element_by_id("timergo").click()    #mouseclick

time.sleep(2)   #1 delay for rendering 
driver.get_screenshot_as_file(screenshot_Link + "\\max1.png") #screenshot max1
time.sleep(2)
driver.set_window_size(300, 300)    #change window size
driver.get_screenshot_as_file(screenshot_Link + "\\winsize.png") #screenshot win size300x300
time.sleep(2)
driver.minimize_window()
time.sleep(1)   #2 delay for minimizing + screenshot
driver.get_screenshot_as_file(screenshot_Link + "\\min.png") #screenshot min
driver.maximize_window()
time.sleep(1)   #3 delay for maximizing + screenshot
driver.get_screenshot_as_file(screenshot_Link + "\\max2.png") #screenshot max2
time.sleep(20)   #wait for expiring eggtimer
driver.get_screenshot_as_file(screenshot_Link + "\\firefox_expired2.png") #screenshot with expired clock


time.sleep(3)   #wait for screenshot and close driver
#driver.send_keys(Keys.ENTER)

driver.quit()

print("firefox test done.")

######################
###INTERNET EXPLORER##
######################


driver = webdriver.Ie(executable_path="E:\Programme\Browser-Treiber Testautomatisierung\internet explorer\IEDriverServer_x64_3.14.0\IEDriverServer.exe")
driver.get("http://e.ggtimer.com")    # opens browser with url

time.sleep(5)   #delay to load browser

driver.get_screenshot_as_file(screenshot_Link + "\\callie.png") #screenshot start browser Firefox

driver.find_element_by_id("start_a_timer").clear() #removes any values from text input field
time.sleep(5)   #delay
driver.find_element_by_id("start_a_timer").send_keys(input_Minutes) #defined user input time
driver.get_screenshot_as_file(screenshot_Link + "\\inputTime_ie.png") #screenshot with inputtime
driver.find_element_by_id("start_a_timer").send_keys(Keys.ENTER)    #hits enter buton

#driver.find_element_by_id("timergo").click()    #mouseclick


time.sleep(6)   #wait for expiring eggtimer
driver.get_screenshot_as_file(screenshot_Link + "\\ie_expired.png") #screenshot with expired clock


time.sleep(3)   #wait for screenshot and close driver
#driver.send_keys(Keys.ENTER)

driver.quit()

print("ie test done.")


######################
####GOOGLE CHROME#####
######################



driver = webdriver.Chrome(executable_path="E:\Programme\Browser-Treiber Testautomatisierung\chrome\chromedriver_win32\chromedriver.exe")
driver.get("http://e.ggtimer.com")    # opens browser with url

time.sleep(5)   #delay to load browser

driver.get_screenshot_as_file(screenshot_Link + "\\callchrome.png") #screenshot start browser Firefox

driver.find_element_by_id("start_a_timer").clear() #removes any values from text input field
time.sleep(5)   #delay
driver.find_element_by_id("start_a_timer").send_keys(input_Letters) #defined user input time
#driver.find_element_by_id("start_a_timer").send_keys(Keys.ENTER)    #hits enter buton
driver.get_screenshot_as_file(screenshot_Link + "\\inputTime_chrome.png") #screenshot with inputtime

driver.find_element_by_id("timergo").click()    #mouseclick

time.sleep(2)   #wait for expiring eggtimer
driver.get_screenshot_as_file(screenshot_Link + "\\chrome_expired.png") #screenshot with expired clock


time.sleep(3)   #wait for screenshot and close driver
#driver.send_keys(Keys.ENTER)

driver.quit()

print("chrome test done.")
