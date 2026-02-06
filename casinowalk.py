#casinowalk
import play

platform = play.new_image("platform.png",size = 75)
platform.hide()

beginscherm = play.new_image("download.png", size= 300)

start_box = play.new_box(color = 'red',width=250, height=85)

start_button = play.new_text('START',color ='white',y= -8, font_size=70) 

reset_button = play.new_text('RESET',color = 'white', font_size = 20)
reset_button.x = 270
reset_button.y = 270
reset_button.hide()

money = 20
money_button = play.new_text (f'€{money} ', color = 'white', font_size = 20)
money_button.hide()
money_button.x=270
money_button.y=250

player = play.new_box(color= 'black', width =45, height = 45)
player.hide()

@play.when_key_pressed("w","up")
def vooruit_function():
    player.y = player.y + 3

@play.when_key_pressed("a")
def links_function():
    player.x = player.x -3

@play.when_key_pressed("s","down")
def achteruit_function():
    player.y = player.y -3

@play.when_key_pressed("d",) 
def rechts_function():
    player.x = player.x +3

@start_box.when_clicked
def start_function():
    start_button.hide()
    start_box.hide()
    reset_button.show()
    money_button.show()
    platform.show()
    beginscherm.hide()
    player.show()

@reset_button.when_clicked
def reset_function():
    start_button.show()
    start_box.show()
    reset_button.hide()
    money_button.hide()
    platform.hide()
    player.hide()
play.start_program()

