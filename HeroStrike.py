#Data Structures Project
#Nicholas Salazar
import pygame
import sys
import time
import os
import random
from Players import Player
from Unit import *
from pygame.locals import *
from Imports import *

global timeTicked
timeTicked = 25 #originally 25
global unitStopper
unitStopper = 0
global BossSwitch
BossSwitch=0
global run2
run2 = True
font = pygame.font.SysFont('comicsans',30,True)
for i in HitSounds:
    i.set_volume(0.3)
for i in deathSounds:
    i.set_volume(0.3)
def Player1Wins():
    global run2
    global BossSwitch
    win.blit(Interface[6],(400,300))
    pygame.display.update()
    pygame.mixer.pause()
    pygame.mixer.Channel(3).play(victorySoundEffect)
    pygame.time.delay(4000)
    pygame.mixer.unpause()
    if Lvl ==Boss2Lvl and BossSwitch == 0:
        BossSwitch=1
        AI1.BaseHP += 1200
        while len(Player1.UnitList)!=0:
            for i in Player1.UnitList:
                Player1.UnitList.remove(i)
        for i in AIList:
            AIList.remove(i)
    elif Lvl == Boss2Lvl and BossSwitch == 1:
        Player1.win = 1
        run2 =False
    else:
    	Player1.win = 1
    	run2=False
def AI1Wins():
    global run2
    win.blit(Interface[7],(400,300))
    pygame.display.update()
    pygame.mixer.pause()
    pygame.mixer.music.stop()
    pygame.mixer.Channel(3).play(loseSoundEffect)
    pygame.time.delay(4000)
    pygame.mixer.unpause()
    run2=False
#Text interface
global TempIncome
TempIncome=1
global TempExp
TempExp=1
global TempMana
TempMana=1
AI1 = Player(200,0,0,0,0,0,1000,0,HumanRace)
Player1 =Player(200,0,0,0,0,0,1000,2,HumanRace)
text = font.render('Gold:',1,(0,255,0))
Manatxt = font.render('Mana:',1,(0,102,224))
Exptxt = font.render('Exp:',1,(225,153,51))
tempExpText = font.render('+'+str(TempExp)+'%',1,(225,153,51))
PlayerBaseHPtxt = font.render('HP:',1,(0,255,0))
Buildings = [0,0,0]
BuildingPlacementX = 144
GoldMine = Building(GoldMine1,GoldMine2,GoldMine3,BuildingPlacementX,550)
Fountain = Building(Fountain1,Fountain2,Fountain3,BuildingPlacementX + 120,506)
Barracks = Building(Barracks1,Barracks2,Barracks3,BuildingPlacementX + 200,486)
TowerDmg = 6 * Player1.TowerDmgMod
MajorasMask = BossUnit(1050,140,Interface[32],Interface[39])
global MeteormodY
global MeteormodX
MeteormodX = 0
MeteormodY =0
global midIncomeActive
midIncomeActive = False
AITowerLvlList =[0,0,1,0,1,1,1,1]
def DrawUpMenu():
    run3=True
    
    while run3 == True:
        win.blit(Interface[8],(0,0))
        clock.tick(27)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if clickedBox(225,136,400,180,mousePos)==True and Player1.UpgR>=1:
                    Player1.Upgrade1()
                    UpgradeSound.play()
                if clickedBox(294,292,336,339,mousePos)==True and Player1.UpgR>=1:
                    Player1.Upgrade2()
                    UpgradeSound.play()
                if clickedBox(220,434,400,480,mousePos)==True and Player1.UpgR>=1:
                    Player1.Upgrade3()
                    UpgradeSound.play()
                if clickedBox(220,578,400,620,mousePos)==True and Player1.UpgR>=1:
                    Player1.Upgrade4()
                    UpgradeSound.play()
                if clickedBox(1029,604,1231,684,mousePos)==True:
                    updateWin(2)
                    run3=False
        drawUpElements()
