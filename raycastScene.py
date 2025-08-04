import pygame
import functions

pygame.init()
ds = pygame.display.set_mode((520, 400))

map_input = "#############E" \
            "#@@@@@@@@@@@#E" \
            "#@@@##@##@@@#E" \
            "#@@@@@@@@@@@#E" \
            "#@@@@@@@@@@@#E"

image = pygame.image.load(r'3D_RAYCAST_PROJECT\02\seta.png')
image = pygame.transform.smoothscale(image, (30, 30))

clock = pygame.time.Clock()

player = functions.Player(60, 60, 30, image, ds)
blocks = functions.map(pygame, ds, map_input, tam=40)


def main():
    run = True

    while run:
        clock.tick(60)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                run = False

        #  Desenha os blocos
        for block in blocks:
            pygame.draw.rect(ds, (255, 255, 255), block)
            pygame.draw.rect(ds, (0, 0, 0), block, 1)

        player.draw()
        player.move_with_keys(blocks)
        res = player.ray(blocks)

        with open("outp.txt", "w") as arquivo:
            arquivo.truncate(0)
            arquivo.seek(0)

            for num in res:
                arquivo.write(f'{str(int(num))}')

        pygame.display.update()
        ds.fill((50, 100, 10))

    pygame.quit()


if __name__ == '__main__':
    main()
