import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("NumPy Graph in Box")

# กำหนดกรอบกราฟ
graph_rect = pygame.Rect(100, 100, 600, 300)

# สร้างข้อมูล NumPy
x_data = np.linspace(0, 4 * np.pi, graph_rect.width)
y_data = np.sin(x_data)

# สเกลข้อมูล y ให้อยู่ในกรอบ
y_min, y_max = y_data.min(), y_data.max()
y_scaled = (y_data - y_min) / (y_max - y_min) * graph_rect.height
y_scaled = graph_rect.height - y_scaled  # y pygame นับจากบนลงล่าง

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    # วาดกรอบกราฟ
    pygame.draw.rect(screen, (0, 255, 0), graph_rect, 2)

    # วาดกราฟลงตรงในกรอบ โดย offset ตำแหน่ง
    for i in range(len(x_data) - 1):
        x1 = graph_rect.left + i
        y1 = graph_rect.top + int(y_scaled[i])
        x2 = graph_rect.left + i + 1
        y2 = graph_rect.top + int(y_scaled[i + 1])
        pygame.draw.line(screen, (255, 0, 0), (x1, y1), (x2, y2), 2)

    pygame.display.flip()

pygame.quit()
