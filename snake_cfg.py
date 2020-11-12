import pygame


# 方块大小
cube = 25
pygame.init()
# 屏幕大小
SCREENSIZE_X = 600
SCREENSIZE_Y = 600

# highest scores的text
pos1 = (50, 500)
text1 = 'Highest Scores: '
color1 = (223, 223, 223)
font_size1 = 30
# curscores 的text
pos2 = (50, 550)
text2 = 'Scores: '
color2 = (223, 223, 223)
font_size2 = 30
# highest 的 text
pos3 = (400, 480)
pos4 = (400, 520)
pos5 = (400, 540)
font_size3 = 20


# UI字体
UIfont_size_big = 60
UIfont_size_small = 30
UIfont1 = pygame.font.SysFont("宋体", UIfont_size_big)
UIfont2 = pygame.font.SysFont("宋体", UIfont_size_small)
UIcolor1 = (255, 151, 23)
UIcolor2 = (255, 151, 23)
