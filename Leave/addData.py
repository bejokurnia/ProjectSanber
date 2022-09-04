import unittest
import random
import string
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


#variable
length=8
randomStr=''.join((random.choice(string.ascii_lowercase) for x in range(length)))

class AddJobTitles(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_add_leave_type_admin(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        browser.maximize_window()
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(1)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a").click() # klik menu leave
        time.sleep(1)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]").click() # klik menu dropdown configure
        time.sleep(3)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/li[2]/a").click() # klik Leave type
        time.sleep(1)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button").click() # klik Add
        time.sleep(1)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys(randomStr) # Isi Name
        time.sleep(2)

        # browser.find_element(By.CSS_SELECTOR,"input[type='radio'][value='true']").click() # pilih Radiobutton
        # time.sleep(2)
        browser.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(2) > div > div > div > div.--status-grouped-field > div:nth-child(1) > div:nth-child(2) > div > label").click() # pilih Radiobutton
        time.sleep(2)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click() # klik Save
        time.sleep(3)

        # validasi
        text_bawah = browser.find_element(By.CLASS_NAME,"oxd-toast-content-text").text
        self.assertEqual(text_bawah, 'Success')
        time.sleep(3)
        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()