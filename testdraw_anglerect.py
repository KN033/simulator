import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rotated Rectangle")

# สร้าง Surface ที่เป็นสี่เหลี่ยม
rect_size = (100, 50)
rect_surface = pygame.Surface(rect_size, pygame.SRCALPHA)  # ใช้ SRCALPHA เพื่อรองรับความโปร่งใส
rect_color = (255, 0, 0)

# วาดสี่เหลี่ยมลงบน surface
pygame.draw.rect(rect_surface, rect_color, (0, 0, *rect_size))

angle = 0
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    angle += 1  # เพิ่มองศา
    screen.fill((255, 255, 255))

    # หมุนสี่เหลี่ยม
    rotated = pygame.transform.rotate(rect_surface, angle)
    rotated_rect = rotated.get_rect(center=(400, 300))  # วางให้อยู่กึ่งกลาง

    # วาดลงจอ
    screen.blit(rotated, rotated_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
