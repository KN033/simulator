import pygame,sys
import math
import numpy as np
import matplotlib.pyplot as plt
import io
pygame.init()

class Screens:
    def __init__(self):
        
        self.Screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Squash Ball Hitting Machine G7 Simulation")
        self.parameterInput = {}
        self.parameterInput.setdefault("Racket angle",45)
        self.parameterInput.setdefault("Width", 2.0)
        self.parameterInput.setdefault("Length", 3.0)

        self.hintpic = pygame.image.load("C:/FRA162-163/simulator/Hint.png")
        self.Fieldpic= pygame.image.load("C:/FRA162-163/simulator/Field.png")
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
            titleText = self.get_font(90).render("SQUASH BALL HITTING", True,(219, 48, 122))#219, 48, 122 pink
            titleRect = titleText.get_rect(center=(640,70))
            self.Screen.blit(titleText,titleRect)
  
            # startText=get_font(33).render("Start",True,(255,255,255))#(255,255,255) white #self, image, pos, text_input, font, base_color, hovering_color young green
            startButton = Button(pos=(640, 660),text_input="Start",font=self.get_font(44),base_color=(255, 255, 255),hovering_color=(255, 215, 0))

            # Hint Button
            hintButton = Button(pos=(700, 120),text_input="?",font=self.get_font(20),base_color=(255, 255, 255),hovering_color=(255, 215, 0))

            # Quit Button
            quitButton = Button(pos=(1200, 40),text_input="X",font=self.get_font(33),base_color=(255, 255, 255),hovering_color=(255, 215, 0))

            pygame.draw.rect(self.Screen,(255,255,255),(800, 150, 400, 400),0,25)
            fieldText= self.get_font(60).render("Field Setting",True,(219,48,122))
            self.Screen.blit(fieldText,(850,170))

            xpos=InputBox(100, 150, 600, 100,"X pos",self.get_font(40))
            ypos=InputBox(100, 270, 600, 100,"Y pos",self.get_font(40))
            freefall=InputBox(100, 390, 600, 100,"Freefall",self.get_font(40))
            racket_angle=InputBox(100, 510, 600, 100,"Racket angle",self.get_font(40))
            length=InputBox(820,260,340,80,"Length",self.get_font(33))
            width=InputBox(820,380,340,80,"Width",self.get_font(33))

            input_boxes = [xpos, ypos, freefall, racket_angle, length, width]
            # input_boxes = [
            # InputBox(100, 150, 600, 100,"X pos",self.get_font(33)),
            # InputBox(100, 270, 600, 100,"Y pos",self.get_font(33)),
            # InputBox(100, 390, 600, 100,"Freefall",self.get_font(33)),
            # InputBox(100, 510, 600, 100,"Racket angle",self.get_font(33)),
            # InputBox(820,260,340,80,"Length",self.get_font(33)),
            # InputBox(820,380,340,80,"Width",self.get_font(33))]

            for Buttons in [startButton, hintButton,quitButton]:
                Buttons.change_color(defaultMouse_pos)
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
                    if startButton.check_for_input(defaultMouse_pos):
                        required_keys = ["X pos", "Y pos", "Freefall", "Racket angle", "Length", "Width"]
                        if all(key in self.parameterInput for key in required_keys):
                            self.result_screen()
                        else:
                            print("กรุณากรอกข้อมูลให้ครบก่อนเริ่ม") 
                    if hintButton.check_for_input(defaultMouse_pos):
                        self.hint_screen()
                    if quitButton.check_for_input(defaultMouse_pos):
                        pygame.quit()
                        sys.exit()
                for box in input_boxes:
                    box.handle_event(event, self.parameterInput)
                

            pygame.display.update()

    def result_screen(self):
        while True:
            # Calculate.__init__(Calculate,self.parameterInput)
            # Calculate.run(Calculate)
            self.calculator = Calculate(self.parameterInput)
            self.calculator.run()
            cal_machine_angle=self.calculator.Machine_angle
            cal_machine_rpm=self.calculator.Machine_rpm
            cal_duty_cycle=self.calculator.duty_cycle
            cal_Vin=self.calculator.Vin
            self.Screen.fill((0,0,0))
            resultMouse_pos=pygame.mouse.get_pos()
            pygame.draw.rect(self.Screen,(255,255,255),(90,100,540,300),0,25)
            pygame.draw.rect(self.Screen,(255,255,255),(90,420,540,250),0,25)
            pygame.draw.rect(self.Screen,(255,255,255),(650,100,540,300),0,25)
            pygame.draw.rect(self.Screen,(255,255,255),(650,420,540,250),0,25)


            sizeImage=pygame.transform.scale(self.Fieldpic, (448, 300))#size of the field image=(2109,1411)
            centerImage=sizeImage.get_rect(center=(400, 300))
            self.Screen.blit(sizeImage, centerImage.topleft)
 

            rect_size = (80, 20)
            rect_surface = pygame.Surface(rect_size, pygame.SRCALPHA)  # โปร่งใส
            pygame.draw.rect(rect_surface,(219, 48, 122),(340,200,*rect_size))
            pygame.draw.line(self.Screen,(255,255,255),(250,180),(400,180),4)

            rotated = pygame.transform.rotate(rect_surface,cal_machine_angle) 
            rotated_rect = rotated.get_rect(center=(340, 200))
            self.Screen.blit(rotated, rotated_rect.topleft)

            pygame.display.flip()


            resultText_Machine_angle=self.get_font(33).render("Machine Angle: {:.2f}".format(cal_machine_angle),True,(219, 48, 122))#219, 48, 122 pink
            self.Screen.blit(resultText_Machine_angle,(100,450))
            resultText_Machine_rpm=self.get_font(33).render("Machine RPM: {:.2f}".format(cal_machine_rpm),True,(219, 48, 122))
            self.Screen.blit(resultText_Machine_rpm,(100,500))
            resultText_duty_cycle=self.get_font(33).render("Duty Cycle: {:.2f}%".format(cal_duty_cycle),True,(219, 48, 122))
            self.Screen.blit(resultText_duty_cycle,(100,550))
            resultText_Vin=self.get_font(33).render("Vin: {:.2f}V".format(cal_Vin),True,(219, 48, 122))
            self.Screen.blit(resultText_Vin,(100,600))

            plot_surface_1 = Calculate.topView()
            plot_surface_2 = Calculate.projectile_motion()


            self.Screen.blit(plot_surface_1, (670, 120))
            self.Screen.blit(plot_surface_2, (670, 440))

            # startText=get_font(33).render("Start",True,(255,255,255))#(255,255,255) white #self, image, pos, text_input, font, base_color, hovering_color young green
            resetButton = Button(pos=(640, 600),text_input="Start",font=self.get_font(44),base_color=(255, 255, 255),hovering_color=(255, 215, 0))

            # Quit Button
            quitButton = Button(pos=(1200, 40),text_input="X",font=self.get_font(33),base_color=(255, 255, 255),hovering_color=(255, 215, 0))


            for Buttons in [resetButton,quitButton]:
                Buttons.change_color(resultMouse_pos)
                Buttons.update(self.Screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resetButton.check_for_input(resultMouse_pos):
                        self.default_screen()
                    if quitButton.check_for_input(resultMouse_pos):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()

    def hint_screen(self):
        while True:      
            hintMouse_pos=pygame.mouse.get_pos()
            self.Screen.fill((0,0,0))
            scaled_image = pygame.transform.scale(self.hintpic, (1280, 720))
            self.Screen.blit(scaled_image,(0,0))

            # startText=get_font(33).render("Start",True,(255,255,255))#(255,255,255) white #self, image, pos, text_input, font, base_color, hovering_color young green
            backButton = Button(pos=(640, 600),text_input="Back",font=self.get_font(40),base_color=(255, 255, 255),hovering_color=(250, 252, 250))
            # Quit Button
            quitButton = Button(pos=(1200, 40),text_input="X",font=self.get_font(33),base_color=(255, 255, 255),hovering_color=(250, 252, 250))

            for Buttons in [backButton,quitButton]:
                Buttons.change_color(hintMouse_pos)
                Buttons.update(self.Screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if backButton.check_for_input(hintMouse_pos):
                        self.default_screen()
                    if quitButton.check_for_input(hintMouse_pos):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()

class Button:
    
    def __init__(self, pos, text_input, font, base_color, hovering_color):
        self.x_pos, self.y_pos = pos
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input

        self.text = self.font.render(self.text_input, True, self.base_color)
        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.button_rect = pygame.Rect(0, 0, self.rect.width + 40, self.rect.height + 20)
        self.button_rect.center = (self.x_pos, self.y_pos)
    def draw(self, screen):
        # Draw rounded rectangle behind text
        
        pygame.draw.rect(screen, (219, 48, 122), self.button_rect, border_radius=20)
        screen.blit(self.text, self.rect)

    def update(self, screen):
        self.draw(screen)

    def check_for_input(self, position):
        return self.button_rect.collidepoint(position)

    def change_color(self, position):
        if self.button_rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)



class InputBox:
    def __init__(self, x, y, w, h, label,f):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (255, 255, 255)
        self.text = ''
        self.font = f
        self.txt_surface = self.font.render(self.text, True, (219,48,122))
        self.active = False
        self.label = label

    def handle_event(self, event,parameter_Input):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            if self.active:
                self.color = (219, 48, 122)
            else:
                self.color = (255, 255, 255)
        elif event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = (219, 48, 122)
            else:
                self.color = (255, 255, 255)
        # Handle text input
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                try:
                    #Screens.parameterInput[self.label] = float(self.text)
                    parameter_Input[self.label] = float(self.text)
                except ValueError:
                    print(f"'{self.text}' ไม่สามารถแปลงเป็น float ได้")
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                 if (len(self.text) < 7) and (event.key in number_keys):
                    if event.key == pygame.K_PERIOD and '.' not in self.text:
                        self.text += '.'
                    elif event.unicode.isdigit() or event.unicode == '.':
                        # ตรวจสอบว่ามีจุดทศนิยมแล้วหรือไม่
                        if event.unicode.isdigit() or (event.unicode == '.' and '.' not in self.text):
                            self.text += event.unicode
          
            self.txt_surface = self.font.render(self.text, True, self.color)



    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0, 25)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, 25)
        label_surface = self.font.render(self.label, True, (219, 48, 122))
        screen.blit(label_surface, (self.rect.x + 30, self.rect.y + 30))
        screen.blit(self.txt_surface, (self.rect.x + 200, self.rect.y + 30))

    def get_value(self):
        return self.text




