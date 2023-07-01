import pygame as pg
pg.init()
win_width, win_hight = 800, 600
window = pg.display.set_mode((win_width, win_hight))
pg.display.set_caption("Ping Pong")
class GameSprite:
    def __init__(self, image, x, y, width, height, speed):
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pg.transform.scale(pg.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def control1 (self):
        keys = pg.key.get_pressed()
        if keys[pg.K_s] and self.rect.y < 480:
            self.rect.y += self.speed
        if keys[pg.K_w] and self.rect.y > 30:
            self.rect.y -= self.speed
    def control2 (self):
        keys = pg.key.get_pressed()
        if keys[pg.K_DOWN] and self.rect.y < 480:
            self.rect.y += self.speed
        if keys[pg.K_UP] and self.rect.y > 30:
            self.rect.y -= self.speed
class Ball(GameSprite):
    def move(self):
        global x2, y2, player1, player2, score1, score2
        self.rect.x += x2
        self.rect.y += y2
        if pg.sprite.collide_rect(player1, self):
            x2 = -2
        if pg.sprite.collide_rect(player2, self):
            x2 = 2
        if self.rect.y < 0:
            y2 = 2
        if self.rect.y > 525:
            y2 = -2
        if self.rect.x < 0:
            score1 += 1
            self.rect.x = 400
        if self.rect.x > win_width - self.width:
            score2 += 1
            self.rect.x = 400
x2, y2 = 3,3

        
back = GameSprite("Fon.png", 0, 0, 800, 600, 0)
player1 = Player("1player.png", 760, 250, 20, 70, 3)
player2 = Player("2player.png", 30, 250, 20, 70, 3)
ball = Ball("Ball.png", 400, 100, 10, 10, 0 )
game = True
over1 = GameSprite("winner-1.png", 0, 0, 800, 600, 0)
over2 = GameSprite("winner-2.png", 0, 0, 800, 600, 0)
score1 = 0
score2 = 0
while game:
    pg.time.Clock().tick(120)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    if ball.rect.x < 0:
        ball.rect.x = 400
        score1 += 1
    if score1 >= 5:
        game = False
    if ball.rect.x < 0:
        ball.rect.x = 400
        score2 += 1
    if score2 >= 5:
        game = False

    back.reset()
    label1 = pg.font.SysFont("Arial", 20).render(f"Score:  {score1}", True, "white")
    window.blit(label1,(650,30))
    label2 = pg.font.SysFont("Arial", 20).render(f"Score:  {score2}", True, "white")
    window.blit(label2,(100,30))
    player1.reset()
    player1.control1()
    player2.reset()
    player2.control2()
    ball.reset()
    ball.move()
    def schet_score():
        global score1, score2
        if score1 >= 5 or score2 >= 5:
            return True
        return False
    def game_over():
        global score1, score2
    if score1 >= 5:
        game = False
        over1.reset()
    if score2 >= 5:
        game = False
        over2.reset()
    pg.display.flip()
 