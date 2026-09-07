import sys
import pygame

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ventana Practica Pygame")
text_font = pygame.font.SysFont("Arial",45)

#Texto Nombre Centrado
text1 = text_font.render("Álvaro Cantillo Sánchez", True, (255,230,245))
text_rect = text1.get_rect(center=(size[0] // 2, size[1] // 2))
screen.blit(text1, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    


