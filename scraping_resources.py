import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def download_list_of_characters():
    url_with_characters_names = 'https://na.leagueoflegends.com/en-us/champions/'
    response_from_the_website = requests.get(url_with_characters_names)
    parsed_website = BeautifulSoup(response_from_the_website.text, 'html.parser')
    website_elements_with_names = parsed_website.find_all(class_='style__Text-sc-12h96bu-3 gPUACV')
    list_of_names = [x.get_text() for x in website_elements_with_names]
    return list_of_names


def download_history_of_a_character_in_paragraphs(character_name):
    character_name = character_name.lower()
    url_with_character_history = 'https://universe.leagueoflegends.com/en_US/story/champion/'+character_name+'/'
    driver = webdriver.Chrome('D:\chrome-webdriver\chromedriver.exe')
    driver.get(url_with_character_history)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    elements_with_paragraphs = driver.find_elements_by_class_name('p_1_sJ')
    paragraphs = [x.text for x in elements_with_paragraphs]
    driver.close()
    driver.quit()
    return paragraphs