def updateWin(Lvl):
    global midIncomeActive
    global TempIncome
    global run2
    global TempMana
    global TempExp
    global MeteormodX
    global MeteormodY
    tempIncomeText = font.render('+'+str(format(TempIncome-1,'.0%')),1,(255,223,0))
    tempManaText = font.render('+'+str(format(TempMana-1,'.0%')),1,(0,102,224))
    tempExpText = font.render('+'+str(format(TempExp-1,'.0%')),1,(225,153,51))
    Base1x = -300
    Base1y = 517
    Base2x = 1050
    Base2y = 490
    InterfaceX = 60
    InterfaceY = 15
    text7 = font.render(str('Power:   '+format(MajorasMask.Power,'.0f') + '/2000'),1,(138,43,226))
    AI1.Tower = AITowerLvlList[Lvl]
    if Lvl==2:
        win.blit(backGround2,(0,100))
    elif Lvl==3:
        win.blit(backGround3,(0,0))
    elif Lvl==1:
        win.blit(backGround1,(0,0))
    elif Lvl ==4:
        win.blit(backGround4,(0,100))
        win.blit(Interface[23],(1100,140))
    elif Lvl == 5:
    	win.blit(backGround5,(0,100))
    elif Lvl == 6:
    	win.blit(backGround6,(0,0))
    elif Lvl ==Boss2Lvl and BossSwitch ==0:
    	win.blit(backGround7,(0,100))
    	MajorasMask.draw(win,0)
    	win.blit(text7, (1010,300))
    elif Lvl == Boss2Lvl and BossSwitch == 1:
        win.blit(backGround8,(0,100))
        MajorasMask.draw(win,1)
        win.blit(text7, (1010,300))
    else:
        win.blit(backGround1,(0,0))
    win.blit(PlayerBase,(Base1x,Base1y))
    win.blit(AIBase,(Base2x,Base2y))
    if Player1.Tower ==1:
        win.blit(Player1.racelist[9],(2,528))
    if AI1.Tower == 1:
    	win.blit(Player1.racelist[9],(1100,528))
    if Player1.Meteor ==True:
        pygame.draw.circle(win,(255,0,0),(mousePos[0],mousePos[1]),30,5)
    win.blit(TopFrame,(0,0))
    win.blit(Interface[25],(5,220))
    win.blit(Interface[24],(5,320))
    win.blit(Interface[0],(InterfaceX,InterfaceY))
    win.blit(Interface[1],(InterfaceX+140,InterfaceY))
    win.blit(Interface[2],(InterfaceX+280,InterfaceY))
    win.blit(Interface[3],(InterfaceX+420,InterfaceY))
    win.blit(Interface[4],(InterfaceX+680,InterfaceY))
    win.blit(Interface[5],(InterfaceX+820,InterfaceY))
    if Player1.race =='Orc' and Player1.Tier==1:
        win.blit(Interface[13],(0,0))
    elif Player1.race =='Human' and Player1.Tier==1:
        win.blit(Interface[14],(0,0))
    elif Player1.race=='Undead' and Player1.Tier==1:
        win.blit(Interface[15],(0,0))
    elif Player1.race=='Orc' and Player1.Tier==2:
        win.blit(Interface[16],(0,0))
    elif Player1.race=='Human' and Player1.Tier==2:
        win.blit(Interface[17],(0,0))
    elif Player1.race=='Undead' and Player1.Tier==2:
        win.blit(Interface[18],(0,0))
    elif Player1.race=='Orc' and Player1.Tier==3:
        win.blit(Interface[19],(0,0))
    elif Player1.race=='Human' and Player1.Tier==3:
        win.blit(Interface[20],(0,0))
    elif Player1.race=='Undead' and Player1.Tier==3:
        win.blit(Interface[21],(0,0))
    win.blit(text,(25,150))
    if Player1.Tier == 3 and Player1.DragonHatchery == 0:
    	win.blit(Interface[41],(402,26))
    HPtxt = font.render(str(format(Player1.BaseHP,'.0f')),1,(0,255,0))
    AIHPtxt = font.render(str(format(AI1.BaseHP,'.0f')),1,(0,255,0))
    text2 = font.render(str(format(Player1.Resources,'.2f')),1,(255,223,0))
    text3 = font.render(str(format(Player1.Mana,'.2f')),1,(0,102,224))
    text4 = font.render(str(format(Player1.Exp,'.2f')),1,(225,153,51))
    win.blit(PlayerBaseHPtxt,(8,475))
    win.blit(PlayerBaseHPtxt,(1146,475))
    win.blit(HPtxt,(52,475))
    win.blit(AIHPtxt,(1190,475))
    win.blit(text2,(155,150))
    win.blit(text3,(160,170))
    win.blit(text4,(160,190))
    win.blit(Manatxt,(25,170))
    win.blit(Exptxt,(25,190))
    win.blit(tempIncomeText,(240,150))
    win.blit(tempManaText,(240,170))
    win.blit(tempExpText,(240,190))
    xmod = 0
    ymod = 0
    upgradeCounter = 0
    if AI1.Tower == 1:
    	win.blit(Interface[40],(1280-TowerRange,622))
    if Player1.Tower == 1:
    	win.blit(Interface[40],(TowerRange,622))
    if midIncomeActive == True:
        win.blit(Interface[35],(609,622))
        MajorasMask.PowerIncreasing = False
        if BossSwitch == 1:
        	MajorasMask.Power -=.5
    elif midIncomeActive != True and Lvl != Boss2Lvl:
        win.blit(Interface[36],(609,622))
    elif midIncomeActive != True and Lvl == Boss2Lvl:
        win.blit(Interface[37],(609,622))
        MajorasMask.Power += 1
        MajorasMask.PowerIncreasing = True
    for i in Buildings:
        if i != 0:
            i.draw(win)
    for i in Player1.upgradeInterfaceList:
    	if upgradeCounter == 3:
    		xmod -=240
    		ymod +=50
    	if i == 1:
    		win.blit(Interface[30], (860 + xmod ,25+ ymod))
    	xmod += 80
    	upgradeCounter += 1
    	if i == 2:
    		win.blit(Interface[30],(1136,60))
    for i in Player1.UnitList:
        AI1.BaseHP = i.move(AIList,2,AI1.BaseHP)
        if i.x > 609 and midIncomeActive != True:
            TempIncome += .30
            midIncomeActive = True
        i.draw(win)

    for i in AIList:
    	if i.x < 609 and midIncomeActive == True:
    		midIncomeActive = False
    		MajorasMask.Power += 0
    		TempIncome -= .30
    	i.draw(win)
    	Player1.BaseHP = i.move(Player1.UnitList,1,Player1.BaseHP)
    	if i.attRange == 400:
    		MeteormodX = +50
    		MeteormodY = +100
    		
    	if Player1.Meteor == True:
    		pygame.draw.circle(win,(255,0,0),(round(i.x)+15 + MeteormodX,round(i.y)+5 + MeteormodY),5,5)
    	MeteormodX = 0
    	MeteormodY = 0
    pygame.display.update()
    if Player1.BaseHP <=0:
        AI1Wins()
    if AI1.BaseHP <=0:
        Player1Wins()
    if run2==False:
        while len(AIList) != 0:  
            for i in AIList:
                AIList.remove(i)
        while len(Player1.UnitList) != 0:
            for i in Player1.UnitList:
                Player1.UnitList.remove(i)
