import numpy as np
import matplotlib.pyplot as plt
import io
import pygame

class YourClass:
    def __init__(self):
        self.parameters = {"X pos": 30, "Y pos": 20}
        self.g = 9.81  # ความเร่งโน้มถ่วง

    # สมมติฟังก์ชันนี้หา velocity และมุม
    def find_perfect_v_bat(self, distance):
        # ตัวอย่างสมมติคืน (X pos, theta, U)
        # สมมติมุม 45 องศา ความเร็ว 20 m/s
        return (self.parameters["X pos"], 45, 20)

    def pythagoras(self, x, y):
        return np.sqrt(x**2 + y**2)

    # ฟังก์ชันสร้าง surface ของกราฟ projectile motion
    def create_projectile_plot_surface(self):
        # คำนวณข้อมูล projectile motion
        data = self.find_perfect_v_bat(self.pythagoras(self.parameters["X pos"], self.parameters["Y pos"]))
        U = data[2]
        theta = data[1]
        Sx = self.pythagoras(self.parameters["X pos"], self.parameters["Y pos"])
        theta_rad = np.radians(theta)

        t_flight = Sx / (U * np.cos(theta_rad))  # เวลาบินโดยประมาณ
        t = np.linspace(0, t_flight, num=100)

        x = U * np.cos(theta_rad) * t
        y = U * np.sin(theta_rad) * t - 0.5 * self.g * t**2

        # วาดกราฟด้วย matplotlib
        fig, ax = plt.subplots(figsize=(4, 3), dpi=100)  # ขนาดกราฟ 400x300 px
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

        plot_surface = pygame.image.load(buf)
        return plot_surface

# ตัวอย่างวิธีใช้ใน pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Projectile Motion Plot in Pygame")

    obj = YourClass()
    plot_surface = obj.create_projectile_plot_surface()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        screen.blit(plot_surface, (800 - plot_surface.get_width() - 10, 10))  # มุมบนขวา
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