class Calculate:
    def __init__(self,parameter):
        self.parameters=parameter
        self.data = {}
        self.g=9.81
        self.R_racket=0.225
        self.machine_heigth=0.3911111
        self.M_bat=0.49
        self.Inertia=0.008
        

        self.e=(1/0.401)
        self.M_ball=0.025

        self.u=2.57

        self.Motor_rpm=4000.0
        self.Machine_rpm=0.0
        self.VCC=12.0
        self.Vin=0.0
        self.duty_cycle=0.0
        self.Machine_angle=0.0

    def pythagoras(self,x,y):
        return (math.sqrt((x**2)+(y**2)))

    def freefall(self,s):
        return (2*9.81*(s-(self.machine_heigth)))**(1/2)
    
    def find_theta(self,vx):
        term1 = (self.e*vx - self.freefall(self.parameters["Freefall"]))/self.e
        term2 = term1/vx
        return math.atan(term2)*180/math.pi

    def Vball(self,theta,vx):
        return vx/math.cos(math.pi/180*theta)

    def Vbat(self,v_ball,theta,vx):
        return (self.e*self.M_ball*v_ball*math.cos(math.pi/180*theta)+self.M_bat*vx)/self.M_bat

    def find_Sx(self,v,theta):
        a = -(0.5*9.81)/((v*math.cos(math.pi/180*theta)))**2
        b = math.tan(math.pi/180*theta)
        c = self.machine_heigth
        # print(a,b,c)
        return (-b-(b**2-4*a*c)**(1/2))/(2*a)

    def find_perfect_v_bat(self,Sx):
        set = []
        error = Sx
        per_sx = 0
        for i in np.linspace(0,10,num=100000):
            if(i != 0):
                V_x = i
                degree = self.find_theta(V_x)
                v_ball = self.Vball(degree,V_x)
                v_bat = self.Vbat(v_ball,degree,V_x)
                sx = self.find_Sx(v_ball,degree)
                w = v_bat/self.R_racket
                rpm = w*(60/(2*math.pi))
                set.append([sx,degree,v_ball,v_bat,w,rpm])
                if Sx-sx < 0:
                    # print(set)
                    if abs(Sx - set[len(set)-1][0]) < abs(Sx -set[len(set)-2][0]):
                        return set[len(set)-1]
                    else:
                        return set[len(set)-2]


    def run(self):
        sx = self.pythagoras(self.parameters["X pos"], self.parameters["Y pos"])
        ans = self.find_perfect_v_bat(sx)
        self.Machine_angle = math.degrees(math.atan(self.parameters["Y pos"]/self.parameters["X pos"]))
        self.Machine_rpm= ans[5]
        self.duty_cycle = (self.Machine_rpm/self.Motor_rpm)*100
        self.Vin = (self.VCC*self.duty_cycle)/100
        return (self.Machine_angle, self.Machine_rpm, self.duty_cycle, self.Vin)

    # def run(self):

    #     ans = self.find_perfect_v_bat((self.pythagoras((self.parameters["X pos"]),(self.parameters["Y pos"]))))
    #     return ans
    
        

