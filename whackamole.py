import pygame
import random


def main():
    # #adding cod eto show functionality of git add, commit, and push
    # print('hi')
    #
    #
    # #code for git pull demo
    # print("this is for the git pull demo")
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        screen.fill("light green")
        # nest for loop 32 times for 32 lines
        # 640/32 = 20
        # 512/32 = 16
        for i in range(20):  # values 0 - 15 so 16 times  #horizontal lines
            pygame.draw.line(screen, (74, 4, 92), (0, 32 * i), (640, 32 * i))
            for j in range(16):  # vertical lines
                pygame.draw.line(screen, (74, 4, 92), (32 * i, 0), (32 * i, 512))
        screen.blit(mole_image, mole_image.get_rect(topleft=(3, 4)))
        while running:
            # screen.blit(mole_image, mole_image.get_rect(topleft=(3, 4)))

            #moved below to show up
            for event in pygame.event.get():
                #if you hit the x button to close the window it closes/stops running
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # event.pos = pygame.mouse.get_pos()
                    # x,y = pygame.mouse.get_pos()
                    x = (random.randrange(0, 20))*32 + 3
                    y = (random.randrange(0, 16))*32 + 4
                    # mole_image = (x,y)
                    screen.fill("light green")
                    for i in range(20):  # values 0 - 15 so 16 times  #horizontal lines
                        pygame.draw.line(screen, (74, 4, 92), (0, 32 * i), (640, 32 * i))
                        for j in range(16):  # vertical lines
                            pygame.draw.line(screen, (74, 4, 92), (32 * i, 0), (32 * i, 512))
                    screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))


                                             #moving the mole around when clicked:
            # for event in pygame.event.get():
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     # event.pos = pygame.mouse.get_pos()
                #     # x,y = pygame.mouse.get_pos()
                #     x = (random.randint(0, 20))*32
                #     y = (random.randint(0, 16))*32
                #     # mole_image = (x,y)
                #     screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
