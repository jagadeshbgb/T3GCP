#import tkinter
import tkinter as tk
import turtle as te
import time
import sys
#(psolved)problem is to write code for game functionality
################################################################################
class T3GameLogic:
    def __init__(self,value):
        #pass
        self.value = value
        print(self.value,"value")
        return
    def fixedpositions(self):
        #[(-200,200),(100,200),(100,-100),(-200,-100)]
        fixedPositions = [(-200,200),(100,200),(100,-100),(-200,-100)]
        for position in fixedpositions:
            print("position",position)
        return
    '''
    def X(self,xValue):
        self.xValue = xValue
        return
    '''
    '''
#problem is to write below function
#################################################
    def next(self,value):
        print(self.value,"value")
        return
    '''
        
#(solved: given new method returned to another method)problem is to get return value from lambda function   
class T3Game:
    #T3GL = T3GameLogic()
    playersDict = {"player1":None,"player2":None}
    labels = {"player1":[],"player2":[]}
    countL = 0
    countP2 = 0
    countP1 = None
    pTCount =1
    mPTSC = None
    PlayerWinner1 = {"condition":False,"value":None}
    PlayerWinner2 = {"condition":False,"value":None}
    GameOver = False
    pTB1 = {"condition":True,"value":None}
    pTB2 = {"condition":True,"value":None}
    pTB3 = {"condition":True,"value":None}
    pTB4 = {"condition":True,"value":None}
    pTB5 = {"condition":True,"value":None}
    pTB6 = {"condition":True,"value":None}
    pTB7 = {"condition":True,"value":None}
    pTB8 = {"condition":True,"value":None}
    pTB9 = {"condition":True,"value":None}
    Screen =[]
    print(playersDict.get("player1"),"player1 key values")
    def __init__(self,T3GL):
        #pass
        self.T3GL = T3GL
        print(self.T3GL,"T3GL")
        
    #new frame
    def window(self,frame=None):
        cF = tk.Frame(frame)
        #cF.pack(fill="both",expand=True)
        print("cF",cF)
        return cF
    

    #label creation
    def label(self,element=None,text=None):
        self.element = element
        self.text = text
        createLabel = tk.Label(self.element,text=self.text)
        print(createLabel,"createLabel")
        createLabel.pack(fill="both",expand = True)
        return createLabel

    #button creation
    def button(self,element=None,text=None,command=None,frame=None):
        #print(command,"command")
        self.element = element
        self.text = text
        self.command = command
        createButton = tk.Button(self.element,text=self.text,command=self.command,frame=None)
        createButton.pack(fill="both",expand=True)
        return createButton   

    #button command
    def newGame(self,frame1=None,frame2=None):
        print("frame1",frame1)
        frame1.pack_forget()
        frame2.pack(fill="both",expand=True)
        #print(self.window(frame))
        #frame.pack_forget()
        #print("playGame")
        #cF = tk.Frame(frame)
        #cF = cF.pack(fill="both",expand=True)
        '''
        self.playersDict = {"player1":None,"player2":None}
        self.labels = {"player1":[],"player2":[]}
        self.countL = 0
        self.countP2 = 0
        self.countP1 = None
        '''
        #######################
        T3G.playersDict = {"player1":None,"player2":None}
        T3G.labels = {"player1":[],"player2":[]}
        T3G.countL = 0
        T3G.countP2 = 0
        T3G.countP1 = None
        T3G.pTCount =1
        T3G.mPTSC = None
        T3G.PlayerWinner1 = {"condition":False,"value":None}
        T3G.PlayerWinner2 = {"condition":False,"value":None}
        T3G.GameOver = False
        T3G.pTB1 = {"condition":True,"value":None}
        T3G.pTB2 = {"condition":True,"value":None}
        T3G.pTB3 = {"condition":True,"value":None}
        T3G.pTB4 = {"condition":True,"value":None}
        T3G.pTB5 = {"condition":True,"value":None}
        T3G.pTB6 = {"condition":True,"value":None}
        T3G.pTB7 = {"condition":True,"value":None}
        T3G.pTB8 = {"condition":True,"value":None}
        T3G.pTB9 = {"condition":True,"value":None}
        #T3G.Screen =[]
        return #self.window(frame)
    #play Game
    #windowscreen=None,playGameScreen=None
    def anotherNewGame(self,rTK=None,windowScreen=None,gameScreen=None):
        #windowScreen.pack(fill="both",expand=True)
        #print("aNG",windowScreen)
        self.rTK = rTK
        self.windowScreen = windowscreen
        self.gameScreen = gameScreen
        #self.newGame(None,None)
        #mSC.showturtle()
        #mSC.pendown()
        #mSC.right(90)
        T3Game.Screen.append(self.rTK)
        T3Game.Screen.append(self.gameScreen)
        T3Game.Screen.append(self.windowScreen)
        print("Screen",T3Game.Screen)
        return
    
    '''
    def playNewGame(self,mSC):
        #print(self.mSC,"self.mSC")
        print(mSC,"mSC")
        mSC.showturtle()
        #mSC.pendown()
        #mSC.goto(-50,-50)
        mSC.penup()
        mSC.right(180)
        mSC.forward(50)
        mSC.right(90)
        mSC.forward(10)
        mSC.pendown()
        mSC.forward(100)
        mSC.right(-90)
        mSC.forward(40)
        mSC.right(-90)
        mSC.forward(100)
        mSC.right(-90)
        mSC.forward(40)
        mSC.right(-90)
        mSC.forward(50)
        mSC.right(-90)
        mSC.penup()
        mSC.forward(20)
        mSC.write("NewGame",align="center",font=("ROBOTIC",10,"bold"))
        mSC.penup()
        ####################################################################
        return
    '''
    
    

    def back(self,*screens):
        #print(frame,"frame")
        #print("bkarguments",arguments)
        #windowscreen.pack(fill="both",expand=True)
        #playGameScreen.pack_forget()
        print(*screens,"bKscreens",screens[len(screens)-1])
        #screens[len(screens)-1].pack_forget()
        for screen in reversed(range(len(screens))):
            print(screen,"screen",screens[screen])
            screens[screen].pack_forget()
        screens[len(screens)-2].pack(fill="both",expand=True)
        #print(*screens,"bKscreens")
        print("labels",self.labels)
        self.countP2 -= 1
        print(self.countP2,"countP2")
        return
    '''
    def storeX(self,value):
        self.valueX = value
        print(self.valueX,"valueStoreX")
        return
    '''
    
    
    def storeOX(self,value):
        self.valueOX = value
        print(self.valueOX,"valueStoreO or X")
        #playersDict['player1'] = self.valueOX
        #print(playersDict.get(playersDict),"playersDict")
        self.playersDict['player1'].append(self.valueOX)
        print(self.playersDict.get('player1'),"playersDict")
        #problem is to write player2 functionality to store value
        return
    #problem is to store the player1 and player2 X or O value
    #O
    def O(self,pGBnO,windowscreen=None,playGameScreen=None):
        print("O")
        value = pGBnO.cget("text")
        print(value,"value")
        #playGameScreen.pack_forget()
        #windowscreen.pack_forget()
        #T3GL = T3GameLogic(value)
        #T3GL.get
        #T3GL.valueO(value)
        #self.T3GL.X(value)
        #self.T3GL.value=value
        #print(self.labels.get("player1"),"labels")
        #labels = self.labels.get("player1")
        #print(self.labels.get("players")[0],"lP")
        print(self.labels.get("player1"),"lp")
        #self.playersDict["player1"] = value
        print(self.playersDict["player1"],"pdp1")
        print("countP2",self.countP2)
        #((value=="X" and (self.labels.get("player1")!=[] or self.labels.get("player1")==[])) or (type(self.playersDict["player1"]) == type(None)) and (type(self.playersDict["player1"]) != type(None))) and (self.countP2==0)
        if(((value=="O" and (self.labels.get("player1")!=[] or self.labels.get("player1")==[])) or (type(self.playersDict["player1"]) == type(None)) or (type(self.playersDict["player1"]) != type(None))) and (self.countP2==0)):
            print("if O")
            if((value=="O" and self.labels.get("player1")!=[])):
                print("if")
                self.countL=0
                self.playersDict["player1"] = value
                self.labels.get("player1")[0].pack_forget()
                #self.labels.get("player1").clear()
                #self.countP2=1
                
            else:
                print("else")
                self.playersDict["player1"] = value
                self.countL=0
                #self.countP2=1
        else:
            print("else outer")
            #print(self.labels.get("player2"),"player2")
            #print((value=="O" and self.labels.get("player2")!=[]),"condition")
            if((value=="O" and (self.labels.get("player2")!=[])and(type(self.playersDict.get("player1")) != type(None)))and self.playersDict.get("player1")!="O"):
                print("if")
                self.countL=0
                self.playersDict["player2"] = value
                for label in self.labels.get("player2"):
                    print("label",label)
                    label.pack_forget()
                #self.labels.get("player2")[0].pack_forget()
                #self.labels.get("player2").clear()
                #self.countP2=0
