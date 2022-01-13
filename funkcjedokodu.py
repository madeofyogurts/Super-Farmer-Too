import pygame
import pygame_gui
import inputimie as ii

class tryby_gry():
    def __init__(self):
        Etap_Poczatek = True
        Etap_Zasady = False
        self.Etap_Rozgrywka = False
        Etap_Gracze = False
        print("A")

    def etap_zasady_gry(self, RozpocznijGre, ZasadyGry, PowrotDoMenu):
        pygame_gui.elements.UIButton.hide(RozpocznijGre)
        pygame_gui.elements.UIButton.hide(ZasadyGry)
        pygame_gui.elements.UIButton.show(PowrotDoMenu)
        print("B")

    def etap_rozpoczecie_gry(self, RozpocznijGre, ZasadyGry, gameDisplay, Liczba_Graczy, Graczy_Dwoch, Graczy_Trzech, Graczy_Czterech, Graczy_Pieciu):
        self.Etap_Rozgrywka == True
        pygame_gui.elements.UIButton.hide(RozpocznijGre)
        pygame_gui.elements.UIButton.hide(ZasadyGry)
        gameDisplay.blit(Liczba_Graczy, (100, 100))
        pygame_gui.elements.UIButton.show(Graczy_Dwoch)
        pygame_gui.elements.UIButton.show(Graczy_Trzech)
        pygame_gui.elements.UIButton.show(Graczy_Czterech)
        pygame_gui.elements.UIButton.show(Graczy_Pieciu)

    def powrot_do_menu(self, RozpocznijGre, ZasadyGry, PowrotDoMenu):
        pygame_gui.elements.UIButton.show(RozpocznijGre)
        pygame_gui.elements.UIButton.show(ZasadyGry)
        pygame_gui.elements.UIButton.hide(PowrotDoMenu)

    def gracze_ustaleni(self, gameDisplay, background, Graczy_Dwoch, Graczy_Trzech, Graczy_Czterech, Graczy_Pieciu, Graczy_Liczba):
        print(Graczy_Liczba)
        imiona_graczy = []
        pygame_gui.elements.UIButton.hide(Graczy_Dwoch)
        pygame_gui.elements.UIButton.hide(Graczy_Trzech)
        pygame_gui.elements.UIButton.hide(Graczy_Czterech)
        pygame_gui.elements.UIButton.hide(Graczy_Pieciu)
        gameDisplay.blit(background, (0, 0))
        for i in range(Graczy_Liczba):
            print("Podaj imię postaci")
            gracz_i_imie = ii.wpisz_imie()
            imiona_graczy.append(gracz_i_imie)
        quit()

    def wyswietlane_teksty(self, gameDisplay, Liczba_Graczy):
        if self.Etap_Rozgrywka == True:
            gameDisplay.blit(Liczba_Graczy, (100, 100))
