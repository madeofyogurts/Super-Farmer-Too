import pygame
import pygame_gui

def zwierzeta(gameDisplay, myfont, przedzwierzatkakroliki, przedzwierzatkaowce, przedzwierzatkaswinie, przedzwierzatkakrowy, przedzwierzatkakonie, przedzwierzatkamalepsy, przedzwierzatkaduzepsy):
    # Liczba_Krolikow = myfont.render(str(przedzwierzatkakroliki), 1, (0,0,0))
    gameDisplay.blit((myfont.render(str(przedzwierzatkakroliki), 1, (0,0,0))), (100, 60))
    # Liczba_Owiec = myfont.render(str(przedzwierzatkaowce), 1, (0,0,0))
    gameDisplay.blit((myfont.render(str(przedzwierzatkaowce), 1, (0,0,0))), (100, 110))
    # Liczba_Swin = myfont.render(str(przedzwierzatkaswinie), 1, (0,0,0))
    gameDisplay.blit((myfont.render(str(przedzwierzatkaswinie), 1, (0,0,0))), (100, 160))
    # Liczba_Krow = myfont.render(str(przedzwierzatkakrowy), 1, (0,0,0))
    gameDisplay.blit((myfont.render(str(przedzwierzatkakrowy), 1, (0,0,0))), (100, 210))
    # Liczba_Koni = myfont.render(str(przedzwierzatkakonie), 1, (0,0,0))
    gameDisplay.blit((myfont.render(str(przedzwierzatkakonie), 1, (0,0,0))), (100, 260))
    # Liczba_Malych_Psow = myfont.render(str(przedzwierzatkamalepsy), 1, (0,0,0))
    gameDisplay.blit((myfont.render(str(przedzwierzatkamalepsy), 1, (0,0,0))), (100, 310))
    # Liczba_Duzych_Psow = myfont.render(str(przedzwierzatkaduzepsy), 1, (0,0,0))
    gameDisplay.blit((myfont.render(str(przedzwierzatkaduzepsy), 1, (0,0,0))), (100, 360))
    # pygame.display.update()

def interfejs(gameDisplay, TEXT_COLOR):
    pygame.draw.rect(gameDisplay, TEXT_COLOR, (20, 45, 150, 350))
    pygame.draw.rect(gameDisplay, TEXT_COLOR, (20, 430, 760, 150))
    gameDisplay.blit(rabbit, (30, 50))
    gameDisplay.blit(sheep, (30, 100))
    gameDisplay.blit(pig, (30, 150))
    gameDisplay.blit(cow, (30, 200))
    gameDisplay.blit(horse, (30, 250))
    gameDisplay.blit(small_dog, (30, 300))
    gameDisplay.blit(big_dog, (30, 350))
    # pygame.display.update()

def Grafika_Kosci_Jeden(WynikJeden, gameDisplay):
    if WynikJeden == "Królik":
        gameDisplay.blit(rabbit, (200, 500))
    elif WynikJeden == "Owca":
        gameDisplay.blit(sheep, (200, 500))
    elif WynikJeden == "Świnia":
        gameDisplay.blit(pig, (200, 500))
    elif WynikJeden == "Koń":
        gameDisplay.blit(horse, (200, 500))
    elif WynikJeden == "Lis":
        gameDisplay.blit(fox, (200, 500))


def Grafika_Kosci_Dwa(WynikDwa, gameDisplay):
    # "Krowa", "Królik", "Wilk"
    if WynikDwa == "Królik":
        gameDisplay.blit(rabbit, (250, 500))
    elif WynikDwa == "Owca":
        gameDisplay.blit(sheep, (250, 500))
    elif WynikDwa == "Świnia":
        gameDisplay.blit(pig, (250, 500))
    elif WynikDwa == "Krowa":
        gameDisplay.blit(cow, (250, 500))
    elif WynikDwa == "Wilk":
        gameDisplay.blit(wolf, (250, 500))

def Tablica_Wymian(gameDisplay, myfont):
    gameDisplay.blit((myfont.render("6", 1, (0,0,0))), (280, 110))
    gameDisplay.blit(rabbit, (300, 100))
    gameDisplay.blit((myfont.render("=", 1, (0,0,0))), (380, 110))
    gameDisplay.blit((myfont.render("1", 1, (0,0,0))), (430, 110))
    gameDisplay.blit(sheep, (450, 100))
    gameDisplay.blit((myfont.render("3", 1, (0,0,0))), (280, 160))
    gameDisplay.blit(sheep, (300, 150))
    gameDisplay.blit((myfont.render("=", 1, (0,0,0))), (380, 160))
    gameDisplay.blit((myfont.render("1", 1, (0,0,0))), (430, 160))
    gameDisplay.blit(pig, (450, 150))
    gameDisplay.blit((myfont.render("2", 1, (0,0,0))), (280, 210))
    gameDisplay.blit(pig, (300, 200))
    gameDisplay.blit((myfont.render("=", 1, (0,0,0))), (380, 210))
    gameDisplay.blit((myfont.render("1", 1, (0,0,0))), (430, 210))
    gameDisplay.blit(cow, (450, 200))
    gameDisplay.blit((myfont.render("2", 1, (0,0,0))), (280, 260))
    gameDisplay.blit(cow, (300, 250))
    gameDisplay.blit((myfont.render("=", 1, (0,0,0))), (380, 260))
    gameDisplay.blit((myfont.render("1", 1, (0,0,0))), (430, 260))
    gameDisplay.blit(horse, (450, 250))
    gameDisplay.blit((myfont.render("1", 1, (0,0,0))), (280, 310))
    gameDisplay.blit(sheep, (300, 300))
    gameDisplay.blit((myfont.render("=", 1, (0,0,0))), (380, 310))
    gameDisplay.blit((myfont.render("1", 1, (0,0,0))), (430, 310))
    gameDisplay.blit(small_dog, (450, 300))
    gameDisplay.blit((myfont.render("1", 1, (0,0,0))), (280, 360))
    gameDisplay.blit(cow, (300, 350))
    gameDisplay.blit((myfont.render("=", 1, (0,0,0))), (380, 360))
    gameDisplay.blit((myfont.render("1", 1, (0,0,0))), (430, 360))
    gameDisplay.blit(big_dog, (450, 350))

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
fox = pygame.image.load("pic-fox.png")
fox = pygame.transform.scale(fox, (35, 35))
wolf = pygame.image.load("pic-wolf.png")
wolf = pygame.transform.scale(wolf, (35, 35))
