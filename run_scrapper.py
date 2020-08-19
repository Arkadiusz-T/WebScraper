import scraping_resources

if __name__ == '__main__':
    print('Welcome to ScraperForFun by Arkadiusz-design')
    print('This script was created for personal development in scraping tasks')
    print('Its purpose is to provide backstory of the champions form LeagueOfLegends online game')
    print('and enforce players decisions during "Champion Select" phase of the game to increase a chance of winning')
    print('------------------------------------------------------------------')
    keep_script_alive_for_next_iteration = True
    while keep_script_alive_for_next_iteration:
        print('To print list of characters type: 1')
        print('To view history of given champion type: 2')
        print('To see how to counter a champion type: 3')
        print('To see best champions for a given role type: 4 ')
        print('To quit type: exit')
        chosen_option = input()

        if chosen_option == '1':
            list_of_characters = scraping_resources.download_list_of_characters()
            [print(name) for name in list_of_characters]
            print('------------------------------------')

        if chosen_option == '2':
            print('Type name of a character: ')
            character_name = input()
            history_of_a_character = scraping_resources.download_history_of_a_character_in_paragraphs(character_name)
            [print(paragraph) for paragraph in history_of_a_character]
            print('------------------------------------')

        if chosen_option == '3':
            print('in development')

        if chosen_option == '4':
            print('in development')

        if chosen_option == 'exit':
            keep_script_alive_for_next_iteration = False


