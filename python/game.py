import pygame, random, math, time

# 初始化 Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

class Ball(pygame.sprite.Sprite):
    def __init__(self, sp, srx, sry, radius, color):
        super().__init__()
        self.speed = sp
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([radius * 2, radius * 2])
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(srx, sry))
        self.direction = random.randint(40, 70)

    def update(self):
        radian = math.radians(self.direction)
        self.dx = self.speed * math.cos(radian)
        self.dy = -self.speed * math.sin(radian)
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y
        
        # 檢查邊界碰撞
        if self.rect.left <= 0 or self.rect.right >= screen.get_width() - 10:
            self.direction = 180 - self.direction  # 反向移動
        elif self.rect.top <= 10:
            self.rect.top = 10
            self.bounceup()
        if self.rect.bottom >= screen.get_height() - 10:
            return True
        else:
            return False

    def bounceup(self):
        self.direction = 360 - self.direction
    
    def bouncelr(self):
        self.direction = (180 - self.direction) % 360

class Brick(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([38, 13])
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

class Pad(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("media/pad.png") 
        self.image.convert()
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height - 20))

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width

    @staticmethod
    def gameover(message):
        global running
        text = font1.render(message, True, (255, 0, 255))
        screen.blit(text, (screen_width // 2 - 100, screen_height // 2 - 20))
        pygame.display.update()
        time.sleep(3)
        running = False

# 遊戲變數初始化
score = 0
font = pygame.font.SysFont("SimHei", 20)
font1 = pygame.font.SysFont("SimHei", 30)
pygame.display.set_caption("打磚塊")
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
allsprite = pygame.sprite.Group()
bricks = pygame.sprite.Group()
ball = Ball(10, 300, 250, 10, (255, 0, 0))
allsprite.add(ball)
pad = Pad()
allsprite.add(pad)
clock = pygame.time.Clock()

# 創建磚塊
for row in range(4):
    for column in range(15):
        color = (0, 255, 0) if row < 2 else (0, 0, 255)
        brick = Brick(color, column * 40 + 1, row * 15 + 1)
        bricks.add(brick)
        allsprite.add(brick)

running = True
playing = False
msgstr = "按左鍵開始遊戲"

# 主遊戲循環
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        playing = True

    if playing:
        screen.blit(background, (0, 0))
        fail = ball.update()
        if fail:
            Pad.gameover("失敗")
        pad.update()
        
        hitbrick = pygame.sprite.spritecollide(ball, bricks, True)
        if hitbrick:
            score += len(hitbrick)
            ball.rect.y += 20  # 向下移動球體
            ball.bounceup()  # 反彈
            if not len(bricks):  # 如果沒有磚塊了
                Pad.gameover("成功")
                
        hitpad = pygame.sprite.spritecollideany(ball, pad)
        if hitpad:
            ball.bounceup()
        
        allsprite.draw(screen)
        msgstr = "得分: " + str(score)
    
    msg = font.render(msgstr, True, (255, 0, 255))
    screen.blit(msg, (screen_width // 2 - 60, screen_height - 20))
    pygame.display.update()

pygame.quit()







