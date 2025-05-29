import pygame
import matplotlib.pyplot as plt
import io

# ฟังก์ชันสร้างกราฟเป็น pygame.Surface
def create_plot_surface(data_x, data_y, size=(300, 200)):
    fig, ax = plt.subplots(figsize=(size[0]/100, size[1]/100), dpi=100)
    ax.plot(data_x, data_y)
    ax.set_title("กราฟตัวอย่าง")
    ax.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='PNG', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)

    img = pygame.image.load(buf)
    return img

def main():
    pygame.init()
    window_width, window_height = 800, 600
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Pygame + Matplotlib Plot Example")

    # ตัวอย่างข้อมูลกราฟ
    data_x = [0, 1, 2, 3, 4, 5]
    data_y = [0, 1, 4, 9, 16, 25]

    # สร้าง surface ของกราฟ
    plot_surface = create_plot_surface(data_x, data_y, size=(300, 200))

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # เคลียร์หน้าจอด้วยสีขาว

        # วางกราฟที่มุมบนขวา เว้นระยะ 10px จากขอบ
        plot_pos = (window_width - plot_surface.get_width() - 10, 10)
        screen.blit(plot_surface, plot_pos)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
