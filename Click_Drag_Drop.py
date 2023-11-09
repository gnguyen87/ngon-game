
"""
Group members: Linh Do, Na Nguyen and Tam Nguyen.
Date: Dec 14 2022
Class: COMP 123
"""


import random
import tkinter as tk
import PIL.Image as Image
from tkinter import YES
import PIL.ImageTk as ImageTk


class Canvas2:

    def __init__(self):
        """Construction function that creates window and widgets within our first canvas: Intro"""
        self.correct_list = [1]
        # self.basket = []
        self.mainWin = tk.Tk()
        self.mainWin.title("Ngon")
        self.mainWin.geometry("960x540")
        self.ballCollection = {}
        self.selectedBall = None
        self.userBasket = []

        # create canvas
        self.canvas = tk.Canvas(self.mainWin, width=960, height=540)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        self.canvas.grid(columnspan=YES, rowspan=YES)

        image = Image.open("banhcuon/BackgroundFinal.png")
        self.canvas.image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor="nw")

        # create name entry widget
        self.nameEntry = tk.Entry(self.canvas, bg="pink", bd=10, font="Times 20", fg="white",
                                  justify=tk.CENTER, relief=tk.GROOVE, width=25)
        self.nameEntry.place(x=560, y=300)

        # create intro label
        self.namelabel = tk.Label(self.canvas, bg="pink", bd=10, font="Times 20", fg="white",
                                  text="Hi there! \n Please enter your name.", justify=tk.CENTER, relief=tk.GROOVE,
                                  width=25,
                                  )
        self.txt = str(self.nameEntry.get())
        self.namelabel.place(x=550, y=200)

        # create Avatar Icon
        avatar = Image.open("banhcuon/IMG_0339.PNG")
        resizeavatar = avatar.resize((350, 350))
        self.Avapic = ImageTk.PhotoImage(resizeavatar)
        self.canvas.create_image(100, 150, anchor=tk.NW, image=self.Avapic)

        # create next button
        self.next = ImageTk.PhotoImage(Image.open('banhcuon/4.png'))
        self.buttonNext = tk.Button(self.mainWin,
                                    command=self.resetToCanvas2, image=self.next)

        self.buttonNext.place(x=700, y=400)

        self.correct_list_easy = ["ground meat", "wood ear", "flour"]

    def resetToCanvas2(self):
        """Reset our canvas to canvas 2, destroying certain previous widgets and adding new ones"""
        self.namelabel.destroy()
        self.buttonNext.destroy()

        #create welcome name label that has user entry name
        txt = self.nameEntry.get()

        self.WelcomeNamelabel = tk.Label(self.canvas, bg="pink", bd=10, font="Times 20", fg="white",
                                         justify=tk.CENTER, relief=tk.GROOVE,
                                         width=25, height=2
                                         )
        self.WelcomeNamelabel["text"] = "Hi, " + txt + "! Welcome to Ngon!"
        self.WelcomeNamelabel.place(x=550, y=200)

        #create Next Label
        self.Nextlabel = tk.Label(self.canvas, bg="pink", bd=10, font="Times 20", fg="white",
                                  justify=tk.CENTER, relief=tk.GROOVE, height=2,
                                  width=30, text="Click 'Next' to continue"
                                  )
        self.Nextlabel.place(x=525, y=300)

        #create Next Button
        self.buttonNext = tk.Button(self.mainWin,
                                    command=self.resetToCanvas3, image=self.next)

        self.buttonNext.place(x=700, y=400)


    def resetToCanvas3(self):
        """Function to change to canvas 3 with instructions for the player"""
        self.canvas.delete('all')
        self.buttonNext.destroy()
        self.nameEntry.destroy()
        self.Nextlabel.destroy()
        self.WelcomeNamelabel.destroy()

        #create instruction canvas
        image = Image.open("banhcuon/backgroundinstruction.png")
        self.canvas.image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor="nw")

        #create Next Button
        self.buttonNext = tk.Button(self.mainWin,
                                    command=self.LevelMenu, image=self.next)

        self.buttonNext.place(x=700, y=400)

    def LevelMenu(self):
        """Function to create our level menu. Each label that depicts a level will lead
        user to the canvas with the background of the dish"""
        self.canvas.destroy()
        self.buttonNext.destroy()

        #create canvas with level menu and buttons
        self.background = ImageTk.PhotoImage(Image.open("banhcuon/Canva4.png"))
        self.canvas = tk.Canvas(self.mainWin, bg="grey",
                                width=960, height=540, bd=0)
        self.canvas.create_image(50, 50, anchor="nw", image=self.background)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        self.canvas.grid(row=0, column=0)

        self.easy = ImageTk.PhotoImage(Image.open('banhcuon/1.png'))
        self.buttonEasy = tk.Button(self.mainWin,
                                    command=self.resetEasy1, image=self.easy)
        self.buttonEasy.place(x=80, y=400)

        self.medium = ImageTk.PhotoImage(Image.open('banhcuon/2.png'))
        self.buttonMedium = tk.Button(self.mainWin,
                                      command=self.resetMedium3, image=self.medium)
        self.buttonMedium.place(x=380, y=400)

        self.hard = ImageTk.PhotoImage(Image.open('banhcuon/3.png'))
        self.buttonHard = tk.Button(self.mainWin,
                                    command=self.sorryCanvas, image=self.hard)
        self.buttonHard.place(x=700, y=400)


    def resetEasy1(self):
        """Function that creates canvas with background information of the Easy level dish"""
        self.canvas.delete('all')
        self.buttonEasy.destroy()
        self.buttonMedium.destroy()
        self.buttonHard.destroy()

        #create background canvas with information
        self.banhcuonBackground = ImageTk.PhotoImage(Image.open("banhcuon/Banhcuon.png"))
        self.canvas.create_image(50, 50, anchor="nw", image=self.banhcuonBackground)
        self.next = ImageTk.PhotoImage(Image.open('banhcuon/4.png'))

        #create Next Button
        self.buttonNext = tk.Button(self.mainWin,
                                        command=self.resetEasy2, image=self.next)
        self.buttonNext.place(x=700, y=400)



    def resetEasy2(self):
        """Function that creates canvas with hint for user at the Easy level dish"""
        self.canvas.delete('all')
        self.buttonNext.destroy()

        #create canvas
        self.canva5 = ImageTk.PhotoImage(Image.open("banhcuon/Canva5.png"))
        self.canvas.create_image(50, 50, anchor="nw", image=self.canva5)

        #create Next Button
        self.next = ImageTk.PhotoImage(Image.open('banhcuon/4.png'))
        self.buttonNext = tk.Button(self.mainWin,
                                        command=self.resetEasy3, image=self.next)
        self.buttonNext.place(x=700, y=400)

    def resetEasy3(self):
        """Function that constructs all the moving ingredients for the Easy level dish"""
        self.canvas.delete('all')
        self.buttonNext.destroy()

        #create canvas
        self.canvaPlay = ImageTk.PhotoImage(Image.open("banhcuon/backgroundwithbasket.png"))
        self.image = self.canvas.create_image(50, 50, anchor="nw", image=self.canvaPlay)

        #create image objects of ingredients
        carrot = Image.open("banhcuon/carrot.png")
        resize_carrot = carrot.resize((85, 85))
        self.carrot_pic = ImageTk.PhotoImage(resize_carrot)

        flour = Image.open("banhcuon/flour.png")
        resize_flour = flour.resize((85, 85))
        self.flour_pic = ImageTk.PhotoImage(resize_flour)

        potato = Image.open("banhcuon/potato.png")
        resize_potato = potato.resize((85, 85))
        self.potato_pic = ImageTk.PhotoImage(resize_potato)

        ground_meat = Image.open("banhcuon/groundmeat.png")
        resize_ground_meat = ground_meat.resize((85, 85))
        self.ground_meat_pic = ImageTk.PhotoImage(resize_ground_meat)

        wood_ear = Image.open("banhcuon/woodear.png")
        resize_wood_ear = wood_ear.resize((85, 85))
        self.wood_ear_pic = ImageTk.PhotoImage(resize_wood_ear)


        self.canvas.bind("<Button-1>", self.chooseBall)

        # Create an instance variable to hold which ball the user has selected
        raw_list_name = ["carrot", "flour", "potato", "ground meat", "wood ear"]
        self.raw_list = [self.carrot_pic, self.flour_pic, self.potato_pic, self.ground_meat_pic, self.wood_ear_pic]
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
        self.correct_list_easy = ["ground meat", "wood ear", "flour"]

        self.correct_list = self.correct_list_easy.copy()

