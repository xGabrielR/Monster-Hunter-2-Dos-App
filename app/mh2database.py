import os
import logging
import pandas as pd
import PySimpleGUI as sg

class MhDatabase( object ):
    
    '''
    -- datasets() -> This function load all csv files and return selected columns & new dataframes.
    -- create_table() -> Create Table for show the data, used on some others functions on the app.
    -- monster_popup() -> After user click on 'Monsters' button, start this function to show selected monster info.
    -- item_popup() -> After user click on 'Itens' button, start this function to show selected itens info.
    -- quest_popup() -> After user click on 'Quests' button, start this function to show another layout to user select rank for quests info.
    -- kitchen_status() -> Combined with other function, this function only show a layout for user select kitchen food status to show.
    -- kitchen_popup() -> User select the season with this layout, after this, start kitchen_status() to select what food status he like to see.
    -- geral_popup() -> First layout user see.
    '''

    def datasets( self ):
        df_train   = pd.read_csv('.csv\\train_quests.csv')
        df_village = pd.read_csv('.csv\\village_quests.csv')
        df_itens    = pd.read_csv('.csv\\itens.csv')
        df_monsters = pd.read_csv('.csv\\monsters.csv')
        df_r_breeder = pd.read_csv('.csv\\recipes_breeder.csv')
        df_r_winter  = pd.read_csv('.csv\\recipes_winter.csv')
        df_r_summer  = pd.read_csv('.csv\\recipes_summer.csv')

        # Select Columns to Show on App
        df_village  = df_village[['rank', 'name', 'season', 'area', 'main', 'main_reward', 'sub_a', 'sub_b', 'sub_a_reward', 'sub_b_reward']]
        df_train    = df_train[['id', 'rank', 'name', 'area', 'main', 'main_reward', 'full_reward', 'sub_a', 'sub_b', 'sub_a_reward', 'sub_b_reward']]
        df_monsters = df_monsters[['name', 'jp_name', 'element', 'weak', 'class','gen']]
        df_itens    = df_itens[['id', 'name', 'jp_name', 'carry', 'rarity', 'buy', 'sell']]
        df_r_summer = df_r_summer[['first_food', 'second_food', 'recipe', 'health', 'stamina', 'attack', 'defense']]
        df_r_winter = df_r_winter[['first_food', 'second_food', 'recipe', 'health', 'stamina', 'attack', 'defense']]
        df_r_breeder = df_r_breeder[['first_food', 'second_food', 'recipe', 'health', 'stamina', 'attack', 'defense']]

        # Generate New DataFrames
        df_i_star   = df_village[df_village['rank'] == 1]
        df_ii_star  = df_village[df_village['rank'] == 2]
        df_iii_star = df_village[df_village['rank'] == 3]
        df_iv_star  = df_village[df_village['rank'] == 4]

        data = {'village_quests': df_village,
                'train_quests': df_train,
                'list_monsters': df_monsters,
                'list_itens': df_itens,
                'recipes_summer': df_r_summer,
                'recipes_winter': df_r_winter,
                'recipes_breeder': df_r_breeder }
        
        generated_data = {'i_rank_quests': df_i_star,
                        'ii_rank_quests': df_ii_star,
                        'iii_rank_quests': df_iii_star,
                        'iv_rank_quests': df_iv_star}

        return data, generated_data

    def create_table( self, data, head, title ):
        layout = [[sg.Table( values=data,
                            headings=head,
                            font=('sans serif', 10),
                            justification='left',
                            pad=(25,25),
                            auto_size_columns=True,
                            num_rows=min(30, len(data)),
                            display_row_numbers=False )]]
        
        window = sg.Window( title, layout, grab_anywhere=False )
        event, values = window.read()
        window.close()

        return None

    def monster_popup( self ):
        monster_layout = [[sg.Text('_'*30)], 
                        [sg.Text('Provide Monster Name or Blank for List Monsters')],
                        [sg.Input(key='monster_name')],
                        [sg.Button('Search')],
                        [sg.Text('_'*30)]]

        monster_window = sg.Window( 'MH2 - Monsters', monster_layout, element_justification='c' )

        while True:
            event, values = monster_window.read()

            if event == 'Search':
                monster_name     = values['monster_name'].title()
                localize_monster = data[0]['list_monsters'][data[0]['list_monsters']['name'].str.contains(monster_name)]

                if localize_monster.empty:
                    sg.popup('I dont finded this Monster 🤔')

                else:
                    self.create_table( localize_monster.values.tolist(), list(localize_monster.columns), 'MH2 - Monsters' )

            if event == sg.WIN_CLOSED:
                break

        return None

    def item_popup( self ):
        item_layout = [[sg.Text('_'*30)], 
            [sg.Text('Provide Item Name or Blank for List Itens')],
            [sg.Input(key='item_name')],
            [sg.Button('Search')],
            [sg.Text('_'*30)]]

        item_window = sg.Window( 'MH2 - Itens', item_layout, element_justification='c' )

        while True:
            event, values = item_window.read()

            if event == 'Search':
                item_name      = values['item_name'].title()
                localize_itens = data[0]['list_itens'][data[0]['list_itens']['name'].str.contains(item_name)]

                if localize_itens.empty:
                    sg.popup('I dont finded this Item 🤔')

                else:
                    self.create_table( localize_itens.values.tolist(), localize_itens.columns.tolist(), 'MH2 - Itens' )

            if event == sg.WIN_CLOSED:
                break

        return None

    def quest_popup( self ):
        quest_layout = [[sg.Text('_'*30)], 
                [sg.Text('Select Quest Rank for Quest List')],
                [sg.Button('1 Star'), sg.Button('2 Star')],
                [sg.Button('3 Star'), sg.Button('4 Star'), sg.Button('Train')],
                [sg.Text('_'*30)]]

        quest_window = sg.Window( 'MH2 - Quests', quest_layout, element_justification='c' )

        while True:
            event, values = quest_window.read()

            if event == '1 Star':
                self.create_table( data[1]['i_rank_quests'].values.tolist(), list(data[1]['i_rank_quests'].columns), 'MH2 - Rank 1 Quests' )

            if event == '2 Star':
                self.create_table( data[1]['ii_rank_quests'].values.tolist(), list(data[1]['ii_rank_quests'].columns), 'MH2 - Rank 2 Quests' )

            if event == '3 Star':
                self.create_table( data[1]['iii_rank_quests'].values.tolist(), list(data[1]['iii_rank_quests'].columns), 'MH2 - Rank 3 Quests' )

            if event == '4 Star':
                self.create_table( data[1]['iv_rank_quests'].values.tolist(), list(data[1]['iv_rank_quests'].columns), 'MH2 - Rank 4 Quests' )

            if event == 'Train':
                self.create_table( data[0]['train_quests'].values.tolist(), list(data[0]['train_quests'].columns), 'MH2 - Train Quests' )

            if event == sg.WIN_CLOSED:
                break

        return None

    def kitchen_status( self, df_aux ):
        status_layout = [[sg.Text('_'*30)],
                [sg.Text('Select Season for Combine List')],
                [sg.Button('Health'), sg.Button('Stamina')],
                [sg.Button('Attack'), sg.Button('Defense')],
                [sg.Button('All Recipes')],
                [sg.Text('_'*30)]]

        status_window = sg.Window( 'MH2 - Kitchen', status_layout, element_justification='c' )

        while True:
            event, values = status_window.read()

            if event == 'Health':
                df_health = df_aux[df_aux['health'] > 0]
                df_health = df_health.sort_values('health', ascending=False )
                self.create_table( df_health.values.tolist(), list(df_health.columns), 'MH2 - Health Recipes' )

            if event == 'Stamina':
                df_stamina = df_aux[df_aux['stamina'] > 0]
                df_stamina = df_stamina.sort_values('stamina', ascending=False )
                self.create_table( df_stamina.values.tolist(), list(df_stamina.columns), 'MH2 - Stamina Recipes' )

            if event == 'Attack':
                df_attack = df_aux[df_aux['attack'] > 0]
                df_attack = df_attack.sort_values('attack', ascending=False )
                self.create_table( df_attack.values.tolist(), list(df_attack.columns), 'MH2 - Attack Recipes' )

            if event == 'Defense':
                df_defense = df_aux[df_aux['defense'] > 0]
                df_defense = df_defense.sort_values('defense', ascending=False )
                self.create_table( df_defense.values.tolist(), list(df_defense.columns), 'MH2 - Defense Recipes' )

            if event == 'All Recipes':
                df_aux = df_aux.copy()
                self.create_table( df_aux.values.tolist(), list(df_aux.columns), 'MH2 - Defense Recipes' )

            if event == sg.WIN_CLOSED:
                break

        return None

    def kitchen_popup( self ):
        kitchen_layout = [[sg.Text('_'*30)],
                [sg.Text('Select Season for Combine List')],
                [sg.Button('Summer'), sg.Button('Winter'), sg.Button('Breeder')],
                [sg.Text('_'*30)]]

        kitchen_window = sg.Window( 'MH2 - Kitchen', kitchen_layout, element_justification='c' )

        while True:
            event, values = kitchen_window.read()

            if event == 'Summer':
                self.kitchen_status( data[0]['recipes_summer'] )
                
            if event == 'Winter':
                self.kitchen_status( data[0]['recipes_winter'] )
                
            if event == 'Breeder':
                self.kitchen_status( data[0]['recipes_breeder'] )
                
            if event == sg.WIN_CLOSED:
                break

        return None

    def geral_popup( self ):
        default_layout = [[sg.Image('.img\\mh2.png', size=(300,225))],
                          [sg.Text('▃▃▃▃▃▃ ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃\n\n▃   MH2 DATABASE\n\n▃   App for Mh2 Hunters!\n\n▃▃▃▃▃▃ ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃')], 
                          [sg.Text(' ')],
                          [sg.Button('Quests'), sg.Button('Monsters'), sg.Button('Mix Sets')],
                          [sg.Button('Itens'), sg.Button('Kitchen')],
                          [sg.Text(' ')]]

        default_window = sg.Window( 'MH2 - Database', default_layout, element_justification='c'  )

        while True:
            event, values = default_window.read()

            if event == 'Quests':
                self.quest_popup()

            if event == 'Monsters':
                self.monster_popup()

            if event == 'Mix Sets':
                sg.popup('Work in Progress ; - ;')

            if event == 'Itens':
                self.item_popup()

            if event == 'Kitchen':
                self.kitchen_popup()

            if event == sg.WIN_CLOSED:
                break

        return None

if __name__ == '__main__':

    # Set Logs Config
    logging.basicConfig( filename= '.log\\mh2database.log',
                        level   = logging.DEBUG,
                        datefmt = '%Y-%m-%d %H:%M:S',
                        format  = '%(asctime)s - %(levelname)s - %(message)s - %(name)s')

    logger = logging.getLogger('mh2database')

    # App Run
    mh_database = MhDatabase()
    logger.info('App Class Runned')
        
    sg.theme('Black')

    data = mh_database.datasets()
    logger.info('Datasets Loaded')

    mh_database.geral_popup()
    logger.info('Visual App Runnned')