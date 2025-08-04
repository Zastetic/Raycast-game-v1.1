import pygame

pygame.init()
ds = pygame.display.set_mode((700, 500))
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            run = False

    with open("outp.txt", "r") as arquivo:
        char = arquivo.readlines()

    # print(char)

    # print(char)
    colors = []
    y = [0, 3]
    for c in range(0, 27):
        try:
            colors.append(int(char[0][y[0]:y[1]]))
            y[0] += 3
            y[1] += 3

        except:
            pass

    # print(colors)
    x = 200

    for color in colors:
        color_2 = (color*255)/200
        pygame.draw.rect(ds, (color_2, 0, 0), (200+x, 300, 1, 100))
        x += 1

    print(colors)

    pygame.display.update()
    ds.fill((0, 0, 0))
