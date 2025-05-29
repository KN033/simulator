import pygame
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
                self.text += event.unicode
            self.txt_surface = self.font.render(self.text, True, self.color)



    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0, 25)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, 25)
        label_surface = self.font.render(self.label, True, (219, 48, 122))
        screen.blit(label_surface, (self.rect.x + 10, self.rect.y - 30))
        screen.blit(self.txt_surface, (self.rect.x + 10, self.rect.y + 10))

    def get_value(self):
        return self.text
