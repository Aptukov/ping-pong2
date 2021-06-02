from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y > 5:
            self.rect.y-=self.speed
        if keys_pressed[K_UP] and self.rect.y < win_height-80:
            self.rect.y+=self.speed
    def update_1(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_S] and self.rect.y > 5:
            self.rect.y-=self.speed
        if keys_pressed[K_W] and self.rect.y < win_height-80:
            self.rect.y+=self.speed

Back=[200, 255, 255]
win_height=500
win_width=500

window=display.set_mode((win_width, win_height))
display.set_caption('Ping-pong')
window.fill(Back)

game=True
finish=False
clock=time.Clock()
FPS=60

Rocket1=Player("Rocket1.png", 30, 200, 4, 50, 150)
Rocket2=Player("Rocket2.png", 520, 200, 4, 50, 150)
Ball=GameSprite("Ball.png", 250, 250, 4,  50, 50)

font.init()
font = font.Font(None, 35)
lose1=font.render("Player 1 LOSE!", True, [180, 0, 0])
lose2=font.render("Player 2 LOSE!", True, [180, 0, 0])

speed_x=3
speed_y=3

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if finish != True:
        window.fill(Back)
        Rocket1.update()
        Rocket2.update_1()
        Ball.rect.x+=speed_x
        Ball.rect.y+=speed_y
        if sprite.collide_rect(Rocket1, Ball) or sprite.collide_rect(Rocket2, Ball):
            speed_x *= -1
            speed_y *= 1
        if Ball.rect_y > win_height - 50 or Ball.rect_y < 0:
            speed_y *= -1
        if Ball.rect.x < 0:
            finish=True
            window.blit(lose1, (250, 250))
            game_over=True
        if Ball.rect.x > win_height:
            finish=True
            window.blit(lose2, (250, 250))
            game_over=True
        Rocket1.reset()
        Rocket2.reset()
        Ball.reset()
    display.update()
    clock.tick(FPS)
