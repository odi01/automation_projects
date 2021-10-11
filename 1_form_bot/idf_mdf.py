from selenium import webdriver
from time import sleep
from PIL import Image
import urllib.request
import base64

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Username\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image
import requests
import io


israeli_id = '123456789'


class AutoMate():

    def __init__(self):
        self.driver = webdriver.Chrome()


    def open_web(self):
        self.driver.get('https://wiz.medone.idf.il/mk/m/6u6dnt6a4e')


    def get_captcha(self):
        # find the captcha element
        ele_captcha = self.driver.find_element_by_xpath(
            "/html/body/form/div[5]/div/div[3]/fieldset/div[2]/div[1]/div/div[2]/div/img")
        # get the captcha as a base64 string
        img_captcha_base64 = self.driver.execute_async_script("""
            var ele = arguments[0], callback = arguments[1];
            ele.addEventListener('load', function fn(){
            ele.removeEventListener('load', fn, false);
            var cnv = document.createElement('canvas');
            cnv.width = this.width; cnv.height = this.height;
            cnv.getContext('2d').drawImage(this, 0, 0);
            callback(cnv.toDataURL('image/jpeg').substring(22));
            }, false);
            ele.dispatchEvent(new Event('load'));
            """, ele_captcha)

        # save the captcha to a file
        with open(r"captcha.jpg", 'wb') as f:
            f.write(base64.b64decode(img_captcha_base64))


    def digits_to_text(self):
        img = Image.open('captcha.jpg')
        text = pytesseract.image_to_string(img, lang='eng',
           config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        self.text = text
        print(text)


    def fill_form(self):
        # fill out the digits
        self.digits_to_text()
        captcha_box = self.driver.find_element_by_xpath('//*[@id="capa3419"]')
        captcha_box.send_keys(self.text)
        sleep(3)

        # fill out the israli id number
        id_code = self.driver.find_element_by_xpath('//*[@id="txt3414"]')
        id_code.send_keys(israeli_id)
        sleep(3)

        # fill out the yes or no question
        yes_or_no = self.driver.find_element_by_xpath(
            '/html/body/form/div[5]/div/div[3]/fieldset/div[2]/div[1]/div/div[7]/div/div')
        yes_or_no.click()
        sleep(2)
        no = self.driver.find_element_by_xpath(
        '/html/body/form/div[5]/div/div[3]/fieldset/div[2]/div[1]/div/div[7]/div/div/select/option[3]')
        no.click()
        sleep(3)

        # click on the send bouttiom
        send_btn = self.driver.find_element_by_xpath('//*[@id="finishForm"]')
        send_btn.click()
        sleep(3)


    def refresh(self):
    	# refreshing if the form didn't succeeded.
    	el = self.driver.find_element_by_tag_name('body')
    	
    	while True:
    		if "Incorrect Captcha" in el.text:
    			self.driver.refresh()
    			sleep(3)
    			bot.get_captcha()
    			bot.digits_to_text()
    			bot.fill_form()
    			bot.refresh()
    		else:
    			print("Succeeded!")
    			break


bot = AutoMate()
bot.open_web()
bot.get_captcha()
bot.digits_to_text()
bot.fill_form()
bot.refresh()
