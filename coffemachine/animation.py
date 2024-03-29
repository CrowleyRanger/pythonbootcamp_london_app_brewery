import os
import time

def clear_screen():
    os.system("cls")

# ==================== FRAMES ==================== #
filling_cup = ['''
        /~~~~~~~~/|
       / /######/ / |
      / /______/ /  |
     ============ /||
     |__________|/ ||
      |\__,,__/    ||
      | __,,__     ||
      |_\====/%____||
      | /~~~~\ %  / |
     _|/      \%_/  |
    | |        | | /
    |__\______/__|/
    ~~~~~~~~~~~~~~
''', '''
        /~~~~~~~~/|
       / /######/ / |
      / /______/ /  |
     ============ /||
     |__________|/ ||
      |\__,,__/    ||
      | __,,__     ||
      |_\====/%____||
      | /~~~~\ %  / |
     _|/      \%_/  |
    | |        | | /
    |__\######/__|/
    ~~~~~~~~~~~~~~
''', '''
        /~~~~~~~~/|
       / /######/ / |
      / /______/ /  |
     ============ /||
     |__________|/ ||
      |\__,,__/    ||
      | __,,__     ||
      |_\====/%____||
      | /~~~~\ %  / |
     _|/      \%_/  |
    | |########| | /
    |__\######/__|/
    ~~~~~~~~~~~~~~
''', '''
        /~~~~~~~~/|
       / /######/ / |
      / /______/ /  |
     ============ /||
     |__________|/ ||
      |\__,,__/    ||
      | __,,__     ||
      |_\====/%____||
      | /~~~~\ %  / |
     _|/######\%_/  |
    | |########| | /
    |__\######/__|/
    ~~~~~~~~~~~~~~
''']

# ==================== ANIMATION ==================== #
def filling_cup_animation():
    for i in range(4):
        clear_screen()
        print(filling_cup[i])
        time.sleep(0.5)