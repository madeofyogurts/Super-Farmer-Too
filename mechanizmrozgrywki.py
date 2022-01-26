import time
import math
import random
import pygame
import pygame_gui
import inputimie as ii
import funkcjedokodu as fdk
import licznikzwierzat as lz

class mechanizm_rogzrywki():
    def __init__(self, gameDisplay):
        print("Gracz")
        self.zwierzetagracza = []

    def rzut_koscmi(self, gameDisplay, myfont, clock, manager, background, TEXT_COLOR, Rzut_Koscia, Kolejny_Etap, i_g):
        KoscJeden = ["Królik", "Owca", "Królik", "Owca", "Królik", "Świnia", "Królik", "Świnia", "Królik", "Koń", "Królik", "Lis"]
        KoscDwa = ["Królik", "Owca", "Królik", "Owca", "Królik", "Owca", "Królik", "Świnia", "Królik", "Krowa", "Królik", "Wilk"]
        WynikJeden = random.choice(KoscJeden)
        WynikDwa = random.choice(KoscDwa)

        print("\nRzut kośćmi gracza :", WynikJeden, "i", WynikDwa)

        #Proces dodawania zwierzątek z inwentarza
        #Najpierw zwierzątka są podliczane do inwentarza gracza
        self.zwierzetagracza.append(WynikJeden)
        self.zwierzetagracza.append(WynikDwa)
        # print(self.zwierzetagracza)
        #Teraz podliczamy pełną ilosć zwierzątek
        przedzwierzatkakroliki = self.zwierzetagracza.count("Królik")
        przedzwierzatkaowce = self.zwierzetagracza.count("Owca")
        przedzwierzatkaswinie = self.zwierzetagracza.count("Świnia")
        przedzwierzatkakrowy = self.zwierzetagracza.count("Krowa")
        przedzwierzatkakonie = self.zwierzetagracza.count("Koń")
        # przedzwierzatkamalepsy = self.zwierzetagracza.count("Mały Pies")
        # przedzwierzatkaduzepsy = self.zwierzetagracza.count("Duży Pies")


        if WynikJeden == WynikDwa:
            if WynikJeden == "Królik":
                przezdwa = przedzwierzatkakroliki / 2
                # print(przezdwa)
                dopodlogi = math.floor(przezdwa)
                # print(dopodlogi)
                for i in range(dopodlogi):
                    self.zwierzetagracza.append(WynikJeden)
                    # print(self.zwierzetagracza)
                if dopodlogi > 0:
                    print("Brawo! Zyskujesz króliki, ilość:", dopodlogi)
            elif WynikJeden == "Owca":
                przezdwa = przedzwierzatkaowce / 2
                # print(przezdwa)
                dopodlogi = math.floor(przezdwa)
                # print(dopodlogi)
                for i in range(dopodlogi):
                    self.zwierzetagracza.append(WynikJeden)
                    # print(self.zwierzetagracza)
                if dopodlogi > 0:
                    print("Brawo! Zyskujesz owce, ilość:", dopodlogi)
            elif WynikJeden == "Świnia":
                przezdwa = przedzwierzatkaswinie / 2
                # print(przezdwa)
                dopodlogi = math.floor(przezdwa)
                # print(dopodlogi)
                for i in range(dopodlogi):
                    self.zwierzetagracza.append(WynikJeden)
                    # print(self.zwierzetagracza)
                if dopodlogi > 0:
                    print("Brawo! Zyskujesz świnie, ilość:", dopodlogi)
            elif WynikJeden == "Krowa":
                przezdwa = przedzwierzatkakrowy / 2
                # print(przezdwa)
                dopodlogi = math.floor(przezdwa)
                # print(dopodlogi)
                for i in range(dopodlogi):
                    self.zwierzetagracza.append(WynikJeden)
                    # print(self.zwierzetagracza)
                if dopodlogi > 0:
                    print("Brawo! Zyskujesz krowy, ilość:", dopodlogi)
            elif WynikJeden == "Koń":
                przezdwa = przedzwierzatkakonie / 2
                # print(przezdwa)
                dopodlogi = math.floor(przezdwa)
                # print(dopodlogi)
                for i in range(dopodlogi):
                    self.zwierzetagracza.append(WynikJeden)
                    # print(self.zwierzetagracza)
                if dopodlogi > 0:
                    print("Brawo! Zyskujesz konie, ilość:", dopodlogi)
            else:
                print(" ")
        #Koniec kości pierwszej

        elif WynikJeden != WynikDwa:
            if WynikJeden == "Królik":
                przezdwajeden = przedzwierzatkakroliki / 2
                # print(przezdwajeden)
                dopodlogijeden = math.floor(przezdwajeden)
                # print(dopodlogijeden)
                for i in range(dopodlogijeden):
                    self.zwierzetagracza.append(WynikJeden)
                    # print(self.zwierzetagracza)
                if dopodlogijeden > 0:
                    print("Brawo! Zyskujesz króliki, ilość:", dopodlogijeden)
            elif WynikJeden == "Owca":
                przezdwajeden = przedzwierzatkaowce / 2
                # print(przezdwajeden)
                dopodlogijeden = math.floor(przezdwajeden)
                # print(dopodlogijeden)
                for i in range(dopodlogijeden):
                    self.zwierzetagracza.append(WynikJeden)
                    # print(self.zwierzetagracza)
                if dopodlogijeden > 0:
                    print("Brawo! Zyskujesz owce, ilość:", dopodlogijeden)
            elif WynikJeden == "Świnia":
                przezdwajeden = przedzwierzatkaswinie / 2
                # print(przezdwajeden)
                dopodlogijeden = math.floor(przezdwajeden)
                # print(dopodlogijeden)
                for i in range(dopodlogijeden):
                    self.zwierzetagracza.append(WynikJeden)
                    # print(self.zwierzetagracza)
                if dopodlogijeden > 0:
                    print("Brawo! Zyskujesz świnie, ilość:", dopodlogijeden)
            elif WynikJeden == "Krowa":
                przezdwajeden = przedzwierzatkakrowy / 2
                # print(przezdwajeden)
                dopodlogijeden = math.floor(przezdwajeden)
                # print(dopodlogijeden)
                for i in range(dopodlogijeden):
                    self.zwierzetagracza.append(WynikJeden)
                    # print(self.zwierzetagracza)
                if dopodlogijeden > 0:
                    print("Brawo! Zyskujesz krowy, ilość:", dopodlogijeden)
            elif WynikJeden == "Koń":
                przezdwajeden = przedzwierzatkakonie / 2
                # print(przezdwajeden)
                dopodlogijeden = math.floor(przezdwajeden)
                # print(dopodlogijeden)
                for i in range(dopodlogijeden):
                    self.zwierzetagracza.append(WynikJeden)
                    # print(self.zwierzetagracza)
                if dopodlogijeden > 0:
                    print("Brawo! Zyskujesz konie, ilość:", dopodlogijeden)
            else:
                print(" ")

            if WynikDwa == "Królik":
                przezdwadwa = przedzwierzatkakroliki / 2
                # print(przezdwadwa)
                dopodlogidwa = math.floor(przezdwadwa)
                # print(dopodlogidwa)
                for i in range(dopodlogidwa):
                    self.zwierzetagracza.append(WynikDwa)
                    # print(self.zwierzetagracza)
                if dopodlogidwa > 0:
                    print("Brawo! Zyskujesz króliki, ilość:", dopodlogidwa)
            elif WynikDwa == "Owca":
                przezdwadwa = przedzwierzatkaowce / 2
                # print(przezdwadwa)
                dopodlogidwa = math.floor(przezdwadwa)
                # print(dopodlogidwa)
                for i in range(dopodlogidwa):
                    self.zwierzetagracza.append(WynikDwa)
                    # print(self.zwierzetagracza)
                if dopodlogidwa > 0:
                    print("Brawo! Zyskujesz owce, ilość:", dopodlogidwa)
            elif WynikDwa == "Świnia":
                przezdwadwa = przedzwierzatkaswinie / 2
                # print(przezdwadwa)
                dopodlogidwa = math.floor(przezdwadwa)
                # print(dopodlogidwa)
                for i in range(dopodlogidwa):
                    self.zwierzetagracza.append(WynikDwa)
                    # print(self.zwierzetagracza)
                if dopodlogidwa > 0:
                    print("Brawo! Zyskujesz świnie, ilość:", dopodlogidwa)
            elif WynikDwa == "Krowa":
                przezdwadwa = przedzwierzatkakrowy / 2
                # print(przezdwadwa)
                dopodlogidwa = math.floor(przezdwadwa)
                # print(dopodlogidwa)
                for i in range(dopodlogidwa):
                    self.zwierzetagracza.append(WynikDwa)
                    # print(self.zwierzetagracza)
                if dopodlogidwa > 0:
                    print("Brawo! Zyskujesz krowy, ilość:", dopodlogidwa)
            elif WynikDwa == "Koń":
                przezdwadwa = przedzwierzatkakonie / 2
                # print(przezdwadwa)
                dopodlogidwa = math.floor(przezdwadwa)
                # print(dopodlogidwa)
                for i in range(dopodlogidwa):
                    self.zwierzetagracza.append(WynikDwa)

                    # print(self.zwierzetagracza)
                if dopodlogidwa > 0:
                    print("Brawo! Zyskujesz konie, ilość:", dopodlogidwa)
            else:
                print(" ")

    #Teraz wyniki z kości są usuwane z inwentarza gracza
        self.zwierzetagracza.remove(WynikJeden)
        self.zwierzetagracza.remove(WynikDwa)
        # print(self.zwierzetagracza)
        #Koniec procesu dodawania zwierzątek z inwentarza!


        if WynikJeden == "Lis": #Zabiera króliki
            if "Mały Pies" not in self.zwierzetagracza:
                print("O nie! Tracisz wszystkie króliki!")
                while "Królik" in self.zwierzetagracza:
                    self.zwierzetagracza.remove("Królik")
                # print("Zwierzęta gracza", self.imie + ":", self.zwierzetagracza)
            else:
                print("Atak lisa! \nNa szczęście mały pies obronił króliki. Tracisz jednego małego psa")
                self.zwierzetagracza.remove("Mały Pies")
        if WynikDwa == "Wilk": #Zabiera wszystkie zwierzęta oprcz królików
            if "Duży Pies" not in self.zwierzetagracza:
                print("O nie! Tracisz wszystkie zwierzęta oprócz królików!")
                while "Owca" in self.zwierzetagracza:
                    self.zwierzetagracza.remove("Owca")
                while "Świnia" in self.zwierzetagracza:
                    self.zwierzetagracza.remove("Świnia")
                while "Krowa" in self.zwierzetagracza:
                    self.zwierzetagracza.remove("Krowa")
                while "Koń" in self.zwierzetagracza:
                    self.zwierzetagracza.remove("Koń")
                # print("Zwierzęta gracza", self.imie + ":", self.zwierzetagracza)
            else:
                print("Atak wilka! \nNa szczęście duży pies obronił zwierzęta przed zjedzeniem! Tracisz jednego dużego psa")
                self.zwierzetagracza.remove("Duży Pies")
        # print("Zwierzęta gracza", self.imie + ":", self.zwierzetagracza)

        self.pozwierzatkakroliki = self.zwierzetagracza.count("Królik")
        self.pozwierzatkaowce = self.zwierzetagracza.count("Owca")
        self.pozwierzatkaswinie = self.zwierzetagracza.count("Świnia")
        self.pozwierzatkakrowy = self.zwierzetagracza.count("Krowa")
        self.pozwierzatkakonie = self.zwierzetagracza.count("Koń")
        self.pozwierzatkampsy = self.zwierzetagracza.count("Mały Pies")
        self.pozwierzatkadpsy = self.zwierzetagracza.count("Duży Pies")
        lz.zwierzeta(gameDisplay, myfont, self.pozwierzatkakroliki, self.pozwierzatkaowce, self.pozwierzatkaswinie, self.pozwierzatkakrowy, self.pozwierzatkakonie, self.pozwierzatkampsy, self.pozwierzatkadpsy)
        print("Zwierzęta gracza :", "Króliki:", self.pozwierzatkakroliki, "Owce:", self.pozwierzatkaowce, "Świnie:", self.pozwierzatkaswinie, "Krowy:", self.pozwierzatkakrowy, "Konie:", self.pozwierzatkakonie, "Małe Psy:", self.pozwierzatkampsy, "Duże Psy:", self.pozwierzatkadpsy)
        
        pygame_gui.elements.UIButton.show(Rzut_Koscia) # Przycisk się nie pojawia
        manager.draw_ui(gameDisplay)
        pygame.display.update()
        pygame.display.flip()
        Wynik_Gracza = False
        self.Etap_Rzut_Koscia = True
        while self.Etap_Rzut_Koscia == True:
            time_delta = clock.tick(60)/1000.0
            mouse = pygame.mouse.get_pos()
            gameDisplay.blit(background, (0, 0))
            lz.interfejs(gameDisplay, TEXT_COLOR)
            lz.zwierzeta(gameDisplay, myfont, self.pozwierzatkakroliki, self.pozwierzatkaowce, self.pozwierzatkaswinie, self.pozwierzatkakrowy, self.pozwierzatkakonie, self.pozwierzatkampsy, self.pozwierzatkadpsy)
            if Wynik_Gracza == True:
                lz.Grafika_Kosci_Jeden(WynikJeden, gameDisplay)
                lz.Grafika_Kosci_Dwa(WynikDwa, gameDisplay)
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        exit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == Rzut_Koscia:
                            Wynik_Gracza = True
                            pygame_gui.elements.UIButton.hide(Rzut_Koscia)
                            pygame_gui.elements.UIButton.show(Kolejny_Etap)
                            pygame.display.update()
                            pygame.display.flip()
                        if event.ui_element == Kolejny_Etap:
                            pygame_gui.elements.UIButton.hide(Kolejny_Etap)
                            pygame.display.update()
                            Wynik_Gracza = False
                            self.Etap_Rzut_Koscia = False

                manager.process_events(event)
            gameDisplay.blit((myfont.render(("Rzut kośćmi gracza " + str(i_g)), 1, (0,0,0))), (40, 450))
            manager.update(time_delta)
            manager.draw_ui(gameDisplay)
            pygame.display.update()
            pygame.display.flip()

            

        print("KONIEC RZUTU GRACZA")
        self.Etap_Cos_Jeszcze = True
        # Kości, którymi gracz będzie rzucać
        # Wynik pierwszy i wynik drugi
        # Wyświetlenie wyników
        # Zwierzęta wylosowane dodawane sa do inwentarza gracza
        # Podliczane są wszystkie zwierzęta w inwentarzu // Zrobić licznik zwierząt danego gracza, aby było widać z boku
        # // Podliczyć jedynie te, które są wylosowane przez gracza

        # Dwie opcje: a) Kiedy wyniki są sobie równe
        #             b) I kiedy się różnią od siebie
        # a) Zwierzę to, po podliczeniu w inwentarzu
        # Bierze się wartość i dzieli przez dwa
        # Po czym używa funkcji podłogi
        # b) W oryginale oddielnie robiono obie Kości
        # Co było o tyle męczące, że rozbijane są kości na wszystkie zwierzęta
        # Zamiast tego zrobić ify na wilka i lisa, a potem normalnie
        # Usunąć dodane kości z inwentarza
        # Runda kończy się ostatecznym podliczeniem zwierząt i aktualizacją tabelki z liczbą zwierząt
        print("AAA")

    def akcjeporzucie(self, gameDisplay, TEXT_COLOR, myfont, manager, time_delta, clock, Wymiana, Koniec_Rundy, Kupno_Cenniejszych, Kupno_Psow, Kupno_Mniej_Cennych, KC_1, KC_2, KC_3, KC_4, KP_1, KP_2, KMC_1, KMC_2, KMC_3, KMC_4, i_g, background):
        gameDisplay.blit(background, (0, 0))
        pygame_gui.elements.UIButton.show(Wymiana)
        pygame_gui.elements.UIButton.show(Koniec_Rundy)
        Pytanie_Boolean = True
        Wymiana_Boolean = False
        Cenniejsze_Boolean = False
        Pies_Boolean = False
        Mniej_Cenne_Boolean = False
        Koniec_Wymiany_KC = False
        Koniec_Wymiany_KP = False
        Koniec_Wymiany_KMC = False
        while self.Etap_Cos_Jeszcze == True:
            time_delta = clock.tick(60)/1000.0
            mouse = pygame.mouse.get_pos()
            self.wymzwierzatkakroliki = self.zwierzetagracza.count("Królik")
            self.wymzwierzatkaowce = self.zwierzetagracza.count("Owca")
            self.wymzwierzatkaswinie = self.zwierzetagracza.count("Świnia")
            self.wymzwierzatkakrowy = self.zwierzetagracza.count("Krowa")
            self.wymzwierzatkakonie = self.zwierzetagracza.count("Koń")
            self.wymzwierzatkampsy = self.zwierzetagracza.count("Mały Pies")
            self.wymzwierzatkadpsy = self.zwierzetagracza.count("Duży Pies")
            lz.interfejs(gameDisplay, TEXT_COLOR)
            lz.zwierzeta(gameDisplay, myfont, self.wymzwierzatkakroliki, self.wymzwierzatkaowce, self.wymzwierzatkaswinie, self.wymzwierzatkakrowy, self.wymzwierzatkakonie, self.wymzwierzatkampsy, self.wymzwierzatkadpsy)
            if Pytanie_Boolean == True:
                gameDisplay.blit((myfont.render("Czy chcesz zrobić coś jeszcze?", 1, (0,0,0))), (40, 450))
                gameDisplay.blit((myfont.render(("Gracz " + str(i_g)), 1, (0,0,0))), (500, 50))
                lz.Tablica_Wymian(gameDisplay, myfont)
            if Wymiana_Boolean == True:
                gameDisplay.blit((myfont.render(("Gracz " + str(i_g)), 1, (0,0,0))), (500, 50))
                gameDisplay.blit((myfont.render("1 - Wymiana mniej cennych zwierząt na zwierzeta cenniejsze", 1, (0,0,0))), (40, 450))
                gameDisplay.blit((myfont.render("2 - Wymiana na małego/dużego psa", 1, (0,0,0))), (40, 480))
                gameDisplay.blit((myfont.render("3 - Wymiana cenniejszych zwierząt na mniej cenne", 1, (0,0,0))), (40, 510))
                lz.Tablica_Wymian(gameDisplay, myfont)
            if Cenniejsze_Boolean == True:
                gameDisplay.blit((myfont.render(("Gracz " + str(i_g)), 1, (0,0,0))), (500, 50))
                gameDisplay.blit((myfont.render("1 - Owca", 1, (0,0,0))), (40, 450))
                gameDisplay.blit((myfont.render("2 - Świnia", 1, (0,0,0))), (40, 470))
                gameDisplay.blit((myfont.render("3 - Krowa", 1, (0,0,0))), (40, 490))
                gameDisplay.blit((myfont.render("4 - Koń", 1, (0,0,0))), (40, 510))
                lz.Tablica_Wymian(gameDisplay, myfont)
            if Pies_Boolean == True:
                gameDisplay.blit((myfont.render(("Gracz " + str(i_g)), 1, (0,0,0))), (500, 50))
                gameDisplay.blit((myfont.render("1 - Mały pies", 1, (0,0,0))), (40, 450))
                gameDisplay.blit((myfont.render("2 - Duzy pies", 1, (0,0,0))), (40, 480))
                lz.Tablica_Wymian(gameDisplay, myfont)
            if Mniej_Cenne_Boolean == True:
                gameDisplay.blit((myfont.render(("Gracz " + str(i_g)), 1, (0,0,0))), (500, 50))
                gameDisplay.blit((myfont.render("1 - Królik", 1, (0,0,0))), (40, 450))
                gameDisplay.blit((myfont.render("2 - Owca", 1, (0,0,0))), (40, 470))
                gameDisplay.blit((myfont.render("3 - Świnia", 1, (0,0,0))), (40, 490))
                gameDisplay.blit((myfont.render("4 - Krowa", 1, (0,0,0))), (40, 510))
                lz.Tablica_Wymian(gameDisplay, myfont)
            if Koniec_Wymiany_KC == True:
                pygame_gui.elements.UIButton.hide(KC_1)
                pygame_gui.elements.UIButton.hide(KC_2)
                pygame_gui.elements.UIButton.hide(KC_3)
                pygame_gui.elements.UIButton.hide(KC_4)
            if Koniec_Wymiany_KP == True:
                pygame_gui.elements.UIButton.hide(KP_1)
                pygame_gui.elements.UIButton.hide(KP_2)
            if Koniec_Wymiany_KMC == True:
                pygame_gui.elements.UIButton.hide(KMC_1)
                pygame_gui.elements.UIButton.hide(KMC_2)
                pygame_gui.elements.UIButton.hide(KMC_3)
                pygame_gui.elements.UIButton.hide(KMC_4)
            Koniec_Wymiany_KC = False
            Koniec_Wymiany_KP = False
            Koniec_Wymiany_KMC = False
            time_delta = clock.tick(60)/1000.0
            mouse = pygame.mouse.get_pos()
            # wyborgracza = input()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        exit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == Wymiana:
                            pygame_gui.elements.UIButton.hide(Wymiana)
                            # pygame_gui.elements.UIButton.hide(Koniec_Rundy)
                            pygame_gui.elements.UIButton.show(Kupno_Cenniejszych)
                            pygame_gui.elements.UIButton.show(Kupno_Psow)
                            pygame_gui.elements.UIButton.show(Kupno_Mniej_Cennych)
                            Pytanie_Boolean = False
                            Wymiana_Boolean = True
                            pygame.display.update()
                        if event.ui_element == Kupno_Cenniejszych:
                            pygame_gui.elements.UIButton.hide(Kupno_Cenniejszych)
                            pygame_gui.elements.UIButton.hide(Kupno_Psow)
                            pygame_gui.elements.UIButton.hide(Kupno_Mniej_Cennych)
                            pygame_gui.elements.UIButton.show(KC_1)
                            pygame_gui.elements.UIButton.show(KC_2)
                            pygame_gui.elements.UIButton.show(KC_3)
                            pygame_gui.elements.UIButton.show(KC_4)
                            Wymiana_Boolean = False
                            Cenniejsze_Boolean = True
                            pygame.display.update()
                        if event.ui_element == KC_1:
                            if self.wymzwierzatkakroliki > 5:
                                self.zwierzetagracza.remove("Królik")
                                self.zwierzetagracza.remove("Królik")
                                self.zwierzetagracza.remove("Królik")
                                self.zwierzetagracza.remove("Królik")
                                self.zwierzetagracza.remove("Królik")
                                self.zwierzetagracza.remove("Królik")
                                self.zwierzetagracza.append("Owca")
                                print("Brawo, owca została zakupiona! Tracisz 6 królików")
                                Koniec_Wymiany_KC = True
                                Cenniejsze_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                            else:
                                print("Akcja jest niemożliwa do wykonania. Gracz nie posiada królików.")
                                Koniec_Wymiany_KC = True
                                Cenniejsze_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                        if event.ui_element == KC_2:
                            if self.wymzwierzatkaowce > 2:
                                self.zwierzetagracza.remove("Owca")
                                self.zwierzetagracza.remove("Owca")
                                self.zwierzetagracza.remove("Owca")
                                self.zwierzetagracza.append("Świnia")
                                print("Brawo, świnia została zakupiona! Tracisz 3 owce")
                                Koniec_Wymiany_KC = True
                                Cenniejsze_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                            else:
                                print("Akcja jest niemożliwa do wykonania. Gracz nie posiada owiec.")
                                Koniec_Wymiany_KC = True
                                Cenniejsze_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                        if event.ui_element == KC_3:
                            if self.wymzwierzatkaswinie > 1:
                                self.zwierzetagracza.remove("Świnia")
                                self.zwierzetagracza.remove("Świnia")
                                self.zwierzetagracza.append("Krowa")
                                print("Brawo, krowa została zakupiona! Tracisz 2 świnie")
                                Koniec_Wymiany_KC = True
                                Cenniejsze_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                            else:
                                print("Akcja jest niemożliwa do wykonania. Gracz nie posiada świni.")
                                Koniec_Wymiany_KC = True
                                Cenniejsze_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                        if event.ui_element == KC_4:
                            if self.wymzwierzatkakrowy > 1:
                                self.zwierzetagracza.remove("Krowa")
                                self.zwierzetagracza.remove("Krowa")
                                self.zwierzetagracza.append("Koń")
                                print("Brawo, koń został zakupiony! Tracisz dwie krowy")
                                Koniec_Wymiany_KC = True
                                Cenniejsze_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                            else:
                                print("Akcja jest niemożliwa do wykonania. Gracz nie posiada krów.")
                                Koniec_Wymiany_KC = True
                                Cenniejsze_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)

                        if event.ui_element == Kupno_Psow:
                            pygame_gui.elements.UIButton.hide(Kupno_Cenniejszych)
                            pygame_gui.elements.UIButton.hide(Kupno_Psow)
                            pygame_gui.elements.UIButton.hide(Kupno_Mniej_Cennych)
                            pygame_gui.elements.UIButton.show(KP_1)
                            pygame_gui.elements.UIButton.show(KP_2)
                            Wymiana_Boolean = False
                            Pies_Boolean = True
                            pygame.display.update()
                        if event.ui_element == KP_1:
                            if "Owca" in self.zwierzetagracza:
                                self.zwierzetagracza.append("Mały Pies")
                                self.zwierzetagracza.remove("Owca")
                                print("Brawo! Zakupiony został mały pies. Tracisz jedną owcę.")
                                Koniec_Wymiany_KP = True
                                Pies_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                            else:
                                print("Akcja jest niemożliwa do wykonania. Gracz nie posiada owiec.")
                                Koniec_Wymiany_KP = True
                                Pies_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                        if event.ui_element == KP_2:
                            if "Krowa" in self.zwierzetagracza:
                                self.zwierzetagracza.append("Duży Pies")
                                self.zwierzetagracza.remove("Krowa")
                                print("Brawo! Zakupiony został duży pies. Tracisz jedną krowę.")
                                Koniec_Wymiany_KP = True
                                Pies_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                            else:
                                print("Akcja jest niemożliwa do wykonania. Gracz nie posiada krów.")
                                Koniec_Wymiany_KP = True
                                Pies_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)

                        if event.ui_element == Kupno_Mniej_Cennych:
                            pygame_gui.elements.UIButton.hide(Kupno_Cenniejszych)
                            pygame_gui.elements.UIButton.hide(Kupno_Psow)
                            pygame_gui.elements.UIButton.hide(Kupno_Mniej_Cennych)
                            pygame_gui.elements.UIButton.show(KMC_1)
                            pygame_gui.elements.UIButton.show(KMC_2)
                            pygame_gui.elements.UIButton.show(KMC_3)
                            pygame_gui.elements.UIButton.show(KMC_4)
                            Wymiana_Boolean = False
                            Mniej_Cenne_Boolean = True
                            pygame.display.update()
                        if event.ui_element == KMC_1:
                            if "Owca" in self.zwierzetagracza:
                                self.zwierzetagracza.remove("Owca")
                                self.zwierzetagracza.append("Królik")
                                self.zwierzetagracza.append("Królik")
                                self.zwierzetagracza.append("Królik")
                                self.zwierzetagracza.append("Królik")
                                self.zwierzetagracza.append("Królik")
                                self.zwierzetagracza.append("Królik")
                                print("Akcja wykonana pomyślnie! Utracono jedną owcę, zyskano sześć królików")
                                Koniec_Wymiany_KMC = True
                                Mniej_Cenne_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                            else:
                                print("Akcja jest niemożliwa do wykonania. Gracz nie posiada owcy.")
                                Koniec_Wymiany_KMC = True
                                Mniej_Cenne_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                        if event.ui_element == KMC_2:
                            if "Świnia" in self.zwierzetagracza:
                                self.zwierzetagracza.remove("Świnia")
                                self.zwierzetagracza.append("Owca")
                                self.zwierzetagracza.append("Owca")
                                self.zwierzetagracza.append("Owca")
                                print("Akcja wykonana pomyślnie! Utracono jedną świnię, zyskano trzy owce")
                                Koniec_Wymiany_KMC = True
                                Mniej_Cenne_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                            else:
                                print("Akcja jest niemożliwa do wykonania. Gracz nie posiada świni.")
                                Koniec_Wymiany_KMC = True
                                Mniej_Cenne_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)

                        if event.ui_element == KMC_3:
                            if "Krowa" in self.zwierzetagracza:
                                self.zwierzetagracza.remove("Krowa")
                                self.zwierzetagracza.append("Świnia")
                                self.zwierzetagracza.append("Świnia")
                                print("Akcja wykonana pomyślnie! Utracono jedną krowę, uzyskano dwie świnie")
                                Koniec_Wymiany_KMC = True
                                Mniej_Cenne_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                            else:
                                print("Akcja jest niemożliwa do wykonania. Gracz nie posiada krowy.")
                                Koniec_Wymiany_KMC = True
                                Mniej_Cenne_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                        if event.ui_element == KMC_4:
                            if "Koń" in self.zwierzetagracza:
                                self.zwierzetagracza.remove("Koń")
                                self.zwierzetagracza.append("Krowa")
                                self.zwierzetagracza.append("Krowa")
                                print("Akcja wykonana pomyślnie! Utracono jednego konia, uzyskano dwie krowy")
                                Koniec_Wymiany_KMC = True
                                Mniej_Cenne_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)
                            else:
                                print("Akcja jest niemożliwa do wykonania. Gracz nie posiada konia.")
                                Koniec_Wymiany_KMC = True
                                Mniej_Cenne_Boolean = False
                                Pytanie_Boolean = True
                                pygame_gui.elements.UIButton.show(Wymiana)


                        if event.ui_element == Koniec_Rundy:
                            pygame_gui.elements.UIButton.hide(Wymiana)
                            pygame_gui.elements.UIButton.hide(Koniec_Rundy)
                            pygame_gui.elements.UIButton.hide(Kupno_Cenniejszych)
                            pygame_gui.elements.UIButton.hide(Kupno_Psow)
                            pygame_gui.elements.UIButton.hide(Kupno_Mniej_Cennych)
                            pygame_gui.elements.UIButton.hide(KC_1)
                            pygame_gui.elements.UIButton.hide(KC_2)
                            pygame_gui.elements.UIButton.hide(KC_3)
                            pygame_gui.elements.UIButton.hide(KC_4)
                            pygame_gui.elements.UIButton.hide(KP_1)
                            pygame_gui.elements.UIButton.hide(KP_2)
                            pygame_gui.elements.UIButton.hide(KMC_1)
                            pygame_gui.elements.UIButton.hide(KMC_2)
                            pygame_gui.elements.UIButton.hide(KMC_3)
                            pygame_gui.elements.UIButton.hide(KMC_4)
                            print("KONIEC RUNDY GRACZA")
                            print("--------------------")
                            self.Etap_Cos_Jeszcze = False
                        self.powymzwierzatkakroliki = self.zwierzetagracza.count("Królik")
                        self.powymzwierzatkaowce = self.zwierzetagracza.count("Owca")
                        self.powymzwierzatkaswinie = self.zwierzetagracza.count("Świnia")
                        self.powymzwierzatkakrowy = self.zwierzetagracza.count("Krowa")
                        self.powymzwierzatkakonie = self.zwierzetagracza.count("Koń")
                        self.powymzwierzatkampsy = self.zwierzetagracza.count("Mały Pies")
                        self.powymzwierzatkadpsy = self.zwierzetagracza.count("Duży Pies")

                        print("Zwierzęta gracza:", "Króliki:", self.powymzwierzatkakroliki, "Owce:", self.powymzwierzatkaowce, "Świnie:", self.powymzwierzatkaswinie, "Krowy:", self.powymzwierzatkakrowy, "Konie:", self.powymzwierzatkakonie, "Małe Psy:", self.powymzwierzatkampsy, "Duże Psy:", self.powymzwierzatkadpsy)
                manager.process_events(event)
            manager.update(time_delta)
            pygame.display.update()
            pygame.display.flip()
            manager.draw_ui(gameDisplay)

            pygame.display.update()
            clock.tick(10)

    def wygrana_czy_nie(self, gameDisplay, TEXT_COLOR, myfont, manager, time_delta, i_g):
        self.wygzwierzatkakroliki = self.zwierzetagracza.count("Królik")
        self.wygzwierzatkaowce = self.zwierzetagracza.count("Owca")
        self.wygzwierzatkaswinie = self.zwierzetagracza.count("Świnia")
        self.wygzwierzatkakrowy = self.zwierzetagracza.count("Krowa")
        self.wygzwierzatkakonie = self.zwierzetagracza.count("Koń")
        self.wygzwierzatkampsy = self.zwierzetagracza.count("Małe Psy")
        self.wygzwierzatkadpsy = self.zwierzetagracza.count("Duże Psy")
        if self.wygzwierzatkakroliki > 0:
            if self.wygzwierzatkaowce > 0:
                if self.wygzwierzatkaswinie > 0:
                    if self.wygzwierzatkakrowy > 0:
                        if self.wygzwierzatkakonie > 0:
                            while True:
                                lz.interfejs(gameDisplay, TEXT_COLOR)
                                lz.zwierzeta(gameDisplay, myfont, self.wygzwierzatkakroliki, self.wygzwierzatkaowce, self.wygzwierzatkaswinie, self.wygzwierzatkakrowy, self.wygzwierzatkakonie, self.wygzwierzatkampsy, self.wygzwierzatkadpsy)
                                gameDisplay.blit((myfont.render("Gratlacje! Wygrywa gracz " + str(i_g), 1, (0,0,0))), (40, 450))
                                manager.update(time_delta)
                                pygame.display.update()
                                pygame.display.flip()
                                manager.draw_ui(gameDisplay)
                                

