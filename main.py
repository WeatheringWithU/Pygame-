import snake_cfg
from functions.Snake import *
from functions.Food import *
from functions.other_function import *


def main(cfg):
    pygame.init()
    SCREESIZE_X, SCREESIZE_Y = cfg.SCREENSIZE_X, cfg.SCREENSIZE_Y
    screensize = (SCREESIZE_X, SCREESIZE_Y)
    screen = pygame.display.set_mode(screensize)
    pygame.display.set_caption('Snake game')
    screen.fill((255, 255, 255))
    clock = pygame.time.Clock()
    # 开始UI 选择开始后循环可以正常进行
    global key
    isdead, level, username = StartUI(screen, cfg, key)
    key = username
    curscores = 0
    snake = Snake()
    food = Food()
    while not isdead:
        # 检测事件
        for event in pygame.event.get():
            # 如果触发了退出事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 如果是按下键盘按键
            elif event.type == pygame.KEYDOWN:
                # 如果按键为方向键 则改变蛇的运动方向
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    snake.changedirection(event.key)
        # 蛇身移动
        snake.move()
        # 将背景填充为白色
        screen.fill((255, 255, 255))
        # 画出贪吃蛇的每个身体块
        pygame.draw.rect(screen, (4, 150, 254), snake.body[0], 0)
        for rect in snake.body[1:]:
            pygame.draw.rect(screen, (20, 220, 39), rect, 0)
        # 判断是否存活
        isdead = snake.isdead(SCREESIZE_X, SCREESIZE_Y)
        # 判断是否吃到方块 吃到则身体加一节 分数加1
        if food.rect == snake.body[0]:
            curscores += 1
            food.remove()
            snake.addnote()
        # 重新设置食物位置
        food.set()
        pygame.draw.rect(screen, (224, 95, 156), food.rect, 0)
        # 记录当前分数
        save_score(level, username, curscores)
        # 展示当前分数
        show_scores(screen, curscores, cfg.pos2, cfg.text2, cfg.color2, font_size=30)
        # 读出当前游戏等级的排行榜数据
        Level_data = read_score(level)
        # 展示最高的三个分数
        show_highest_score(screen, Level_data, cfg.pos3, cfg.pos4, cfg.pos5, cfg.color2, cfg.font_size3)
        # 更新屏幕状态
        pygame.display.update()
        # 设置时间间隔
        if level == 1:
            clock.tick(10)
        elif level == 2:
            clock.tick(15)

    # 如果死亡 返回输出UI
    return EndUI(screen, cfg)


if __name__ == '__main__':
    key = ''
    while True:
        if not main(snake_cfg):
            break
