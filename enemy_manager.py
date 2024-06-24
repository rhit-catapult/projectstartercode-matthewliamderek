import enemy_module
import pygame
import math
import gc
import sys
import enemy_bullets_module
import random

class enemy_manager:
    def __init__(self, screen, player):
        self.enemies = []
        self.screen = screen
        self.player = player
        self.kills = 0
        self.spawned = 0
        self.hit_player = False
        self.bullets = []
        self.Types = {"Enemy" : enemy_module.Enemy, "Shooter" : enemy_module.Shooter, "Elite" : enemy_module.Elite}

    def add_enemy(self):
        type = random.randint(0, len(self.Types) - 1)
        match type:
            case 0:
                type = self.Types["Enemy"]
            case 1:
                type = self.Types["Shooter"]
            case 2:
                type = self.Types["Elite"]

        self.enemies.append(type(self.screen, self.player, self))
        self.spawned += 1

        return
    def shoot(self, screen, x, y, width, height, color, angle):
        self.bullets.append(enemy_bullets_module.EnemyBullet(screen, x, y, width, height, color, angle))

    def checkBulletOffScreenAndMove(self):
        for bullet in self.bullets:
            bullet.move()
            bullet.draw()
            if bullet.off_screen():
                self.bullets.remove(bullet)

    def check_for_dead(self):
        for enemy in self.enemies:

            for bullet in self.player.weapon.bullets:
                if (bullet.x < enemy.x+15 and bullet.y > enemy.y-15 and bullet.y < enemy.y+15 and bullet.x > enemy.x -15) or (bullet.y+4 < enemy.y + 15 and bullet.y+4 > enemy.y-15 and bullet.x <enemy.x+15 and bullet.x>enemy.x-15) or (bullet.x+4 > enemy.x-15 and bullet.x+4 < enemy.x+15 and bullet.y > enemy.y-15 and bullet.y < enemy.y+15) or (bullet.x+4 > enemy.x-15 and bullet.x+4 < enemy.x+15 and bullet.y+4 > enemy.y-15 and bullet.y-4 < enemy.y+15):
                    self.enemies.remove(enemy)
                    self.player.weapon.bullets.remove(bullet)
                    self.kills += 1
                    gc.collect()

                   # print(len(self.enemies))
                   # print(len(self.player.weapon.bullets))

    def spawn_enemies(self):
        for enemy in self.enemies:
            enemy.draw()


    def check_hit_player(self):
        for bullet in self.bullets:
            if bullet.hitPlayer(self.player):
                self.hit_player = True
                pygame.mixer.music.unload()
                pygame.mixer.music.load("sfx/total_distortion_you_are_dead.mp3")
                pygame.mixer.music.play()
        for enemy in self.enemies:
            if (self.player.x < enemy.x+15 and self.player.y > enemy.y-15 and self.player.y < enemy.y+15 and self.player.x > enemy.x -15) or (self.player.y+20 < enemy.y + 15 and self.player.y+20 > enemy.y-15 and self.player.x <enemy.x+15 and self.player.x>enemy.x-15) or (self.player.x+20 > enemy.x-15 and self.player.x+20 < enemy.x+15 and self.player.y > enemy.y-15 and self.player.y < enemy.y+15) or (self.player.x+20 > enemy.x-15 and self.player.x+20 < enemy.x+15 and self.player.y+20 > enemy.y-15 and self.player.y-20 < enemy.y+15):
                self.hit_player = True
                pygame.mixer.music.unload()
                pygame.mixer.music.load("sfx/total_distortion_you_are_dead.mp3")
                pygame.mixer.music.play()


                #sys.exit()  ## COMMENT THIS LINE OUT IF YOU DONT WANT TO DIE
        return self.hit_player
                #print(hit_player)
    def move_enemies(self):

        for enemy in self.enemies:
            first_pos = (enemy.x, enemy.y)
            enemy.move()
            #move every enemy that is spawned in

            for enemy2 in self.enemies:
                #for every enemy, go through every other enemy and grab its distnace, if the distance is too small, undo the move.
                if enemy2 is not enemy:
                    distance = math.sqrt((enemy.x - enemy2.x)**2 + (enemy.y - enemy2.y)**2)
                    if distance < 35:
                        enemy.x, enemy.y = first_pos
                        break

        # for enemy in self.enemies:
        #     enemy.move()

    # add a method to check to see if an enemy has been hit, or anything else that would kill a enemy, then remove it from the enemies list . do this once a method has been made in the enemies module to check to see if the enemy should be removed.



