#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from time import sleep

# only required to crop screenshots to show an element of interest
# from PIL import Image

class Clicker:      
    
    def get_check(self, address):
        print("[+] Getting address: " + address)
        self.driver.get(address)
        title = self.driver.title
        print("[i] " + title)
        
        if title == "Attention Required! | Cloudflare":
            print("[!] Cloudflare protection enabled; quitting")
            self.close_driver()

    def click(self, selector):
        print("[+] Clicking selector: " + selector)
        
        # old method
        # button = self.driver.find_element_by_css_selector(selector)
        
        button = self.driver.find_element(By.CSS_SELECTOR, selector)
        try:
            self.ac.move_to_element(button)
            button.click()
        except:
            script = "document.querySelector('"+selector+"').click()"
            print("[+] Resorting to javascript: " + script)
            self.driver.execute_script(script)
        print("[i] " + self.driver.title)
        
    def get_click(self, address, selector):
        self.get_check(address)
        self.click(selector)

    def get_click_multiple(self, address, selector, times):
        self.get_check(address)
        for i in range(0, times):
            self.click(selector)

    def get_multiple(self, addresses):
        for address in addresses:
            self.get_check(address)
        
    def wait_for_element(self, selector):
        print("[+] Waiting for element to become visible: " + selector)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        print("[i] " + self.driver.title)

    def get_click_wait(self, address, selector, waitfor):
        self.get_click(address, selector)
        self.wait_for_element(waitfor)

    def process_line(self, line):
        
        # automates actions on a webpage assuming a certain  format
        # url - css selector to click - css selector to wait to appear before moving on
        print("[+] Processing line: " + line)
        line = line.split(" ")
        if len(line) == 3:
            (address, selector, waitfor) = line
            self.get_click_wait(address, selector, waitfor)
        elif len(line) == 2:
            (address, selector) = line
            self.get_click(address, selector)
        elif len(line) == 1:
            self.get_check(line[0])
        else:
            print("[!] Unexpected line length")
        
    def init_driver(self, chrome_options):
        print("[+] Initialising driver")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.ac = ActionChains(self.driver)

    def close_driver(self):
        print("[+] Closing and quitting driver")
        self.driver.close()
        self.driver.quit()
        
        # chromedriver is one stubborn process
        os.system("kill -9 `ps aux | grep chromedriver | awk '{print $2}' | awk NR==1`")
    
    def screenshot(self, name):
        self.driver.save_screenshot(name)
        print("[+] Saved screenshot under name " + name)
    
    def screenshot_element(self, selector, name):
        self.screenshot(name)
        element = self.driver.find_element_by_css_selector(selector)
        (x, y, w, h) = (element.location['x'], element.location['y'], element.size['width'], element.size['height'])
        left = x-w/2
        right = x+w/2
        top = y-h/2
        bottom = y+h/2
        img = Image.open(name)
        img = img.crop((int(left), int(top), int(right), int(bottom)))
        img.save(name)
        print("[+] Cropped image to show element " + selector)
