import pygame

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ejercicio 2: Pizarra de Dibujo Simple")
reloj = pygame.time.Clock()

blanco = (255, 255, 255)
negro = (0, 0, 0)

pantalla.fill(blanco)

dibujando = False
punto_anterior = None

ejecutando = True
while ejecutando:
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      ejecutando = False

    # Activa el dibujo y guarda el punto inicial al presionar el clic izquierdo
    elif evento.type == pygame.MOUSEBUTTONDOWN:
      if evento.button == 1:
        dibujando = True
        punto_anterior = evento.pos

    # Detiene el dibujo y reinicia la posición al soltar el clic
    elif evento.type == pygame.MOUSEBUTTONUP:
      if evento.button == 1:
        dibujando = False
        punto_anterior = None

    # Dibuja la línea continua y actualiza el punto previo al mover el ratón
    elif evento.type == pygame.MOUSEMOTION:
      if dibujando and punto_anterior is not None:
        punto_actual = evento.pos
        pygame.draw.line(pantalla, negro, punto_anterior, punto_actual, 4)
        punto_anterior = punto_actual

  pygame.display.flip()
  reloj.tick(60)

pygame.quit()