##################################################################
            else:
                print("else")
                #problem is whether to change the if condition or not
                if(self.playersDict.get("player1")!="O"):
                    self.playersDict["player2"] = value
                    #self.countL=0
                else:
                    for label in self.labels.get("player2"):
                        print("label",label)
                        label.pack_forget()
                    self.labels.get("player2")[len(self.labels.get("player2"))-1].pack()
        ########################################################################
        print(self.labels.get("player1"),"pL")
        #print(self.labels.get("player2"),"lp2")
        #if(value=="O" and self.labels.get("player2")!=[]):
        #self.labels.get()
        '''
        print(labels,"labels")
        if(type(labels)!=type(None)):
            for value in self.labels.keys():
                print(value,"Lvalue")
                if(self.value)
    
        if(type(self.labels.get("player1"))!=type(None)):
            print(self.labels.get("player1"),"labels")
        '''
        print(self.playersDict["player1"],"player1Dict")
        print(self.playersDict["player2"],"player2Dict")
        return #self.storeOX(value)
       
    #X
    def X(self,pGBnX):
        #print("X")
        value = pGBnX.cget("text")
        print(value,"value")
        #self.countL=0
        #T3GL = T3GameLogic(value)
        #self.T3GL.value=value
        #self.playersDict["player1"] = value
        print(self.playersDict["player1"],"pdp1")
        print(self.countP2,"countP2")
        '''
        if((value=="X" and self.labels.get("player1")!=[]) or (type(self.playersDict["player1"]) == type(None)) or (type(self.playersDict["player1"]) != type(None))):
            self.labels.get("player1")[0].pack_forget()
            self.labels.get("player1").clear()
            self.playersDict["player1"] = value
        print(self.labels.get("player1"),"pL")
        '''
        #(solved)problem is to solve player1 and player2 mismatching values
        if(((value=="X" and (self.labels.get("player1")!=[] or self.labels.get("player1")==[])) or (type(self.playersDict["player1"]) == type(None)) and (type(self.playersDict["player1"]) != type(None))) and (self.countP2==0)):
            print("if X")
            if((value=="X" and self.labels.get("player1")!=[])):
                print("if")
                self.countL=0
                self.playersDict["player1"] = value
                self.labels.get("player1")[0].pack_forget()
                #self.labels.get("player1").clear()
            else:
                print("else")
                self.playersDict["player1"] = value
                self.countL=0
        else:
        #(solved)problem is to forget labels and pack specific label
            print("else")
            print(self.playersDict["player1"],"playersDict")
            if((value=="X" and self.labels.get("player2")!=[]) and self.playersDict.get("player1")!="X"):
                print("if")
                self.countL=0
                self.playersDict["player2"] = value
                for label in self.labels.get("player2"):
                    print("label",label)
                    label.pack_forget()
                #self.labels.get("player2")[0].pack_forget()
                #self.labels.get("player2").clear()
            else:
                print("else")
                if(self.playersDict.get("player1")!="X"):
                    self.playersDict["player2"] = value
                    #self.countL=0
                else:
                    print("length",len(self.labels.get("player2")))
                    for label in self.labels.get("player2"):
                        print("label",label)
                        label.pack_forget()
                    self.labels.get("player2")[len(self.labels.get("player2"))-1].pack(fill="both",expand=True)
        print(self.playersDict["player1"],"player1Dict")
        print(self.playersDict["player2"],"player2Dict")
        return #self.storeOX(value)
    #windowscreen=None,playGameScreen=None,playGameScreen2=None
    #player2
    #count=0
    def next(self,*screens):
        #self.countP2 = len(screens)
        #print(self.countP2,"countP2")
        #print(windowscreen,"ws",playGameScreen,"pgs")
        #windowscreen.pack_forget()
        #playGameScreen.pack_forget()
        #playGameScreen2.pack(fill="both",expand=True)
        print(*screens,"nTscreens")
        #print(playersdict)
##############################################################################################################################    
        print(self.playersDict.get("player1"),"player1")
        print(type("O")==type(None),"condition")
