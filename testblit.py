import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Load and Resize Image")

# โหลดภาพ
image = pygame.image.load("C:/FRA162-163/simulator/Hint.png")  # เปลี่ยนเป็นชื่อไฟล์ของคุณ

# ปรับขนาด
resized_image = pygame.transform.scale(image, (1000, 700))  # กว้าง 200 สูง 150

# ตำแหน่งวาง (center)
rect = resized_image.get_rect(center=(500, 350))

# ลูปหลัก
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    screen.blit(resized_image, rect.topleft)
    pygame.display.flip()

pygame.quit()
