import enemy_module
import pygame
import math
import gc
import sys
import enemy_bullets_module
import bullets_module
import weapon_pickup_module
import weapon_module
import player_module
import random
import inspect
global titan_health
global speed_amount
global life_amount


class enemy_manager:
    def __init__(self, screen, player):
        self.enemies = []
        self.screen = screen
        self.player = player
        self.kills = 0
        self.spawned = 0
        self.hit_player = False
        self.bullets = []
        self.pickups = []
        self.spawnedTitan = 0
        self.Types = {"Enemy" : enemy_module.Enemy, "Shooter" : enemy_module.Shooter, "Elite" : enemy_module.Elite, "Kamikaze" : enemy_module.Kamikaze, "Titan" : enemy_module.Titan}

    def add_enemy(self):
        chance = random.randint(1, 100)
        type = self.Types["Enemy"]
        match chance:
            case chance if 1 < chance < 40:
                type = self.Types["Enemy"]
            case chance if 41 < chance < 64:
                type = self.Types["Kamikaze"]
            case chance if 65 < chance < 85:
                type = self.Types["Shooter"]
            case chance if 86 < chance < 100:
                type = self.Types["Elite"]

        self.enemies.append(type(self.screen, self.player, self))
        self.spawned += 1

    def add_titan(self):
        if self.kills % 50 == 0 and self.kills != self.spawnedTitan and self.kills != 0:
            self.spawnedTitan = self.kills
            self.enemies.append(enemy_module.Titan(self.screen, self.player, self))
            self.spawned += 1

    def shoot(self, screen, x, y, width, height, color, angle):
        self.bullets.append(enemy_bullets_module.EnemyBullet(screen, x, y, width, height, color, angle))

    def checkBulletOffScreenAndMove(self):
        for bullet in self.bullets:
            bullet.move()
            bullet.draw()
            if bullet.off_screen():
                self.bullets.remove(bullet)

    def check_for_dead(self):
        enemiesToRemove = []
        grenadesToExplode = []
        for enemy in self.enemies:

            for bullet in self.player.weapon.bullets:
                if (bullet.x < enemy.x+15 and bullet.y > enemy.y-15 and bullet.y < enemy.y+15 and bullet.x > enemy.x -15) or (bullet.y+4 < enemy.y + 15 and bullet.y+4 > enemy.y-15 and bullet.x <enemy.x+15 and bullet.x>enemy.x-15) or (bullet.x+4 > enemy.x-15 and bullet.x+4 < enemy.x+15 and bullet.y > enemy.y-15 and bullet.y < enemy.y+15) or (bullet.x+4 > enemy.x-15 and bullet.x+4 < enemy.x+15 and bullet.y+4 > enemy.y-15 and bullet.y-4 < enemy.y+15):
                    # make way for if the bullet is the grenade, it will cause the target to explode in a radius around them and play the explosion sound
                    if isinstance(bullet, bullets_module.Grenade):
                        if not bullet in grenadesToExplode:
                            grenadesToExplode.append(bullet)
                    if isinstance(enemy, enemy_module.Kamikaze):
                        enemy.stopSound()
                        explosion_sound = pygame.mixer.Sound("sfx/explosion.wav")
                        explosion_sound.set_volume(1)
                        explosion_sound.play()
                    if isinstance(enemy, enemy_module.Titan):
                        self.player.weapon.bullets.remove(bullet)
                        enemy.titan_health += 1
                        if enemy.titan_health >= 10:
                            try:
                                enemy.titan_health = 0
                                self.enemies.remove(enemy)
                                self.kills += 1
                                choice = random.randint(1, 3)
                                if choice == 1:
                                    self.player.weapon.addPickup(enemy.x, enemy.y, "Fast Bullet")
                                if choice == 2:
                                    self.player.weapon.addPickup(enemy.x, enemy.y, "Shotgun")
                                if choice == 3:
                                    self.player.weapon.addPickup(enemy.x, enemy.y, "Grenade")
                                gc.collect()
                            except:
                                pass
                    else:
                        chance = random.randint(20, 100)
                        if (isinstance(enemy, enemy_module.Shooter) and not type(enemy) == enemy_module.Elite):
                            if chance >= 90:
                                self.player.weapon.addPickup(enemy.x, enemy.y, "Fast Bullet")
                            elif chance >= 85:
                                if self.player.speed == 7:
                                    pass
                                else:
                                    self.player.speed_up()
                                    power_up_sound = pygame.mixer.Sound("sfx/power_up.wav")
                                    power_up_sound.set_volume(1)
                                    power_up_sound.play(0)
                        elif isinstance(enemy, enemy_module.Elite):
                            if chance >= 85:
                                self.player.weapon.addPickup(enemy.x, enemy.y, "Shotgun")
                            elif chance >= 80:
                                if self.player.speed == 7:
                                    pass
                                else:
                                    self.player.speed_up()
                                    power_up_sound = pygame.mixer.Sound("sfx/power_up.wav")
                                    power_up_sound.set_volume(1)
                                    power_up_sound.play(0)
                        elif isinstance(enemy, enemy_module.Kamikaze):
                            if chance >= 90:
                                self.player.weapon.addPickup(enemy.x, enemy.y, "Grenade")
                            elif chance >= 85:
                                if self.player.speed == 7:
                                    pass
                                else:
                                    self.player.speed_up()
                                    power_up_sound = pygame.mixer.Sound("sfx/power_up.wav")
                                    power_up_sound.set_volume(1)
                                    power_up_sound.play(0)

                        if enemy not in enemiesToRemove:
                            enemiesToRemove.append(enemy)
                        #except Exception as e:
                        #    print(f"failed to remove {enemy} due to {e}")


                        try:
                            self.player.weapon.bullets.remove(bullet)
                        except:
                            print(f"failed to remove {bullet}")
                        gc.collect()

        for enemy in enemiesToRemove:
            self.enemies.remove(enemy)
            self.kills += 1
            gc.collect()
        for grenade in grenadesToExplode:
            explosion_sound = pygame.mixer.Sound("sfx/grenade_explosion.wav")
            explosion_sound.set_volume(1)
            explosion_sound.play()
            for i in range(24):
                self.player.weapon.grenadeFire(grenade.x, grenade.y, math.pi / 12 * i, pygame.Color("Green"))

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
                if isinstance(enemy, enemy_module.Kamikaze):
                    enemy.stopSound()
                    explosion_sound = pygame.mixer.Sound("sfx/explosion.wav")
                    explosion_sound.set_volume(1)
                    explosion_sound.play()
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