# print(Calculate({
#     "X pos": 1.0,
#     "Y pos": 1.0,
#     "Freefall": 1.0,
#     "Racket angle": 45,
#     "Length": 3.0,
#     "Width": 2.0
# }).run())



    # pos = [0.94,1.32,1.70,2.08,2.46]

    
    # for a in pos:
    #     data[a] = find_perfect_v_bat(Sx=a)
    #     #print(data[a])


    def projectile_motion(self):
        self.data= self.find_perfect_v_bat(self.pythagoras(self.parameters["X pos"], self.parameters["Y pos"]))
        U = self.data[2]
        theta = self.data[1]
        Sx = self.pythagoras(self.parameters["X pos"], self.parameters["Y pos"])
        theta_rad = np.radians(theta)  # Convert angle to radians   
        # Time of flight approximation
        t_flight = Sx/(U * np.cos(theta_rad))  # Extend time artificially   
        # Time intervals
        t = np.linspace(0, t_flight, num=100)   
        # Equations of motion
        x = U * np.cos(theta_rad) * t
        y = U * np.sin(theta_rad) * t - 0.5 * self.g * t**2
    
    #     print(f"Minimum y value: {min(y)}")  # Check if y goes negative   
    #     # Plotting
        # plt.figure(figsize=(8, 5))
        # plt.plot(x, y, label="Projectile Trajectory")
        # plt.plot([x[-1]], [y[-1]], 'ro', label="Target")
        # # plt.axvline(Sx, color='r', linestyle='--', label=f'Sx={Sx} m')
        # # plt.axhline(0, color='black', linewidth=1)
        # plt.xlabel('Horizontal Distance (m)')
        # plt.ylabel('Vertical Distance (m)')
        # plt.title('Projectile Motion')
        # plt.legend()
        # plt.grid()    
        # plt.show()
        fig, ax = plt.subplots(figsize=(5, 2.5), dpi=100)  # ขนาดกราฟ 600x450 px
        ax.plot(x, y, label="Projectile Trajectory")
        ax.plot([x[-1]], [y[-1]], 'ro', label="Target")
        ax.set_xlabel('Horizontal Distance (m)')
        ax.set_ylabel('Vertical Distance (m)')
        ax.set_title('Projectile Motion')
        ax.legend()
        ax.grid()

        buf = io.BytesIO()
        plt.savefig(buf, format='PNG', bbox_inches='tight')
        plt.close(fig)
        buf.seek(0)

        plot_surface2 = pygame.image.load(buf)
        return plot_surface2


    def topView(self):
        self.data= self.find_perfect_v_bat(self.pythagoras(self.parameters["X pos"], self.parameters["Y pos"]))
        U = self.data[2]
        theta = self.data[1]
        Sx = self.pythagoras(self.parameters["X pos"], self.parameters["Y pos"])
        theta_rad = np.radians(theta) 
        machine_angle_rad = np.radians(self.Machine_angle)  # Convert angle to radians
         # Convert angle to radians   
        # Time of flight approximation
        t_flight = Sx/(U * np.cos(theta_rad))  # Extend time artificially   
        # Time intervals
        t = np.linspace(0, t_flight, num=100)   
        # Equations of motion
        x = U * np.cos(theta_rad) * t
        z = (U * np.cos(theta_rad) * t )*np.sin(machine_angle_rad)

        # Plot in matplotlib
        fig, ax = plt.subplots(figsize=(6, 2.5), dpi=100)
        ax.plot(x, z, label="Top View Trajectory")
        ax.plot([x[-1]], [z[-1]], 'ro', label="Target")
        ax.set_xlabel('Y axis Distance (m)')
        ax.set_ylabel('Z axis Distance (m)')
        ax.set_title('Top View Trajectory')
        ax.legend()
        ax.grid()

    # Convert plot to Pygame surface
        buf = io.BytesIO()
        plt.tight_layout()
        fig.savefig(buf, format="png")
        buf.seek(0)
        plt.close(fig)

        img = pygame.image.load(buf)
        plot_surface1 = pygame.transform.smoothscale(img, (width, height))
        fig, ax = plt.subplots()

        return plot_surface1
        # plt.figure(figsize=(8, 5))
        # plt.plot(x, z, label="Top View Trajectory")
        # plt.plot([x[-1]], [z[-1]], 'ro', label="Target")
        # # plt.axvline(Sx, color='r', linestyle='--', label=f'Sx={Sx} m')
        # # plt.axhline(0, color='black', linewidth=1)
        # plt.xlabel('Y axis Distance (m)')
        # plt.ylabel('Z axis Distance (m)')
        # plt.title('Top View Trajectory')
        # plt.legend()
        # plt.grid()    
        # plt.show()
        

