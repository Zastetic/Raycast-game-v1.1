import pygame

pygame.init()
ds = pygame.display.set_mode((700, 500))
run = True
clock = pygame.time.Clock()

color_list_saved = []
final_color_list_saved = []

skip_render = False

while run:
    skip_render = False
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            run = False

    with open("outp.txt", "r") as arquivo:
        color_list = arquivo.readlines()

        if color_list == color_list_saved:
            skip_render = True
        color_list_saved = color_list[:]

    # print(char)
    index = 0
    final_color_list = []
    r = ""

    if not skip_render:
        try:
            for char in color_list[0]:
                if char == "/":
                    final_color_list.append('.')
                    final_color_list[index] = int(r)
                    r = ""
                    index += 1
                else:
                    r += char
        except:
            final_color_list = final_color_list_saved
        final_color_list_saved = final_color_list
    
    final_color_list = final_color_list_saved

    colors = []
    y = [0, 3]

    for c in range(0, 27):
        try:
            colors.append(int(char[0][y[0]:y[1]]))
            y[0] += 3
            y[1] += 3

        except:
            pass

    inicial_y = 350
    inicial_x = 1
    div = 6

    pygame.draw.rect(ds, (255, 255, 255), (0, 0, ds.get_width(), ds.get_height()), 3)

    for color in range(0, len(final_color_list)):
        pygame.draw.rect(ds, 
                    (final_color_list[color], final_color_list[color], final_color_list[color]), 

                    (inicial_x+color*8, 
                     inicial_y-(final_color_list[color]/div), 
                     8, 
                     40+(final_color_list[color]/(div-3))))
        
    
    pygame.display.update()
    ds.fill((0, 0, 0))
