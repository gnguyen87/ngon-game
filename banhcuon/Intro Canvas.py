import random
from tkinter import YES

from PIL import ImageTk, Image
# from imageTools import *

import tkinter as tk


class BasicGui:

    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Introduction")

        # create canvas
        self.canvas = tk.Canvas(self.mainWin, width=960, height=540)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        self.canvas.grid(columnspan=YES, rowspan=YES)

        image = Image.open("PicsforFinal/BackgroundFinal.png")
        self.canvas.image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor="nw")

        # create name entry widget
        self.nameEntry = tk.Entry(self.canvas, bg="pink", bd=10, font="Times 20", fg="white",
                                  justify=tk.CENTER, relief=tk.GROOVE, width=25)
        self.nameEntry.place(x=560, y=300)

        # create intro label
        self.namelabel = tk.Label(self.canvas, bg="pink", bd=10, font="Times 20",fg="white",
                                  text="Hi there! \n Please enter your name.", justify=tk.CENTER, relief=tk.GROOVE,
                                  width=25,
                                  )
        self.txt = str(self.nameEntry.get())
        self.namelabel.place(x=550, y=200)

        # create Avatar Icon
        avatar = Image.open("PicsforFinal/IMG_0339.PNG")
        resizeavatar = avatar.resize((350, 350))
        self.Avapic = ImageTk.PhotoImage(resizeavatar)
        # self.AvaLabel = tk.Label(self.canvas, image=self.Avapic)
        self.canvas.create_image(100, 150, anchor=tk.NW, image=self.Avapic)

        imageNextButton = Image.open("PicsforFinal/NextButtonFinal.png")
        resizeNextButton = imageNextButton.resize((128,38))
        self.imageButton = ImageTk.PhotoImage(resizeNextButton)
        self.buttonNext = tk.Button(self.canvas,
                                    command=self.reset, image=self.imageButton)

        self.buttonNext.place(x=800, y=400)

    def createBall(self):
        carrot = Image.open("PicsforFinal/Dishes Pics/banhcuon/carrot - Edited.png")
        resize_carrot = carrot.resize((100, 100))
        self.carrot_pic = ImageTk.PhotoImage(resize_carrot)

        flour = Image.open("PicsforFinal/Dishes Pics/banhcuon/flour - Edited.png")
        resize_flour = flour.resize((100, 100))
        self.flour_pic = ImageTk.PhotoImage(resize_flour)

        potato = Image.open("PicsforFinal/Dishes Pics/banhcuon/potato - Edited.png")
        resize_potato = potato.resize((100, 100))
        self.potato_pic = ImageTk.PhotoImage(resize_potato)

        ground_meat = Image.open("PicsforFinal/Dishes Pics/banhcuon/ground meat - Edited.png")
        resize_ground_meat = ground_meat.resize((100, 100))
        self.ground_meat_pic = ImageTk.PhotoImage(resize_ground_meat)

        wood_ear = Image.open("PicsforFinal/Dishes Pics/banhcuon/wood ear - Edited.png")
        resize_wood_ear = wood_ear.resize((100, 100))
        self.wood_ear_pic = ImageTk.PhotoImage(resize_wood_ear)

        basket = Image.open("PicsforFinal/Basket.png")
        resize_basket = basket.resize((500, 500))
        self.basket_pic = ImageTk.PhotoImage(resize_basket)

        self.basket_ob = self.canvas.create_image(220, 60, anchor=tk.NW, image=self.basket_pic)

        self.correct_list = [self.carrot_pic, self.flour_pic, self.potato_pic, self.ground_meat_pic, self.wood_ear_pic]

        # Bind the canvas and main window to respond to mouse button and keyboard entry
        self.canvas.bind("<Button-1>", self.chooseBall)
        self.mainWin.bind("<Up>", self.moveBallUp)
        self.mainWin.bind("<Down>", self.moveBallDown)
        self.mainWin.bind("<Left>", self.moveBallLeft)
        self.mainWin.bind("<Right>", self.moveBallRight)

        self.userBasket = []




        # Create an instance variable to hold which ball the user has selected
        self.selectedBall = None  ##why none, can it take any other value???!?!?

        # Save info about the balls.  This randomizes the balls, and their speeds,
        # and uses a dictionary keyed by the ID from the canvas.  Each entry in the
        # dictionary is also a dictionary, with separate keys values for each feature
        self.ballCollection = {}
        for ballColor in self.correct_list:
            nextDict = {}
            xStart = random.randint(30, 280)
            yStart = random.randint(30, 280)
            deltaX = 10
            deltaY = 10
            nextBall = self.canvas.create_image(xStart, yStart, anchor=tk.NW, image=ballColor)
            nextDict['xDist'] = deltaX
            nextDict['yDist'] = deltaY
            nextDict['moving'] = True
            nextDict['correct'] = True
            self.ballCollection[nextBall] = nextDict

        self.correct_listID =[]
        for i in self.ballCollection:
            if self.ballCollection[i]['correct']:
                self.correct_listID.append(i)

    def run(self):
        try:
            while True:
                self.mainWin.update_idletasks()  # redraw
                self.mainWin.update()

        except tk.TclError:
            pass  # to avoid errors when the window is closed

    def stop(self):
        self.mainWin.destroy()

    def reset(self):
        self.namelabel.destroy()
        self.buttonNext.destroy()
        # create intro label
        txt = self.nameEntry.get()

        self.namelabel = tk.Label(self.canvas, bg="pink", bd=10, font="Times 20",fg="white",
                                  justify=tk.CENTER, relief=tk.GROOVE,
                                  width=25, height=2
                                  )
        self.namelabel["text"] = "Hi, " + txt + "! Welcome to Ngon!"
        self.namelabel.place(x=550, y=200)

        self.welcomelabel = tk.Label(self.canvas, bg="pink", bd=10, font="Times 20",fg="white",
                                     justify=tk.CENTER, relief=tk.GROOVE, height=2,
                                     width=30, text="Click 'Next' or Hit 'Enter' to continue"
                                     )
        self.welcomelabel.place(x=525, y=300)

        imageNextButton = Image.open("PicsforFinal/NextButtonFinal.png")
        resizeNextButton = imageNextButton.resize((128, 38))
        self.imageButton = ImageTk.PhotoImage(resizeNextButton)
        self.buttonNext = tk.Button(self.canvas,
                                    command=self.reset1, image=self.imageButton)

        self.buttonNext.place(x=800, y=400)
        self.buttonNext.bind("<Return>", self.reset1)


    def reset1(self):
        self.namelabel.destroy()
        self.buttonNext.destroy()
        self.welcomelabel.destroy()

        # create Instruction label
        #
        self.Instruction = tk.Label(self.canvas, bg="pink", bd=10, font="Times 20", fg="white",
                                    justify=tk.CENTER, relief=tk.GROOVE,
                                    width=30, height=10
                                    )
        self.Instruction["text"] = "Instructions"
        self.Instruction.place(x=500, y=100)


        # create Button
        imageNextButton = Image.open("PicsforFinal/NextButtonFinal.png")
        resizeNextButton = imageNextButton.resize((128, 38))
        self.imageButton = ImageTk.PhotoImage(resizeNextButton)
        self.buttonNext = tk.Button(self.canvas,
                                    command=self.Easy, image=self.imageButton)

        self.buttonNext.place(x=800, y=400)

    def Easy(self):
        self.Instruction.destroy()
        self.buttonNext.destroy()
        self.canvas.delete('all')
        self.nameEntry.destroy()

        image = Image.open("PicsforFinal/BackgroundFinal.png")
        self.canvas.image = ImageTk.PhotoImage(image)
        self.background=self.canvas.create_image(0, 0, image=self.canvas.image, anchor="nw")

        self.createBall()
        self.go()

    def go(self):
        """Takes no inputs, and runs its own loop for the GUI.  This is so we can move
        the balls without waiting for some user input."""
        try:
            while True:
                self.moveBalls()
                self.mainWin.update_idletasks()  # redraw
                self.mainWin.update()  # process events
        except tk.TclError:
            pass  # to avoid errors when the window is closed

    def moveBalls(self):
        """Takes no inputs, and moves the balls in the ball list.  It bounces
        back when it reaches the walls of the canvas"""
        for ballId in self.ballCollection:
            ballInfo = self.ballCollection[ballId]
            if ballInfo['moving']:
                (x0, y0) = self.canvas.coords(ballId)
                if x0 >= 800 or x0 <= 10:
                    ballInfo['xDist'] = - ballInfo['xDist']
                if y0 >= 370 or y0 <= 30:
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
        ballSet = self.canvas.find_overlapping(x -10, y - 10, x + 10, y + 10)
        newballSet = tuple(item for item in ballSet if item != self.background)
        try:
            if len(ballSet) > 0:
                self.selectedBall = newballSet[0]
                ballInfo = self.ballCollection[self.selectedBall]
                ballInfo['moving'] = False
                self.userBasket.append(self.selectedBall)
                self.canvas.moveto(self.selectedBall,420, 400)
            if len(self.userBasket) == len(self.correct_listID):
                self.Result()
        except:
            pass


    def moveBallUp(self, event):
        """Callback function that is triggered by the user typing the up arrow. It checks if any ball
        has been selected, and if so it moves it up by 5 pixels."""
        if self.selectedBall != None:
            self.canvas.move(self.selectedBall, 0, -5)


    def moveBallDown(self, event):
        """Callback function that is triggered by the user typing the down arrow. It checks if any ball
        has been selected, and if so it moves it down by 5 pixels."""
        if self.selectedBall != None:
            self.canvas.move(self.selectedBall, 0, 5)


    def moveBallLeft(self, event):
        """Callback function that is triggered by the user typing the left arrow. It checks if any ball
        has been selected, and if so it moves it left by 5 pixels."""
        if self.selectedBall != None:
            self.canvas.move(self.selectedBall, -5, 0)

    def moveBallRight(self, event):
        """Callback function that is triggered by the user typing the right arrow. It checks if any ball
        has been selected, and if so it moves it right by 5 pixels."""
        if self.selectedBall != None:
            self.canvas.move(self.selectedBall, 5, 0)

    def Result(self):
        self.canvas.delete('all')
        image = Image.open("PicsforFinal/BackgroundFinal.png")
        self.canvas.image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor="nw")

        avatar = Image.open("PicsforFinal/IMG_0339.PNG")
        resizeavatar = avatar.resize((350, 350))
        self.Avapic = ImageTk.PhotoImage(resizeavatar)
        # self.AvaLabel = tk.Label(self.canvas, image=self.Avapic)
        self.canvas.create_image(100, 150, anchor=tk.NW, image=self.Avapic)

        self.resultlabel = tk.Label(self.canvas, bg="pink", bd=10, font="Times 20", fg="white",
                                    justify=tk.CENTER, relief=tk.GROOVE,
                                    width=30, height=10
                                    )
        self.resultlabel.place(x=500, y=100)

        if set(self.userBasket) == set(self.correct_listID):
            self.resultlabel["text"] = "Congratulations"
        else:
            self.resultlabel["text"] = "Shame"

# ------------------ Main program ----------------------

myGui = BasicGui()
myGui.run()