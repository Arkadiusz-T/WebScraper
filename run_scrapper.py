from scraping_resources import Scrappo

if __name__ == '__main__':
    print('Welcome to ScraperForFun by Arkadiusz-design')
    print('This script was created for personal development in scraping tasks')
    print('Its purpose is to provide backstory of the champions form LeagueOfLegends online game')
    print('and enforce players decisions during "Champion Select" phase of the game to increase a chance of winning')
    print('------------------------------------------------------------------')
    scrapo = Scrappo()
    keep_script_alive_for_next_iteration = True
    while keep_script_alive_for_next_iteration:
        print('To print list of characters type: 1')
        print('To view history of given champion type: 2')
        print('To see how to counter a champion type: 3')
        print('To see best champions for a given role type: 4 ')
        print('To quit type: exit')
        chosen_option = input()

        if chosen_option == '1':
            [print(name) for name in scrapo.characters_names]
            print('------------------------------------')

        if chosen_option == '2':
            print('Type name of a character: ')
            character_name = input()
            history_of_a_character = scrapo.download_history_of_a_character(character_name)
            print('Counters: {}'.format(history_of_a_character))
            print('------------------------------------')

        if chosen_option == '3':
            print('What a name of champion do you want to counter: ')
            name_of_a_champion_to_counter = input()
            counters_to_a_champion = scrapo.download_counter_to_a_champion(name_of_a_champion_to_counter)
            print(counters_to_a_champion)
            print('------------------------------------')

        if chosen_option == '4':
            winrate_raport = scrapo.generate_winrate_raport()
            print('------------------------------------')
            print('in development')

        if chosen_option == 'exit':
            keep_script_alive_for_next_iteration = False


