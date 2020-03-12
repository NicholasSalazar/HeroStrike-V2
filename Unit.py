import os
import pygame
import random
import sys
import math
import copy
import time

pygame.init()
def lU(UL,Directory):
    x = pygame.image.load(os.path.join(Directory,UL))
    return x
def loadUnit(y):
    x = [lU('0.png','Units/'+y),lU('1.png','Units/'+y),lU('2.png','Units/'+y),\
          lU('3.png','Units/'+y),lU('4.png','Units/'+y),lU('5.png','Units/'+y),\
          lU('6.png','Units/'+y),lU('7.png','Units/'+y),lU('8.png','Units/'+y),\
          lU('9.png','Units/'+y),lU('10.png','Units/'+y)]
    return x
def lS(LS,Directory):
    x = pygame.mixer.Sound(os.path.join(Directory,LS))
    return x
#arrowProjectile = [lU('0.png','Units/Projectile'),lU('1.png','Units/Projectile'),lU('2.png','Units/Projectile'),\
#lU('3.png','Units/Projectile'),lU('4.png','Units/Projectile'),lU('5.png','Units/Projectile')]
DeathSound1 = lS('DeathSound1.wav','Sounds')
DeathSound2 = lS('DeathSound2.wav','Sounds')
deathSounds = [DeathSound2, DeathSound1]
BowSoundEffect = lS('BowSoundEffect.wav','Sounds')
SpearSoundEffect = lS('SpearSoundEffect.wav','Sounds')
SwordSoundEffect = lS('SwordSoundEffect.wav','Sounds')
MajoraUnitDeathSoundEffect = lS('MajoraUnitDeath.wav','Sounds')
HitSounds = [BowSoundEffect, SpearSoundEffect, SwordSoundEffect]
#projectileList = []
for i in HitSounds:
    i.set_volume(0.3)
for i in deathSounds:
    i.set_volume(0.3)

#class Projectile(object):
    #def __init__(self,x,y,dx,dy,direction,imageList):
        #self.x, self.y = x,y
        #self.direction = direction
        #self.imageList = imageList
        #self.dx, self.dy = dx,dy
        #self.speed = 20
        #self.d = math.sqrt(((self.dx)**2) + ((self.dy)**2))
        #self.slopeX = self.dx / self.d
        #self.slopeY = self.dy / self.d
    #def draw(self,window):
        #self.y += self.slopeY * self.speed
        #self.x += self.slopeX * self.speed
        #window.blit(self.imageList[self.direction],(self.x,self.y)) 
