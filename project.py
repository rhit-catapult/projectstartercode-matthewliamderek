##SHAPE SHOOTER BY MATTHEW, LIAM, AND DEREK FOR 2024 OPERATION CATAPULT AT ROSE HULMAN INSTITUTE OF TECHNOLOGY.
## THIS IS THE FINAL WORKING VERSION.


import pygame
import sys
import random
import time
import player_module
import enemy_module
import enemy_manager
import time
import math
import wall_module
global speed_amount
global life_amount

speed_amount = 0
life_amount = 0

def main():
    pygame.event.set_grab(True)
    # turn on pygame
    pygame.init()
    pygame.mixer.music.load("sfx/Serious Sam 2 (soundtrack) - Sirius-Be Quick Or Be Dead.mp3")
    pygame.mixer.music.set_volume(10)
    pygame.mixer.music.play(-1)

    # create a screen
    pygame.display.set_caption("Shape Shooter")
    # TODO: Change the size of the screen as you see fit!


    supershots = 3

    ## Green text variable used for flashing restart screen opun death.

    green = True
    score_font = pygame.font.Font('font/scorefont.ttf', 70)
    restartGreen = score_font.render("PLAY AGAIN", True, (75,204,31))
    restartYellow = score_font.render("PLAY AGAIN", True, (238,234,37))

    exitGreen = score_font.render("EXIT", True, (75, 204, 31))
    exitYellow = score_font.render("EXIT", True, (238, 234, 37))


    ##START SCREEN INITIALIZATION STUFF
    startBG = pygame.image.load("images/startBG.png")
    title_font = pygame.font.Font('font/scorefont.ttf', 150)
    start_font = pygame.font.Font('font/scorefont.ttf', 90)
    startTitle = title_font.render("Shape Shooter", True, (255, 0, 0))
    startGreen = start_font.render("START", True, (75,204,31))




    #REMOVE THE PYGAME.FULLSCREEN AT THE END TO MAKE IT NOT FORCE FULLSCREEN, IT WILL INSTEAD BE A SQUARE 800 by 800 window.
    screen = pygame.display.set_mode((800,800))
    player = player_module.Player(screen,400,400,3)
    enemies = enemy_manager.enemy_manager(screen,player)
    # enemies.add_enemy()
    # let's set the framerate
    clock = pygame.time.Clock()
    init_clock = time.time()
    walls = []

    walls.append(wall_module.Wall(screen, (0, 0, 0), (0, 0, 120, 250), 10))
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(0, 550, 120, 250), 10))

    # top side
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(0, 0, 250, 120), 10))
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(500, 0, 250, 120), 10))

    # right side
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(screen.get_width() - 120, 0, 120, 250), 10))
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(screen.get_width() - 120, 550, 120, 250), 10))

    # bottom side
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(0, screen.get_height() - 120, 250, 120), 10))
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(500, screen.get_height() - 120, 250, 120), 10))

    ## INFO MENU VARIABLE DECLERATIONS BELOW:

    info_font = pygame.font.Font('font/scorefont.ttf', 50)
    enemy_label = info_font.render("Enemy", True, (255, 255, 255))
    weapon_label = info_font.render("Weapon", True, (255, 255, 255))
    info_label = info_font.render('Info:', True, (255, 255, 255))
    stats_font = pygame.font.SysFont('trebuchetms', 20)

            #purple:
    purple_title = info_font.render("Basic", True, pygame.Color((189, 87, 218)))

    purple_stats = stats_font.render("•The most basic enemy", True, (0, 0, 0))
    purple_stats2 = stats_font.render("•Will die when shot", True, (0, 0, 0))
    purple_stats3 = stats_font.render("•No gun", True, (0, 0, 0))
    purple_stats4 = stats_font.render("•No special powers", True, (0, 0, 0))
    purple_stats5 = stats_font.render("•Won't drop anything", True, (0, 0, 0))

    green_title = info_font.render("Titan", True, pygame.Color(37, 145, 37))

    green_stats = stats_font.render("•VERY tanky", True, (0, 0, 0))
    green_stats2 = stats_font.render("•Takes 15 shots to die", True, (0, 0, 0))
    green_stats3 = stats_font.render("•No gun", True, (0, 0, 0))
    green_stats4 = stats_font.render("•Eats their protein", True, (0, 0, 0))
    green_stats5 = stats_font.render("•Will drop a weapon", True, (0, 0, 0))

            #red:
    red_title = info_font.render("Kamikaze", True, pygame.Color("Red"))

    red_stats = stats_font.render("•Runs really FAST", True, (0, 0, 0))
    red_stats2 = stats_font.render("•Will die when shot", True, (0, 0, 0))
    red_stats3 = stats_font.render("•No gun", True, (0, 0, 0))
    red_stats4 = stats_font.render("•Ex singer", True, (0, 0, 0))
    red_stats5 = stats_font.render("•Might drop a grenade launcher", True, (0, 0, 0))

            #yellow:
    yellow_title = info_font.render("Shotgun", True, pygame.Color("Yellow"))

    yellow_stats = stats_font.render("•Normal speed", True, (0, 0, 0))
    yellow_stats2 = stats_font.render("•Will die when shot", True, (0, 0, 0))
    yellow_stats3 = stats_font.render("•Has a shotgun", True, (0, 0, 0))
    yellow_stats4 = stats_font.render("•Shoots 3 at a time", True, (0, 0, 0))
    yellow_stats5 = stats_font.render("•Might drop its gun", True, (0, 0, 0))

            #blue:
    blue_title = info_font.render("Pistol", True, pygame.Color("Blue"))

    blue_stats = stats_font.render("•Normal speed", True, (0, 0, 0))
    blue_stats2 = stats_font.render("•Will die when shot", True, (0, 0, 0))
    blue_stats3 = stats_font.render("•Has a pistol", True, (0, 0, 0))
    blue_stats4 = stats_font.render("•Shoots 1 at a time", True, (0, 0, 0))
    blue_stats5 = stats_font.render("•Might drop a spare rifle", True, (0, 0, 0))

    sniper_title = info_font.render("Sniper Rifle", True, pygame.Color(255, 255, 255))

    sniper_stats = stats_font.render("•Chance to drop from", True, (0, 0, 0))
    sniper_stats2 = stats_font.render("Pistol and Titan enemies", True, (0, 0, 0))
    sniper_stats3 = stats_font.render("•Bullets shoot faster", True, (0, 0, 0))
    sniper_stats4 = stats_font.render("•35 Ammo per Rifle", True, (0, 0, 0))
    sniper_stats5 = stats_font.render("•Snipin's a good job, mate", True, (0, 0, 0))

    shotgun_title = info_font.render("Shotgun", True, (255, 255, 255))

    shotgun_stats = stats_font.render("•Chance to drop from", True, (0, 0, 0))
    shotgun_stats2 = stats_font.render("Shotgun and Titan enemies", True, (0, 0, 0))
    shotgun_stats3 = stats_font.render("•Multiple bullets shot", True, (0, 0, 0))
    shotgun_stats4 = stats_font.render("•25 Ammo per Shotgun", True, (0, 0, 0))
    shotgun_stats5 = stats_font.render("•And I want the front seat", True, (0, 0, 0))

    launcher_title = info_font.render("Grenade Launcher", True, (255, 255, 255))

    launcher_stats = stats_font.render("•Chance to drop from", True, (0, 0, 0))
    launcher_stats2 = stats_font.render("Kamikaze and Titans", True, (0, 0, 0))
    launcher_stats3 = stats_font.render("•Releases shrapnel", True, (0, 0, 0))
    launcher_stats4 = stats_font.render("•10 Ammo per Launcher", True, (0, 0, 0))
    launcher_stats5= stats_font.render("•Kablewwwwwwwy!", True, (0, 0, 0))

    controls_title1 = info_font.render("Controls", True, (255, 255, 255))
    controls_title2 = stats_font.render("WASD or Arrow Keys to Move", True, (255, 255, 255))
    controls_title3 = stats_font.render("Space Button or Mouse Click to Shoot your Weapon", True, (255, 255, 255))
    controls_title4 = stats_font.render("Aim your Weapon by Moving your Mouse or Using your Mousepad", True, (255, 255, 255))
    controls_title5 = stats_font.render("Press F to Use a Super Shot", True, (255, 255, 255))

    #trebuchet





    score_font = pygame.font.Font('font/scorefont.ttf', 70)

    spawn_time = 2
    while True:
        final_clock = time.time()
        clock.tick(60)
        if spawn_time - .00002 > 0 and player.playing:
            spawn_time -= .00015
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_f]:
                    if supershots > 0:
                        supershots -= 1
                        for k in range(0, 360, 5):
                            player.weapon.fire(player.x, player.y, k, True)
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()


            if ((event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)) and not enemies.hit_player and player.playing:
                pos = pygame.mouse.get_pos()
                if not (pos[0] - player.x == 0):
                    angle = math.atan((pos[1] - player.y) / (pos[0] - player.x))
                    if pos[0] - player.x < 0:
                        angle += math.pi
                        #bullets.append(testBullet(screen, player.x, player.y, angle))
                    player.weapon.fire(player.x+10, player.y+10, angle, False)
            elif event.type == pygame.MOUSEBUTTONDOWN and enemies.hit_player:
                pos = pygame.mouse.get_pos()
                if (pos[0] < screen.get_width()/2 - (restartGreen.get_width()/2)+ restartGreen.get_width()) and (pos[0] > screen.get_width()/2 - (restartGreen.get_width()/2)) and pos[1] > screen.get_height()/2 + 100 and pos[1] < screen.get_height()/2 + 100+restartGreen.get_height():
                    enemies.hit_player = False
                    enemies.enemies = []
                    player.weapon.changeWeapon("Bullet", 0)
                    pygame.mixer.music.load("sfx/Serious Sam 2 (soundtrack) - Sirius-Be Quick Or Be Dead.mp3")
                    player.weapon.bullets = []
                    enemies.kills = 0
                    supershots = 3
                    speed_amount = 0
                    life_amount = 0
                    player.speed = 3
                    player.speed_reset()
                    pygame.mixer.music.play()
                    player.x = player.OriginalX
                    player.weapon.pickups = []
                    player.y = player.OriginalY
                if (pos[0] < screen.get_width()/2 - (exitGreen.get_width()/2) + exitGreen.get_width()) and (pos[0] > screen.get_width()/2 - (exitGreen.get_width()/2)) and pos[1] > screen.get_height()/2 + 175 and pos[1] < screen.get_height()/2 + 175 + exitGreen.get_height():
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not player.playing:
                pos = pygame.mouse.get_pos()
                if (pos[0] < screen.get_width()/2 - (startGreen.get_width()/2)+ startGreen.get_width()) and (pos[0] > screen.get_width()/2 - (startGreen.get_width()/2)) and pos[1] > screen.get_height()/2 + 50 and pos[1] < screen.get_height()/2 + 50 + startGreen.get_height():
                    player.playing = True



            # TODO: Add you events code
        #player.weapon.fire(player.x, player.y, random.randint(0,360))  # Fisher gun
        # no cheating Dr. Fisher
        ## START GAME SCREEN
        if not player.playing:
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(startBG, (0, 0))
            screen.blit(startTitle, (screen.get_width()/2-(startTitle.get_width()/2),screen.get_height()/2-200))
            screen.blit(startGreen, (screen.get_width()/2-(startGreen.get_width()/2),screen.get_height()/2+50))




            screen.blit(enemy_label, (10, screen.get_height() - 520))
            screen.blit(info_label, (20, screen.get_height()-490))
            pygame.draw.circle(screen, pygame.Color("Purple"),(45,screen.get_height()-420),20)
            basic_enemy_image = pygame.image.load("images/basic_enemy_face.bmp")
            basic_enemy_image = pygame.transform.scale(basic_enemy_image, (38, 38))
            screen.blit(basic_enemy_image, (25, screen.get_height() - 420 - 20))

            pygame.draw.circle(screen, pygame.Color(37, 145, 37), (45, screen.get_height()-120), 20)
            titan_enemy_image = pygame.image.load("images/titan_enemy_face.bmp")
            titan_enemy_image = pygame.transform.scale(titan_enemy_image, (40, 40))
            screen.blit(titan_enemy_image, (25, screen.get_height() - 120 - 20))

            pygame.draw.circle(screen, pygame.Color("Red"),(45,screen.get_height()-195),20)
            kamikaze_enemy_image = pygame.image.load("images/kamikaze_enemy_face.bmp")
            kamikaze_enemy_image = pygame.transform.scale(kamikaze_enemy_image, (40, 40))
            screen.blit(kamikaze_enemy_image, (25, screen.get_height() - 195 - 20))

            pygame.draw.circle(screen, pygame.Color("Yellow"),(45,screen.get_height()-270),20)
            elite_enemy_image = pygame.image.load("images/elite_enemy_face.bmp")
            elite_enemy_image = pygame.transform.scale(elite_enemy_image, (40, 40))
            screen.blit(elite_enemy_image, (25, screen.get_height() - 270 - 20))

            pygame.draw.circle(screen, pygame.Color("Blue"),(45,screen.get_height()-345),20)
            pistol_enemy_image = pygame.image.load("images/pistol_enemy_face.bmp")
            pistol_enemy_image = pygame.transform.scale(pistol_enemy_image, (40, 40))
            screen.blit(pistol_enemy_image, (25, screen.get_height() - 345 - 20))

            screen.blit(weapon_label, (690, screen.get_height() - 445))
            screen.blit(info_label, (710, screen.get_height()-415))

            sniper_rifle_image = pygame.image.load("images/sniper_rifle_image.bmp")
            sniper_rifle_image = pygame.transform.scale(sniper_rifle_image, (80, 40))
            screen.blit(sniper_rifle_image, (700, screen.get_height() - 345 - 20))

            if mouse_pos[0] <= 780 and mouse_pos[0] >= 700 and mouse_pos[1] < screen.get_height() - 345 + 20 and mouse_pos[1] >= screen.get_height() - 345 - 20:
                pygame.draw.rect(screen, (136,136,136), pygame.Rect((450, screen.get_height()-395), (250, 150)))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((450, screen.get_height()-395), (250, 150)), 4)
                screen.blit(sniper_title, (450+125 - sniper_title.get_width()/2,screen.get_height()-390))
                screen.blit(sniper_stats, (450 + 5, screen.get_height()-360))
                screen.blit(sniper_stats2, (450 + 5, screen.get_height()-340))
                screen.blit(sniper_stats3, (450 + 5, screen.get_height()-320))
                screen.blit(sniper_stats4, (450 + 5, screen.get_height()-300))
                screen.blit(sniper_stats5, (450 + 5, screen.get_height()-280))

            shotgun_image = pygame.image.load("images/shotgun_image.bmp")
            shotgun_image = pygame.transform.scale(shotgun_image, (82.5, 20))
            screen.blit(shotgun_image, (700, screen.get_height() - 260 - 20))

            if mouse_pos[0] <= 780 and mouse_pos[0] >= 700 and mouse_pos[1] < screen.get_height() - 270 + 20 and mouse_pos[1] >= screen.get_height() - 270 - 20:
                pygame.draw.rect(screen, (136, 136, 136), pygame.Rect((450, screen.get_height() - 320), (250, 150)))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((450, screen.get_height() - 320), (250, 150)), 4)
                screen.blit(shotgun_title, (450 + 125 - shotgun_title.get_width() / 2, screen.get_height() - 315))
                screen.blit(shotgun_stats, (450 + 5, screen.get_height() - 285))
                screen.blit(shotgun_stats2, (450 + 5, screen.get_height() - 265))
                screen.blit(shotgun_stats3, (450 + 5, screen.get_height() - 245))
                screen.blit(shotgun_stats4, (450 + 5, screen.get_height() - 225))
                screen.blit(shotgun_stats5, (450 + 5, screen.get_height() - 205))

            grenade_launcher_image = pygame.image.load("images/grenade_launcher.bmp")
            grenade_launcher_image = pygame.transform.scale(grenade_launcher_image, (80, 40))
            screen.blit(grenade_launcher_image, (700, screen.get_height() - 195 - 20))

            if mouse_pos[0] <= 780 and mouse_pos[0] >= 700 and mouse_pos[1] < screen.get_height()-195+20 and mouse_pos[1] >= screen.get_height()-195-20:
                #DISPLAY INFO FOR Red
                pygame.draw.rect(screen, (136,136,136), pygame.Rect((450, screen.get_height()-245), (250, 150)))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((450, screen.get_height()-245), (250, 150)), 4)
                screen.blit(launcher_title, (450+125 - launcher_title.get_width()/2,screen.get_height()-240))
                screen.blit(launcher_stats, (450 + 5, screen.get_height()-210))
                screen.blit(launcher_stats2, (450 + 5, screen.get_height()-190))
                screen.blit(launcher_stats3, (450 + 5, screen.get_height()-170))
                screen.blit(launcher_stats4, (450 + 5, screen.get_height()-150))
                screen.blit(launcher_stats5, (450 + 5, screen.get_height()-130))


            if mouse_pos[0] <= 65 and mouse_pos[0] >= 25 and mouse_pos[1] < screen.get_height() - 120 + 20 and mouse_pos[1] >= screen.get_height() - 120 - 20:
                pygame.draw.rect(screen, (136, 136, 136), pygame.Rect((80, screen.get_height() - 220), (250, 150)))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((80, screen.get_height()-220), (250, 150)), 4)
                screen.blit(green_title, (80 + 125 - green_title.get_width()/2, screen.get_height()-215))
                screen.blit(green_stats, (80 + 5, screen.get_height()-185))
                screen.blit(green_stats2, (80 + 5, screen.get_height()-165))
                screen.blit(green_stats3, (80 + 5, screen.get_height()-145))
                screen.blit(green_stats4, (80 + 5, screen.get_height()-125))
                screen.blit(green_stats5, (80 + 5, screen.get_height()-105))

            #print("hovering over purple")
            if mouse_pos[0] <= 65 and mouse_pos[0] >= 25 and mouse_pos[1] < screen.get_height()-195+20 and mouse_pos[1] >= screen.get_height()-195-20:
                #DISPLAY INFO FOR Red
                pygame.draw.rect(screen, (136,136,136), pygame.Rect((80, screen.get_height()-245), (300, 150)))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((80, screen.get_height()-245), (300, 150)), 4)
                screen.blit(red_title, (80+150 - red_title.get_width()/2,screen.get_height()-240))
                screen.blit(red_stats, (80 + 5, screen.get_height()-210))
                screen.blit(red_stats2, (80 + 5, screen.get_height()-190))
                screen.blit(red_stats3, (80 + 5, screen.get_height()-170))
                screen.blit(red_stats4, (80 + 5, screen.get_height()-150))
                screen.blit(red_stats5, (80 + 5, screen.get_height()-130))


                #print("hovering over red")
            if mouse_pos[0] <= 65 and mouse_pos[0] >= 25 and mouse_pos[1] < screen.get_height()-270+20 and mouse_pos[1] >= screen.get_height()-270-20:

                #DISPLAY INFO FOR Yellow
                pygame.draw.rect(screen, (136,136,136), pygame.Rect((80, screen.get_height()-320), (250, 150)))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((80, screen.get_height()-320), (250, 150)), 4)
                screen.blit(yellow_title, (80+125 - yellow_title.get_width()/2,screen.get_height()-315))
                screen.blit(yellow_stats, (80 + 5, screen.get_height()-285))
                screen.blit(yellow_stats2, (80 + 5, screen.get_height()-265))
                screen.blit(yellow_stats3, (80 + 5, screen.get_height()-245))
                screen.blit(yellow_stats4, (80 + 5, screen.get_height()-225))
                screen.blit(yellow_stats5, (80 + 5, screen.get_height()-205))

                #print("hovering over yellow")
            if mouse_pos[0] <= 65 and mouse_pos[0] >= 25 and mouse_pos[1] < screen.get_height()-345+20 and mouse_pos[1] >= screen.get_height()-345-20:
                #DISPLAY INFO FOR Blue
                pygame.draw.rect(screen, (136,136,136), pygame.Rect((80, screen.get_height()-395), (250, 150)))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((80, screen.get_height()-395), (250, 150)), 4)
                screen.blit(blue_title, (80+125 - blue_title.get_width()/2,screen.get_height()-390))
                screen.blit(blue_stats, (80 + 5, screen.get_height()-360))
                screen.blit(blue_stats2, (80 + 5, screen.get_height()-340))
                screen.blit(blue_stats3, (80 + 5, screen.get_height()-320))
                screen.blit(blue_stats4, (80 + 5, screen.get_height()-300))
                screen.blit(blue_stats5, (80 + 5, screen.get_height()-280))
                #print("hovering over blue")

            if mouse_pos[0] <= 65 and mouse_pos[0] >= 25 and mouse_pos[1] < screen.get_height()-420+20 and mouse_pos[1] >= screen.get_height()-420-20:
                #DISPLAY INFO FOR PURPLE
                pygame.draw.rect(screen, (136,136,136), pygame.Rect((80, screen.get_height()-470), (250, 150)))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((80, screen.get_height()-470), (250, 150)), 4)
                screen.blit(purple_title, (80+125 - purple_title.get_width()/2,screen.get_height()-465))
                screen.blit(purple_stats, (80 + 5, screen.get_height()-435))
                screen.blit(purple_stats2, (80 + 5, screen.get_height()-415))
                screen.blit(purple_stats3, (80 + 5, screen.get_height()-395))
                screen.blit(purple_stats4, (80 + 5, screen.get_height()-375))
                screen.blit(purple_stats5, (80 + 5, screen.get_height()-355))

            pygame.draw.rect(screen, (136, 136, 136), pygame.Rect((0, screen.get_height() - 670), (controls_title1.get_width() + 20, controls_title1.get_height() + 20)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((0, screen.get_height() - 670), (controls_title1.get_width() + 20, controls_title1.get_height() + 20)), 4)
            screen.blit(controls_title1, (10, screen.get_height() - 660))
            if mouse_pos[0] <= 130 and mouse_pos[0] >= 0 and mouse_pos[1] < (screen.get_height()-670) + controls_title1.get_height() + 20 and mouse_pos[1] >= screen.get_height()-670:
                pygame.draw.rect(screen, (136, 136, 136), pygame.Rect((0, 0), (612, 130)))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((0, 0), (612, 130)), 4)
                screen.blit(controls_title1, (25, screen.get_height() - 790))
                screen.blit(controls_title2, (25, screen.get_height() - 760))
                screen.blit(controls_title3, (25, screen.get_height() - 740))
                screen.blit(controls_title4, (25, screen.get_height() - 720))
                screen.blit(controls_title5, (25, screen.get_height() - 700))

            """
            this can be used to make a player image for the title screen
            player_model = pygame.image.load("images/head.png")
            player_model = pygame.transform.scale(player_model, (60, 60))
            player_model = pygame.transform.rotate(player_model, 340)
            screen.blit(player_model, (700, screen.get_height() - 740))

            shotgun_model = pygame.image.load("images/shotgun_image.bmp")
            shotgun_model = pygame.transform.scale(shotgun_model, (82.5, 20))
            shotgun_model = pygame.transform.rotate(shotgun_model, 330)
            screen.blit(shotgun_model, (640, screen.get_height() - 740))
            """



        ##END GAME SCREEN
        if enemies.hit_player and player.playing:
            topscorefile = open("topscore","r")
            #print(int(topscorefile.read()))
            screen.fill((0, 0, 0))
            spawn_time = 2
            enemies.bullets = []
            enemies.enemies = []
            try:

                high_score = int(topscorefile.read())
                topscorefile.close()

            except:
                high_score = 0
            if enemies.kills > high_score:
                topscorefile = open("topscore","w")

                high_score = enemies.kills
                topscorefile.write(str(high_score))

                topscorefile.close()

            game_over_text = title_font.render("GAME OVER", True, (255, 0, 0))
            high_score_text = score_font.render(f'HIGH SCORE: {high_score}', True, (255, 0, 0))
            screen.blit(game_over_text, (screen.get_width() / 2 - (game_over_text.get_width() / 2), screen.get_height() / 2 - game_over_text.get_height() / 2 - 100))
            screen.blit(high_score_text,
                        (screen.get_width() / 2 - (high_score_text.get_width() / 2), screen.get_height() / 2))
            screen.blit(score_label, (screen.get_width()/2 - (score_label.get_width()/2), screen.get_height()/2 + (game_over_text.get_height()+10)-180))





            if final_clock - init_clock > .3:
                init_clock = final_clock
                green = not green
            if green:
                screen.blit(restartGreen, (screen.get_width()/2 - (restartGreen.get_width()/2), screen.get_height()/2 + 100))
                screen.blit(exitGreen, (screen.get_width() / 2 - (exitGreen.get_width()/2), screen.get_height()/2 + 175))
            elif not green:
                screen.blit(restartYellow, (screen.get_width()/2 - (restartGreen.get_width()/2), screen.get_height()/2 + 100))
                screen.blit(exitYellow, (screen.get_width()/2 - (exitYellow.get_width()/2), screen.get_height()/2 + 175))

        ## GAME SCREEN
        if not enemies.hit_player and player.playing:
            # TODO: Fill the screen with whatever background color you like!
            screen.fill((110, 79, 33))


            ##DRAW BACKGROUND:::


            ## BLACK LINES AROUND RECKTANGLES

            #left side

            for wall in walls:
                wall.process()
                if wall.isCollided(player):
                    player.colliding(pygame.Rect(wall.rect))


            ##BROWN EDGE RECTANGLES
            #left side
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(0, 0, 110, 240))
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(0, 560, 110, 240))

            #top side
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(0, 0, 240, 110))
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(510, 0, 250, 110))

            #right side
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(screen.get_width()-110, 0, 120, 240))
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(screen.get_width()-110, 560, 120, 250))

            #bottom side
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(0, screen.get_height()-110, 240, 120))
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(510, screen.get_height()-110, 250, 120))




            ## START GAME CODE HERE::
            if final_clock - init_clock > spawn_time:
                enemies.add_enemy()
                init_clock = final_clock

            enemies.spawn_enemies()
            enemies.add_titan()
            enemies.move_enemies()
            enemies.check_for_dead()
            enemies.check_hit_player()
            enemies.checkBulletOffScreenAndMove()
            player.process()


            ## SCORE COUNTER

            score_label = score_font.render(f"SCORE: {enemies.kills}", True, (255, 0, 0))
            screen.blit(score_label, (5, 0))

            ## AMMO COUNTER


            ammo_label = score_font.render(f"AMMO: {player.weapon.ammo_counter()}", True, (255, 0, 0))
            screen.blit(ammo_label, (525, 0))

            ## SUPERSHOT AMMO

            super_label = score_font.render(f"SUPERS: {supershots}", True, (255, 0, 0))
            screen.blit(super_label, (525, 50))

            speed_boost_image = pygame.image.load("images/speed_boost.bmp")
            speed_boost_image = pygame.transform.scale(speed_boost_image, (30, 40))
            screen.blit(speed_boost_image, (10, 55))

            try:
                speed_label = score_font.render(f"{int((player.speed - 3) * 4)}", True, (255, 0, 0))
            except:
                speed_label = score_font.render("0", True, (255, 0, 0))
            screen.blit(speed_label, (50, 55))

            """
            false_life_image = pygame.image.load("images/false_life.bmp")
            false_life_image = pygame.transform.scale(false_life_image, (40, 40))
            screen.blit(false_life_image, (10, 175))
            """

            """
            try:
                life_label = score_font.render(f"{life_amount}", True, (255, 0, 0))
            except:
                life_label = score_font.render("0", True, (255, 0, 0))
            screen.blit(life_label, (50, 175))
            """

            #pygame.draw.rect(screen, (2s55,255,255), player.hitbox)

            # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()
