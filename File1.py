#Робимо прості змінні
import pygame
pygame.init()
mw = pygame.display.set_mode((500, 500))
back = (200, 255, 255)
mw.fill(back)
move_right = False
move_left = False
game_over = False



#Тут тиримо класси з Арканоїда
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

#Створюємо Котика
Pop_cat = Picture("D:\Картинки для Пайтона\Pop_cat.png", 250, 75, 75, 75  )
Pop_cat = pygame.transform.scale(Pop_cat, (75, 70))
#Створюємо перших рибок
Fish1 = Picture("D:\Картинки для Пайтона\Fish1.png", 100, 350, 25, 25 )
Fish1 = pygame.transform.scale(Fish1, (75, 70))
Fish2 = Picture("D:\Картинки для Пайтона\Fish1.png", 100, 350, 25, 25 )
Fish2 = pygame.transform.scale(Fish1, (75, 70))
#Створюємо Других рибок
Fish3 = Picture("D:\Картинки для Пайтона\Fish1.png", 100, 350, 25, 25 )
Fish3 = pygame.transform.scale(Fish1, (75, 70))
Fish4 = Picture("D:\Картинки для Пайтона\Fish1.png", 100, 350, 25, 25 )
Fish4 = pygame.transform.scale(Fish1, (75, 70))
#Створюємо Огірочок
Cucumber = Picture("D:\Картинки для Пайтона\Cucumber.png", 300, 350, 25, 25)
Cucumber = pygame.transform.scale(Cucumber, (75, 70))
#Далі йде ігровий





















