import pygame
import pygame_gui
import inputimie as ii
import mechanizmrozgrywki as mr

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

    def gracze_ustaleni(self, gameDisplay, background, Graczy_Dwoch, Graczy_Trzech, Graczy_Czterech, Graczy_Pieciu, Graczy_Liczba, Rozpocznij_Gre):
        print(Graczy_Liczba)
        imiona_graczy = []
        pygame_gui.elements.UIButton.hide(Graczy_Dwoch)
        pygame_gui.elements.UIButton.hide(Graczy_Trzech)
        pygame_gui.elements.UIButton.hide(Graczy_Czterech)
        pygame_gui.elements.UIButton.hide(Graczy_Pieciu)
        gameDisplay.blit(background, (0, 0))
        pygame.display.update()
        for i in range(Graczy_Liczba):
            print("Podaj imię postaci")
            gracz_i_imie = ii.wpisz_imie()
            imiona_graczy.append(gracz_i_imie)
        print(imiona_graczy)
        self.Etap_Rozgrywka = False
        # Printuje informacje o imionach Graczy
        pygame_gui.elements.UIButton.show(Rozpocznij_Gre)
        return imiona_graczy

    def rozpocznij_runde(self, Rozpocznij_Gre):
        self.Etap_Runda = True
        pygame_gui.elements.UIButton.hide(Rozpocznij_Gre)

    def wyswietlane_teksty(self, gameDisplay, Liczba_Graczy, Super_Farmer, TEXT_COLOR):
        if self.Etap_Rozgrywka == True:
            gameDisplay.blit(Liczba_Graczy, (50, 100))
        if self.Etap_Poczatek == True:
            gameDisplay.blit(Super_Farmer, (325, 200))
        if self.Etap_Runda == True:
            pygame.draw.rect(gameDisplay, TEXT_COLOR, (20, 45, 150, 350))
            pygame.draw.rect(gameDisplay, TEXT_COLOR, (20, 430, 760, 150))
            gameDisplay.blit(rabbit, (30, 50))
            gameDisplay.blit(sheep, (30, 100))
            gameDisplay.blit(pig, (30, 150))
            gameDisplay.blit(cow, (30, 200))
            gameDisplay.blit(horse, (30, 250))
            gameDisplay.blit(small_dog, (30, 300))
            gameDisplay.blit(big_dog, (30, 350))

    def rundy_gry(self, gracz1, gracz2, gracz3, gracz4, gracz5):
        gracz1.rzut_koscmi()
        # Najpierw rzut kości jednej osoby
        # Potem czy chce coś z tymi zwierzetami zrobić
        # Spawdzenie, czy ta osoba wygrywa
        # Potem rzut kości kolejnej osoby
        # I czy ona chce coś zrobić
        # I czy ta osoba wygrywa
        print("A")

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

