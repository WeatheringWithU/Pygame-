import pygame
import sys
import json


def show_scores(screen, scores, pos, text, color, font_size=30):
    cur_font = pygame.font.SysFont("宋体", font_size)
    cur_font.set_bold(False)
    cur_font.set_italic(False)
    text_fmt = cur_font.render(text + str(scores), False, color)
    screen.blit(text_fmt, pos)


def StartUI(screen, cfg, key):
    # 调用用户名输入UI
    if key == '':
        username = inputUI(screen)
    else:
        username = key
    # 欢迎为大号字体
    cur_font1 = cfg.UIfont1
    text_fmt1 = cur_font1.render('Welcome!', False, cfg.UIcolor1)
    # 选项为小号字体 选项1为level1 选项2为level2
    cur_font2 = cfg.UIfont2
    text_fmt2 = cur_font2.render('level1', False, cfg.UIcolor2)
    text_fmt3 = cur_font2.render('level2', False, cfg.UIcolor2)
    # alpha通道起到滤镜效果 填充一层模糊界面
    surface = screen.convert_alpha()
    surface.fill((127, 255, 212, 2))
    # 定义文字位置并创建按钮
    text_rect1 = text_fmt1.get_rect()
    text_rect1.centerx, text_rect1.centery = cfg.SCREENSIZE_X / 2, cfg.SCREENSIZE_Y / 2 - 50
    # 显示文字1 即欢迎选项
    surface.blit(text_fmt1, text_rect1)

    # 定义按钮的位置 屏幕中心位置
    button_width, button_height = 100, 40
    button_start_x_left = cfg.SCREENSIZE_X / 2 - button_width - 20
    button_start_x_right = cfg.SCREENSIZE_X / 2 + 20
    button_start_y = cfg.SCREENSIZE_Y / 2 - button_height / 2 + 20
    pygame.draw.rect(surface, (0, 255, 255), (button_start_x_left, button_start_y, button_width, button_height))
    # 定义按钮1的矩形
    text_level1_rect = text_fmt2.get_rect()
    text_level1_rect.centerx, text_level1_rect.centery = button_start_x_left + button_width / 2, button_start_y + button_height / 2
    surface.blit(text_fmt2, text_level1_rect)
    # 定义按钮2的矩形
    pygame.draw.rect(surface, (0, 255, 255), (button_start_x_right, button_start_y, button_width, button_height))
    text_level2_rect = text_fmt3.get_rect()
    text_level2_rect.centerx, text_level2_rect.centery = button_start_x_right + button_width / 2, button_start_y + button_height / 2
    surface.blit(text_fmt3, text_level2_rect)
    while True:
        screen.blit(surface, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button:
                # 鼠标选择level1 返回死亡为False 速度为10
                if text_level1_rect.collidepoint(pygame.mouse.get_pos()):
                    return False, 1, username
                # 鼠标选择level2 返回死亡为False 速度为15
                if text_level2_rect.collidepoint(pygame.mouse.get_pos()):
                    return False, 2, username
        pygame.display.update()


def EndUI(screen, cfg):
    # 欢迎为大号字体
    cur_font1 = cfg.UIfont1
    text_fmt1 = cur_font1.render('Game Over!', False, cfg.UIcolor1)
    # 选项为小号字体 选项1为level1 选项2为level2
    cur_font2 = cfg.UIfont2
    text_fmt2 = cur_font2.render('restart', False, cfg.UIcolor2)
    text_fmt3 = cur_font2.render('quit', False, cfg.UIcolor2)
    # alpha通道起到滤镜效果 填充一层模糊界面
    surface = screen.convert_alpha()
    surface.fill((127, 255, 212, 2))
    # 定义文字位置并创建按钮
    text_rect1 = text_fmt1.get_rect()
    text_rect1.centerx, text_rect1.centery = cfg.SCREENSIZE_X / 2, cfg.SCREENSIZE_Y / 2 - 50
    # 显示文字1 即欢迎选项
    surface.blit(text_fmt1, text_rect1)
    # 定义按钮的位置 屏幕中心位置
    button_width, button_height = 100, 40
    button_start_x_left = cfg.SCREENSIZE_X / 2 - button_width - 20
    button_start_x_right = cfg.SCREENSIZE_X / 2 + 20
    button_start_y = cfg.SCREENSIZE_Y / 2 - button_height / 2 + 20
    pygame.draw.rect(surface, (0, 255, 255), (button_start_x_left, button_start_y, button_width, button_height))
    # 定义按钮1的矩形
    text_restart_rect = text_fmt2.get_rect()
    text_restart_rect.centerx, text_restart_rect.centery = button_start_x_left + button_width / 2, button_start_y + button_height / 2
    surface.blit(text_fmt2, text_restart_rect)
    # 定义按钮2的矩形
    pygame.draw.rect(surface, (0, 255, 255), (button_start_x_right, button_start_y, button_width, button_height))
    text_quit_rect = text_fmt3.get_rect()
    text_quit_rect.centerx, text_quit_rect.centery = button_start_x_right + button_width / 2, button_start_y + button_height / 2
    surface.blit(text_fmt3, text_quit_rect)
    while True:
        screen.blit(surface, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button:
                # 鼠标选择restart 返回死亡为False
                if text_restart_rect.collidepoint(pygame.mouse.get_pos()):
                    return True
                # 鼠标选择quit 返回死亡为True
                if text_quit_rect.collidepoint(pygame.mouse.get_pos()):
                    return False
        pygame.display.update()


def save_score(level, username, score):
    file = open('score_record.txt', 'r')
    data = json.load(file)
    file.close()
    file = open('score_record.txt', 'w')
    # 写入对应等级的该用户名的分数
    data['Level' + str(level)][username] = score
    json.dump(data, file)
    file.close()


def read_score(level):
    # 生成代表等级的字符串
    Level = 'Level' + str(level)
    file = open('score_record.txt', 'r')
    data = json.load(file)

    # 得到排序后的该等级的分数--元组形式 (姓名，分数)
    Level_data = sorted(data[Level].items(), key=lambda x: x[1], reverse=True)
    file.close()
    # 读取前三个数据即前三高分
    if len(Level_data) < 3:
        return Level_data[0:]
    else:
        return Level_data[0:3]


def show_highest_score(screen, Level_data, pos1, pos2, pos3, color, font_size=20):
    # 三个位置显示三个最高分 其中排第一的字体大小为其他的二倍
    # 当最高分不够三个时，用--和0代替
    cur_font1 = pygame.font.SysFont("宋体", 2 * font_size)
    cur_font2 = pygame.font.SysFont("宋体", font_size)
    text_fmt1 = cur_font1.render('1  ' + '----    0', False, color)
    text_fmt2 = cur_font2.render('2  ' + '----    0', False, color)
    text_fmt3 = cur_font2.render('3  ' + '----    0', False, color)
    if len(Level_data) >= 1:
        text_fmt1 = cur_font1.render('1  ' + Level_data[0][0] + '    ' + str(Level_data[0][1]), False, color)
        if len(Level_data) >= 2:
            text_fmt2 = cur_font2.render('2  ' + Level_data[1][0] + '    ' + str(Level_data[1][1]), False, color)
            if len(Level_data) >= 3:
                text_fmt3 = cur_font2.render('3  ' + Level_data[2][0] + '    ' + str(Level_data[2][1]), False, color)

    screen.blit(text_fmt1, pos1)
    screen.blit(text_fmt2, pos2)
    screen.blit(text_fmt3, pos3)


def inputUI(screen):
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(250, 400, 140, 32)
    color_inactive = (221, 174, 255)
    color_active = (251, 73, 255)
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 如果鼠标点到输入框内
                if input_box.collidepoint(event.pos):
                    # 激活输入框
                    active = not active
                else:
                    active = False
                # 随着输入框的激活改变边框的颜色
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((127, 255, 212))
        # 生成一个新的surface对象并在上面渲染指定的文本
        txt_surface = font.render(text, True, color)
        txt_please = font.render('Input Username:', True, color)
        # 如果字符串太长 则增加输入框的长度
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # 绘制文字
        screen.blit(txt_please, (input_box.x - 180, input_box.y + 5))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # 绘制输入框
        pygame.draw.rect(screen, color, input_box, 2)
        # 显示图像
        pygame.display.flip()
        clock.tick(30)


def init_score_json():
    dict = {
        'Level1':
            {'Liming': 1, 'srs': 7},
        'Level2':
            {'Lihua': 2, 'srs': 4}
    }
    file = open('score_record.txt', 'w')
    # 写入对应等级的该用户名的分数
    json.dump(dict, file)
    file.close()
