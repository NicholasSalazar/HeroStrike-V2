class Player():
    def __init__(self,StartR,Upg1Lvl,Upg2Lvl,Upg3Lvl,Upg4Lvl,Difficulty,BaseHP,UpgR,racelist):
        self.StartR = StartR
        self.Upg1Lvl = Upg1Lvl
        self.Upg2Lvl = Upg2Lvl
        self.Upg3Lvl = Upg3Lvl
        self.Upg4Lvl = Upg4Lvl
        self.Diff = Difficulty
        self.Resources = StartR
        self.BaseHP = BaseHP
        self.UpgR=UpgR
        self.HPmod = 1
        self.ATTmod = 1
        self.MANAmod = 1
        self.EXPmod = 1
        self.VELmod = 1
        self.Meteor = False
        self.INCOMEmod = 1
        self.Unit1=racelist[0]
        self.Unit2=racelist[1]
        self.Unit3=racelist[2]
        self.Mana = 0
        self.Exp = 0
        self.race = 'Human'
        self.Tier = 1
        self.win = 0
        self.TowerDmgMod = 1 #originally 1
        self.upgradeInterfaceList = [0,0,0,0,0,0,0]
        self.racelist = racelist
        self.Tower = 0
        self.UnitList = []
        self.DragonHatchery = 0

    def Upgrade1(self):
        if self.Upg1Lvl <3:
            self.Upg1Lvl +=1
            self.HPmod +=.05
            self.ATTmod +=.05
            self.UpgR-=1
        else:
            print("At MAX")
    def Upgrade2(self):
        if self.Upg2Lvl <3:
            self.Upg2Lvl +=1
            self.INCOMEmod +=.05
            self.UpgR-=1
        else:
            print('AT MAX')
    def Upgrade3(self):
        if self.Upg3Lvl <3:
            self.Upg3Lvl +=1
            self.MANAmod +=.05
            self.UpgR-=1
        else:
            print('AT MAX')
    def Upgrade4(self):
        if self.Upg4Lvl <3:            
            self.Upg4Lvl +=1
            self.EXPmod +=.10
            self.UpgR-=1
        else:
            print('At MAx')
    def raceChange(self,race):
        if race == 'Human':
            self.race = 'Human'
            self.StartR +=100
            self.INCOMEmod = 1.10
            self.HPmod = 1.10
        elif race == 'Orc':
            self.Unit1=self.racelist[0]
            self.Unit2=self.racelist[1]
            self.Unit3=self.racelist[2]
            self.race = 'Orc'
            self.HPmod = 1.05
            self.ATTmod = 1.20
            self.racelist = self.racelist
            self.TowerDmgMod += 0.2

        elif race == 'Undead':
            self.Unit1=self.racelist[0]
            self.Unit2=self.racelist[1]
            self.Unit3=self.racelist[2]
            self.race = 'Undead'
            self.VELmod = 1.10
            self.EXPmod = 1.10
            self.MANAmod = 1.10
            self.racelist = self.racelist
def DrawVictoryScreen():
    run5 = True
    while run5 == True:
        
        clock.tick(27)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        win.blit(VictoryScreen,(0,0))
        if Player1.Diff == .9:
            win.blit(victoryText[0],(450,350))
        if Player1.Diff == 1:
            win.blit(victoryText[1],(450,350))
        if Player1.Diff == 1.2:
            win.blit(victoryText[2],(450,350))
        pygame.display.update()
def drawUpElements():
    font = pygame.font.SysFont('comicsans',30,True)
    uptext1 = font.render(str(Player1.Upg1Lvl),2,(0,255,0))
    uptext2 = font.render(str(Player1.Upg2Lvl),2,(0,255,0))
    uptext3 = font.render(str(Player1.Upg3Lvl),2,(0,255,0))
    uptext4 = font.render(str(Player1.Upg4Lvl),2,(0,255,0))
    uptext5 = font.render(str(Player1.UpgR),2,(255,0,0))
    win.blit(uptext1,(808,160))
    win.blit(uptext2,(808,321))
    win.blit(uptext3,(808,473))
    win.blit(uptext4,(808,598))
    win.blit(uptext5,(835,70))
    pygame.display.update()