#(solved)problem is when player1 value is not none
        if(type(self.playersDict.get("player1"))==type(None) and self.countL==0 and self.countP2==0):
            print("player1 if")
            player1 = self.label(screens[len(screens)-2],"Player did not selected X or O")
            print(player1,"player1")
            if(type(self.playersDict.get("player1"))==type(None)):
                self.labels["player1"].append(player1)
                self.countL+=1
                #self.countP2 += 1
            #print("countP2 P1if",self.countP2)
        elif(self.countP2==0 and type(self.playersDict.get("player1"))!=type(None)):
            print("player1 elif")
            #count+=1
            for screen in screens:
                print(screen,"screens")
                screen.pack_forget()
            #if(type(self.playersDict.get("player1"))!=type(None)):
                #self.count+=1
            if self.countL>0:
                screens[len(screens)-2].pack(fill="both",expand=True)
            else:
                screens[len(screens)-1].pack(fill="both",expand=True)
                self.countP2 += 1
                self.countP1 = False
                print("countP2",self.countP2)
        else:
            self.countP1 = True
        #(solved)problem is when next button is clicked after selecting same player1 choice getting pack in last frame
        #print("countP2 P1else",self.countP2)
        #print(self.playersDict.get("player2"),"player2")
        #print(type(""))
        #print(type(self.playersDict.get("player2"))==type(None),"player2")
        #(solved)problem is text is printing unlimited times
        print(self.countL,"countL")
        print(self.playersDict.get("player1"),"player1")
        print(type(self.playersDict.get("player1"))!=type(None),"condition")
        print(*screens,"nTscreens")
        print(self.countP2,"countP2")
        #'''
        if(type(self.playersDict.get("player1"))!=type(None) and self.countL==0 and self.countP2==1):
            print("player2 if")
            if((type(self.playersDict.get("player2"))==type(None)) and self.countL==0 and self.countP2==1):
                player2 = self.label(screens[len(screens)-1],f"Player did not select player1 choice {self.playersDict.get('player1')}")
                print(player2,"player2")
                if(type(self.playersDict.get("player2"))==type(None)and self.countL==0):#and self.countL==0
                    #self.labels["player2"].append(player2)
                    #'''
                    for label in self.labels.get("player2"):
                        print(label,"label")
                        label.pack_forget()
                    self.labels["player2"].clear()
                    #'''
                    self.labels["player2"].append(player2)
                    self.countL+=1
                #self.countP2 = 0
                #count+=1
            #(solved)problem is to write elif condition for player2 value is not none
            #(solved)problem is to change the label value when player1 and player2 values are not none
            elif(self.countP2==1 and type(self.playersDict.get("player2"))!=type(None)and self.countP1):
                print("player2 elif")            
                #print("player2 else")
                #count+=1
                #print(screens,"screens")
                print("countL",self.countL)
                if((self.playersDict.get("player1")==self.playersDict.get("player2")) and self.countP1 and self.countL==0):
                    player2 = self.label(screens[len(screens)-2],f"Player did not select player1 choice {self.playersDict.get('player1')}")
                    for label in self.labels.get("player2"):
                        print(label,"label")
                        label.pack_forget()
                    self.labels["player2"].clear()
                    self.labels["player2"].append(player2)
                    self.countL+=1
                    #self.countL+=1
                for screen in screens:
                    screen.pack_forget()
                if self.countL>0:
                    screens[len(screens)-2].pack(fill="both",expand=True)
                else:
                    screens[len(screens)-1].pack(fill="both",expand=True)
                    self.countP2 += 1
                #screens[len(screens)-2].pack(fill="both",expand=True)
        #'''
        print(self.playersDict["player1"],"player1Dict")
        print(self.playersDict["player2"],"player2Dict")
        '''
        #self.countP2+=1
        #self.count+=1
        #self.countP2+=1
        self.countP2D+=1
        #self.countP2D2= self.countP2
        #problem is to increment countP2 should increase only one time after many next clicks without moving next frame
        #if(self.countP2D>self.countP2):
        #    self.countP2+=1
        #print(self.countP2,"countP2")
        if(self.countP2D>1):
            pass
        else:
            sel.countP2+=1
        '''
        return

        '''
        #print(T3GL,"T3GL")
        #T3GL = T3GameLogic.next(T3GL.value)
        ##############################################################################################
        #T3GL.next()
        #T3GameLogic.next(self.T3GL.value)
        #result=self.O(playGameScreenP2)
        #print(result,"result")
        #result = self.storeOX()
        #print(playersdict1,"playersdict1")
        #print("labels",self.labels["player1"])
        #for value in self.labels:
        #    print(value,"value")
        
        return #self.back(labels)
        #problem is when i click next it should return x or o value
        '''
    '''
    def window(self,frame):
        cF = tk.Frame(frame)
        cF = cF.pack(fill="both",expand=True)
        return cF
    '''
    def playerTurnScreen(self):
        self.pTS = te.Turtle()
        #print("pTS",self.pTS)
        self.pTS.hideturtle()
        self.pTS.penup()
        self.pTS.goto(-100,-150)
        self.pTS.pendown()
        self.pTS.forward(100)
        self.pTS.right(90)
        self.pTS.forward(50)
        self.pTS.right(90)
        self.pTS.forward(100)
        self.pTS.right(90)
        self.pTS.forward(50)
        self.pTS.penup()
        self.pTS.right(90)
        self.pTS.forward(50)
        self.pTS.right(90)
        self.pTS.forward(25)
        player = str(self.playersDict.get(f"player{self.pTCount}"))
        print("player",player)
        self.pTS.write(f"Player{self.pTCount} Turn {player}",align="center",font=("ROBOTIC",10,"bold"))
        #self.pTS.clear()
        if(self.pTCount==2):
            self.pTCount=0
        return (self.pTS,player)
    def demo(self):
        #problem is to return demoScreen or screen
        self.demoScreen = te.Screen()#Screen()
        print("dSC1",self.demoScreen)
        #self.__mSC = self.__mainScreen.getscreen()
        #self.__demoScreen = te.Screen()
        self.__screen = te.Turtle()
        #self.__demoScreen = 
        #self.__demoScreen1 = te.getscreen()
        #self.__demoScreen = self.__screen.getscreen()
        #self.demoScreen = self.__screen.getscreen()
        self.__screen.penup()
        self.__screen.goto(-200,200)
        self.__screen.forward(100)
        self.__screen.right(-90)
        self.__screen.forward(15)
        self.__screen.pendown()
        self.__screen.forward(50)
        self.__screen.right(90)
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.forward(50)
        self.__screen.right(90)
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.forward(25)
        self.__screen.right(90)
        self.__screen.penup()
        self.__screen.forward(50)
        self.__screen.write("Demo",align="center",font=("ROBOTIC",10,"bold"))
        #'''
        self.__screen.penup()
        self.__screen.goto(-200,200)
        self.__screen.pendown()
        self.__screen.forward(300)
        self.__screen.right(90)
        self.__screen.forward(300)
        self.__screen.right(90)
        self.__screen.forward(300)
        self.__screen.right(90)
        self.__screen.forward(300)
        self.__screen.right(90)
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.forward(300)
        self.__screen.right(-90)
        self.__screen.forward(100)
        self.__screen.right(-90)
        self.__screen.forward(300)
        self.__screen.right(90)
        self.__screen.penup()
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.pendown()
        self.__screen.forward(300)
        self.__screen.penup()
        self.__screen.right(-90)
        self.__screen.forward(100)
        self.__screen.right(-90)
        self.__screen.pendown()
        self.__screen.forward(300)
        self.__screen.right(90)
        self.__screen.penup()
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.forward(300)
        self.__screen.right(-90)
        self.__screen.forward(50)
        self.__screen.right(-90)
        self.__screen.forward(100)
        self.__screen.pendown()
        #self.pTS = te.Turtle()
        #self.screen.goto(-100,-150)
        self.__pTSC=self.playerTurnScreen()
        print("pTSC",self.__pTSC)
        #self.pTSC.clear()
        #'''
        '''
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.forward(50)
        self.__screen.right(90)
        self.__screen.forward(100)
        self.__screen.right(90)
        self.__screen.forward(50)
        self.__screen.penup()
        self.__screen.right(90)
        self.__screen.forward(50)
        self.__screen.right(90)
        self.__screen.forward(25)
        self.__screen.write(f"Player1 Turn {self.playersDict.get('player1')}",align="center",font=("ROBOTIC",10,"bold"))
        '''
        #'''
        self.__screen.penup()
        self.__screen.hideturtle()
        self.__screen.goto(-200,200)
        #self.screen.showturtle()
        #self.moveCursor = self.screen.getscreen()
        #self.moveCursor.onclick(self.clicked)
        self.__screen.goto(-150,150)
        #self.pTSC=self.playerTurnScreen()
        #print("pTSC",self.pTSC)
        self.__screen.write(f"{self.playersDict.get('player1')}",align="center",font=("ROBOTIC",20,"bold"))        
        self.__pTSC[0].clear()
        self.pTCount+=1
        self.__pTSC = self.playerTurnScreen()
        self.__screen.goto(-150,50)
        self.__screen.write(f"{self.playersDict.get('player2')}",align="center",font=("ROBOTIC",20,"bold"))
        self.__pTSC[0].clear()
        print("self.__pTSC",self.__pTSC)
        self.pTCount+=1
        self.__pTSC = self.playerTurnScreen()
        self.__screen.goto(-50,50)
        self.__screen.write(f"{self.playersDict.get('player1')}",align="center",font=("ROBOTIC",20,"bold"))
        self.__pTSC[0].clear()
        self.pTCount+=1
        self.__pTSC = self.playerTurnScreen()
        self.__screen.goto(50,150)
        self.__screen.write(f"{self.playersDict.get('player2')}",align="center",font=("ROBOTIC",20,"bold"))
        self.__pTSC[0].clear()
        self.pTCount+=1
        self.__pTSC = self.playerTurnScreen()
        self.__screen.goto(-50,150)
        self.__screen.write(f"{self.playersDict.get('player1')}",align="center",font=("ROBOTIC",20,"bold"))
        self.__pTSC[0].clear()
        self.pTCount+=1
        self.__pTSC = self.playerTurnScreen()
        self.__screen.goto(50,-50)
        self.__screen.write(f"{self.playersDict.get('player2')}",align="center",font=("ROBOTIC",20,"bold"))
        self.__pTSC[0].clear()
        self.pTCount+=1
        self.__pTSC = self.playerTurnScreen()
        self.__screen.goto(-50,-50)
        self.__screen.write(f"{self.playersDict.get('player1')}",align="center",font=("ROBOTIC",20,"bold"))
        self.__pTSC[0].clear()
        self.pTCount+=1
        self.__screen.showturtle()
        #self.pTSC = self.playerTurnScreen()
        #(solved)problem is to display who is winner and clear text player1 and text player2
        self.__screen.goto(-150,-150)
        self.__screen.pendown()
        self.__screen.forward(200)
        self.__screen.right(90)
        self.__screen.forward(50)
        self.__screen.right(90)
        self.__screen.forward(200)
        self.__screen.right(90)
        self.__screen.forward(50)
        self.__screen.penup()
        self.__screen.goto(-50,-170)
        self.__screen.hideturtle()
        self.__screen.pendown()
        self.__screen.write(f"Player1 {self.playersDict.get('player1')} Winner",align="center",font=("ROBOTIC",10,"bold"))
        self.__screen.speed(10)
        time.sleep(5)
        self.__screen.penup()
        self.__screen.clear()
        #'''
        return (self.__screen,self.demoScreen)

    def main(self):
        self.__mainScreen = te.Turtle()
        self.__mainScreen.penup()
        self.__mainScreen.goto(-200,200)
        self.__mainScreen.pendown()
        self.__mainScreen.forward(300)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(300)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(300)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(300)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(100)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(300)
        self.__mainScreen.right(-90)
        self.__mainScreen.forward(100)
        self.__mainScreen.right(-90)
        self.__mainScreen.forward(300)
        self.__mainScreen.right(90)
        self.__mainScreen.penup()
        self.__mainScreen.forward(100)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(100)
        self.__mainScreen.right(90)
        self.__mainScreen.pendown()
        self.__mainScreen.forward(300)
        self.__mainScreen.penup()
        self.__mainScreen.right(-90)
        self.__mainScreen.forward(100)
        self.__mainScreen.right(-90)
        self.__mainScreen.pendown()
        self.__mainScreen.forward(300)
        self.__mainScreen.right(90)
        self.__mainScreen.penup()
        self.__mainScreen.forward(100)
        self.__mainScreen.right(90)
        self.__mainScreen.forward(300)
        self.__mainScreen.right(-90)
        self.__mainScreen.forward(50)
        self.__mainScreen.right(-90)
        self.__mainScreen.forward(100)
        self.__mainScreen.penup()
        self.pTCount=1
        self.mPTSC=self.playerTurnScreen()
        self.busy = False
        #(solved)problem is to print mPTSC
        #self.box = self.T3GL.fixedPositions()
        #problem is to write game logic in same class. calling different class is getting complex
        self.__mSC = self.__mainScreen.getscreen()
        #self.__mSC.onclick(self.mainScreenCursor(self.__mSC,self.X,self.y))
        self.__mSC.onclick(lambda x,y:self.mainScreenCursor(x,y,self.__mainScreen))
        #problem is to display player2 choice and onclick method is async 
        #print(self.__mSCOK,"mSCOK")
        #self.__mPTSC[0].clear()
        #self.pTCount += 1
        #self.__mPTSC = self.playerTurnScreen()
        print("async")
