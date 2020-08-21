import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class Scrappo():

    def __init__(self):
        self.characters_names = self._download_list_of_characters_names()


    def _download_list_of_characters_names(self):
        url_with_characters_names = 'https://na.leagueoflegends.com/en-us/champions/'
        response_from_the_website = requests.get(url_with_characters_names)
        parsed_website = BeautifulSoup(response_from_the_website.text, 'html.parser')
        website_elements_with_names = parsed_website.find_all(class_='style__Text-sc-12h96bu-3 gPUACV')
        list_of_names = [x.get_text() for x in website_elements_with_names]
        list_of_names = [x.lower() for x in list_of_names]
        return list_of_names

    def is_this_name_a_champion_name(self, name):
        if name.lower() in self.characters_names:
            return True
        else:
            return False

    def download_history_of_a_character(self, character_name):
        character_name = character_name.lower()
        if self.is_this_name_a_champion_name(character_name):
            print("Scraping history af a champion, please wait...")
        else:
            return 'that name is not a champion name'
        url_with_character_history = 'https://universe.leagueoflegends.com/en_US/story/champion/'+character_name+'/'
        path_to_driver = r'D:\chrome-webdriver\chromedriver.exe'
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(path_to_driver, chrome_options=chrome_options)
        driver.get(url_with_character_history)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
        elements_with_paragraphs = driver.find_elements_by_class_name('p_1_sJ')
        paragraphs = [x.text for x in elements_with_paragraphs]
        history_of_a_champion = '\n'.join(paragraphs)
        driver.close()
        driver.quit()
        return history_of_a_champion
