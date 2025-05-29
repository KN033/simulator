import math
import numpy as np
import matplotlib.pyplot as plt


class Calculate:
    def __init__(self,parameter):
        self.parameters=parameter
        self.g=9.81
        self.R_racket=0.225
        self.machine_heigth=0.3911111
        self.M_bat=0.49
        self.Inertia=0.008

        self.e=(1/0.401)
        self.M_ball=0.025

        self.u=2.57

    def pythagoras(self):
        return (math.sqrt(((self.parameters["X pos"])**2)+((self.parameters["Y pos"])**2)))
    
    def freefall(self,s):
        return (2*9.81*(s-(self.machine_heigth)))**(1/2)
    
    def find_theta(self,vx):
        term1 = (self.e*vx - self.freefall(self.parameters["Freefall"]))/self.e
        term2 = term1/vx
        return math.atan(term2)*180/math.pi

    def Vball(theta,vx):
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
                    
            
# print("POC 5.94 m",find_perfect_v_bat(5.94))

    pos = [0.94,1.32,1.70,2.08,2.46]

    data = {}
    for a in pos:
        data[a] = find_perfect_v_bat(a)
        #print(data[a])


    def projectile_motion(self,a,data):
        U = data[a][2]
        theta = data[a][1]
        Sx = a
        theta_rad = np.radians(theta)  # Convert angle to radians   
        # Time of flight approximation
        t_flight = Sx/(U * np.cos(theta_rad))  # Extend time artificially   
        # Time intervals
        t = np.linspace(0, t_flight, num=100)   
        # Equations of motion
        x = U * np.cos(theta_rad) * t
        y = U * np.sin(theta_rad) * t - 0.5 * self.g * t**2
    
        print(f"Minimum y value: {min(y)}")  # Check if y goes negative   
        # Plotting
        plt.figure(figsize=(8, 5))
        plt.plot(x, y, label=f'U={U} m/s, θ={theta}°')
        plt.axvline(Sx, color='r', linestyle='--', label=f'Sx={Sx} m')
        plt.axhline(0, color='black', linewidth=1)
        plt.xlabel('Horizontal Distance (m)')
        plt.ylabel('Vertical Distance (m)')
        plt.title('Projectile Motion')
        plt.legend()
        plt.grid()    
        plt.show()

# projectile_motion(0.94)

    def projectile_motion(self,pos,data):
        x_data = []
        y_data = []
        U_data = []
        for a in pos:
            U = data[a][2]
            theta = data[a][1]
            Sx = a
            theta_rad = np.radians(theta)  # Convert angle to radians   
        # Time of flight approximation
            t_flight = Sx/(U * np.cos(theta_rad))  # Extend time artificially   
        # Time intervals
            t = np.linspace(0, t_flight, num=100)   
        # Equations of motion
            x = U * np.cos(theta_rad) * t
            y = self.machine_heigth + U * np.sin(theta_rad) * t - 0.5 * self.g * t**2
            x_data.append(x)
            y_data.append(y)

    
        print(f"Minimum y value: {min(y)}")  # Check if y goes negative   
    # Plotting
        plt.figure(figsize=(8, 5))
        plt.plot(x_data[0], y_data[0], label=f'U={data[0.94][2]:.2f} m/s, θ={data[0.94][1]:.2f}°', color='r')
        plt.plot(x_data[1], y_data[1], label=f'U={data[1.32][2]:.2f} m/s, θ={data[1.32][1]:.2f}°', color='r')
        plt.plot(x_data[2], y_data[2], label=f'U={data[1.70][2]:.2f} m/s, θ={data[1.70][1]:.2f}°', color='r')
        plt.plot(x_data[3], y_data[3], label=f'U={data[2.08][2]:.2f} m/s, θ={data[2.08][1]:.2f}°', color='r')
        plt.plot(x_data[4], y_data[4], label=f'U={data[2.46][2]:.2f} m/s, θ={data[2.46][1]:.2f}°', color='r')
        # plt.axvline(Sx, color='r', linestyle='-', label=f'Sx={Sx} m')
        # plt.axhline(0, color='black', linewidth=1)
        plt.xlabel('Horizontal Distance (m)')
        plt.ylabel('Vertical Distance (m)')
        plt.title('Projectile Motion')
        plt.gca().xaxis.set_major_locator(plt.MultipleLocator(0.2))  # Set x grid width to 0.1 m
        plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.2))  # Set y grid width to 0.1 m
        plt.axis('equal')
        plt.legend()
        plt.grid()    
        plt.show()

        

# R = 0.225
# machine_height = 0.3911111
# M_bat = 0.49
# Inertia = 0.0080

# e = 1/0.401
# M_ball = 0.025

# u = 2.57
# machine_degree = 45

# starting_position_height = 1.5

