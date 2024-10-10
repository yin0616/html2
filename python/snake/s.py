import random, sys, time, pygame
from pygame.locals import *
from collections import deque

# 螢幕設置
Screen__height = 480
Screen__wight = 600
Size = 20  # 小方格大小
Line_Width = 1
# 遊戲座標範圍
Area_x = (0, Screen__wight // Size - 1)
Area_y = (2, Screen__height // Size - 1)
# 食物初步設置
# 食物分值 + 顏色
food_style_List = [(10, (255, 100, 100)), (20, (100, 255, 100)), (30, (100, 100, 255))]
# 整體顏色設置
Light = (100, 100, 100)
Dark = (200, 200, 200)
Black = (0, 0, 0)
Red = (200, 30, 30)
Back_ground = (40, 40, 60)

# 文本輸出格式設置
def Print_Txt(screen, font, x, y, text, fcolor=(255, 255, 255)):
    Text = font.render(text, True, fcolor)
    screen.blit(Text, (x, y))

# 初始化蛇
def init_snake():
    snake = deque()
    snake.append((2, Area_y[0]))
    snake.append((1, Area_y[0]))
    snake.append((0, Area_y[0]))
    return snake

# 食物設置
def Creat_Food(snake):
    # 創建一個包含所有可能的食物位置的集合
    all_positions = set((x, y) for x in range(Area_x[0], Area_x[1] + 1) for y in range(Area_y[0], Area_y[1] + 1))
    
    # 從這個集合中移除蛇的身體所在的位置
    for position in snake:
        all_positions.discard(position)
    
    # 從剩下的位置中隨機選擇一個作為食物的位置
    food_x, food_y = random.choice(list(all_positions))
    
    return food_x, food_y

# 食物風格
def Food_Style():
    return food_style_List[random.randint(0, 2)]  # 返回隨機分值和顏色

def main():
    pygame.init()
    screen = pygame.display.set_mode((Screen__wight, Screen__height))  # 初始化顯示螢幕
    pygame.display.set_caption('貪吃蛇')  # 視窗標題

    # 字體設置
    font1 = pygame.font.SysFont("SimHei", 24)
    font2 = pygame.font.SysFont(None, 72)
    fwidth, fheight = font2.size("gameover")

    # 初始化變量
    snake = init_snake()
    food = Creat_Food(snake)
    food_style = Food_Style()
    pos = (0, 1)  # 初始方向
    game_over = False
    game_start = False
    score = 0
    orispeed = 0.3
    speed = orispeed
    last_move_time = time.time()
    pause = False
    b = True  # 控制蛇移動

    while True:
        # 處理事件
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if game_over:
                        # 重置遊戲
                        game_start = True
                        game_over = False
                        b = True
                        snake = init_snake()
                        food = Creat_Food(snake)
                        food_style = Food_Style()
                        pos = (1, 0)
                        score = 0
                        last_move_time = time.time()
                elif event.key == K_SPACE:
                    if not game_over:
                        pause = not pause
                elif event.key in (K_UP, K_w) and not pos[1]:
                    pos = (0, -1)
                    b = False
                elif event.key in (K_DOWN, K_s) and not pos[1]:
                    pos = (0, 1)
                    b = False
                elif event.key in (K_LEFT, K_a) and not pos[0]:
                    pos = (-1, 0)
                    b = False
                elif event.key in (K_RIGHT, K_d) and not pos[0]:
                    pos = (1, 0)
                    b = False

        # 填充背景色
        screen.fill(Back_ground)

        # 畫網格線
        for x in range(Size, Screen__wight, Size):
            pygame.draw.line(screen, Black, (x, Area_y[0] * Size), (x, Screen__height))
        for y in range(Size, Screen__height, Size):
            pygame.draw.line(screen, Black, (0, y), (Screen__wight, y), Line_Width)

        # 如果遊戲沒有結束，讓蛇移動
        if not game_over:
            curTime = time.time()
            if curTime - last_move_time > speed:
                if not pause:
                    last_move_time = curTime
                    next_s = (snake[0][0] + pos[0], snake[0][1] + pos[1])

                    # 吃到食物
                    if next_s == food:
                        snake.appendleft(next_s)
                        score += food_style[0]
                        speed = orispeed - 0.03 * (score // 100)
                        food = Creat_Food(snake)
                        food_style = Food_Style()
                    else:
                        # 檢查是否撞到牆或自身
                        if Area_x[0] <= next_s[0] <= Area_x[1] and Area_y[0] <= next_s[1] <= Area_y[1] and next_s not in snake:
                            snake.appendleft(next_s)
                            snake.pop()
                        else:
                            game_over = True

        # 畫食物
        if not game_over:
            pygame.draw.rect(screen, food_style[1], (food[0] * Size, food[1] * Size, Size, Size), 0)
            # 畫蛇
            for s in snake:
                pygame.draw.rect(screen, Dark, (s[0] * Size + Line_Width, s[1] * Size + Line_Width, Size - Line_Width * 2, Size - Line_Width * 2), 0)

            Print_Txt(screen, font1, 30, 7, f"速度: {score // 100}")
            Print_Txt(screen, font1, 450, 7, f"得分: {score}")

            # 畫gameover
            if game_over and game_start:
                Print_Txt(screen, font2, (Screen__wight - fwidth) // 2, (Screen__height - fheight) // 2, "gameover", Red)

        pygame.display.update()

if __name__ == '__main__':
    main()
      






     



