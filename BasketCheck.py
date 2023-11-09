import random
from tkinter import messagebox
import time
from tkinter import YES
import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk


# from tkinter import *


class CanvasGUI2:

    def __init__(self):
        self.rootWin = tk.Tk()
        self.rootWin.title("Second Canvas example")
        self.rootWin.geometry('960x540')

        # Create a canvas object that is 500 by 500 pixels wide, with a yellow background
        # self.canvas = tk.Canvas(self.rootWin, bg="yellow", width=500, height=500, bd=0)
        # self.canvas.grid(row=1, column=1)
        # # Show all the canvas
        # self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        #
        self.canvas = tk.Canvas(self.rootWin, width=960, height=540)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        self.canvas.grid(columnspan=YES, rowspan=YES)

        # self.frame = tk.Frame(self.rootWin, width=200, height=540)

        image = Image.open("BackgroundFinal.png")
        self.canvas.image = ImageTk.PhotoImage(image)
        self.background=self.canvas.create_image(0,0,image=self.canvas.image, anchor="nw")
        ####
        # self.canvas2 = tk.Canvas(self.rootWin, bg="maroon",
        #                         width=500, height=250, bd=0)
        # self.canvas2.config(scrollregion=self.rootWin.bbox(tk.ALL))
        # self.canvas2.grid(row=2, column=1)

        # Load an image in the script
        carrot = Image.open("banhcuon/carrot.png")
        resize_carrot = carrot.resize((100, 100))
        self.carrot_pic = ImageTk.PhotoImage(resize_carrot)

        flour = Image.open("banhcuon/flour.png")
        resize_flour = flour.resize((100, 100))
        self.flour_pic = ImageTk.PhotoImage(resize_flour)

        potato = Image.open("banhcuon/potato.png")
        resize_potato = potato.resize((100, 100))
        self.potato_pic = ImageTk.PhotoImage(resize_potato)

        ground_meat = Image.open("banhcuon/groundmeat.png")
        resize_ground_meat = ground_meat.resize((100, 100))
        self.ground_meat_pic = ImageTk.PhotoImage(resize_ground_meat)

        wood_ear = Image.open("banhcuon/woodear.png")
        resize_wood_ear = wood_ear.resize((100, 100))
        self.wood_ear_pic = ImageTk.PhotoImage(resize_wood_ear)

        basket = Image.open("basket.png")
        resize_basket = basket.resize((100, 100))
        self.basket_pic = ImageTk.PhotoImage(resize_basket)

        self.basket_ob = self.canvas.create_image(420, 400, anchor=tk.NW, image=self.basket_pic)

        self.raw_list = [self.carrot_pic, self.flour_pic, self.potato_pic, self.ground_meat_pic, self.wood_ear_pic]

        # self.clock = tk.Label(self.canvas, text = "10")
        # self.clock.grid(row = 0, column = 0)

        # Bind the canvas and main window to respond to mouse button and keyboard entry
        self.canvas.bind("<Button-1>", self.chooseBall)
        # self.rootWin.bind("<Up>", self.moveBallUp)
        # self.rootWin.bind("<Down>", self.moveBallDown)
        # self.rootWin.bind("<Left>", self.moveBallLeft)
        # self.rootWin.bind("<Right>", self.moveBallRight)

        self.userBasket = []
        # Create an instance variable to hold which ball the user has selected
        self.selectedBall = None  ##why none, can it take any other value???!?!?
        raw_list_name = ["carrot", "flour", "potato", "ground meat", "wood ear"]
        # Save info about the balls.  This randomizes the balls, and their speeds,
        # and uses a dictionary keyed by the ID from the canvas.  Each entry in the
        # dictionary is also a dictionary, with separate keys values for each feature
        self.ballCollection = {}
        self.id_name = {}
        m = 0
        for ballColor in self.raw_list:
            nextDict = {}
            xStart = random.randrange(30, 800, 20)
            yStart = random.randrange(30, 280, 20)
            deltaX = random.randrange(5, 10, 1)
            deltaY = random.randrange(5, 10, 1)
            nextBall = self.canvas.create_image(xStart, yStart, anchor=tk.NW, image=ballColor)
            self.id_name[nextBall] = raw_list_name[m]
            m += 1
            nextDict['xDist'] = deltaX
            nextDict['yDist'] = deltaY
            nextDict['moving'] = True
            self.ballCollection[nextBall] = nextDict
        print("id_name: ", self.id_name)
        # for ballColor in self.raw_list:
        #     nextDict = {}
        #     xStart = random.randint(30, 280)
        #     yStart = random.randint(30, 280)
        #     deltaX = 10
        #     deltaY = 10
        #     nextBall = self.canvas.create_image(xStart, yStart, anchor=tk.NW, image=ballColor)
        #     nextDict['xDist'] = deltaX
        #     nextDict['yDist'] = deltaY
        #     nextDict['moving'] = True
        #     self.ballCollection[nextBall] = nextDict

    def go(self):
        """Takes no inputs, and runs its own loop for the GUI.  This is so we can move
        the balls without waiting for some user input."""
        try:
            while True:
                self.moveBalls()
                self.rootWin.update_idletasks()  # redraw
                self.rootWin.update()  # process events
                # self.basketCheck()
                if self.basketCheck() == True:
                    self.canvas.delete("all")
                    print("You win!!!!")
                    break
                elif self.basketCheck() == False and self.userBasket != [] :
                    print("You lose :((((")
                    break


        except tk.TclError:
            pass  # to avoid errors when the window is closed

    def moveBalls(self):
        """Takes no inputs, and moves the balls in the ball list.  It bounces
        back when it reaches the walls of the canvas"""
        for ballId in self.ballCollection:
            ballInfo = self.ballCollection[ballId]
            if ballInfo['moving']:
                (x0, y0) = self.canvas.coords(ballId)
                if x0 >= 800 or x0 <= 20:
                    ballInfo['xDist'] = - ballInfo['xDist']
                if y0 >= 370 or y0 <= 20:
                    ballInfo['yDist'] = - ballInfo['yDist']
                self.canvas.move(ballId, ballInfo['xDist'], ballInfo['yDist'])

                # --------------------------------------------------------------------------
        # Below here are the callback methods for the canvas to respond to mouse
        # and key inputs

    def chooseBall(self, event):
        """Called when the user clicks on the canvas, this determines if there is a
        ball currently selected or not. If there is a selected ball, then it "unselects" it
        and starts it moving again as normal. If there is no selected ball, then it
        checks if there is a ball close enough to where the mouse was clicked If so, then it selects
        that ball (or one of them) and stops it moving. It remembers which ball has been selected."""
        x = event.x
        y = event.y
        ballSet = self.canvas.find_overlapping(x -5, y - 5, x + 5, y + 5)
        newballSet = tuple(item for item in ballSet if item != self.background)
        try:
            # if self.background in ballSet:
            #     ballSet = tuple(list(ballSet).remove(self.background))
            # if self.selectedBall != None:
            #     ballInfo = self.ballCollection[self.selectedBall]
            #     ballInfo['moving'] = True
            #     self.selectedBall = None
            if len(ballSet) > 0:
                self.selectedBall = newballSet[0]
                ballInfo = self.ballCollection[self.selectedBall]
                ballInfo['moving'] = False
                self.canvas.moveto(self.selectedBall, 420, 400)
                self.userBasket.append(self.selectedBall)
                # self.canvas.delete(self.selectedBall)
                print(self.userBasket)
        except:
            pass

    def basketCheck(self):
        correct_list = ["ground meat", "wood ear", "flour"]
        for i in self.userBasket:
            # print(self.id_name[i])
            if self.id_name[i] not in correct_list:
                # self.userBasket.remove(i)
                return False
        if len(self.userBasket) == len(correct_list):
                return True



        # print("True")




    #
    # def UserBasketList(self, event):
    #     basketZone = self.canvas.find_overlapping(350,350 , 500, 500)
    #     self.userList = []
    #     if self.selectedBall!=None:
    #         if self.selectedBall :
    #             self.userList.append(self.selectedBall)
    #             self.canvas.delete(self.selectedBall)

    # def checkUserAnswer(self):
    #     if len(self.userList) == len(self.correct_list):
    #         for correctItem in self.correct_list:
    #             for userItem in self.userList:
    #                 if correctItem == userItem:

    # def moveBallUp(self, event):
    #     """Callback function that is triggered by the user typing the up arrow. It checks if any ball
    #     has been selected, and if so it moves it up by 5 pixels."""
    #     if self.selectedBall != None:
    #         self.canvas.move(self.selectedBall, 0, -5)
    #
    #
    # def moveBallDown(self, event):
    #     """Callback function that is triggered by the user typing the down arrow. It checks if any ball
    #     has been selected, and if so it moves it down by 5 pixels."""
    #     if self.selectedBall != None:
    #         self.canvas.move(self.selectedBall, 0, 5)
    #
    #
    # def moveBallLeft(self, event):
    #     """Callback function that is triggered by the user typing the left arrow. It checks if any ball
    #     has been selected, and if so it moves it left by 5 pixels."""
    #     if self.selectedBall != None:
    #         self.canvas.move(self.selectedBall, -5, 0)
    #
    # def moveBallRight(self, event):
    #     """Callback function that is triggered by the user typing the right arrow. It checks if any ball
    #     has been selected, and if so it moves it right by 5 pixels."""
    #     if self.selectedBall != None:
    #         self.canvas.move(self.selectedBall, 5, 0)

    # end of class CanvasGUI

    # --- here it goes...


myGui = CanvasGUI2()
myGui.go()
