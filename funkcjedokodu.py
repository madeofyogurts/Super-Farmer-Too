import pygame
import pygame_gui
import inputimie as ii
import mechanizmrozgrywki as mr
import licznikzwierzat as lz

class tryby_gry():
    def __init__(self):
        self.Etap_Poczatek = True
        self.Etap_Zasady = False
        self.Etap_Rozgrywka = False
        self.Etap_Gracze = False
        self.Etap_Runda = False
        print("A")

    def etap_zasady_gry(self, RozpocznijGre, ZasadyGry, PowrotDoMenu):
        self.Etap_Poczatek = False
        pygame_gui.elements.UIButton.hide(RozpocznijGre)
        pygame_gui.elements.UIButton.hide(ZasadyGry)
        pygame_gui.elements.UIButton.show(PowrotDoMenu)
        print("B")

    def etap_rozpoczecie_gry(self, RozpocznijGre, ZasadyGry, gameDisplay, Liczba_Graczy, Graczy_Dwoch, Graczy_Trzech, Graczy_Czterech, Graczy_Pieciu):
        self.Etap_Poczatek = False
        self.Etap_Rozgrywka = True
        pygame_gui.elements.UIButton.hide(RozpocznijGre)
        pygame_gui.elements.UIButton.hide(ZasadyGry)
        # gameDisplay.blit(Liczba_Graczy, (100, 100))
        pygame_gui.elements.UIButton.show(Graczy_Dwoch)
        pygame_gui.elements.UIButton.show(Graczy_Trzech)
        pygame_gui.elements.UIButton.show(Graczy_Czterech)
        pygame_gui.elements.UIButton.show(Graczy_Pieciu)

    def powrot_do_menu(self, RozpocznijGre, ZasadyGry, PowrotDoMenu):
        self.Etap_Poczatek = True
        pygame_gui.elements.UIButton.show(RozpocznijGre)
        pygame_gui.elements.UIButton.show(ZasadyGry)
        pygame_gui.elements.UIButton.hide(PowrotDoMenu)

    def gracze_ustaleni(self, gameDisplay, background, Graczy_Dwoch, Graczy_Trzech, Graczy_Czterech, Graczy_Pieciu, Graczy_Liczba, Rozpocznij_Gre, myfont):
        print(Graczy_Liczba)
        imiona_graczy = []
        pygame_gui.elements.UIButton.hide(Graczy_Dwoch)
        pygame_gui.elements.UIButton.hide(Graczy_Trzech)
        pygame_gui.elements.UIButton.hide(Graczy_Czterech)
        pygame_gui.elements.UIButton.hide(Graczy_Pieciu)
        gameDisplay.blit(background, (0, 0))
        pygame.display.update()
        for i in range(Graczy_Liczba):
            gracz_i_imie = ii.wpisz_imie(gameDisplay, background, myfont, i)
            imiona_graczy.append(gracz_i_imie)
        print(imiona_graczy)
        self.Etap_Rozgrywka = False
        # Printuje informacje o imionach Graczy
        pygame_gui.elements.UIButton.show(Rozpocznij_Gre)
        return imiona_graczy

    def rozpocznij_runde(self, Rozpocznij_Gre):
        self.Etap_Runda = True
        pygame_gui.elements.UIButton.hide(Rozpocznij_Gre)
        pygame.display.update()

    def wyswietlane_teksty(self, gameDisplay, Liczba_Graczy, Super_Farmer, TEXT_COLOR):
        if self.Etap_Rozgrywka == True:
            gameDisplay.blit(Liczba_Graczy, (50, 100))
        if self.Etap_Poczatek == True:
            gameDisplay.blit(Super_Farmer, (325, 200))
        if self.Etap_Runda == True:
            print("A")


    def rundy_gry(self, clock, manager, background, TEXT_COLOR, gracz1, gracz2, gracz3, gracz4, gracz5, gameDisplay, myfont, Wymiana, Koniec_Rundy, Kupno_Cenniejszych, Kupno_Psow, Kupno_Mniej_Cennych, KC_1, KC_2, KC_3, KC_4, KP_1, KP_2, KMC_1, KMC_2, KMC_3, KMC_4, i_g, Graczy_Liczba, Rzut_Koscia, Kolejny_Etap):
        while True:
            time_delta = clock.tick(60)/1000.0
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        exit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        print("A")
                manager.process_events(event)
            manager.update(time_delta)
            gameDisplay.blit(background, (0, 0))
            lz.interfejs(gameDisplay, TEXT_COLOR)
            gracz1.rzut_koscmi(gameDisplay, myfont, clock, manager, background, TEXT_COLOR, Rzut_Koscia, Kolejny_Etap, i_g[0])
            gracz1.akcjeporzucie(gameDisplay, TEXT_COLOR, myfont, manager, time_delta, clock, Wymiana, Koniec_Rundy, Kupno_Cenniejszych, Kupno_Psow, Kupno_Mniej_Cennych, KC_1, KC_2, KC_3, KC_4, KP_1, KP_2, KMC_1, KMC_2, KMC_3, KMC_4, i_g[0])
            gameDisplay.blit(background, (0, 0))
            lz.interfejs(gameDisplay, TEXT_COLOR)
            gracz2.rzut_koscmi(gameDisplay, myfont, clock, manager, background, TEXT_COLOR, Rzut_Koscia, Kolejny_Etap, i_g[1])
            gracz2.akcjeporzucie(gameDisplay, TEXT_COLOR, myfont, manager, time_delta, clock, Wymiana, Koniec_Rundy, Kupno_Cenniejszych, Kupno_Psow, Kupno_Mniej_Cennych, KC_1, KC_2, KC_3, KC_4, KP_1, KP_2, KMC_1, KMC_2, KMC_3, KMC_4, i_g[1])
            if Graczy_Liczba > 2:
                gameDisplay.blit(background, (0, 0))
                lz.interfejs(gameDisplay, TEXT_COLOR)
                gracz3.rzut_koscmi(gameDisplay, myfont, clock, manager, background, TEXT_COLOR, Rzut_Koscia, Kolejny_Etap, i_g[2])
                gracz3.akcjeporzucie(gameDisplay, TEXT_COLOR, myfont, manager, time_delta, clock, Wymiana, Koniec_Rundy, Kupno_Cenniejszych, Kupno_Psow, Kupno_Mniej_Cennych, KC_1, KC_2, KC_3, KC_4, KP_1, KP_2, KMC_1, KMC_2, KMC_3, KMC_4, i_g[2])
                if Graczy_Liczba > 3:
                    gameDisplay.blit(background, (0, 0))
                    lz.interfejs(gameDisplay, TEXT_COLOR)
                    gracz4.rzut_koscmi(gameDisplay, myfont, clock, manager, background, TEXT_COLOR, Rzut_Koscia, Kolejny_Etap, i_g[3])
                    gracz4.akcjeporzucie(gameDisplay, TEXT_COLOR, myfont, manager, time_delta, clock, Wymiana, Koniec_Rundy, Kupno_Cenniejszych, Kupno_Psow, Kupno_Mniej_Cennych, KC_1, KC_2, KC_3, KC_4, KP_1, KP_2, KMC_1, KMC_2, KMC_3, KMC_4, i_g[3])
                    if Graczy_Liczba > 4:
                        gameDisplay.blit(background, (0, 0))
                        lz.interfejs(gameDisplay, TEXT_COLOR)
                        gracz5.rzut_koscmi(gameDisplay, myfont, clock, manager, background, TEXT_COLOR, Rzut_Koscia, Kolejny_Etap, i_g[4])
                        gracz5.akcjeporzucie(gameDisplay, TEXT_COLOR, myfont, manager, time_delta, clock, Wymiana, Koniec_Rundy, Kupno_Cenniejszych, Kupno_Psow, Kupno_Mniej_Cennych, KC_1, KC_2, KC_3, KC_4, KP_1, KP_2, KMC_1, KMC_2, KMC_3, KMC_4, i_g[4])

            print("EEE")
            # Najpierw rzut kości jednej osoby
            # Potem czy chce coś z tymi zwierzetami zrobić
            # Spawdzenie, czy ta osoba wygrywa
            # Potem rzut kości kolejnej osoby
            # I czy ona chce coś zrobić
            # I czy ta osoba wygrywa
            manager.update(time_delta)

rabbit = pygame.image.load("pic-rabbit.png")
rabbit = pygame.transform.scale(rabbit, (35, 35))
sheep = pygame.image.load("pic-sheep.png")
sheep = pygame.transform.scale(sheep, (35, 35))
pig = pygame.image.load("pic-pig.png")
pig = pygame.transform.scale(pig, (35, 35))
cow = pygame.image.load("pic-cow.png")
cow = pygame.transform.scale(cow, (35, 35))
horse = pygame.image.load("pic-horse.png")
horse = pygame.transform.scale(horse, (35, 35))
small_dog = pygame.image.load("pic-small-dog.png")
small_dog = pygame.transform.scale(small_dog, (35, 35))
big_dog = pygame.image.load("pic-big-dog.png")
big_dog = pygame.transform.scale(big_dog, (35, 35))

