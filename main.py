from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyfiglet
from os import system
import time

system('cls && title [TikTok Views By Wazo#0001]')

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
driver.set_window_size(150, 380)

i = 0
a = 0
x = 0

def loop1():
    global i
    time.sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
        driver.set_window_position(-10000,0)
    except:
        print("Captcha...")
        driver.refresh()
        loop1()
    try:
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/input").send_keys(vidUrl)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/div/button").click()
        time.sleep(8)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        time.sleep(10)
        driver.refresh()
        i += 1
        total = i * 1000
        time.sleep(45)
        loop1()
    except:
        print("Error...")
        driver.refresh()
        loop1()

def loop2():
    pass

def loop3():
    pass

def loop4():
    pass

system("cls")
print(' __        __     _      _____   ___     __     __  ___   _____  __        __  ____  ')
print(' \ \      / /    / \    |__  /  / _ \    \ \   / / |_ _| | ____| \ \      / / / ___| ')
print('  \ \ /\ / /    / _ \     / /  | | | |    \ \ / /   | |  |  _|    \ \ /\ / /  \___ \ ')
print('   \ V  V /    / ___ \   / /_  | |_| |     \ V /    | |  | |___    \ V  V /    ___) |')
print('    \_/\_/    /_/   \_\ /____|  \___/       \_/    |___| |_____|    \_/\_/    |____/ ')
print ('')
vidUrl = input('[>] TikTok Video URL: ')
print("")

bot = 1

driver.get("https://vipto.de/")

if bot == 1:
    loop1()
elif bot == 2:
    pass
elif bot == 3:
    pass
else:
    pass
