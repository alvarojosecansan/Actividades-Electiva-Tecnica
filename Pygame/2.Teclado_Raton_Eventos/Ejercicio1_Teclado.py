import pygame

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ejercicio 1: Detección de Teclas con Shift y Mayús")
reloj = pygame.time.Clock()

ejecutando = True
while ejecutando:
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      ejecutando = False

    elif evento.type == pygame.KEYUP:
      key = pygame.key.name(evento.key)

      shift_sostenido = evento.mod & pygame.KMOD_SHIFT

      if shift_sostenido:
        print(f"Tecla {key.upper()} (con SHIFT sostenido)")
      else:
        print(f"Tecla {key} fue presionada")

  pantalla.fill((240, 240, 240))
  pygame.display.flip()
  reloj.tick(60)

pygame.quit()