def DrawRaceMenu():
    run4=True
    win.blit(Interface[9],(0,0))
    pygame.display.update()
    while run4 == True:
        clock.tick(27)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                
                if clickedBox(19,105,376,677,mousePos)==True:
                    Player1.raceChange('Human')
                    Player1.racelist = HumanRace
                    updateWin(1)
                    run4=False
                if clickedBox(396,103,839,522,mousePos)==True:
                    Player1.raceChange('Orc')
                    Player1.racelist = OrcRace
                    updateWin(1)
                    run4=False
                if clickedBox(875,105,1245,520,mousePos)==True:
                    Player1.raceChange('Undead')
                    Player1.racelist = UndeadRace
                    updateWin(1)
                    run4=False 
global run
run = True
diffscrn = False
Tutscrn = False
TutCounter = 0
#Main Menu screen
DrawMenu()
while run == True:
    clock.tick(27)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            
            if clickedBox(500,220,750,320,mousePos) == True and diffscrn != True and Tutscrn == False:
                run = True
                diffscrn = True
                win.blit(DifBG,(0,0))
            elif clickedBox(500,401,845,498,mousePos) == True and diffscrn != True:
                Tutscrn = True
                win.blit(Interface[26],(0,0))
                TutCounter +=1
            elif clickedBox(115,190,448,470,mousePos) == True and diffscrn == True and Tutscrn == False:
                run=False
                Player1.Diff = .9
                DrawRaceMenu()
            elif clickedBox(491,190,790,470,mousePos) == True and diffscrn == True and Tutscrn == False:
                run=False
                Player1.Diff = 1
                DrawRaceMenu()
            elif clickedBox(840,190,1140,470,mousePos) == True and diffscrn == True and Tutscrn == False:
                run=False
                Player1.Diff = 1.2
                DrawRaceMenu()
            if clickedBox(1092,619,1245,695,mousePos)==True and Tutscrn == True and TutCounter ==1:
                win.blit(Interface[27],(0,0))
                TutCounter +=1
            elif clickedBox(1092,619,1245,695,mousePos)==True and Tutscrn == True and TutCounter ==2:
                win.blit(Interface[33],(0,0))
                TutCounter +=1
            elif clickedBox(1092,619,1245,695,mousePos)==True and Tutscrn == True and TutCounter ==3:
                win.blit(Interface[38],(0,0))
                TutCounter +=1
            elif clickedBox(1092,619,1245,695,mousePos)==True and Tutscrn == True and TutCounter ==4:
                win.blit(Interface[28],(0,0))
                TutCounter +=1
            elif clickedBox(1092,619,1245,695,mousePos)==True and Tutscrn == True and TutCounter ==5:
                win.blit(Interface[29],(0,0))
                TutCounter +=1
            elif clickedBox(1092,619,1245,695,mousePos)==True and Tutscrn == True and TutCounter ==6:
                win.blit(Interface[34],(0,0))
                TutCounter +=1
            elif clickedBox(1092,619,1245,695,mousePos)==True and Tutscrn == True and TutCounter ==7:
                run = True
                diffscrn = False
                Tutscrn = False
                TutCounter = 0
                #Main Menu screen
                DrawMenu()
                
                
                
            
    pygame.time.delay(30)
    pygame.display.update()