#############################################################################################
        return self.__mainScreen
    def GameWinDraw(self,mSC):
        mSC.goto(-150,-150)
        mSC.pendown()
        mSC.forward(200)
        mSC.right(90)
        mSC.forward(50)
        mSC.right(90)
        mSC.forward(200)
        mSC.right(90)
        mSC.forward(50)
        mSC.penup()
        mSC.goto(-50,-170)
        mSC.hideturtle()
        mSC.pendown()
        return
    def playNewGame(self,mSC):
        #print(self.mSC,"self.mSC")
        print(mSC,"mSC")
        mSC.showturtle()
        #mSC.pendown()
        #mSC.goto(-50,-50)
        mSC.penup()
        mSC.right(180)
        mSC.forward(50)
        mSC.right(90)
        mSC.forward(10)
        mSC.pendown()
        mSC.forward(100)
        mSC.right(-90)
        mSC.forward(40)
        mSC.right(-90)
        mSC.forward(100)
        mSC.right(-90)
        mSC.forward(40)
        mSC.right(-90)
        mSC.forward(50)
        mSC.right(-90)
        mSC.penup()
        mSC.forward(20)
        mSC.write("NewGame",align="center",font=("ROBOTIC",10,"bold"))
        mSC.penup()
        mSC.hideturtle()
