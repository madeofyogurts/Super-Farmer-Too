import time
import math
import random
import pygame
import pygame_gui
import inputimie as ii
import funkcjedokodu as fdk

class mechanizm_rogzrywki():
    def __init__():
        print("Gracz")
        self.zwierzetagracza = []

    def rzut_koscmi():
        # Kości, którymi gracz będzie rzucać
        # Wynik pierwszy i wynik drugi
        # Wyświetlenie wyników
        # Zwierzęta wylosowane dodawane sa do inwentarza gracza
        # Podliczane są wszystkie zwierzęta w inwentarzu //
        # // Podliczyć jedynie te, które są wylosowane przez gracza

        # Dwie opcje: a) Kiedy wyniki są sobie równe
        #             b) I kiedy się różnią od siebie
        # a) Zwierzę to, po podliczeniu w inwentarzu
        # Bierze się wartość i dzieli przez dwa
        # Po czym używa funkcji podłogi
        # b) W oryginale oddielnie robiono obie Kości
        # Co było o tyle męczące, że rozbijane są kości na wszystkie zwierzęta
        # 