# plt.figure(figsize=(8, 6))
#         plt.plot(x, y, label="Top View Trajectory")
#         plt.plot([x[-1]], [y[-1]], 'ro', label="Target")
#         plt.xlabel("X Distance (m)")
#         plt.ylabel("Y Distance (m)")
#         plt.title("Projectile Motion (Top View)")
#         plt.axis("equal")
#         plt.grid()
#         plt.legend()
#         plt.show()
    # def projectile_motion(self):
    #     x_data = []
    #     y_data = []
    #     U = data[a][2]
    #     theta = data[a][1]
    #     Sx = a
    #     theta_rad = np.radians(theta)  # Convert angle to radians   
    #     # Time of flight approximation
    #     t_flight = Sx/(U * np.cos(theta_rad))  # Extend time artificially   
    #     # Time intervals
    #     t = np.linspace(0, t_flight, num=100)   
    #     # Equations of motion
    #     x = U * np.cos(theta_rad) * t
    #     y = self.machine_heigth + U * np.sin(theta_rad) * t - 0.5 * self.g * t**2
    #     x_data.append(x)
    #     y_data.append(y)

    
    #     print(f"Minimum y value: {min(y)}")  # Check if y goes negative   
    # # Plotting
    #     plt.figure(figsize=(8, 5))
    #     plt.plot(x_data[0], y_data[0], label=f'U={data[0.94][2]:.2f} m/s, θ={data[0.94][1]:.2f}°', color='r')
    #     plt.plot(x_data[1], y_data[1], label=f'U={data[1.32][2]:.2f} m/s, θ={data[1.32][1]:.2f}°', color='r')
    #     plt.plot(x_data[2], y_data[2], label=f'U={data[1.70][2]:.2f} m/s, θ={data[1.70][1]:.2f}°', color='r')
    #     plt.plot(x_data[3], y_data[3], label=f'U={data[2.08][2]:.2f} m/s, θ={data[2.08][1]:.2f}°', color='r')
    #     plt.plot(x_data[4], y_data[4], label=f'U={data[2.46][2]:.2f} m/s, θ={data[2.46][1]:.2f}°', color='r')
    #     # plt.axvline(Sx, color='r', linestyle='-', label=f'Sx={Sx} m')
    #     # plt.axhline(0, color='black', linewidth=1)
    #     plt.xlabel('Horizontal Distance (m)')
    #     plt.ylabel('Vertical Distance (m)')
    #     plt.title('Projectile Motion')
    #     plt.gca().xaxis.set_major_locator(plt.MultipleLocator(0.2))  # Set x grid width to 0.1 m
    #     plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.2))  # Set y grid width to 0.1 m
    #     plt.axis('equal')
    #     plt.legend()
    #     plt.grid()    
    #     plt.show()

        

# R = 0.225
# machine_height = 0.3911111
# M_bat = 0.49
# Inertia = 0.0080

# e = 1/0.401
# M_ball = 0.025

# u = 2.57
# machine_degree = 45

# starting_position_height = 1.5
#pygame.rect.Rect
Screens.default_screen(self=Screens())