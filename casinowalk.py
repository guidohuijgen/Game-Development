#casinowalk
import play

achtergrond = play.new_image("achtergrond.png",size = 120, transparency=0)

beginscherm = play.new_image("download.png", size= 300, transparency=100)

player = play.new_image("player.png", size = 30, transparency=0)

shop = play.new_image("shop.png", size = 25, transparency= 0)
shop.x = 350
shop.y = 260

start_box = play.new_box(color = 'red',width=250, height=85)

start_button = play.new_text('START',color ='white',y= -8, font_size=70) 

reset_button = play.new_text('RESET',color = 'white', font_size = 20)
reset_button.x = 270
reset_button.y = 270
reset_button.hide()

money = 20
money_button = play.new_text (f'€{money} ', color = 'white', font_size = 20)
money_button.x=270
money_button.y=240
money_button.hide()

if money <= 0:
    game_over = play.new_text("Je bent blut...", color = "red",font_size = 60)
    play.stop_program

@play.when_key_pressed("w","up")
def vooruit_function():
    player.y = player.y + 6
@play.when_key_pressed("a","left")
def links_function():
    player.x = player.x -6
@play.when_key_pressed("s","down")
def achteruit_function():
    player.y = player.y -6
@play.when_key_pressed("d","right") 
def rechts_function():
    player.x = player.x +6
    
@player.when_clicked
def draai_function():
    @play.when_key_pressed("a", "left")
    def loop_links_function():
        player.angle = 90
    @play.when_key_pressed("s","down")
    def loop_naarbeneden_function():
        player.angle = 180
    @play.when_key_pressed("d","right")
    def loop_rechts_function():
        player.angle = 270
    @play.when_key_pressed("w","up")
    def loop_naarvoren_function():
        player.angle = 0

@start_box.when_clicked
def start_function():
    start_button.hide()
    start_box.hide()
    achtergrond.transparency = 100
    money_button.show()
    reset_button.show()
    beginscherm.transparency = 0
    shop.transparency = 100
    player.transparency = 100
   
@reset_button.when_clicked
def reset_function():
    start_button.show()
    start_box.show()
    reset_button.hide()
    money_button.hide()
    beginscherm.transparency =100
    achtergrond.transparency = 0
    shop.transparency = 0
    player.transparency = 0
    
play.start_program()

