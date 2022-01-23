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
        gameDisplay.blit(rabbit, (200, 300))
    elif WynikJeden == "Owca":
        gameDisplay.blit(sheep, (200, 300))
    elif WynikJeden == "Świnia":
        gameDisplay.blit(pig, (200, 300))
    elif WynikJeden == "Koń":
        gameDisplay.blit(horse, (200, 300))
    elif WynikJeden == "Lis":
        gameDisplay.blit(fox, (200, 300))


def Grafika_Kosci_Dwa(WynikDwa, gameDisplay):
    # "Krowa", "Królik", "Wilk"
    if WynikDwa == "Królik":
        gameDisplay.blit(rabbit, (200, 350))
    elif WynikDwa == "Owca":
        gameDisplay.blit(sheep, (200, 350))
    elif WynikDwa == "Świnia":
        gameDisplay.blit(pig, (200, 350))
    elif WynikDwa == "Krowa":
        gameDisplay.blit(cow, (200, 350))
    elif WynikDwa == "Wilk":
        gameDisplay.blit(wolf, (200, 350))

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
