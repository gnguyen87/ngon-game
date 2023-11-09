import random
import tkinter as tk


class BasicGui:

    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Raindrops on my guitar")
        #create canvas
        self.canvas = tk.Canvas(self.mainWin, bg="maroon",
                                width=250, height=500, bd=0)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        self.canvas.grid(row=0, column=0)
        #create frame
        self.frame = tk.Frame(self.mainWin, bg="light gray",
                                width=250, height=500, bd=0)
        self.frame.grid(row=0, column=1)
        # Show all of the canvas
        buttonQuit = tk.Button(self.frame,
                            text = 'Quit',
                            font= "Arial 12",
                            command = self.stop)
        buttonQuit.grid(row=0, column=0)
        buttonNext = tk.Button(self.frame,
                            text = 'Next',
                            font= "Arial 12",
                            command = self.reset)
        buttonNext.grid(row=1, column=0)
        # Create an instance variable to hold which ball the user has selected
        self.selectedBall = None  ##why none, can it take any other value???!?!?

        # Save info about the balls.  This randomizes the balls, and their speeds,
        # and uses a dictionary keyed by the ID from the canvas.  Each entry in the
        # dictionary is also a dictionary, with separate keys values for each feature
        self.ballCollection = {}



    def run(self):
        try:
            while True:
                self.mainWin.update_idletasks() # redraw
                self.moveBalls()
                self.mainWin.update() # process events
        except tk.TclError:
            pass # to avoid errors when the window is closed


    def stop(self):
        self.mainWin.destroy()

    def reset(self):
        self.canvas.delete('all')
        self.ballCollection = {}
        self.canvas = tk.Canvas(self.mainWin, bg="light green",
                                width=250, height=500, bd=0)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        self.canvas.grid(row=0, column=0)
        # # create frame
        # self.frame = tk.Frame(self.mainWin, bg="light gray",
        #                       width=250, height=500, bd=0)
        # self.frame.grid(row=0, column=1)
        # # Show all of the canvas
        # buttonQuit = tk.Button(self.frame,
        #                        text='Quit',
        #                        font="Arial 12",
        #                        command=self.stop)
        # buttonQuit.grid(row=0, column=0)
        buttonNext = tk.Button(self.frame,
                               text='Next',
                               font="Arial 12",
                               command=self.reset1)
        buttonNext.grid(row=1, column=0)

    def reset1(self):
        self.canvas.delete('all')
        self.ballCollection = {}
        self.canvas["bg"] = "pink"
        # self.canvas = tk.Canvas(self.mainWin, bg="pink",
        #                         width=250, height=500, bd=0)
        # self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        # self.canvas.grid(row=0, column=0)
        # create frame
        # self.frame = tk.Frame(self.mainWin, bg="light gray",
        #                       width=250, height=500, bd=0)
        # self.frame.grid(row=0, column=1)
        # # Show all of the canvas
        # buttonQuit = tk.Button(self.frame,
        #                        text='Quit',
        #                        font="Arial 12",
        #                        command=self.stop)
        # buttonQuit.grid(row=0, column=0)
        # buttonNext = tk.Button(self.frame,
        #                        text='Next',
        #                        font="Arial 12",
        #                        command=self.reset)
        # buttonNext.grid(row=1, column=0)
        buttonEasy = tk.Button(self.canvas,
                               text='EASY',
                               font="Arial 12",
                               height = 5,
                               bg = "yellow",
                               command= self.resetEasy)
        buttonEasy.grid(row=1, column=1)

    def resetEasy(self):
        self.canvas.delete('all')
        self.canvas = tk.Canvas(self.mainWin, bg="yellow",
                                width=250, height=500, bd=0)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        self.canvas.grid(row=0, column=0)
        # create frame
        self.frame = tk.Frame(self.mainWin, bg="light gray",
                              width=250, height=500, bd=0)
        self.frame.grid(row=0, column=1)
        # Show all of the canvas
        buttonQuit = tk.Button(self.frame,
                               text='Quit',
                               font="Arial 12",
                               command=self.stop)
        buttonQuit.grid(row=0, column=0)
        buttonNext = tk.Button(self.frame,
                               text='Next',
                               font="Arial 12",
                               command=self.reset)
        buttonNext.grid(row=1, column=0)

        self.canvas.bind("<Button-1>", self.chooseBall)
        self.mainWin.bind("<Up>", self.moveBallUp)
        self.mainWin.bind("<Down>", self.moveBallDown)
        self.mainWin.bind("<Left>", self.moveBallLeft)
        self.mainWin.bind("<Right>", self.moveBallRight)


        for ballColor in ['red', 'green', 'blue', 'LightBlue', 'LightGreen']:
            nextDict = {}
            xStart = random.randint(20, 220)
            yStart = random.randint(20, 480)
            deltaX = random.randint(1, 2)
            deltaY = random.randint(1, 2)
            nextBall = self.canvas.create_oval(xStart, yStart, xStart + 20, yStart + 20,
                                               fill=ballColor, outline="black")
            nextDict['xDist'] = deltaX
            nextDict['yDist'] = deltaY
            nextDict['moving'] = True
            self.ballCollection[nextBall] = nextDict

    def moveBalls(self):
        """Takes no inputs, and moves the balls in the ball list.  It bounces
        back when it reaches the walls of the canvas"""
        for ballId in self.ballCollection:
            ballInfo = self.ballCollection[ballId]
            if ballInfo['moving']:
                (x0, y0, x1, y1) = self.canvas.coords(ballId)
                if x1 >= 250 or x0 <= 5:
                    ballInfo['xDist'] = - ballInfo['xDist']
                if y1 >= 500 or y0 <= 5:
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
        ballSet = self.canvas.find_overlapping(x - 5, y - 5, x + 5, y + 5)
        if self.selectedBall != None:
            ballInfo = self.ballCollection[self.selectedBall]
            ballInfo['moving'] = True
            self.selectedBall = None
        elif len(ballSet) > 0:
            self.selectedBall = ballSet[0]
            ballInfo = self.ballCollection[self.selectedBall]
            ballInfo['moving'] = False

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


# ------------------ Main program ----------------------

myGui = BasicGui()
myGui.run()