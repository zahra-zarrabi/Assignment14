import random
import time
import sys

import pygame
pygame.init()
class Color:
    green = (10,70,20)
    pink = (230, 7, 255)
    red = (100, 5, 2)
    blue = (6, 0, 250)
    yellow = (255, 235, 0)
    light=(80,57,66)

class Gerdali:
    images=['orange.png','anar.png','persimmon.png']
    def __init__(self):
        self.r=50
        self.x=random.randint(7,Game.width-7)
        self.y=random.randint(7,Game.height-7)
        self.color=random.choice([Color.yellow,Color.green,Color.pink,Color.red,Color.blue])
        self.image_path=random.choice(Gerdali.images)
        self.image=pygame.image.load(self.image_path)
        self.area = pygame.draw.circle(Game.screen, self.color, (self.x, self.y), self.r)
    def show(self):
        self.area = pygame.draw.circle(Game.screen,self.color,(self.x,self.y),self.r)
        Game.screen.blit(self.image,[self.x-30,self.y-30])
    def move(self):
        self.x=random.randint(5,Game.width-7)
        self.y=random.randint(5,Game.height-7)

class Game:
    width=900
    height=600
    screen=pygame.display.set_mode((width,height))
    bg_color=Color.light
    score=0
    secund=0
    @staticmethod
    def play():
        clock=pygame.time.Clock()
        gerdalies=[Gerdali()]

        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    for gerdali in gerdalies:
                        if gerdali.area.collidepoint(event.pos):
                            if gerdali==gerdalies[-1]:
                                while True:
                                    temp=Gerdali()
                                    if all(temp.image_path != g.image_path or temp.color !=g.color for g in gerdalies):
                                        gerdalies.append(temp)
                                        Game.score +=1
                                        break

                            else:
                                Game.play()
                        gerdali.move()

            Game.screen.fill((Game.bg_color))
            for gerdali in gerdalies:
                 gerdali.show()

            endtime = time.time()
            second = endtime - start_time
            if second > 70:
                print('game over')
                sys.exit()
            if len(gerdalies) == 16:
                print('you win')
                sys.exit()

            pygame.display.set_caption('score: ' + str(Game.score)+'                          time: %d' % int(second))
            pygame.display.update()
            clock.tick(24)

if __name__ =="__main__":
    start_time=time.time()
    Game.play()