TempExp=1
TempAtt=1
TempMana=1
TempIncome=1
TempHP=1
TempExpSpell=1
TempMeteorSpell=1
xtime = 65000
global k
global k2
global AIUnitSpawnY
global newTimeList
newTimeList = []
global newUnitList
newUnitList = []
global newAmountList
newAimeList = []
AIUnitSpawnY=610
k2=1
k=1
def clickedUnit(UnitImage,hitpoints,attRange,Dmg,resources,Vel): #Need to add more arguements to mod hp/dmg
    global k
    p=0
    spawnY = 620
    p = ['Unit',i]
    p = map(str,p)
    name = ''.join(p)
    if UnitImage == PDragon1 and Player1.Tier == 3:
    	spawnY -= 80
    	hitpoints = hitpoints/(Player1.HPmod*TempHP)
    Player1.UnitList.append(Unit(name,100,spawnY,hitpoints*Player1.HPmod*TempHP,attRange\
                         ,1*Player1.VELmod*Vel,UnitImage,Dmg*Player1.ATTmod*TempAtt))
    Player1.Resources -= resources
    k +=1
def AIUnit(UnitImage,hitpoints,attRange,Dmg,Vel,UnitX,UnitY): #Need to add more arguements to mod hp/dmg
    global k2
    global AIUnitSpawnY
    p=0
    p = ['Unit',i]
    p = map(str,p)
    name = ''.join(p)
    AIList.append(Unit(name,UnitX,UnitY,hitpoints*Player1.Diff,attRange,-1*Vel,UnitImage,Dmg*Player1.Diff))
    k2 +=1
def AISpawn(x,Unit,hitpoints,attRange,Dmg,Vel,UnitX,UnitY):
    global timeTicked
    global TrackTime
    global unitStopper
    unitCaptureVariable = 9
    if timeTicked == 20:
    	unitCaptureVariable = 13
    if timeTicked == 100:
    	unitCaptureVariable = 50
    if (TrackTime *timeTicked/100 >=x and TrackTime * timeTicked/100 <= x+unitCaptureVariable\
    and not((TrackTime*timeTicked/100 >= unitStopper and TrackTime*timeTicked/100 <= unitStopper + 50))):
    	AIUnit(Unit,hitpoints,attRange,Dmg,Vel,UnitX,UnitY)
    	unitStopper = TrackTime*timeTicked/100

if random.randint(0,10)>=5:
    Build1=True
else:
    Build2=True
#Unit Stats

DiffCounter = 0
DiffListCounter = 0
for i in DifficultyListModifier:
	for i in DifficultyListModifier[DiffListCounter]:
		if Player1.Diff == .9:
			continue
		elif Player1.Diff == 1:
			DifficultyListModifier[DiffListCounter][DiffCounter] += 1
			DiffCounter += 1
		elif Player1.Diff == 1.2:
			DifficultyListModifier[DiffListCounter][DiffCounter] += 2
			DiffCounter += 1
	
	DiffListCounter +=1
	DiffCounter = 0
global repeatCounter
repeatCounter = 5
def spawnRepeat(timeList,UnitList,amountList):
	global timeTicked
	global TrackTime
	global newTimeList
	global newUnitList
	global newAmountList
	global repeatCounter
	if len(newTimeList) == 0:
		repeatCounter=5
		newTimeList = timeList[:]
		newUnitList = UnitList[:]
		newAmountList = amountList[:]
	x = amountList[len(amountList)-1] *150 + 1000
	tempTimeVariable = timeList[len(timeList)-1]
	if timeList[len(timeList)-1] + x <= TrackTime * timeTicked/100:
		for i in newTimeList:
			timeList.append(i+tempTimeVariable)
		for i in newUnitList:
			UnitList.append(i)
		for i in newAmountList:
			amountList.append(i+repeatCounter)
		repeatCounter += 5 
