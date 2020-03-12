import pygame
import sys
import time
import os
import random
from pygame.locals import *
pygame.init()
def lU(UL,Directory):
    x = pygame.image.load(os.path.join(Directory,UL))
    return x
def lS(LS,Directory):
    x = pygame.mixer.Sound(os.path.join(Directory,LS))
    return x
def lM(LM,Directory):
    x = pygame.mixer.music.load(os.path.join(Directory,LM))
    return x
win = pygame.display.set_mode((1250,700))
Music1 = lM('IntroMusic.mp3','Music')
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans',30,True)
backGround1 = lU('Lvl1BG.jpg','Backgrounds')
backGround2 = lU('Lvl2BG.jpg','Backgrounds')
backGround3 = lU('Lvl3BG.png','Backgrounds')
backGround4 = lU('Lvl4BG.jpg','Backgrounds')
backGround5 = lU('Lvl5BG.jpg','Backgrounds')
backGround6 = lU('Lvl6BG.png','Backgrounds')
backGround7 = lU('Lvl7BGPhase1.png','Backgrounds')
backGround8 = lU('Lvl7BGPhase2.jpg','Backgrounds')
backGroundList = []
for i in range(15):
    x = lU('Trans' + str(i+1) + '.png', 'Backgrounds/Transition')
    backGroundList.append(x)
TopFrame = lU('TopFrame.png','UI')
playBtn = lU('PlayBtn.png','UI')
Title = lU('Title.png','UI')
pygame.display.set_caption("Hero Strike")
Tutorial = lU('Tutorial.png','UI')
PlayerBase = lU('Command_Center.png','UI')
AIBase = lU('Command_Center2.png','UI')
MenuBG = lU('MenuBG.jpg','UI')
DifBG = lU('DifficultyScrn.png','UI')
BlackBorder = lU('BlackBorder.png','UI')
icon = lU('icon.png','UI')
#Miscellaneous
font = pygame.font.SysFont('comicsans',30,True)
mousePos = pygame.mouse.get_pos()
pygame.display.update()
keys = pygame.key.get_pressed()
pygame.display.set_icon(icon)
AIList = []
pygame.mixer.music.play(-1)
TowerRange = 400 #originally 400
Boss2Lvl = 7
#Interface
Interface = [lU('Unit1Dwarf.png','UI'),lU('Unit2Dwarf.png','UI'),lU('Unit3Dwarf.png','UI'),\
             lU('Unit4Dwarf.png','UI'),lU('Unit5Tower.png','UI'),lU('UpgradeBtn1.png','UI'),lU("Player1WINSImage.png",'UI'),\
             lU("YouLose.png",'UI'),lU('UpgradeBG.png','UI'),lU('RaceBG.png','UI'),lU('GoldMine1.png','Buildings'),\
             lU('GoldMine2.png','Buildings'),lU('GoldMine3.png','Buildings'),lU('OrcInterface1.png','UI'),lU('HumanInterface1.png','UI'),\
             lU('SkeletonInterface1.png','UI'),lU('OrcInterface2.png','UI'),lU('HumanInterface2.png','UI'),lU('SkeletonInterface2.png','UI'),\
             lU('OrcInterface3.png','UI'),lU('HumanInterface3.png','UI'),lU('SkeletonInterface3.png','UI'),lU('Boss1Phase1.png','UI'),lU('Boss1Phase1Portrait.png','UI')\
             ,lU('MeteorPower.png','UI'),lU('ExpPower.png','UI'),lU('TutPicture1.png','UI'),lU('TutPicture2.png','UI')\
             ,lU('TutPicture3.png','UI'),lU('TutPicture4.png','UI'),lU('GreenCheck.png','UI'),lU('Boss2Phase1.png','UI'),lU('Boss2Phase1Portrait.png','UI'),\
             lU('TutPicture5.png','UI'),lU('TutPicture6.png','UI'),lU('midbarGreen.png','UI'),lU('midbarRed.png','UI'),lU('midbarPurple.png','UI'),\
             lU('TutPicture7.png','UI'),lU('Boss2Phase2Portrait.png','UI'),lU('TowerRange.png','UI'),lU('DragonGreyedOut.png','UI')]#41
##Lvl1 AI units
UL= ['0.png','1.png','2.png','3.png','4.png','5.png','6.png','7.png',\
     '8.png','9.png','10.png']
#Units
def loadUnit(y):
    x = [lU('0.png','Units/'+y),lU('1.png','Units/'+y),lU('2.png','Units/'+y),\
          lU('3.png','Units/'+y),lU('4.png','Units/'+y),lU('5.png','Units/'+y),\
          lU('6.png','Units/'+y),lU('7.png','Units/'+y),lU('8.png','Units/'+y),\
          lU('9.png','Units/'+y),lU('10.png','Units/'+y)]
    return x
