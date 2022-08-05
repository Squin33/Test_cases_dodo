from importlib.resources import path
from multiprocessing.connection import wait
from socket import timeout
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://dodopizza.ru/moscow#combos')
def test_case_1_top_menu():
    pizza_tag = browser.find_element(By.XPATH, '//*[@id="react-app"]/nav/div/ul/li[1]/a')
    pizza_tag.click()
    time.sleep(1)
def test_case_2_combo():
    combo = browser.find_element(By.XPATH, '/*[@id="react-app"]/nav/div/ul/li[2]/a')
    combo.click()
    time.sleep(1)
def test_case_3_zakuski():
    zakuski = browser.find_element(By.XPATH, '//*[@id="react-app"]/nav/div/ul/li[3]/a')
    zakuski.click()
    time.sleep(1)
def test_case_4_desert():
    desert = browser.find_element(By.XPATH, '//*[@id="react-app"]/nav/div/ul/li[4]/a')
    desert.click()
    time.sleep(1)
def test_case_5_drink():
    drink = browser.find_element(By.XPATH, '//*[@id="react-app"]/nav/div/ul/li[5]/a')
    drink.click()
    time.sleep(1)
def test_case_6_other():
    other = browser.find_element(By.XPATH,  '//*[@id="react-app"]/nav/div/ul/li[6]/a')
    other.click()
    time.sleep(2)
def test_case_7_akcii():
    akcii = browser.find_element(By.XPATH, '//*[@id="react-app"]/nav/div/ul/li[7]/a')
    akcii.click()
    time.sleep(20)
def test_case_8_conctacts():
    contacts = browser.find_element(By.XPATH, '//*[@id="react-app"]/nav/div/ul/li[8]/a')
    contacts.click()
    time.sleep(1)
def test_case_9_about():
    about = browser.find_element(By.XPATH, '//*[@id="react-app"]/div/div[1]/nav/div/ul/li[9]/a')
    about.click()
    time.sleep(1)
def test_case_10_work():
    work = browser.find_element(By.XPATH, '//*[@id="react-app"]/div/div[1]/nav/div/ul/li[10]/a')
    work.click()
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    browser.find_element(By.XPATH, '//*[@id="react-app"]/div/div[1]/nav/div/ul/li[1]/a').click()
    time.sleep(1)
def test_case_11_buy():
    pizza_tag = browser.find_element(By.XPATH, '//*[@id="pizzas"]/article[5]')
    time.sleep(1)
    pizza_tag.click()
def test_case_12_order():
    order = browser.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div[2]/button').click()
    time.sleep(1)
def test_case_13_order_2():
    delivery = browser.find_element(By.XPATH, '//*[@id="react-app"]/nav/div/div[2]/button').click()
    time.sleep(1)
def test_case_14_purcgase():
    purchase_1 = browser.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[1]/main/div/div[2]/section/button').click()
    time.sleep(4)
def test_case_15_telephone():#Тестируем максимальное количество чисел, которое можно ввести
    call = browser.find_element(By.XPATH, '//*[@id="phn-input"]')
    call.send_keys('999999999999999999')
def test_case_16_telephone_field():#Можно ли ввести в после ввода номера буквы
    call_2 = browser.find_element(By.XPATH, '//*[@id="phn-input"]')
    call_2.clear()
    call_2.send_keys('gggggggggg')
    browser.quit()










