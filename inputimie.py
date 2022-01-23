import pygame
import pygame_gui

def wpisz_imie(gameDisplay, background, myfont, i):
    imie = []
    wybor_imienia = True
    while wybor_imienia == True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    imie.append("1")
                elif event.key == pygame.K_2:
                    imie.append("2")
                elif event.key == pygame.K_3:
                    imie.append("3")
                elif event.key == pygame.K_4:
                    imie.append("4")
                elif event.key == pygame.K_5:
                    imie.append("5")
                elif event.key == pygame.K_6:
                    imie.append("6")
                elif event.key == pygame.K_7:
                    imie.append("7")
                elif event.key == pygame.K_8:
                    imie.append("8")
                elif event.key == pygame.K_9:
                    imie.append("9")
                elif event.key == pygame.K_0:
                    imie.append("0")
                elif event.key == pygame.K_q:
                    imie.append("q")
                elif event.key == pygame.K_w:
                    imie.append("w")
                elif event.key == pygame.K_e:
                    imie.append("e")
                elif event.key == pygame.K_r:
                    imie.append("r")
                elif event.key == pygame.K_t:
                    imie.append("t")
                elif event.key == pygame.K_y:
                    imie.append("y")
                elif event.key == pygame.K_u:
                    imie.append("u")
                elif event.key == pygame.K_i:
                    imie.append("i")
                elif event.key == pygame.K_o:
                    imie.append("o")
                elif event.key == pygame.K_p:
                    imie.append("p")
                elif event.key == pygame.K_a:
                    imie.append("a")
                elif event.key == pygame.K_s:
                    imie.append("s")
                elif event.key == pygame.K_d:
                    imie.append("d")
                elif event.key == pygame.K_f:
                    imie.append("f")
                elif event.key == pygame.K_g:
                    imie.append("g")
                elif event.key == pygame.K_h:
                    imie.append("h")
                elif event.key == pygame.K_j:
                    imie.append("j")
                elif event.key == pygame.K_k:
                    imie.append("k")
                elif event.key == pygame.K_l:
                    imie.append("l")
                elif event.key == pygame.K_z:
                    imie.append("z")
                elif event.key == pygame.K_x:
                    imie.append("x")
                elif event.key == pygame.K_c:
                    imie.append("c")
                elif event.key == pygame.K_v:
                    imie.append("v")
                elif event.key == pygame.K_b:
                    imie.append("b")
                elif event.key == pygame.K_n:
                    imie.append("n")
                elif event.key == pygame.K_m:
                    imie.append("m")
                    print(imie)
                elif event.key == pygame.K_BACKSPACE: # Ten przycisk nie działa
                    imie.remove(imie[-1])
                    print(imie)
                elif event.key == pygame.K_RETURN: # Ten przycisk też nie działa
                    print(imie)
                    imie = [''.join(imie)]
                    print(imie)
                    wybor_imienia = False
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit((myfont.render(("Wpisz imię gracza numer " + str(i+1)), 1, (0,0,0))), (200, 200))
        gameDisplay.blit((myfont.render((str(imie)), 1, (0,0,0))), (200, 300))
        pygame.display.update()
    return imie