class Unit(object):
    def __init__(self,name,x,y,hitpoints,attRange,vel,image,Dmg):
        self.x = x
        self.y = y
        self.Stage = 1
        self.Forward =True
        self.Attack = False
        self.Wait = False
        self.hitpoints = hitpoints
        self.attRange = attRange
        self.vel = vel
        self.image = image
        self.Dmg = Dmg
        self.name=name
        self.HitBase=False
    def draw(self,window):
        if self.Attack==True:
            if self.Stage+1 >=12:
                self.Stage=7
        elif self.Attack==False:
            if self.Stage +1 >=8:
                self.Stage = 1
        window.blit(self.image[self.Stage],(self.x,self.y))
        self.Stage +=1
    #Unit Collision and attack
    def move(self,List,ListNO,PlayerBaseHP):
        if ListNO==2:
            px = 0
            PlayerModifier = 1
            for i in List:
                if self.x+self.attRange >= List[px].x:
                    self.Attack=True
                    self.Forward=False
                    if ((List[px].attRange == 60 and self.attRange == 200) or (List[px].attRange == 200 and self.attRange == 50)\
                    or (List[px].attRange == 50 and self.attRange == 60)):
                    	PlayerModifier = 2.00
                    else:
                    	PlayerModifier = 1
                    List[px].hitpoints -= (self.Dmg/len(List)) * PlayerModifier
                    #if px == 0:
                        #print('PlayerUnit dealt ', self.Dmg,' to aiUnit with ', List[px].hitpoints,' hitpoints left')
                    randomHitSound = random.choice(HitSounds)
                    randomHitSound.play()
                    PlayerModifier = 1
                    if i.hitpoints <=0:
                        List.remove(i)
                        randomDeathSound = random.choice(deathSounds)
                        pygame.mixer.Channel(1).play(randomDeathSound)

                else:
                    self.Attack=False
                    self.Forward=True
                    px+=1
        elif ListNO==1:
            px2 = 0
            AIModifier = 1
            for i in List:
                if self.x-self.attRange <= List[px2].x:
                    self.Attack=True
                    self.Forward=False
                    if ((List[px2].attRange == 60 and self.attRange == 200) or (List[px2].attRange == 200 and self.attRange == 50)\
                    or (List[px2].attRange == 50 and self.attRange == 60)):
                    	AIModifier = 2.00
                    else:
                    	AIModifier = 1
                    List[px2].hitpoints -= (self.Dmg/len(List))
                    #if px2 == 0:
                        #print('AIUnit dealt ', self.Dmg,' to PlayerUnit with ', List[px2].hitpoints,' hitpoints left')
                    randomHitSound = random.choice(HitSounds)
                    pygame.mixer.Channel(4).play(randomHitSound)
                    if i.hitpoints <=0:
                        List.remove(i)
                        randomDeathSound = random.choice(deathSounds)
                        pygame.mixer.Channel(0).play(randomDeathSound)
                else:
                    self.Attack=False
                    self.Forward=True
                    px2 +=1
        if len(List)==0 and ListNO==2 and self.x+self.attRange>=1120:
            PlayerBaseHP -= self.Dmg
            randomHitSound = random.choice(HitSounds)
            randomHitSound.play()
            self.HitBase=True
            self.Attack=True
        if len(List)==0 and ListNO==1 and self.x-self.attRange<=20:
            PlayerBaseHP -= self.Dmg
            randomHitSound = random.choice(HitSounds)
            randomHitSound.play()
            self.HitBase=True
            self.Attack=True
        if len(List)==0 and self.HitBase==False:
            self.Attack=False
            self.Forward=True
        if self.Attack == False and self.Wait ==False:
            self.x +=self.vel
        return PlayerBaseHP

class Building(object):
    def __init__(self,image1,image2,image3,x,y):
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.primary = 0 
        self.x = x
        self.y = y

    def draw(self,window):
        if self.primary != 0:
            window.blit(self.primary,(self.x,self.y))


    def upgrade(self,Blist,index):
        if self.primary == 0:
            self.primary = self.image1
            Blist[index]=self
        elif self.primary == self.image1:
            self.primary = self.image2
            Blist[index]=self
        elif self.primary == self.image2:
            self.primary = self.image3
            Blist[index]=self




class BossUnit(object):
    def __init__(self,x,y,Image1,Image2):
        self.x = x
        self.y = y
        self.Image1 = Image1
        self.Image2 = Image2
        self.casting = False
        self.counter = 0
        self.tempTimingVariable = 0
        self.tempTimingVariable2 = 0
        self.Power = 0
        self.baseX = x
        self.baseY = y
        self.PowerIncreasing = True 
    def castSpell(self,unitList,timing,soundEffect1,soundEffect2,PlayerBaseHP):
        if self.Power < 1500:
            self.counter = 0
            self.casting = False
            pass
        elif self.PowerIncreasing == False:
            self.casting = False
            self.counter = 0
            self.x = self.baseX
            self.y = self.baseY
        else:
            if self.counter == 0:
                self.tempTimingVariable = copy.deepcopy(timing)
                self.tempTimingVariable2 = copy.deepcopy(timing)
            self.casting = True
            if self.casting == True and timing + 100 > self.tempTimingVariable:
                if self.counter % 2  == 0:
                    self.x += 35
                    self.counter+=1
                else:
                    self.x -= 35
                    self.counter+=1
                if self.counter == 1:
                    soundEffect1.play()
                if timing  > self.tempTimingVariable + 3000:
                    soundEffect1.play()
                    self.tempTimingVariable = copy.deepcopy(timing)
                    print('self:',self.tempTimingVariable,'timing:' ,timing)
            if self.Power >= 2000:
                print('self2:',self.tempTimingVariable,'timing:' ,timing)
                self.casting = False
                self.counter = 0
                self.Power = 0
                for i in unitList:
                    unitList.remove(i)
                    print('removed',i)
                pygame.mixer.Channel(6).play(soundEffect2)
                pygame.time.delay(2500)
                PlayerBaseHP = 0
                self.x = self.baseX
                self.y = self.baseY
        return PlayerBaseHP
    def draw(self,window,stage):
        if stage == 0:
            window.blit(self.Image1,(self.x,self.y))
        elif stage == 1:
            window.blit(self.Image2,(self.x,self.y))
