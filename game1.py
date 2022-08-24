import pygame
import MyVector as mv #지난 번에 구현했던 vector 클래스

#컬러 설정할때 편하라고 정의해 놓은 딕셔너리
rgb = {
    'BLACK':(0, 0, 0),
    'WHITE':(255, 255, 255),
    'BLUE':(0, 0, 255),
    'GREEN':(0, 255, 0),
    'RED':(255, 0, 0)
}

#Implementor
class Actor:

    def __init__(self, x, y):
        self.pos = mv.MyVector(x, y)
        self.name = ""
        self.skill = ""

    def setPos(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def move(self, delta):
        self.pos = self.pos + delta
    
    def setName(self, name):
        self.name = name
    
    def setSkill(self, skill):
        pass


#Concrete Implementor 1
class Hero(Actor):

    def setSkill(self, skill):
        self.skill = skill

#Concrete Implementor 2
class Enermy(Actor):

    def setSkill(self, skill):
        self.skill = skill



#Abstraction 
class GameFramework:

    def __init__(self):
        self.pygame = pygame
        self.screen = 0

        self.nY = 0 #화면 차원
        self.nX = 0

        self.hero = 0 # 지금은 주인공이 1명있다고 가정

        print("init")

    def setDisplay(self, nX, nY): #게임화면의 크기를 결정
        self.nY = nY
        self.nX = nX
        self.screen = self.pygame.display.set_mode([self.nX, self.nY])
        self.pygame.display.set_caption("Prince") #게임창의 이름

    #Bridge Pattern에서 Implementor를 속성으로 가질 수 있도록 하는 부분
    #Abstraction과 Implementor가 연결되는 부분
    def setHero(self, hero:Actor):
        self.hero = hero

    def ready(self):
        self.pygame.init() #pygame 초기화

    def drawPolygon(self, color, points, thickness):
        self.pygame.draw.polygon(self.screen, color, points, thickness)

    def drawEdges(self):
        p1 = mv.MyVector(0, 0)
        p2 = mv.MyVector(0, 10)
        p3 = mv.MyVector(10, 0)
        
        self.drawPolygon(rgb["WHITE"], [p1.vec(), p2.vec(), p3.vec()], 1)

    def printText(self, msg, color, pos):
        font= self.pygame.font.SysFont("consolas",20)
        textSurface     = font.render(msg,True, color, None) #self.pygame.Color(color)
        textRect        = textSurface.get_rect()
        textRect.topleft= pos
        self.screen.blit(textSurface, textRect)

    #게임 실행
    def launch(self):
        pass



class WhiteGame(GameFramework):

    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()
  
        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done: 
            clock.tick(60) #set on 30 frames per second

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    done = True

                elif event.type == self.pygame.KEYDOWN: #키를 눌렀을때
                    print("key down")
                    if event.key == self.pygame.K_LEFT: #어떤키가 눌렸는가?
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT:
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN:
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP:
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP:
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False


            if keyFlag == True:

                self.hero.move(delta) #주인공의 위치가 업데이트가 됨

                print("pressed", self.hero.pos.getState()) #in console
                self.screen.fill(rgb["WHITE"]) #특성을 살린 부분
                self.printText(self.hero.name, rgb["RED"], self.hero.pos.vec()) 
                self.printText(self.hero.skill, rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()



class BlackGame(GameFramework):

    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()
  
        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done: 
            clock.tick(30) #set on 30 frames per second

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    done = True

                elif event.type == self.pygame.KEYDOWN:
                    print("key up")
                    if event.key == self.pygame.K_LEFT:
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT:
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN:
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP:
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP:
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False


            if keyFlag == True:

                self.hero.move(delta)

                print("pressed", self.hero.pos.getState()) #in console
                self.screen.fill(rgb["BLACK"]) #특성화된 부분
                self.printText(self.hero.name, rgb["RED"], self.hero.pos.vec()) 
                self.printText(self.hero.skill, rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()



game = BlackGame() 
game.ready()
game.setDisplay(1500, 1000)

hero = Hero(0, 0)
hero.setName("prince")
hero.setSkill("swing a sword")

monster = Enermy(50, 50)
monster.setName("weak moster")
monster.setSkill("hit the body")

game.setHero(monster)

game.launch()






