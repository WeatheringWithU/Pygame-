import pygame


class Snake(object):
    def __init__(self):
        # 设定初始方向为向右 初始身体为空
        self.direction = pygame.K_RIGHT
        self.body = []

        # 初始化5个身体块
        for x in range(5):
            self.addnote()

    def addnote(self):
        # left top为身体块的定位位置
        left, top = (0, 00)
        if self.body:
            left, top = (self.body[0].left, self.body[0].top)
        node = pygame.Rect(left, top, 25, 25)
        if self.direction == pygame.K_LEFT:
            node.left -= 25
        elif self.direction == pygame.K_RIGHT:
            node.left += 25
        elif self.direction == pygame.K_UP:
            node.top -= 25
        elif self.direction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0, node)

    # 删除身体块
    def delnote(self):
        self.body.pop()

    def isdead(self, SCREENSIZE_X=600, SCREENSIZE_Y=600):
        # 撞墙
        if self.body[0].x not in range(SCREENSIZE_X):
            return True
        if self.body[0].y not in range(SCREENSIZE_Y):
            return True
        # 撞自己
        if self.body[0] in self.body[1:]:
            return True
        # 撞block

        return False

    def move(self):
        # 在前进方向上头部增加一个方块 尾部减少一个方块
        self.addnote()
        self.delnote()

    def changedirection(self, curkey):
        LR = [pygame.K_LEFT, pygame.K_RIGHT]
        UD = [pygame.K_UP, pygame.K_DOWN]
        if curkey in LR + UD:
            if (curkey in LR) and (self.direction in LR):
                return
            if (curkey in UD) and (self.direction in UD):
                return
            self.direction = curkey

