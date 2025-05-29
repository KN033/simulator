import pygame,sys
from Buttons import Button
from Inputboxs import InputBox

class Screens:
    def __init__(self):
        pygame.init()
        self.Screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Squash Ball Hitting Machine G7 Simulation")
        self.parameterInput = {}
        self.parameterInput.setdefault("Racket angle",45)
        self.parameterInput.setdefault("Width", 2.0)
        self.parameterInput.setdefault("Length", 3.0)

        self.hintpic = pygame.image.load("C:/FRA162-163/simulator/Hint.png")
        # self.hintpic=pygame.image.load("C:\FRA162-163\simulator\Hint.png")

    def get_font(self,size):
        return pygame.font.Font(None,size)

    def input_box(self,title,rect_size):
        input_box_text=self.get_font(33).render(title,True,(219,48,122))
        return (pygame.Rect(self.Screen,(255,255,255),rect_size,0,25)),(self.Screen.blit(input_box_text,(rect_size[0],rect_size[1])))
    
    def default_screen (self):
        while True:
            self.Screen.fill((0,0,0))
            defaultMouse_pos = pygame.mouse.get_pos()
            titleText = self.get_font(70).render("SQUASH BALL HITTING", True,(219, 48, 122))#219, 48, 122 pink
            titleRect = titleText.get_rect(center=(640,100))
            self.Screen.blit(titleText,titleRect)
  
            # startText=get_font(33).render("Start",True,(255,255,255))#(255,255,255) white #self, image, pos, text_input, font, base_color, hovering_color young green
            startButton=Button(shape=pygame.Rect(self.Screen,(219, 48, 122),(640,600,100,40),0,50),pos=(640,600),text_input="Start",font=self.get_font(33),base_color=(255,255,255), hovering_color=(250, 252, 250))

            #Hint Button
            hintButton=Button(shape=pygame.draw.circle(self.Screen,(255,255,255),(700,120),50),pos=(700,120),text_input="?",font=self.get_font(20),base_color=(255,255,255),hovering_color=(250, 252, 250))

            #Quit Button
            quitButton=Button(shape=pygame.Rect(self.Screen,(255,0,0),(1200,40,40,40),0,25),pos=(1200,40),text_input="X",font=self.get_font(33),base_color=(255,255,255),hovering_color=(250,252,250))
            #Field Setting  #255, 143, 171 PASTEL PINK

            pygame.Rect(self.Screen,(255,255,255),(800, 130, 300, 400),0,25)
            fieldText= self.get_font(33).render("Field Setting",True,(219,48,122))
            self.Screen.blit(fieldText,(850,150))

            input_boxes = [
            InputBox(100, 130, 600, 60,"X pos",self.get_font(33)),
            InputBox(100, 210, 600, 60,"Y pos",self.get_font(33)),
            InputBox(100, 290, 600, 60,"Freefall",self.get_font(33)),
            InputBox(100, 370, 600, 60,"Racket angle",self.get_font(33)),
            InputBox(820,250,260,60,"Length",self.get_font(33)),
            InputBox(820,350,260,60,"Width",self.get_font(33))]

            for Buttons in [startButton, hintButton,quitButton]:
                Buttons.changeColor(defaultMouse_pos)
                Buttons.update(self.Screen)

            for box in input_boxes:
                box.draw(self.Screen)

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if startButton.checkForInput(defaultMouse_pos):
                    #     self.result_screen()
                    if startButton.checkForInput(defaultMouse_pos):
                        required_keys = ["X pos", "Y pos", "Freefall", "Racket angle", "Length", "Width"]
                        if all(key in self.parameterInput for key in required_keys):
                            self.result_screen()
                        else:
                            print("กรุณากรอกข้อมูลให้ครบก่อนเริ่ม") 
                    if hintButton.checkForInput(defaultMouse_pos):
                        self.hint_screen()
                    if quitButton.checkForInput(defaultMouse_pos):
                        pygame.quit()
                        sys.exit()
                for box in input_boxes:
                    box.handle_event(event, self.parameterInput)
                

            pygame.display.update()


    def result_screen(self):
        while True:
            self.Screen.fill((0,0,0))
            resultMouse_pos=pygame.mouse.get_pos()
            pygame.Rect(self.Screen,(255,255,255),(90,100,540,300),0,25)
            pygame.Rect(self.Screen,(255,255,255),(650,100,540,300),0,25)
            pygame.Rect(self.Screen,(255,255,255),(650,420,540,250),0,25)
            pygame.Rect(self.Screen,(255,255,255),(90,420,600,250),0,25)


            # resetText=get_font(33).render("Start",True,(255,255,255))#(255,255,255) white #self, image, pos, text_input, font, base_color, hovering_color young green
            resetButton=Button(shape=pygame.draw.rect(self.Screen,(219, 48, 122),(640,600,100,40),0,50),pos=(640,600),text_input="Reset",font=self.get_font(33),base_color=(255,255,255), hovering_color=(250, 252, 250))

            #Quit Button
            quitButton=Button(shape=pygame.draw.rect(self.Screen,(255,0,0),(1200,40,40,40),0,25),pos=(1200,40),text_input="X",font=self.get_font(33),base_color=(255,255,255),hovering_color=(250,252,250))
            #Field Setting  #255, 143, 171 PASTEL PINK

            for Buttons in [resetButton,quitButton]:
                Buttons.changeColor(resultMouse_pos)
                Buttons.update(self.Screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resetButton.checkForInput(resultMouse_pos):
                        self.default_screen()
                    if quitButton.checkForInput(resultMouse_pos):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()

    def hint_screen(self):
        while True:      
            hintMouse_pos=pygame.mouse.get_pos()
            self.Screen.fill(0,0,0)
            self.Screen.blit(self.hintpic,(0,0))

            backButton=Button(shape=pygame.draw.rect(self.Screen,(219, 48, 122),(640,600,100,40),0,50),pos=(640,600),text_input="Back",font=self.get_font(33),base_color=(255,255,255), hovering_color=(250, 252, 250))
            quitButton=Button(shape=pygame.draw.rect(self.Screen,(255,0,0),(1200,40,40,40),0,25),pos=(1200,40),text_input="X",font=self.get_font(33),base_color=(255,255,255),hovering_color=(250,252,250))
            for Buttons in [backButton,quitButton]:
                Buttons.changeColor(hintMouse_pos)
                Buttons.update(self.Screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if backButton.checkForInput(hintMouse_pos):
                        self.default_screen()
                    if quitButton.checkForInput(hintMouse_pos):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()

Screens.default_screen()

