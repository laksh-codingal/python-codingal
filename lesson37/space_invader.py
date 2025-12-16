
import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTNCE = 27

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("C:/Users/laksh/OneDrive/Desktop/python codingal/lesson37/bg.png")
pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load("C:/Users/laksh/OneDrive/Desktop/python codingal/lesson37/ufo.png")
pygame.siplay.set_icon(icon)

playerimg = pygame.image.load("C:/Users/laksh/OneDrive/Desktop/python codingal/lesson37/player.png")
playerX = PLAYER_START_X
player_Y = PLAYER_START_Y
playerX_change = 0

enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bulletimg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y


score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y ):
    score = font.render("Score : " + str(score_value), True, pygame.Color("white"))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, pygame.Color("white"))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTNCE
