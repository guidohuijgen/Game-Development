#casinowalk
import play
# Moeten boxes worden
# achtergrond = play.new_image("achtergrond.png",size = 120, transparency=0)

beginscherm = play.new_box (color = "light blue", width= 800, height = 1000, transparency=100)

player = play.new_image("player.png", size = 30, transparency=0)

shop = play.new_image("shop.png", size = 25, transparency= 0)
shop.x = 350
shop.y = 260

# IPV Image moet dit een box worden!!!
# shop_achtergrond = play.new_image("shopachtergrond.png", size =150, transparency=0)

pijltje_terug = play.new_image("pijl.png", size = 20, transparency=0)
pijltje_terug.x = 350
pijltje_terug.y = 260

coin = play.new_image("munt.png", size = 10, transparency = 0)
coin.y = 244
coin.x = 240

start_box = play.new_box(color = 'red',width=250, height=85)

start_button = play.new_text('START',color ='white',y= -8, font_size=70)

welcoming_text = play.new_text('Welcome to Casino Walk!', color = 'black', y = 52, font_size = 20)

press_start_to_start_text = play.new_text('Press start to start the game!', color = 'black', y= -55, font_size = 20)

reset_button = play.new_text('RESET',color = 'black', font_size = 20)
reset_button.x = 270
reset_button.y = 270
reset_button.hide()

money = 20
money_button = play.new_text (f'{money} ', color = 'black', font_size = 25)
money_button.x=270
money_button.y=240
money_button.hide()

if money <= 0:
    game_over = play.new_text("Je bent blut...", color = "red",font_size = 60)
    play.stop_program

@start_box.when_clicked
def start_function():
    start_button.hide()
    start_box.hide()
    # achtergrond.transparency = 100
    money_button.show()
    reset_button.show()
    # beginscherm.transparency = 0
    shop.transparency = 100
    player.transparency = 100
    coin.transparency = 100
    player.y = 0
    player.x = 0
    welcoming_text.transparency = 0
    press_start_to_start_text.transparency = 0

@reset_button.when_clicked
def reset_function():
    start_button.show()
    start_box.show()
    reset_button.hide()
    money_button.hide()
    # beginscherm.transparency =100
    # achtergrond.transparency = 0
    shop.transparency = 0
    player.transparency = 0
    coin.transparency = 0
    welcoming_text.transparency = 100
    press_start_to_start_text.transparency = 100
    
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

@shop.when_clicked
def shop_open_function():
    # achtergrond.transparency = 0
    player.transparency = 0
    reset_button.transparency = 0
    money_button.transparency = 0
    shop.transparency = 0
    # shop_achtergrond.transparency = 100
    pijltje_terug.transparency = 100
    coin.transparency = 0

@pijltje_terug.when_clicked
def shop_sluiten_function():
    # achtergrond.transparency = 100
    player.transparency = 100
    reset_button.transparency =100
    money_button.transparency = 100
    shop.transparency = 100
    # shop_achtergrond.transparency = 0
    pijltje_terug.transparency = 0
    coin.transparency = 100

@play.repeat_forever
def doorloop_function():
    if player.x > 415:
        player.x = -415
    if player.x < -415:
        player.x = 415
    if player.y > 315:
        player.y = -315
    if player.y < -315:
        player.y = 315


play.start_program()