#Unit Stats and SpawnLists ------------------------------------------------------------------------------------
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
Pokemon1 = loadUnit('BossUnit1')
Pokemon3 = loadUnit('BossUnit3')
Pokemon4 = loadUnit('BossUnit4')
Dwarf1R=50
Dwarf2R=200
Dwarf3R=60
Dwarf1Att=2
Dwarf2Att=2
Dwarf3Att=4
Dwarf1Hp=200
Dwarf2Hp=50
Dwarf3Hp=550
Dragon1R = 60
Dragon1Att = 20
Dragon1Hp = 5000
tierMod = 0
Intro = 0
Intro2 = 0
Dwarf1Speed=3.5
Dwarf2Speed=3
Dwarf3Speed=1.5
Dragon1Speed=2
MajorasModifier = 10
AIUnitSpawnY=610

#Units 
Dwarf1Unit = Unit('DwarfScout',1000,AIUnitSpawnY,Dwarf1Hp,Dwarf1R,Dwarf1Speed,Dwarf1,Dwarf1Att)
Dwarf2Unit = Unit('DwarfRanger',1000,AIUnitSpawnY,Dwarf2Hp,Dwarf2R,Dwarf2Speed,Dwarf2,Dwarf2Att)
Dwarf3Unit = Unit('DwarfBeserker',1000,AIUnitSpawnY,Dwarf3Hp,Dwarf3R,Dwarf3Speed,Dwarf3,Dwarf3Att)
Dragon1Unit = Unit('Dragon',1000,AIUnitSpawnY-150,Dragon1Hp,Dragon1R,Dwarf3Speed,Dragon1,Dragon1Att)
Pokemon1Unit = Unit('Pokemon1',1000,AIUnitSpawnY,Dwarf1Hp,Dwarf1R,Dwarf1Speed*2,Pokemon1,Dwarf1Att)
Pokemon2Unit = Unit('Pokemon2',1000,AIUnitSpawnY,Dwarf3Hp,Dwarf3R,Dwarf3Speed,Pokemon3,Dwarf3Att)
Pokemon3Unit = Unit('Pokemon3',1000,AIUnitSpawnY,Dragon1Hp-2000,Dragon1R,Dwarf3Speed,Pokemon4,Dragon1Att-13)
Boss2Unit1 = Unit('MaskedDwarfScout',1000,AIUnitSpawnY-50,Dwarf1Hp*MajorasModifier,Dwarf1R,Dwarf1Speed,Boss2Unit1,Dwarf1Att*MajorasModifier)
Boss2Unit2 = Unit('MaskedDwarfRanger',1000,AIUnitSpawnY-50,Dwarf2Hp*MajorasModifier,Dwarf2R,Dwarf2Speed,Boss2Unit2,Dwarf2Att*MajorasModifier)
Boss2Unit3 = Unit('MaskedDwarfBeserker',1000,AIUnitSpawnY-50,Dwarf3Hp*MajorasModifier,Dwarf3R,Dwarf3Speed,Boss2Unit3,Dwarf3Att*MajorasModifier)
GSUnit = Unit('GreatSkeleton',1000,AIUnitSpawnY-150,Dwarf3Hp,Dwarf2R+200,Dwarf3Speed,GreatSkeleton,Dwarf3Att)
#Cyclops = Unit('Cyclops',1000,AIUnitSpawnY-50,Dragon1Hp,Dragon1R,Dwarf3Speed,Dragon1,Dragon1Att)
#Lvl Spawning Lists
lvl1timeSpawnList = [1000,3620,5350,6570,8930,13350,18000,20000]
lvl1unitSpawnList = [Dwarf1Unit,Dwarf2Unit,Dwarf1Unit,Dwarf1Unit,Dwarf2Unit,Dwarf2Unit,Dwarf1Unit,Dwarf2Unit]
lvl1amountSpawnList = [4,4,6,4,8,7,12,1]
#lvl1amountSpawnList = [0,0,0,0,0,0,0,0]
#lvl 2
lvl2timeSpawnList = [7700,8900,10500,13400,17450,19500,25550,27600,31900,33700,35750,36800,39850]
lvl2unitSpawnList = [Dwarf3Unit,Dwarf2Unit,Dwarf3Unit,Dwarf1Unit,Dwarf2Unit,Dwarf1Unit,Dwarf3Unit,Dwarf3Unit,Dwarf2Unit,Dwarf3Unit,\
            Dwarf2Unit,Dwarf1Unit,Dwarf1Unit]
