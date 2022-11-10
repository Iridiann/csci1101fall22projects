import pygame

pygame.int()

#Game settings.
monitor_display = (800, 600)

game_display = pygame.display.setmode(monitor_display)

pygame.display.set_caption("Tank Domination")

system_clock = pygame.time.Clock()

game_characteristics = {
    "sky":{
        "color":(135, 206, 235)
    }
}

#Game logic.
game_running_flag = True

while game_running_flag:
    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            game_running_flag = False

        if not game_running_flag:
            pygame.quit()

            break

        #Running game mechanincs.
        game_display.fill(game_characteristics["sky"]["color"])

        pygame.display.update()

        system_clock.tick(30)