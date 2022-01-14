import time
import math
import random
import pygame
import pygame_gui
import inputimie as ii
import funkcjedokodu as fdk

class mechanizm_rogzrywki():
    def __init__(self, gameDisplay):
        print("Gracz")
        self.zwierzetagracza = []

    def rzut_koscmi(self):
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
        elif WynikDwa == "Wilk": #Zabiera wszystkie zwierzęta oprcz królików
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
        pozwierzatkampsy = self.zwierzetagracza.count("Mały Pies")
        pozwierzatkadpsy = self.zwierzetagracza.count("Duży Pies")
        print("Zwierzęta gracza :", "Króliki:", self.pozwierzatkakroliki, "Owce:", self.pozwierzatkaowce, "Świnie:", self.pozwierzatkaswinie, "Krowy:", self.pozwierzatkakrowy, "Konie:", self.pozwierzatkakonie, "Małe Psy:", pozwierzatkampsy, "Duże Psy:", pozwierzatkadpsy)
        print("KONIEC RZUTU GRACZA")
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
