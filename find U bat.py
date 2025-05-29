import math
import numpy as np
import matplotlib.pyplot as plt

g = 9.81

R = 0.225
machine_height = 0.3911111
M_bat = 0.49
Inertia = 0.0080

e = 1/0.401
M_ball = 0.025

u = 2.57
machine_degree = 45

starting_position_height = 1.5

def freefall(s):
    return (2*9.81*(s-machine_height))**(1/2)

def find_theta(vx):
    term1 = (e*vx - freefall(starting_position_height))/e
    term2 = term1/vx
    return math.atan(term2)*180/math.pi

def Vball(theta,vx):
    return vx/math.cos(math.pi/180*theta)

def Vbat(v_ball,theta,vx):
    return (e*M_ball*v_ball*math.cos(math.pi/180*theta)+M_bat*vx)/M_bat

def find_Sx(v,theta):
    a = -(0.5*9.81)/((v*math.cos(math.pi/180*theta)))**2
    b = math.tan(math.pi/180*theta)
    c = machine_height
    # print(a,b,c)
    return (-b-(b**2-4*a*c)**(1/2))/(2*a)

def find_perfect_v_bat(Sx):
    set = []
    error = Sx
    per_sx = 0
    for i in np.linspace(0,10,num=100000):
        if(i != 0):
            V_x = i
            degree = find_theta(V_x)
            v_ball = Vball(degree,V_x)
            v_bat = Vbat(v_ball,degree,V_x)
            sx = find_Sx(v_ball,degree)
            w = v_bat/R
            rpm = w*(60/(2*math.pi))
            set.append([sx,degree,v_ball,v_bat,w,rpm])
            if Sx-sx < 0:
                # print(set)
                if abs(Sx - set[len(set)-1][0]) < abs(Sx -set[len(set)-2][0]):
                    return set[len(set)-1]
                else:
                    return set[len(set)-2]
            
pos_1m = find_perfect_v_bat(1)


pos = [0.94,1.32,1.70,2.08,2.46]

data = {}
for a in pos:
    data[a] = find_perfect_v_bat(a)
    print(data[a])


def projectile_motion(a):
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
    y = U * np.sin(theta_rad) * t - 0.5 * g * t**2
    
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

def projectile_motion(pos):
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
        y = machine_height + U * np.sin(theta_rad) * t - 0.5 * g * t**2
        x_data.append(x)
        y_data.append(y)

    
    # print(f"Minimum y value: {min(y)}")  # Check if y goes negative   
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

def torque(a):
    t = ((starting_position_height*2)/9.81)**(1/2)
    w = data[a][4]
    alpha = data[a][4]/t
    a = alpha*R
    F = M_ball*a
    tq = Inertia*alpha + F*R
    print(w,t,a,alpha,F)
    return tq
print("torque :",torque(2.46))
print("Free fall :",freefall(1.5))
projectile_motion(pos)