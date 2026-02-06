#casinowalk
import play
import time

#beginscherm = play.new_image("download.png", size= 300)
#platform = play.new_image("platform.png",size = 75)

start_box = play.new_box(color = 'red',width=250, height=85)

start_button = play.new_text('START',color ='white',y= -8, font_size=70) 

reset_button = play.new_text('RESET',color = 'white', font_size = 20)
reset_button.x = 270
reset_button.y = 270
reset_button.hide()

money = 0
money_button = play.new_text (f'€{money} ', color = 'white', font_size = 20)
money_button.hide()
money_button.x=270
money_button.y=250

reset_button = play.new_text('RESET',color = 'black', font_size = 20)
reset_button.x = 270
reset_button.y = 270
reset_button.hide()

player = play.new_box(color= 'black', width =45, height = 45)
player.hide()

if money <= 0:
    game_over = play.new_text("Je bent blut...", color = "red",font_size = 60)
    for i in [0,4]:
        time.sleep(1)
        game_over.hide()
        time.sleep(1)
        game_over.show()
    play.stop_program

@start_box.when_clicked
def start_function():
    start_button.hide()
    start_box.hide()
    #platform.show()
    money_button = play.new_text (f'€{money} ', color = 'white', font_size = 20)
    money_button.x=270
    money_button.y=250
    money_button.show()
    reset_button.show()
    # reset_button = play.new_text('RESET',color = 'black', font_size = 20)
    # reset_button.x = 270
    # reset_button.y = 270
    #beginscherm.hide()
    # player = play.new_box(color= 'black', width =45, height = 45)
    player.show()
    @play.when_key_pressed("w","up")
    def vooruit_function():
        player.y = player.y + 2
    @play.when_key_pressed("a","left")
    def links_function():
        player.x = player.x -2
    @play.when_key_pressed("s","down")
    def achteruit_function():
        player.y = player.y -2
    @play.when_key_pressed("d","right") 
    def rechts_function():
        player.x = player.x +2


@reset_button.when_clicked
def reset_function():
    start_button.show()
    start_box.show()
    reset_button.hide()
    money_button.hide()
    #beginscherm.show()
    #platform.hide()
    # player = play.new_box(color= 'black', width =45, height = 45)
    player.hide()
    
play.start_program()