#Sound Files
MeteorSound = lS('MeteorSound.wav','Sounds')
MeteorSound.set_volume(0.4)
Tower1Human = lU('Tower1(Human).png','Units/Tower1')
Tower1Orc = lU('Tower1(Orc).png','Units/Tower1')
Tower1Undead = lU('Tower1(Undead).png','Units/Tower1')
GoldMine1 = lU('GoldMine1.png','Buildings')
GoldMine2 = lU('GoldMine2.png','Buildings')
GoldMine3 = lU('GoldMine3.png','Buildings')
Fountain1 = lU('Fountain1.png','Buildings')
Fountain2 = lU('Fountain2.png','Buildings')
Fountain3 = lU('Fountain3.png','Buildings')
Barracks1 = lU('Barracks1.png','Buildings')
Barracks2 = lU('Barracks2.png','Buildings')
Barracks3 = lU('Barracks3.png','Buildings')
UpgradeSound = lS('UpgradeSound.wav','Sounds')
UpgradeSound.set_volume(0.3)
DeathSound1 = lS('DeathSound1.wav','Sounds')
DeathSound2 = lS('DeathSound2.wav','Sounds')
boomSound = lS('boomSound.wav','Sounds')
clashSound = lS('Clash.wav','Sounds')
clashSound.set_volume(0.4)
MajorasScreamSoundEffect = lS('MajorasScreamSoundEffect.wav','Sounds')
deathSounds = [DeathSound2, DeathSound1]
BowSoundEffect = lS('BowSoundEffect.wav','Sounds')
SpearSoundEffect = lS('SpearSoundEffect.wav','Sounds')
SwordSoundEffect = lS('SwordSoundEffect.wav','Sounds')
loseSoundEffect = lS('loseSound.wav','Sounds')
victorySoundEffect = lS('victorySound.wav','Sounds')
goldMineSoundEffect = lS('GoldMine.wav','Sounds')
dragonHatcherySoundEffect = lS('dragonSound.wav','Sounds')
dragonHatcherySoundEffect.set_volume(0.2)
goldMineSoundEffect.set_volume(0.3)
fountainSoundEffect = lS('Fountain.wav','Sounds')
barracksSoundEffect = lS('Barracks.wav','Sounds')
MajoraUnitDeathSoundEffect = lS('MajoraUnitDeath.wav','Sounds')
MajorasAwakeningSoundEffect = lS('MajorasAwakening.wav','Sounds')
HitSounds = [BowSoundEffect, SpearSoundEffect, SwordSoundEffect]
Boss2Unit1 = loadUnit('Boss2Unit1')
Boss2Unit2 = loadUnit('Boss2Unit2')
Boss2Unit3 = loadUnit('Boss2Unit3')
GreatSkeleton = loadUnit('GreatSkeleton')
Dwarf1 = loadUnit('Dwarf1')
Dwarf2 = loadUnit('Dwarf2')
Dwarf3 = loadUnit('Dwarf3')
PDwarf1 = loadUnit('PDwarf1')
PDwarf2 = loadUnit('PDwarf2')
PDwarf3 = loadUnit('PDwarf3')
PDragon1 = loadUnit('PDragon1')
Dragon1 = loadUnit('Dragon1')
Orc1=loadUnit('Orc1')
Orc2=loadUnit('Orc2')
Orc3=loadUnit('Orc3')
Human1=loadUnit('Human1')
Human2=loadUnit('Human2')
Human3=loadUnit('Human3')
Skeleton1=loadUnit('Skeleton1')
Skeleton2=loadUnit('Skeleton2')
Skeleton3=loadUnit('Skeleton3')
Pokemon1 = loadUnit('BossUnit1')
Pokemon3 = loadUnit('BossUnit3')
Pokemon4 = loadUnit('BossUnit4')
#UpgradedUnits
Human1Plate=loadUnit('Human1Plate')
Human2Plate=loadUnit('Human2Plate')
Human3Plate=loadUnit('Human3Plate')
Human1Gold=loadUnit('Human1Gold')
Human2Gold=loadUnit('Human2Gold')
Human3Gold=loadUnit('Human3Gold')
Orc1Plate=loadUnit('Orc1Plate')
Orc2Plate=loadUnit('Orc2Plate')
Orc3Plate=loadUnit('Orc3Plate')
Orc1Gold=loadUnit('Orc1Gold')
Orc2Gold=loadUnit('Orc2Gold')
Orc3Gold=loadUnit('Orc3Gold')
Skeleton1Plate=loadUnit('Skeleton1Plate')
Skeleton2Plate=loadUnit('Skeleton2Plate')
Skeleton3Plate=loadUnit('Skeleton3Plate')
Skeleton1Gold=loadUnit('Skeleton1Gold')
Skeleton2Gold=loadUnit('Skeleton2Gold')
Skeleton3Gold=loadUnit('Skeleton3Gold')
Cyclops = loadUnit('Cyclops')
VictoryScreen = lU('VictoryScreen.png','Backgrounds')
font = pygame.font.SysFont('comicsans',100,True)
easyText = font.render('EASY',1,(0,0,255))
mediumText = font.render('MEDIUM',1,(0,255,0))
hardText = font.render('HARD',1,(255,0,0))
victoryText = [easyText, mediumText, hardText]
HumanRace = [Human1,Human2,Human3,Human1Plate,Human2Plate,Human3Plate,\
                         Human1Gold,Human2Gold,Human3Gold,Tower1Human]
OrcRace = [Orc1,Orc2,Orc3,Orc1Plate,Orc2Plate,Orc3Plate,Orc1Gold,\
                             Orc2Gold,Orc3Gold,Tower1Orc]
UndeadRace = [Skeleton1,Skeleton2,Skeleton3,Skeleton1Plate,Skeleton2Plate,\
                             Skeleton3Plate,Skeleton1Gold,Skeleton2Gold,Skeleton3Gold,Tower1Undead]





#Miscellaneous Functions
def DrawMenu():
    win.blit(MenuBG,(0,0))
    pygame.draw.rect(win,(255,0,0),(500,220,250,100) ,0)
    win.blit(playBtn,(530,230))
    win.blit(Title,(400,80))
    pygame.draw.rect(win,(255,0,0),(500,400,350,100) ,0)
    win.blit(Tutorial,(530,410))


def clickedBox(x1,y1,x2,y2,mousePos):
    if mousePos[0] > x1 and mousePos[1] > y1 and mousePos[0] < x2 \
       and mousePos[1] < y2:
        return True
    else:
        return False
def inCircle(circle, point):
    center = circle.getCenter()
    distance = ((point.getX() - center.getX()) ** 2 + (point.getY() - center.getY()) ** 2) ** 0.5
    return distance < circle.radius