def spawning(time, unit, amount):
	global timeTicked
	global TrackTime
	modTime = 150
	
	for i in range(len(time)):
		AISpawn(time[i],unit[i].image,unit[i].hitpoints,unit[i].attRange,unit[i].Dmg,unit[i].vel,unit[i].x,unit[i].y)
		localTimeVariable = time[i]
		if amount[i] != 0 and time[i] < TrackTime * timeTicked/100:
			for e in range(amount[i]-1):
				time.insert(i + e, localTimeVariable + modTime)
				modTime += 150
				unit.insert(i + e, unit[i])
				amount[i] = 0
				amount.insert(i + e,0)


global tempMusic
tempMusic=0
def Boss1Intro(Lvl):
    updateWin(Lvl)
    win.blit(BlackBorder,(0,0))
    win.blit(BlackBorder,(0,600))
    win.blit(Interface[22],(480,190))
    BossTxt = font.render('You will feel the power of my POKEMON!',2,(255,0,0))
    win.blit(BossTxt,(400,650))
    BossTxt2 = font.render('BOSS:Rival',2,(255,0,0))
    win.blit(BossTxt2,(550,50))
    pygame.display.update()
    pygame.time.delay(5000)
def Boss2Intro(Lvl):
    updateWin(Lvl)
    win.blit(BlackBorder,(0,0))
    win.blit(BlackBorder,(0,600))
    win.blit(Interface[31],(450,190))
    BossTxt = font.render('..........................................',2,(248,0,211))
    win.blit(BossTxt,(440,650))
    BossTxt2 = font.render('BOSS: Majoras Mask',2,(148,0,211))
    MajorasAwakeningSoundEffect.play()
    win.blit(BossTxt2,(490,70))
    pygame.display.update()
    pygame.time.delay(5000) 
def Boss2Intro2(Lvl):
    global tempMusic
    moverx = 0
    e = 0
    pygame.mixer.music.stop()
    win.blit(Interface[31],(450,190))
    pygame.display.update()
    pygame.mixer.Channel(5).play(clashSound)
    pygame.time.delay(2500)
    pygame.mixer.Channel(5).play(MajorasScreamSoundEffect)
    for i in range(60):
    	if i % 2 == 0:
    		win.blit(backGroundList[e],(0,0))
    		win.blit(Interface[31],(450+moverx,190))
    		pygame.time.delay(40)
    		moverx += 40
    		pygame.display.update()
    	else:
    		win.blit(backGroundList[e],(0,0))
    		win.blit(Interface[31],(450+moverx,190))
    		pygame.time.delay(40)
    		moverx -=40
    		pygame.display.update()
    	e+= 1
    	if e >= 14:
    		e = 0
    boomSound.play()
    pygame.time.delay(700)
    tempMusic=0