lvl2amountSpawnList = [5,6,5,7,6,6,7,9,9,6,10,8,6,7]
#lvl 3
lvl3timeSpawnList = [800,2800,4800,5500,9900,10800,12000,14500,17000]
lvl3unitSpawnList = [Dwarf1Unit,Dwarf2Unit,Dwarf1Unit,Dwarf3Unit,Dwarf2Unit,GSUnit,Dwarf1Unit,Dwarf2Unit,Dwarf3Unit]
lvl3amountSpawnList = [7,4,7,5,10,2,3,20,11]
#lvl 4
lvl4timeSpawnList = [1000,3000,7000,9000,12000,15000,18000,22000]
lvl4unitSpawnList = [Pokemon1Unit, Pokemon1Unit, Pokemon2Unit, Pokemon2Unit, Pokemon3Unit, Pokemon1Unit, Pokemon2Unit, Pokemon3Unit]
lvl4amountSpawnList = [4,3,3,3,3,4,3,2]
#lvl 5
lvl5timeSpawnList = [8000,12000,14000,16000,17000]
lvl5unitSpawnList = [Dwarf2Unit,Dwarf1Unit,GSUnit,Dwarf3Unit,Dwarf3Unit,GSUnit]
lvl5amountSpawnList = [12,8,2,10,8,2]
#lvl 6
lvl6timeSpawnList = [1000,4000,9000,13000,150000]
lvl6unitSpawnList = [Dwarf3Unit,Dwarf3Unit,Dwarf2Unit,GSUnit,GSUnit,Dwarf1Unit]
lvl6amountSpawnList = [7,5,7,13,3,3,14]
#lvl 7
Boss2Phase1timeSpawnList = [800,1320,6350,7570,10930,15350,18000,19000]
Boss2Phase1unitSpawnList = [Dwarf1Unit,Dwarf1Unit,Dwarf1Unit,GSUnit,Dwarf1Unit,Dwarf2Unit,Dwarf1Unit,Dwarf1Unit]
Boss2Phase1amountSpawnList = [2,4,3,1,3,7,12,24]
Boss2Phase2timeSpawnList = [900,1500,3000,3500,6000,11500,15900,25500,32000,36000,42000,49000,52000,56000,58000]
Boss2Phase2unitSpawnList = [Boss2Unit1, Boss2Unit2, Boss2Unit1, Boss2Unit3,GSUnit, Boss2Unit3,Boss2Unit2,Boss2Unit3,Boss2Unit1,GSUnit,Boss2Unit1,Boss2Unit2,\
Boss2Unit3,Boss2Unit1,GSUnit]
Boss2Phase2amountSpawnList = [4,2,4,4,3,3,4,6,5,5,10,7,3,5,4]
DifficultyListModifier = [lvl1amountSpawnList,lvl2amountSpawnList,lvl3amountSpawnList,lvl4amountSpawnList,lvl5amountSpawnList,lvl6amountSpawnList,\
Boss2Phase1amountSpawnList, Boss2Phase2amountSpawnList]



