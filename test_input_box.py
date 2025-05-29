import pygame

pygame.init()

# กำหนดขนาดหน้าจอ
screen = pygame.display.set_mode((600, 200))
pygame.display.set_caption("Input Box Example")

# สี
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
COLOR_TEXT = pygame.Color('black')
FONT = pygame.font.Font(None, 32)

clock = pygame.time.Clock()

# สร้าง Input Box class
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, COLOR_TEXT)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # ถ้าคลิกในกล่อง, ให้ toggle การ active
            if self.rect.collidepoint(event.pos):
                #self.active = not self.active
                self.active = True
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)  # พิมพ์ข้อความที่กรอก
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, COLOR_TEXT)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

# สร้างอินพุตบ็อกซ์
input_box = InputBox(100, 80, 140, 32)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        input_box.handle_event(event)

    input_box.update()

    screen.fill((255, 255, 255))
    input_box.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