run2 = True
global TrackTime
TrackTime=0
#Starting Lvl
Lvl = 1
#Main runtime
while run2 == True:
        clock.tick(timeTicked)
        mousePos = pygame.mouse.get_pos()
        TrackTime += clock.get_time()
        if tempMusic ==0:
            if Lvl ==1:
                lM('Lvl1Track.mp3','Music')
                pygame.mixer.music.play(-1)
                tempMusic =1
            elif Lvl ==2:
                lM('Lvl2Track.mp3','Music')
                pygame.mixer.music.play(-1)
                tempMusic = 1
            elif Lvl ==3:
                lM('Lvl3Track.mp3','Music')
                pygame.mixer.music.play(-1)
                tempMusic = 1
            elif Lvl ==4:
                lM('Lvl4Track.mp3','Music')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(.4)
                tempMusic = 1
            elif Lvl ==5:
                lM('Lvl5Track.mp3','Music')
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(-1)
                tempMusic = 1
            elif Lvl ==6:
                lM('Lvl6Track.mp3','Music')
                pygame.mixer.music.play(-1)
                tempMusic = 1
            elif Lvl == Boss2Lvl and BossSwitch==0:
                lM('Boss2Track.mp3','Music')
                pygame.mixer.music.play(-1)
                tempMusic = 1
            elif Lvl == Boss2Lvl and BossSwitch==1:
                lM('Boss2Track2.wav','Music')
                pygame.mixer.music.play(-1)
                tempMusic=1
        Player1.Resources+=(.9*((Player1.INCOMEmod-1)+TempIncome)) #orginally .7
        Player1.Mana+=(1*((Player1.MANAmod-1)+TempMana))
        Player1.Exp+=(.5*((Player1.EXPmod-1)+TempExp))
        if Player1.Tier ==1:
            UnitImage = Player1.Unit1
            Player1.Unit1 = Player1.racelist[0]
            Player1.Unit2 = Player1.racelist[1]
            Player1.Unit3 = Player1.racelist[2]
            Player1.Unit5 = Player1.racelist[9]
        elif Player1.Tier ==2:
            Player1.Unit1 = Player1.racelist[3]
            Player1.Unit2 = Player1.racelist[4]
            Player1.Unit3 = Player1.racelist[5]
            Player1.Unit5 = Player1.racelist[9]
        elif Player1.Tier ==3:
            Player1.Unit1 = Player1.racelist[6]
            Player1.Unit2 = Player1.racelist[7]
            Player1.Unit3 = Player1.racelist[8]
            Player1.Unit5 = Player1.racelist[9]
            Player1.Unit4 = PDragon1
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN or i.type == pygame.KEYDOWN:
                mousePos = pygame.mouse.get_pos()
                
                if (i.type == pygame.KEYDOWN and i.key == K_r) == True and i.mod and pygame.KMOD_LSHIFT == True:
                    run2=False
                if (clickedBox(107,37,178,125,mousePos) == True or (i.type == pygame.KEYDOWN and i.key == K_1)) == True and Player1.Resources >=50:
                    clickedUnit(Player1.Unit1,Dwarf1Hp,Dwarf1R,Dwarf1Att,50,3.5)
                    
                if (clickedBox(214,44,277,123,mousePos) == True or (i.type == pygame.KEYDOWN and i.key == K_2)) == True and Player1.Resources >=75:
                    clickedUnit(Player1.Unit2,Dwarf2Hp,Dwarf2R,Dwarf2Att,75,3)
                    
                if (clickedBox(314,33,380,120,mousePos) == True or (i.type == pygame.KEYDOWN and i.key == K_3)) == True and Player1.Resources >=150:
                    clickedUnit(Player1.Unit3,Dwarf3Hp,Dwarf3R,Dwarf3Att,150,1.5)
                if clickedBox(414,41,480,120,mousePos) == True and Player1.Resources >=500 and Player1.Tier ==3 and Player1.DragonHatchery ==1:
                   clickedUnit(Player1.Unit4,Dragon1Hp,Dragon1R,Dragon1Att,500,Dragon1Speed)
                if clickedBox(537,41,637,120,mousePos) == True and Player1.Resources >=300 and Player1.Tower !=1:
                    Player1.Tower=1
                    Player1.Resources -= 300
                if clickedBox(872,36,916,73,mousePos)==True and Player1.Resources >=250 and Player1.upgradeInterfaceList[0] != 1:
                    TempMana += .20
                    Player1.Resources -= 250
                    Player1.upgradeInterfaceList[0] = 1
                    Fountain.upgrade(Buildings,1)
                    fountainSoundEffect.play()
                if clickedBox(947,34,987,72,mousePos)==True and Player1.Resources>=250 and Player1.upgradeInterfaceList[1] != 1:
                    TempAtt += .10
                    Player1.Resources -= 250
                    Player1.upgradeInterfaceList[1] = 1
                    if Player1.upgradeInterfaceList[4] == 1:
                        Barracks.upgrade(Buildings,2)
                        barracksSoundEffect.play()
                if clickedBox(1024,34,1066,74,mousePos)==True and Player1.Resources>=250 and Player1.upgradeInterfaceList[2] != 1:
                    TempMeteorSpell+=.10
                    Player1.Resources -= 250
                    Player1.upgradeInterfaceList[2] = 1
                if clickedBox(872,93,917,126,mousePos)==True and Player1.Resources>=250 and Player1.upgradeInterfaceList[3] != 1:
                    TempIncome +=.20
                    Player1.Resources -= 250
                    Player1.upgradeInterfaceList[3] = 1
                    GoldMine.upgrade(Buildings,0)
                    goldMineSoundEffect.play()
                if clickedBox(950,93,985,126,mousePos)==True and Player1.Resources>=250 and Player1.upgradeInterfaceList[4] != 1:
                    TempHP += .10
                    Player1.Resources -= 250
                    Player1.upgradeInterfaceList[4] = 1
                    if Player1.upgradeInterfaceList[1] == 1:
                        Barracks.upgrade(Buildings,2)
                        barracksSoundEffect.play()
                if clickedBox(1024,89,1067,126,mousePos)==True and Player1.Resources>=250 and Player1.upgradeInterfaceList[5] != 1:
                    TempExp+=.10
                    Player1.Resources -= 250
                    Player1.upgradeInterfaceList[5] = 1
                if clickedBox(1124,48,1215,114,mousePos)==True and Player1.Exp>=1000 and Player1.Tier != 3:
                    Player1.Tier +=1
                    TempHP += .20
                    TempAtt += .20
                    tierMod += .05
                    Player1.Exp -= 1000
                    resetUpgradeCounter=0
                    for k in Player1.upgradeInterfaceList:
                    	Player1.upgradeInterfaceList[resetUpgradeCounter] = 0
                    	resetUpgradeCounter+=1
                    UpgradeSound.play()
                if clickedBox(1124,48,1215,114,mousePos)==True and Player1.Exp>=2000 and Player1.Tier == 3 and Player1.DragonHatchery !=1:
                	Player1.DragonHatchery = 1
                	Player1.Exp -= 2000
                	Player1.upgradeInterfaceList[6] = 2
                	dragonHatcherySoundEffect.play()
                if (clickedBox(10,245,79,306,mousePos)==True or (i.type == pygame.KEYDOWN and i.key == K_q)) == True and Player1.Mana>=250:
                    Player1.Mana -=250
                    Player1.Exp += 100*TempExpSpell
                if Player1.Meteor ==True:
                    MeteorSound.play()
                    for a in AIList:
                    	if a.attRange == 400:
                    		MeteormodX = 50
                    		MeteormodY = 100
                    	if a.x +15+ MeteormodX >= mousePos[0]-30  and a.x +15+ MeteormodX<=mousePos[0]+30 \
                    	and a.y+5 + MeteormodY >= mousePos[1]-30 and a.y+5 +MeteormodY<=mousePos[1]+30 :
                            a.hitpoints-=1000*TempMeteorSpell
                            if a.hitpoints <=0:
                                AIList.remove(a)
                                break
                            MeteormodX = 0
                            MeteormodY = 0
                    Player1.Meteor=False
                if (clickedBox(12,332,86,403,mousePos)==True or (i.type == pygame.KEYDOWN and i.key == K_w)) == True and Player1.Mana>=250:
                    Player1.Meteor = True
                    Player1.Mana-=250
        if keys[pygame.K_LEFT]== True and Player1.Mana >= 300:
            Player1.Exp += 100
        if keys[pygame.K_RIGHT]== True and Player1.Mana>=250:
        	continue
        if Player1.Tower == 1:
            for i in AIList:
                if TowerRange >= i.x:
                    i.hitpoints -= (TowerDmg)
                    random.choice(HitSounds).play()
                    if i.hitpoints <=0:
                        AIList.remove(i)
                        pygame.mixer.Channel(1).play(random.choice(deathSounds))
                    
                    break
        if AI1.Tower == 1:
        	for i in Player1.UnitList:
        		if TowerRange+ 450 <= i.x:
        			if Lvl == Boss2Lvl and BossSwitch == 1:
        				i.hitpoints -= ((TowerDmg + 12) * Player1.Diff)/(Player1.TowerDmgMod)
        				random.choice(HitSounds).play()
        				
        			else:
	        			i.hitpoints -= ((TowerDmg +6) *Player1.Diff)/(Player1.TowerDmgMod)
	        			random.choice(HitSounds).play()
	        			
        			if i.hitpoints <= 0:
        				Player1.UnitList.remove(i)
        				pygame.mixer.Channel(1).play(random.choice(deathSounds))
        			break
        if Lvl==1:
            spawning(lvl1timeSpawnList,lvl1unitSpawnList,lvl1amountSpawnList)
            spawnRepeat(lvl1timeSpawnList,lvl1unitSpawnList,lvl1amountSpawnList)        
        if Lvl ==2:
            spawning(lvl2timeSpawnList,lvl2unitSpawnList,lvl2amountSpawnList)
            spawnRepeat(lvl2timeSpawnList,lvl2unitSpawnList,lvl2amountSpawnList)
        if Lvl == 3:
            spawning(lvl3timeSpawnList,lvl3unitSpawnList,lvl3amountSpawnList)
            spawnRepeat(lvl3timeSpawnList,lvl3unitSpawnList,lvl3amountSpawnList)
        if Lvl ==4:
            if Intro ==0:
                Boss1Intro(Lvl)
                Intro = 1
            spawning(lvl4timeSpawnList,lvl4unitSpawnList,lvl4amountSpawnList)
            spawnRepeat(lvl4timeSpawnList,lvl4unitSpawnList,lvl4amountSpawnList)
        if Lvl ==5:
        	spawning(lvl5timeSpawnList,lvl5unitSpawnList,lvl5amountSpawnList)
        	spawnRepeat(lvl5timeSpawnList,lvl5unitSpawnList,lvl5amountSpawnList)
        if Lvl ==6:
        	spawning(lvl6timeSpawnList,lvl6unitSpawnList,lvl6amountSpawnList)
        	spawnRepeat(lvl6timeSpawnList,lvl6unitSpawnList,lvl6amountSpawnList)
        if Lvl == 7:
            if Intro ==0:
                Boss2Intro(Lvl)
                Intro = 1
            if BossSwitch != 1:
            	spawning(Boss2Phase1timeSpawnList,Boss2Phase1unitSpawnList,Boss2Phase1amountSpawnList)
            	spawnRepeat(Boss2Phase1timeSpawnList,Boss2Phase1unitSpawnList,Boss2Phase1amountSpawnList)
            if BossSwitch == 1 or MajorasMask.Power >= 2000:
                BossSwitch = 1
                if Intro2 == 0:
                    Boss2Intro2(Lvl)
                    TrackTime = 0
                    newTimeList = []
                    newUnitList = []
                    newAmountList = []
                    MajorasMask.Power = 0
                Intro2=1
                spawning(Boss2Phase2timeSpawnList,Boss2Phase2unitSpawnList,Boss2Phase2amountSpawnList)
                spawnRepeat(Boss2Phase2timeSpawnList,Boss2Phase2unitSpawnList,Boss2Phase2amountSpawnList)
                Player1.BaseHP = MajorasMask.castSpell(Player1.UnitList,round(TrackTime * timeTicked/100), MajorasScreamSoundEffect, boomSound,Player1.BaseHP)
                
        if Lvl != 8:   
            updateWin(Lvl)
        #Reset for next lvl
        if run2==False and Player1.win == 1:
            Player1.Tier = 1
            TempExp=1
            TempAtt=1
            BossSwitch=0
            MajorasMask.Power= 0
            midIncomeActive = False
            for i in Buildings:
                if i != 0:
                    i.primary = 0
            Buildings = [0,0,0]
            TempMana=1
            TempIncome=1
            Intro = 0
            TempHP=1
            TempExpSpell=1
            newTimeList = []
            newAmountList = []
            newUnitList = []
            TempMeteorSpell=1
            Player1.DragonHatchery = 0
            tempMusic = 0
            repeatCounter = 3
            Player1.Tower=0
            resetUpgradeCounter=0
            for i in Player1.upgradeInterfaceList:
            	Player1.upgradeInterfaceList[resetUpgradeCounter] = 0
            	resetUpgradeCounter+=1
            Lvl +=1
            Player1.UpgR += 1
            TrackTime = 0
            for i in AIList:
                AIList.remove(i)
            for i in Player1.UnitList:
                Player1.UnitList.remove(i)
            Player1.BaseHP =1000
            Player1.Resources = Player1.StartR
            Player1.Mana = 100
            Player1.Exp = 100
            AI1.BaseHP =1000
            if Lvl != 8:
                DrawUpMenu()
            pygame.display.update()
            Player1.win = 0
            pygame.mixer.music.stop()
            run2=True
            if Lvl == 8:
                victorySoundEffect.play()
                run2 = False
                DrawVictoryScreen()
                pygame.display.update()
        elif run2==False:
            for i in AIList:
                AIList.remove(i)
            for i in Player1.UnitList:
                Player1.UnitList.remove(i)
            Player1.Tier = 1
            for i in Buildings:
                if i != 0:
                    i.primary = 0
            Buildings = [0,0,0]
            Player1.Tower = 0
            tempMusic=0
            Player1.win = 0
            MajorasMask.Power= 0
            TempExp=1
            midIncomeActive = False
            TempAtt=1
            BossSwitch=0
            Player1.DragonHatchery = 0
            resetUpgradeCounter=0
            for i in Player1.upgradeInterfaceList:
                Player1.upgradeInterfaceList[resetUpgradeCounter] = 0
                resetUpgradeCounter+=1
            TempMana=1
            Intro=0
            Intro2=0
            TempIncome=1
            TempHP=1
            repeatCounter = 3
            Player1.BaseHP =1000
            Player1.Resources = Player1.StartR
            Player1.Mana = 100
            newTimeList = []
            newUnitList = []
            newAmountList =[]
            Player1.Exp = 100
            TrackTime = 0
            pygame.mixer.music.stop()
            AI1.BaseHP =1000
            DrawUpMenu()
            pygame.display.update()
            run2 = True