##########
    def resetMedium3(self):
        """Function that constructs all the moving ingredients for the Medium level dish"""
        self.canvas.delete('all')
        self.buttonNext.destroy()
        self.buttonEasy.destroy()
        self.buttonMedium.destroy()
        self.buttonHard.destroy()
        #create canvas
        self.canvaPlay = ImageTk.PhotoImage(Image.open("banhcuon/backgroundwithbasket.png"))
        self.image = self.canvas.create_image(50, 50, anchor="nw", image=self.canvaPlay)

        #create image objects of ingredients
        banhmi = Image.open("banhmi/banhmi.png")
        resize_banhmi = banhmi.resize((85, 85))
        self.banhmi_pic = ImageTk.PhotoImage(resize_banhmi)

        cilantro = Image.open("banhmi/cilantro.png")
        resize_cilantro = cilantro.resize((85, 85))
        self.cilantro_pic = ImageTk.PhotoImage(resize_cilantro)

        cucai = Image.open("banhmi/cucai.png")
        resize_cucai = cucai.resize((85, 85))
        self.cucai_pic = ImageTk.PhotoImage(resize_cucai)

        kewpie = Image.open("banhmi/kewpie.png")
        resize_kewpie = kewpie.resize((85, 85))
        self.kewpie_pic = ImageTk.PhotoImage(resize_kewpie)

        oregano = Image.open("banhmi/oregano.png")
        resize_oregano = oregano.resize((85, 85))
        self.oregano_pic = ImageTk.PhotoImage(resize_oregano)

        spices = Image.open("banhmi/spices.png")
        resize_spices = spices.resize((85, 85))
        self.spices_pic = ImageTk.PhotoImage(resize_spices)


        self.canvas.bind("<Button-1>", self.chooseBall)

        # Create an instance variable to hold which ball the user has selected
        raw_list_name = ["banhmi", "cilantro", "cucai", "kewpie", "oregano", "spices"]
        self.raw_list = [self.banhmi_pic ,self.cilantro_pic, self.cucai_pic, self.kewpie_pic, self.oregano_pic, self.spices_pic]
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
        self.correct_list_medium = ["banhmi", "cilantro", "spices"]

        self.correct_list = self.correct_list_medium.copy()



    def winCanvas(self):
        """Function to create canvas that shows message to user when they win"""
        self.canvas.delete('all')
        self.buttonNext.destroy()

        self.userBasket = []
        self.ballCollection = {}

        #create canvas
        image = Image.open("banhcuon/Win.png")
        self.winbg = ImageTk.PhotoImage(image)

        self.canvas.create_image(0, 0, anchor="nw", image=self.winbg)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))


        #create Quit Button
        button = Image.open("banhcuon/playagain.png")
        self.playagain = ImageTk.PhotoImage(button)
        self.buttonNext = tk.Button(self.canvas, command=self.LevelMenu,
                                     image=self.playagain)
        self.buttonNext.place(x=700, y=400)

    def loseCanvas(self):
        """Function to create canvas that shows message to user when they lose and a message indicating
        what mistake they made"""

        self.canvas.delete('all')
        self.buttonNext.destroy()
        self.userBasket = []
        self.ballCollection = {}

        #create canvas
        image = Image.open("banhcuon/Lose.png")
        self.losebg = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.losebg)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        # self.canvas.grid(row=0, column=0)
        #create label that indicate what mistake user makes
        self.Emsg = tk.Label(self.canvas)
        self.Emsg.place(x=650, y=10)
        self.Emsg.config(text="You might have selected " + self.wrong_item + ", which is wrong")


        #create Quit Button

        button = Image.open("banhcuon/playagain.png")
        self.playagain = ImageTk.PhotoImage(button)
        self.buttonNext = tk.Button(self.canvas, command=self.LevelMenu,
                                     image=self.playagain)
        self.buttonNext.place(x=700, y=400)




    def sorryCanvas(self):
        """Function to show message to user for pending program constructions"""
        self.canvas.delete('all')
        self.buttonNext.destroy()
        self.buttonEasy.destroy()
        self.buttonMedium.destroy()
        self.buttonHard.destroy()

        #create canvas
        loseBg = Image.open("banhcuon/backgroundwithcow.png")
        self.canva5 = ImageTk.PhotoImage(loseBg)
        self.canvas5 = tk.Canvas(self.mainWin,
                                 width=900, height=540, bd=0)

        self.canvas.create_image(0, 0, anchor="nw", image=self.canva5)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

        #create message label
        self.Emsg = tk.Label(self.canvas)
        self.Emsg.place(x=350, y=270)
        self.Emsg.config(text="We apologize. Gameplay not available yet. More updates coming soon!!!!")
        self.next = ImageTk.PhotoImage(Image.open('banhcuon/4.png'))

        #create Next Button
        self.next = ImageTk.PhotoImage(Image.open('banhcuon/4.png'))
        self.buttonNext = tk.Button(self.mainWin,
                                    command=self.LevelMenu, image=self.next)
        self.buttonNext.place(x=700, y=400)


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
        ballSet = self.canvas.find_overlapping(x - 25, y - 25, x + 25, y + 25)
        newballSet = tuple(item for item in ballSet if item != self.image and item != self.canvaPlay)
        try:
            if len(ballSet) > 0:
                self.selectedBall = newballSet[0]
                ballInfo = self.ballCollection[self.selectedBall]
                ballInfo['moving'] = False
                self.userBasket.append(self.selectedBall)
                self.canvas.moveto(self.selectedBall, 420, 450)
                print(self.userBasket)
                return self.userBasket
        except:
            pass

    def basketCheck(self):
        """Function that checks the user basket against the correct list of ingredients for the Easy level dish"""
        for i in self.userBasket:
            if self.id_name[i] not in self.correct_list:
                self.wrong_item = self.id_name[i]
                return False
        if len(self.userBasket) == len(self.correct_list):
            return True

    def go(self):
        """Takes no inputs, and runs its own loop for the GUI.  This is so we can move
        the balls without waiting for some user input."""
        try:
            while True:
                self.basketCheck()
                if len(self.userBasket) != len(self.correct_list) and self.basketCheck() != False:
                    self.moveBalls()
                    self.mainWin.update_idletasks()  # redraw
                    self.mainWin.update()  # process events
                elif self.basketCheck() == True:
                    self.mainWin.update_idletasks()  # redraw
                    self.mainWin.update()
                    self.winCanvas()
                elif self.basketCheck() == False:
                    self.mainWin.update_idletasks()  # redraw
                    self.mainWin.update()
                    self.loseCanvas()
        except tk.TclError:
            pass  # to avoid errors when the window is closed


    def stop(self):
        """Function to quit the program"""
        self.mainWin.destroy()
# ------------------ Main program ----------------------

myGui = Canvas2()
myGui.go()