#######################################################################################
        #self.pNGSC = mSC.getscreen()
        #self.pNGSC.onclick(lambda x,y:self.callBackPlayNewGame(x,y,mSC,self.pNGSC))
        ####################################################################
        '''
        self.exit = mSC.getscreen()
        self.exit.onclick(lambda x,y:self.cBExit(x,y,self.exit,mSC))
        mSC.showturtle()
        mSC.right(90)
        mSC.forward(60)
        '''
        return
    '''
    def GameDraw(self,mSC):
        
        return
    '''
    
    def callBackPlayNewGame(self,mSC=None):
        print("cBPNG")
        #print("x",x,"y",y)
        #(-160,-219)(-60,-219)(-160,-256)(-61,-257)
        #print(self.Screen[0])
        #self.demoScreen.bye()
        #(-113,-239)
        #if(x<0)
        '''
        pMinX=-160
        pMaxX =-60
        pMinY=-250
        pMaxY=-220
        #print("condition1",(minX>x and x>maxX))
        #print("condition2",(minY>y and maxY>y))
        if((minX<x and maxX>x) and(minY<y and maxY>y)):            
            self.pNGSC.clear()
            #self.pNGSC.reset()
            print("Screen",self.Screen[0])
            T3Game.Screen[0].deiconify()
            #problem is to pack forget last screen in tkInter
    ############################################################################################
            T3Game.Screen[1].pack_forget()
            T3Game.Screen[len(T3Game.Screen)-1].pack(fill="both",expand=True)
            #self.newGame()
            #self.pNGSC = mainScreen.getscreen()
        '''
        mSC.clear()
        T3Game.Screen[0].deiconify()
        T3Game.Screen[1].pack_forget()
        T3Game.Screen[len(T3Game.Screen)-1].pack(fill="both",expand=True)
        return
    '''
    def cBExit(self,x,y,exit,mSC):
        return
    '''
    def exit(self,mSC):
        mSC.showturtle()
        mSC.goto(-50,-220)
        mSC.pendown()
        mSC.right(-90)
        mSC.forward(100)
        mSC.right(90)
        mSC.forward(40)
        mSC.right(90)
        mSC.forward(100)
        mSC.right(90)
        mSC.forward(40)
        mSC.penup()
        mSC.goto(-10,-245)
        mSC.write("Exit",align="center",font=("ROBOTIC",10,"bold"))
        #self.pExit = mSC.getscreen()
        #self.pExit.onclick(lambda x,y:self.cBExit(x,y,mSC,self.pExit))
        mSC.hideturtle()
        return
    #problem is to onclick given multiple times
    def cBExit(self,x=None,y=None,mSC=None,pEXit=None):
        print("cBExit")
        #print("x",x,"y",y)
        #(-50,-220)(-50,-250)(50,-220)(50,-250)
        #(-3,-233)
        '''
        eMinX = -50
        eMaxX = 50
        eMinY = -250
        eMaxY = -220
        if((minX<x and maxX>x) and(minY<y and maxY>y)):
            print("exit")
        '''
        self.demoScreen.bye()
        sys.exit()       
        return
        
        
        
    def mainScreenCursor(self,x,y,mSC):
        print(x,y,mSC,"x","y","mSC")
        #mPTSC[0].clear()
        #mSC.goto(x,y)
        minX = -200
        maxX = 100
        minY = -100
        maxY = 200
        if self.busy:
            return
        self.busy = True
        '''
        if(self.pTCount==0):
            self.pTCount+=1
        '''
        #player = str(self.playersDict.get(f"player{self.pTCount}"))
        #print("playerMSC",player)
        #self.__pTSC1 = None
        #self.__mPTSC = self.playerTurnScreen()
        #self.__pTSC2 = None
        #self.__pTSC3 = None
        #self.__pTSC4 = None
        #self.__pTSC5 = None
        #self.__pTSC6 = None
        #self.__pTSC7 = None
        #self.__pTSC8 = None
        #self.__pTSC9 = None
        try:
            if((x>minX and y>minY) and (x<maxX and y<maxY) and self.GameOver==False):
                print("msc",mSC)
                #mSC.goto(x,y)
                #print(-100>x and 100<y,"-100>x and 100>y")
                if(-100>x and 100<y and self.pTB1.get("condition")):
                    mSC.hideturtle()
                    #mSC.goto(-150,150)
                    #self.__pTSC1 = self.playerTurnScreen()
                    mSC.goto(-150,110)
                    #print(self.__pTSC1,"pTSC1") 
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB1["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    #print()
                    self.pTCount += 1
                    self.mPTSC = self.playerTurnScreen()
                    print("self.mPTSC",self.mPTSC)
                    mSC.showturtle()
                    #time.sleep(5)
                    self.pTB1["condition"]=False
                    #self.pTB1["value"] = self.mPTSC[1]
                #(solved)problem is condition sometimes getting true and sometimes false even clicking right block
    ##########################################################################################################
                #(solved)problem is to write logic and condition is true in a dictionary
                elif(0>x and -100<x and 200>y and y>100 and self.pTB2.get("condition")):
                    mSC.hideturtle()
                    #mSC.goto(-50,110)
                    #self.__pTSC2 = self.playerTurnScreen()
                    mSC.goto(-50,110)
                    #self.__pTSC1 = self.playerTurnScreen()
                    #(solved)problem is not displaying player 2 choice
                    print(f"{self.mPTSC[1]}","mPTSC")
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB2["value"] = self.mPTSC[1]
                    #self.__pTSC1 = self.playerTurnScreen()
                    self.mPTSC[0].clear()
                    self.pTCount += 1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB2["condition"]=False
                    #self.pTB2["value"] = self.mPTSC[1]
                elif(x>0 and y>100 and self.pTB3.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(50,110)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB3["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount += 1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB3["condition"]=False
                    #self.pTB3["value"] = self.mPTSC[1]
                elif(-100>x and y>0 and 100>y and self.pTB4.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(-150,10)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB4["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount+=1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB4["condition"]=False
                elif(x>-100 and y<100 and x<0 and y>0 and self.pTB5.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(-50,10)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB5["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount+=1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB5["condition"]=False
                elif(x<100 and y<100 and y>0 and x>0 and self.pTB6.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(50,10)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB6["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount+=1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB6["condition"]=False
                elif(x<-100 and y<0 and self.pTB7.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(-150,-90)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB7["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount+=1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB7["condition"]=False
                elif(x>-100 and y>-100 and y<0 and x<0 and self.pTB8.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(-50,-90)
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB8["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount+=1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB8["condition"]=False
                elif(x<100 and y>-100 and y<0 and x>0 and self.pTB9.get("condition")):
                    mSC.hideturtle()
                    mSC.goto(50,-90)
                    #(solved)problem is to fix right position
                    mSC.write(f"{self.mPTSC[1]}",align="center",font=("ROBOTIC",50,"bold"))
                    self.pTB9["value"] = self.mPTSC[1]
                    self.mPTSC[0].clear()
                    self.pTCount+=1
                    self.mPTSC = self.playerTurnScreen()
                    mSC.showturtle()
                    self.pTB9["condition"]=False
                #(solved)problem is to fix the glitch while writing moving to other block
                #####################################################################
            #player = str(self.playersDict.get(f"player{self.pTCount}"))
            #pTBV = str(self.pTBf"{value}".get("value"))
            #for value in range(1,4):
            #print(f"{pTBV}","PTB"+value)
            print(self.pTB1.get("value"),"pTB1")
            print(self.pTB2.get("value"),"pTB2")
            print(self.pTB3.get("value"),"pTB3")
            print(self.pTB4.get("value"),"pTB4")
            print(self.pTB5.get("value"),"pTB5")
            print(self.pTB6.get("value"),"pTB6")
            print(self.pTB7.get("value"),"pTB7")
            print(self.pTB8.get("value"),"pTB8")
            print(self.pTB9.get("value"),"pTB9")
            #(solved)problem is getting wrong value in pTB3
            if(((self.pTB1.get("condition")==False) or (self.pTB2.get("condition")==False) or (self.pTB3.get("condition")==False) or (self.pTB3.get("condition")==False) or (self.pTB4.get("condition")==False) or (self.pTB5.get("condition")==False) or (self.pTB6.get("condition")==False) or (self.pTB7.get("condition")==False) or (self.pTB8.get("condition")==False) or (self.pTB9.get("condition")==False)) and (self.GameOver == False)):
                print("if")
                #print(True!=None)
                #####################################################################################################
                #print((self.pTB1.get("value")==self.pTB2.get("value")==self.pTB3.get("value"))==None,"condition")
                #print(False!=None)
                #print(True==None)
                #print(False == None)
                print((self.pTB1.get("value")==(("X"))or(self.pTB1.get("value")==("O"))),"condition1")
                print(((self.pTB2.get("value")=="X")and (self.pTB5.get("value")=="X") and (self.pTB8.get("value")=="X")) or ((self.pTB2.get("value")=="O") and (self.pTB5.get("value")=="O") and (self.pTB8.get("value")=="O")),"condition2")
                #(solved)problem is to cross check the condition
                #if((self.pTB1.get("value")==("X"or"O")) and (self.pTB2.get("value")==("X"or"O")) and (self.pTB3.get("value")==("X"or"O"))):#==self.pTB2.get("value")==self.pTB3.get("value"))==False)==None)):
                if(((self.pTB1.get("value")=="X")and (self.pTB2.get("value")=="X") and (self.pTB3.get("value")=="X")) or ((self.pTB1.get("value")=="O") and (self.pTB2.get("value")=="O") and (self.pTB3.get("value")=="O"))):
                    #print("pTB1",type(self.pTB1.get("value"))==None,True!=None)
                    #print()
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    '''
                    mSC.goto(-150,-150)
                    #self.mPTSC[0].clear()
                    mSC.pendown()
                    mSC.forward(200)
                    mSC.right(90)
                    mSC.forward(50)
                    mSC.right(90)
                    mSC.forward(200)
                    mSC.right(90)
                    mSC.forward(50)
                    mSC.penup()
                    mSC.right(90)
                    mSC.forward(50)
                    mSC.right(90)
                    mSC.forward(30)
                    mSC.forward(200)
                    mSC.right(90)
                    mSC.forward(50)
                    mSC.right(90)
                    mSC.forward(200)
                    mSC.right(90)
                    mSC.forward(50)
                    mSC.penup()
                    mSC.goto(-50,-170)
                    mSC.hideturtle()
                    mSC.pendown()
                    '''
                #(solved)problem is to write out if and elif using playerwinner1 and playerwinner2
                #(solved)problem is to write logic for second and third rows and columns and daigonals
                    if(self.pTB1.get('value')==self.playersDict.get('player1')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('player1')
                        #print(self.PlayerWinner1,"PlayerWinner1")
                        #mSC.write(f"PLAYER1 {self.pTB1.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    elif(self.pTB2.get('value')==self.playersDict.get('player2')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('player2')
                        #print(self.PlayerWinner2,"PlayerWinner2")
                        #mSC.write(f"PLAYER2 {self.pTB1.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                #problem is to show new game or exit after player won the game or draw
                    #return
                elif(((self.pTB4.get("value")=="X")and (self.pTB5.get("value")=="X") and (self.pTB6.get("value")=="X")) or ((self.pTB4.get("value")=="O") and (self.pTB5.get("value")=="O") and (self.pTB6.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB4.get('value')==self.playersDict.get('player1')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('player1')
                        #print(self.PlayerWinner1,"PlayerWinner1")
                        #mSC.write(f"PLAYER1 {self.pTB1.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    elif(self.pTB5.get('value')==self.playersDict.get('player2')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('player2')
                elif(((self.pTB7.get("value")=="X")and (self.pTB8.get("value")=="X") and (self.pTB9.get("value")=="X")) or ((self.pTB7.get("value")=="O") and (self.pTB8.get("value")=="O") and (self.pTB9.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB7.get('value')==self.playersDict.get('player1')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('player1')
                        #print(self.PlayerWinner1,"PlayerWinner1")
                        #mSC.write(f"PLAYER1 {self.pTB1.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    elif(self.pTB7.get('value')==self.playersDict.get('player2')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('player2')
                elif(((self.pTB1.get("value")=="X")and (self.pTB4.get("value")=="X") and (self.pTB7.get("value")=="X")) or ((self.pTB1.get("value")=="O") and (self.pTB4.get("value")=="O") and (self.pTB7.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB1.get('value')==self.playersDict.get('player1')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('player1')
                        #print(self.PlayerWinner1,"PlayerWinner1")
                        #mSC.write(f"PLAYER1 {self.pTB1.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    elif(self.pTB1.get('value')==self.playersDict.get('player2')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('player2')
                elif(((self.pTB2.get("value")=="X")and (self.pTB5.get("value")=="X") and (self.pTB8.get("value")=="X")) or ((self.pTB2.get("value")=="O") and (self.pTB5.get("value")=="O") and (self.pTB8.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB2.get('value')==self.playersDict.get('player1')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('player1')
                        #print(self.PlayerWinner1,"PlayerWinner1")
                        #mSC.write(f"PLAYER1 {self.pTB1.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    elif(self.pTB2.get('value')==self.playersDict.get('player2')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('player2')
                elif(((self.pTB3.get("value")=="X")and (self.pTB6.get("value")=="X") and (self.pTB9.get("value")=="X")) or ((self.pTB3.get("value")=="O") and (self.pTB6.get("value")=="O") and (self.pTB9.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB3.get('value')==self.playersDict.get('player1')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('player1')
                        #print(self.PlayerWinner1,"PlayerWinner1")
                        #mSC.write(f"PLAYER1 {self.pTB1.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    elif(self.pTB3.get('value')==self.playersDict.get('player2')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('player2')
                elif(((self.pTB1.get("value")=="X")and (self.pTB5.get("value")=="X") and (self.pTB9.get("value")=="X")) or ((self.pTB1.get("value")=="O") and (self.pTB5.get("value")=="O") and (self.pTB9.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB9.get('value')==self.playersDict.get('player1')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('player1')
                        #print(self.PlayerWinner1,"PlayerWinner1")
                        #mSC.write(f"PLAYER1 {self.pTB1.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    elif(self.pTB9.get('value')==self.playersDict.get('player2')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('player2')
                elif(((self.pTB3.get("value")=="X")and (self.pTB5.get("value")=="X") and (self.pTB7.get("value")=="X")) or ((self.pTB3.get("value")=="O") and (self.pTB5.get("value")=="O") and (self.pTB7.get("value")=="O"))):
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    if(self.pTB7.get('value')==self.playersDict.get('player1')):
                        self.PlayerWinner1['condition'] = True
                        self.PlayerWinner1['value'] = self.playersDict.get('player1')
                        #print(self.PlayerWinner1,"PlayerWinner1")
                        #mSC.write(f"PLAYER1 {self.pTB1.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    elif(self.pTB7.get('value')==self.playersDict.get('player2')):
                        self.PlayerWinner2['condition'] = True
                        self.PlayerWinner2['value'] = self.playersDict.get('player2')
                elif((self.pTB1.get("value")!=None) and (self.pTB2.get("value")!=None) and (self.pTB3.get("value")!=None) and (self.pTB4.get("value")!=None) and (self.pTB5.get("value")!=None) and (self.pTB6.get("value")!=None) and (self.pTB7.get("value")!=None) and (self.pTB8.get("value")!=None) and (self.pTB9.get("value")!=None)):
                    print("all values not none")
                    self.mPTSC[0].clear()
                    self.GameWinDraw(mSC)
                    self.GameOver = True
                if(self.PlayerWinner1.get('condition')):
                    print(self.PlayerWinner1,"PlayerWinner1 out if")
                    mSC.write(f"PLAYER1 {self.PlayerWinner1.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    self.GameOver = True
                    self.playNewGame(mSC)
                    mSC.penup()
                    self.exit(mSC)
                elif(self.PlayerWinner2.get('condition')):
                    mSC.write(f"PLAYER2 {self.PlayerWinner2.get('value')} WINNER",align="center",font=("ROBOTIC",10,"bold"))
                    self.GameOver = True
                    self.playNewGame(mSC)
                    mSC.penup()
                    self.exit(mSC)
                elif(self.GameOver == True):
                    mSC.write(f"Game Draw",align="center",font=("ROBOTIC",10,"bold"))
                    #self.GameOver = True
                    self.playNewGame(mSC)
                    mSC.penup()
                    self.exit(mSC)
            pMinX=-160
            pMaxX =-60
            pMinY=-250
            pMaxY=-220
            eMinX = -50
            eMaxX = 50
            eMinY = -250
            eMaxY = -220
            #print(self.PlayerWinner1,"PlayerWinner1 out")
            #print("x",x,"y",y)
            #(solved)problem is to write positions using playerwinner1 and playerwinner2 True
            #problem is to recheck the cbpng and cbe
            if(self.PlayerWinner1.get('condition')):
                if((pMinX<x and pMaxX>x) and(pMinY<y and pMaxY>y)):
                    self.callBackPlayNewGame(mSC)
                elif((eMinX<x and eMaxX>x) and(eMinY<y and eMaxY>y)):
                    self.cBExit()
            elif(self.PlayerWinner2.get('condition')):
                if((pMinX<x and pMaxX>x) and(pMinY<y and pMaxY>y)):
                    self.callBackPlayNewGame(mSC)
                elif((eMinX<x and eMaxX>x) and(eMinY<y and eMaxY>y)):
                    self.cBExit()
            elif(self.GameOver == True):
                if((pMinX<x and pMaxX>x) and(pMinY<y and pMaxY>y)):
                    self.callBackPlayNewGame(mSC)
                elif((eMinX<x and eMaxX>x) and(eMinY<y and eMaxY>y)):
                    self.cBExit()
        #(solved)problem is to write exit method
        finally:
            self.busy=False
        #time.sleep(5)
        return #mPTSC

    #def packForget(self,label,)
    def playGame(self,rTK):
        rTK.withdraw()
        self.demoSc = self.demo()
        #self.mainSc = self.main()
        self.moveCursor = self.demoSc[0].getscreen()
        self.moveCursor.onclick(self.clicked)
        #self.demoSc.getscreen().ontimer(self.clearDSc,5000)
        #(solved)problem is ontimer method is executing asynchronously
        #time.sleep(5)
        self.mainSc = self.main()
        #self.demoSc.clear()
        #self.screen.clear()
        te.done()
        #problem is to complete main game
    ##################################################################
        #self.screen = te.Turtle()
        #self.screen = self.tt.getscreen()
        '''
        screen = te.Screen()
        screen.title("Tic Tac Toe")
        back = te.Turtle()
        back.shape("square")
        back.shapesize(1,3)
        back.penup()
        back.goto(-250,250)
        back.write("Back",align="center",font=("Arial",14,"bold"))
        
        
        def goBack(x,y):
            screen.bye()
            rTK.deiconify()
            return
        back.onclick(goBack)
        '''
        #######################################
        #(pSolved)problem is function need to be complete
        #def screen(X=None,Y=None):
        #def 
        '''    
        self.screen.penup()
        self.screen.goto(-200,200)
        self.screen.forward(100)
        self.screen.right(-90)
        self.screen.forward(15)
        self.screen.pendown()
        self.screen.forward(50)
        self.screen.right(90)
        self.screen.forward(100)
        self.screen.right(90)
        self.screen.forward(50)
        self.screen.right(90)
        self.screen.forward(100)
        self.screen.right(90)
        self.screen.forward(25)
        self.screen.right(90)
        self.screen.penup()
        self.screen.forward(50)
        self.screen.write("Demo",align="center",font=("ROBOTIC",10,"bold"))
        self.screen.penup()
        self.screen.goto(-200,200)
        #screen.right(90)
        '''
        '''
        self.screen.pendown()
        self.screen.forward(300)
        self.screen.right(90)
        self.screen.forward(300)
        self.screen.right(90)
        self.screen.forward(300)
        self.screen.right(90)
        self.screen.forward(300)
        #screen.penup()
        self.screen.right(90)
        self.screen.forward(100)
        self.screen.right(90)
        self.screen.forward(300)
        self.screen.right(-90)
        self.screen.forward(100)
        self.screen.right(-90)
        self.screen.forward(300)
        self.screen.right(90)
        self.screen.penup()
        self.screen.forward(100)
        self.screen.right(90)
        self.screen.forward(100)
        self.screen.right(90)
        self.screen.pendown()
        self.screen.forward(300)
        self.screen.penup()
        self.screen.right(-90)
        self.screen.forward(100)
        self.screen.right(-90)
        self.screen.pendown()
        self.screen.forward(300)
        self.screen.right(90)
        self.screen.penup()
        self.screen.forward(100)
        self.screen.right(90)
        self.screen.forward(300)
        self.screen.right(-90)
        self.screen.forward(50)
        self.screen.right(-90)
        self.screen.forward(100)
        self.screen.pendown()
        self.screen.forward(100)
        self.screen.right(90)
        self.screen.forward(50)
        self.screen.right(90)
        self.screen.forward(100)
        self.screen.right(90)
        self.screen.forward(50)
        self.screen.penup()
        self.screen.right(90)
        self.screen.forward(50)
        self.screen.right(90)
        #screen.write("Player1 Turn")
        self.screen.forward(25)
        self.screen.write(f"Player1 Turn {self.playersDict.get('player1')}",align="center",font=("ROBOTIC",10,"bold"))
        self.screen.penup()
        self.moveCursor = self.screen.getscreen()
        self.moveCursor.onclick(self.clicked)
        #print(self.result,"result")
        #self.screen.hideturtle()
        #(solved)problem is to write a method player turn to goto(-200,200)
        #screenBk = te.Turtle()
        #screen.left(180)
        #screen.forward(-300)
        #screen.forward(-300,300)
        #screen.goto(-300,300)
        #screen.forward(100)
        #screen.right(90)
        '''
        #screen.mainloop()
        return
    def clicked(self,x,y):
        print("clicked at",x,y)
        self.demoSc.goto(x,y)
        self.mainSc.goto(x,y)
    #problem is screen is not global
        return
    '''
    def clearDSc(self):
        self.demoSc.clear()
        return
    '''
    


    
    


    

    

    
    

#open GUI
T3GUIG = tk.Tk()
T3GUIG.title("TicTacToe")

#draw shapes,patterns,pictures by controlling a cursor
#te = te.Turtle()

#object
T3GL = T3GameLogic(None)
T3G = T3Game(T3GL)
#T3G = T3Game()
'''
#label creation
mainscreenlabel = T3G.label(windowscreen,"Tik Tac Toe")
#print(mainscreenlabel)

#button creation
buttoncreation = T3G.button(windowscreen,"Play Game",command = lambda :T3G.playGame(windowscreen,playGameScreen),frame=None)
'''

#windowscreen
windowscreen = T3G.window(T3GUIG)
windowscreen.pack(fill="both",expand=True)
print(windowscreen,"windowscreen")



#playGame frame player1
playGameScreen = T3G.window(T3GUIG)
#playGame player1 label
pGSLO = T3G.label(playGameScreen,"Player1")
#playGame Button
pGBnO = T3G.button(playGameScreen,"O",command=lambda:T3G.O(pGBnO,windowscreen,playGameScreen),frame=None)
#playGame Button
pGBnX = T3G.button(playGameScreen,"X",command=lambda:T3G.X(pGBnX),frame=None)

'''
#playGame player2 label
pGSLX = T3G.label(playGameScreen,"Player2")
#playGame Button
pGBnO = T3G.button(playGameScreen,"O",command=lambda:T3G.O(pGBnO,windowscreen,playGameScreen),frame=None)
#playGame Button
pGBnX = T3G.button(playGameScreen,"X",command=lambda:T3G.X(pGBnX),frame=None)
'''

#playGame frame player2
playGameScreenP2 = T3G.window(T3GUIG)
#playGame player1 label
pGSLO = T3G.label(playGameScreenP2,"Player2")
#playGame Button
pGBnO = T3G.button(playGameScreenP2,"O",command=lambda:T3G.O(pGBnO,windowscreen,playGameScreen),frame=None)
#playGame Button
pGBnX = T3G.button(playGameScreenP2,"X",command=lambda:T3G.X(pGBnX),frame=None)



#playGame Button
pGBnNt = T3G.button(playGameScreen,"Next",command=lambda:T3G.next(windowscreen,playGameScreen,playGameScreenP2),frame=None)
#playGameScreen.pack(fill="both",expand=True)
print("pGBnNt",pGBnNt)


#playGame Button
pGBnBk = T3G.button(playGameScreen,"Back",command=lambda:T3G.back(windowscreen,playGameScreen),frame=None)
#playGameScreen.pack(fill="both",expand=True)
print("pGBnBk",pGBnBk)
'''windowscreen=windowscreen,playGameScreenP2=playGameScreenP2,'''
#problem is to complete below Next function
def Next(*arguments,elementFrame=None,text=None,classObject=None,frame=None):
    print(arguments,"arguments")
    for value in arguments:
        print(value,"value")
    nT = classObject.button(element=elementFrame,text=text,command=lambda:classObject.next(*arguments),frame=frame)
    return nT

#(solved)problem is to complete below back function
#####################################################
def Back(*arguments,elementFrame=None,text=None,classObject=None,frame=None):
    print(arguments,"arguments")
    for value in arguments:
        print(value,"value")
    bK = classObject.button(element=elementFrame,text=text,command=lambda:classObject.back(*arguments),frame=frame)
    return bK

#GameScreen
gS = T3G.window(T3GUIG)
gSB = T3G.button(gS,"Play Game",command=lambda:T3G.playGame(T3GUIG),frame=None)
#playGame Buttonnt and Buttonbk
nTScreens = [windowscreen,playGameScreen,playGameScreenP2,gS]
bKScreens = [windowscreen,playGameScreen,playGameScreenP2]
pGBnNtP2 = Next(*nTScreens,elementFrame=playGameScreenP2,text="Next",classObject=T3G)
print(pGBnNtP2,"pGBnNtP2")
pGBnBkP2 = Back(*bKScreens,elementFrame=playGameScreenP2,text="Back",classObject=T3G)

#gameScreen Buttonbk
bKScreens+=[gS]
print(bKScreens,"bKScreens")
gSBBk = Back(*bKScreens,elementFrame=gS,text="Back",classObject =T3G)



#label creation
mainscreenlabel = T3G.label(windowscreen,"Tic Tac Toe")
#print(mainscreenlabel)

#button creation
buttoncreation = T3G.button(windowscreen,"New Game",command = lambda :T3G.newGame(windowscreen,playGameScreen),frame=None)
newGame = T3G.anotherNewGame(rTK=T3GUIG,windowScreen=windowscreen,gameScreen=gS)

#print(buttoncreation,"buttoncreation")
#print("windowscreen",windowscreen)
#print(buttoncreation)
#subscreen
#mainscreenlabel.pack_forget()
#label creation
#subscreenlabel = T3G.label(T3GUIG,"Player1")

'''
#playGame frame
playGameScreen = T3G.window(T3GUIG)
pGBnBk = T3G.button(playGameScreen,"Back",command=lambda:T3G.back(playGameScreen),frame=None)
#playGameScreen.pack(fill="both",expand=True)
print("pGBnBk",pGBnBk)
'''




#application running and responsive
T3GUIG.mainloop()
