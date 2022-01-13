import pygame
import pygame_gui
import inputimie as ii
import funkcjedokodu as fdk

# Generalne, potrzebne
pygame.init()
pygame.display.set_caption("Super Farmer") #Tytuł okienka
t_g = fdk.tryby_gry()

# Wymiary ekranu
SCREEN_X = 800
SCREEN_Y = 600

# Ustawienie podstawowych wartości
gameDisplay=pygame.display.set_mode((SCREEN_X,SCREEN_Y))
clock=pygame.time.Clock()

background = pygame.Surface((SCREEN_X, SCREEN_Y))
background.fill(pygame.Color('#9CCC65'))

# Kolory
GREEN_BACKGROUND = (156, 204, 101) # Tło - #9CCC65
BUTTON = (29, 32, 31) # Przyciski - nieużywane, jak zakodować inny kolor przycisku?
TEXT_COLOR = (241, 191, 152) # Jak zakodować inny kolor tekstu?
myfont = pygame.font.SysFont("monospace", 15)

# Etapy gry
Etap_Poczatek = True
Etap_Zasady = False
Etap_Rozgrywka = False
Etap_Gracze = False

# Przyciski
manager = pygame_gui.UIManager((SCREEN_X, SCREEN_Y)) # UIManager kontroluje, wszystko, co dzieje się na ekranie kodu, a także aktualizuje każdą klatkę programu

# Etap 1 - Początek
RozpocznijGre = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(250, 250, 300, 100), text="Rozpocznij Grę", manager=manager)
ZasadyGry = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(250, 400, 300, 100), text="Zasady Gry", manager=manager)

# Etap 2 - Zasady Gry
PowrotDoMenu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(50, 400, 300, 100), text="Powrót", manager=manager)
pygame_gui.elements.UIButton.hide(PowrotDoMenu)

# Etap 3 - Rozgrywka
Liczba_Graczy = myfont.render("Wybierz liczbę graczy:", 1, (0,0,0))
Graczy_Dwoch = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(50, 150, 50, 50), text="2", manager=manager)
pygame_gui.elements.UIButton.hide(Graczy_Dwoch)
Graczy_Trzech = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(125, 150, 50, 50), text="3", manager=manager)
pygame_gui.elements.UIButton.hide(Graczy_Trzech)
Graczy_Czterech = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(200, 150, 50, 50), text="4", manager=manager)
pygame_gui.elements.UIButton.hide(Graczy_Czterech)
Graczy_Pieciu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(275, 150, 50, 50), text="5", manager=manager)
pygame_gui.elements.UIButton.hide(Graczy_Pieciu)
Imiona_Graczy = []

while True:
    gameDisplay.blit(background, (0, 0)) # Tworzy zdefiniowane wyżej tło, umieszcza je w prawym górnym rogu
    manager.draw_ui(gameDisplay)
    time_delta = clock.tick(60)/1000.0
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == RozpocznijGre:
                    t_g.etap_rozpoczecie_gry(RozpocznijGre, ZasadyGry, gameDisplay, Liczba_Graczy, Graczy_Dwoch, Graczy_Trzech, Graczy_Czterech, Graczy_Pieciu)
                if event.ui_element == ZasadyGry:
                    t_g.etap_zasady_gry(RozpocznijGre, ZasadyGry, PowrotDoMenu)
                if event.ui_element == PowrotDoMenu:
                    t_g.powrot_do_menu(RozpocznijGre, ZasadyGry, PowrotDoMenu)
                if event.ui_element == Graczy_Dwoch:
                    Graczy_Liczba = 2
                    t_g.gracze_ustaleni(gameDisplay, background, Graczy_Dwoch, Graczy_Trzech, Graczy_Czterech, Graczy_Pieciu, Graczy_Liczba)
                if event.ui_element == Graczy_Trzech:
                    Graczy_Liczba = 3
                    t_g.gracze_ustaleni(gameDisplay, background, Graczy_Dwoch, Graczy_Trzech, Graczy_Czterech, Graczy_Pieciu, Graczy_Liczba)
                if event.ui_element == Graczy_Czterech:
                    Graczy_Liczba = 4
                    t_g.gracze_ustaleni(gameDisplay, background, Graczy_Dwoch, Graczy_Trzech, Graczy_Czterech, Graczy_Pieciu, Graczy_Liczba)
                if event.ui_element == Graczy_Pieciu:
                    Graczy_Liczba = 5
                    t_g.gracze_ustaleni(gameDisplay, background, Graczy_Dwoch, Graczy_Trzech, Graczy_Czterech, Graczy_Pieciu, Graczy_Liczba)

        manager.process_events(event)
    manager.update(time_delta) # Tak często UIManager aktualizuje program

    # gameDisplay.fill(GREEN_BACKGROUND)
    t_g.wyswietlane_teksty(gameDisplay, Liczba_Graczy)

    pygame.display.update()
    clock.tick(10)
