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

    def rzut_koscmi(self, gameDisplay, myfont):
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

    def akcjeporzucie(self, gameDisplay, myfont, manager, time_delta, clock, Wymiana, Koniec_Rundy, Kupno_Cenniejszych, Kupno_Psow, Kupno_Mniej_Cennych):
        pygame_gui.elements.UIButton.show(Wymiana)
        pygame_gui.elements.UIButton.show(Koniec_Rundy)
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
            gameDisplay.blit((myfont.render("Czy chcesz zrobić coś jeszcze?", 1, (0,0,0))), (40, 450))
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
                            pygame_gui.elements.UIButton.hide(Koniec_Rundy)
                            pygame_gui.elements.UIButton.show(Kupno_Cenniejszych)
                            pygame_gui.elements.UIButton.show(Kupno_Psow)
                            pygame_gui.elements.UIButton.show(Kupno_Mniej_Cennych)
                            pygame.display.update()
                            wymianyopcjejeden = print("Możliwe wymiany: 1 - Kupno cenniejszych zwierząt hodowlanych, 2 - Kupno małego lub dużego psa, 3 - Wymiana zwierząt na mniej cenne")
                            if wymianyopcjejeden == "1":
                                cennezwierzatka = input("Jakie zwierzę chcesz zakupić? 1 - Owca, 2 - Świnia, 3 - Krowa, 4 - Koń")
                                if cennezwierzatka == "1":
                                    if self.wymzwierzatkakroliki > 5: 
                                        self.zwierzetagracza.remove("Królik")
                                        self.zwierzetagracza.remove("Królik")
                                        self.zwierzetagracza.remove("Królik")
                                        self.zwierzetagracza.remove("Królik")
                                        self.zwierzetagracza.remove("Królik")
                                        self.zwierzetagracza.remove("Królik")
                                        self.zwierzetagracza.append("Owca")
                                        print("Brawo, owca została zakupiona! Tracisz 6 królików")
                                    else:
                                        print("Akcja jest niemożliwa do wykonania. Gracz nie posiada królików.")
                                elif cennezwierzatka == "2":
                                    if self.wymzwierzatkaowce > 2:
                                        self.zwierzetagracza.remove("Owca")
                                        self.zwierzetagracza.remove("Owca")
                                        self.zwierzetagracza.remove("Owca")
                                        self.zwierzetagracza.append("Świnia")
                                        print("Brawo, świnia została zakupiona! Tracisz 3 owce")
                                    else:
                                        print("Akcja jest niemożliwa do wykonania. Gracz nie posiada owiec.")
                                elif cennezwierzatka == "3":
                                    if self.wymzwierzatkaswinie > 1:
                                        self.zwierzetagracza.remove("Świnia")
                                        self.zwierzetagracza.remove("Świnia")
                                        self.zwierzetagracza.append("Krowa")
                                        print("Brawo, krowa została zakupiona! Tracisz 2 świnie")
                                    else:
                                        print("Akcja jest niemożliwa do wykonania. Gracz nie posiada świni.")
                                elif cennezwierzatka == "4":
                                    if self.wymzwierzatkakrowy > 1:
                                        self.zwierzetagracza.remove("Krowa")
                                        self.zwierzetagracza.remove("Krowa")
                                        self.zwierzetagracza.append("Koń")
                                        print("Brawo, koń został zakupiony! Tracisz dwie krowy")
                                    else:
                                        print("Akcja jest niemożliwa do wykonania. Gracz nie posiada krów.")

                            elif wymianyopcjejeden == "2":
                                piesczypies = input("1 - Mały Pies, 2 - Duży Pies")
                                if piesczypies == "1":
                                    if "Owca" in self.zwierzetagracza:
                                        self.zwierzetagracza.append("Mały Pies")
                                        self.zwierzetagracza.remove("Owca")
                                        print("Brawo! Zakupiony został mały pies. Tracisz jedną owcę.")
                                    else:
                                        print("Akcja jest niemożliwa do wykonania. Gracz nie posiada owiec.")
                                if piesczypies == "2":
                                    if "Krowa" in self.zwierzetagracza:
                                        self.zwierzetagracza.append("Duży Pies")
                                        self.zwierzetagracza.remove("Krowa")
                                        print("Brawo! Zakupiony został duży pies. Tracisz jedną krowę.")
                                    else:
                                        print("Akcja jest niemożliwa do wykonania. Gracz nie posiada krów.")
                            elif wymianyopcjejeden == "3":
                                namniejcenne = input("Jakie zwierzęta chcesz zakupić? 1 - króliki, 2 - Owce, 3 - Świnie, 4 - Krowy")
                                if namniejcenne == "1":
                                    if "Owca" in self.zwierzetagracza:
                                        self.zwierzetagracza.remove("Owca")
                                        self.zwierzetagracza.append("Królik")
                                        self.zwierzetagracza.append("Królik")
                                        self.zwierzetagracza.append("Królik")
                                        self.zwierzetagracza.append("Królik")
                                        self.zwierzetagracza.append("Królik")
                                        self.zwierzetagracza.append("Królik")
                                        print("Akcja wykonana pomyślnie! Utracono jedną owcę, zyskano sześć królików")
                                    else:
                                        print("Akcja jest niemożliwa do wykonania. Gracz nie posiada owcy.")
                                elif namniejcenne == "2":
                                    if "Świnia" in self.zwierzetagracza:
                                        self.zwierzetagracza.remove("Świnia")
                                        self.zwierzetagracza.append("Owca")
                                        self.zwierzetagracza.append("Owca")
                                        self.zwierzetagracza.append("Owca")
                                        print("Akcja wykonana pomyślnie! Utracono jedną świnię, zyskano trzy owce")
                                    else:
                                        print("Akcja jest niemożliwa do wykonania. Gracz nie posiada świni.")

                                elif namniejcenne == "3":
                                    if "Krowa" in self.zwierzetagracza:
                                        self.zwierzetagracza.remove("Krowa")
                                        self.zwierzetagracza.append("Świnia")
                                        self.zwierzetagracza.append("Świnia")
                                        print("Akcja wykonana pomyślnie! Utracono jedną krowę, uzyskano dwie świnie")
                                    else:
                                        print("Akcja jest niemożliwa do wykonania. Gracz nie posiada krowy.")
                                elif namniejcenne == "4":
                                    if "Koń" in self.zwierzetagracza:
                                        self.zwierzetagracza.remove("Koń")
                                        self.zwierzetagracza.append("Krowa")
                                        self.zwierzetagracza.append("Krowa")
                                        print("Akcja wykonana pomyślnie! Utracono jednego konia, uzyskano dwie krowy")
                                    else:
                                        print("Akcja jest niemożliwa do wykonania. Gracz nie posiada konia.")
                                        

                        elif event.ui_element == Koniec_Rundy:
                            pygame_gui.elements.UIButton.hide(Wymiana)
                            pygame_gui.elements.UIButton.hide(Koniec_Rundy)
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
