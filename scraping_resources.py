import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class Scrappo():

    def __init__(self):
        self.characters_names = self.__download_list_of_characters_names()


    def __download_list_of_characters_names(self):
        """
            this method use request library to get list of characters
            :return: list od all released characters in game
        """
        url_with_characters_names = 'https://na.leagueoflegends.com/en-us/champions/'
        response_from_the_website = requests.get(url_with_characters_names)
        parsed_website = BeautifulSoup(response_from_the_website.text, 'html.parser')
        website_elements_with_names = parsed_website.find_all(class_='style__Text-sc-12h96bu-3 gPUACV')
        list_of_names = [x.get_text() for x in website_elements_with_names]
        list_of_names = [x.lower() for x in list_of_names]
        return list_of_names

    def is_this_name_a_champion_name(self, name):
        """
            true if param name is a champion name, else return false
            :param name: string passed by user
            :return: bolean
        """
        if name.lower() in self.characters_names:
            return True
        else:
            return False

    def download_history_of_a_character(self, character_name):
        """
            this method scrap history of a champion
            :param character_name: string passed by user
            :return: string
        """
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

    def download_counter_to_a_champion(self, name_of_a_champion_to_counter):
        """
            get 3 counters of a given champion
            :param name_of_a_champion_to_counter: string passed by user
            :return: string
        """
        character_name = name_of_a_champion_to_counter.lower()
        if self.is_this_name_a_champion_name(character_name):
            print("Scraping counters af a champion, please wait...")
        else:
            return 'that name is not a champion name'
        url_with_statistics = 'https://na.op.gg/champion/' + name_of_a_champion_to_counter + '/statistics/'
        path_to_driver = r'D:\chrome-webdriver\chromedriver.exe'
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(path_to_driver, chrome_options=chrome_options)
        driver.get(url_with_statistics)
        lane_prediction = driver.find_element_by_class_name('champion-stats-header__position__role')
        print("Counters for champion: {} \nLane: {}".format(name_of_a_champion_to_counter, lane_prediction.text))
        counters_web_elements = driver.find_elements_by_class_name('champion-stats-header-matchup__table__champion')
        counters_text = [x.text for x in counters_web_elements]
        return ', '.join(counters_text)

    def generate_winrate_raport(self):
        """
            get 5 best champions for each role
            :return: dictionary with role name as keys and values as champion names
        """
        pass
