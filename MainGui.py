
# Import Module
from tkinter import *
from TshCalculator import TshCalculator

DISPLAY_START_POSITION_X = 700
DISPLAY_START_POSITION_Y = 100
DISPLAY_REC_WIDTH = 80

FONT_SIZE = 12

class MainGui():
    global label1
    global label2
    global label3
    global label4
    global label5
    global label6
    global label7
    global label8
    global label9
    global stringVarLabel1
    global stringVarLabel2
    global stringVarLabel3
    global stringVarLabel4
    global stringVarLabel5
    global stringVarLabel6
    global stringVarLabel7
    global stringVarLabel8
    global stringVarLabel9

    global textFullName
    global textBirthDay
    global buttonCalculate

    def __init__(self):
        # Create Tkinter Object
        self.root = Tk()

        # Set Geometry
        self.root.geometry("1000x600")

        self.tshCal = TshCalculator()

        self.init_gui()

    def gui_draw_rectangle(self, parentFrame, sizeX, sizeY, posX, posY):
        # Frame 1
        outerFrame = Frame(parentFrame,bg="black",width=sizeX,height=sizeY)
        outerFrame.pack()
        outerFrame.place(x=posX, y=posY)

        # Frame 2
        innerFrame = Frame(outerFrame,bg="white",width=sizeX,height=sizeY)
        innerFrame.pack(pady=2,padx=2)

    def gui_draw_answer(self, parentFrame):
        self.gui_draw_rectangle(parentFrame, DISPLAY_REC_WIDTH, DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_X, DISPLAY_START_POSITION_Y)
        self.gui_draw_rectangle(parentFrame, DISPLAY_REC_WIDTH, DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_X + DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_Y)
        self.gui_draw_rectangle(parentFrame, DISPLAY_REC_WIDTH, DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_X + 2 * DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_Y)
        self.gui_draw_rectangle(parentFrame, DISPLAY_REC_WIDTH, DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_X, DISPLAY_START_POSITION_Y + DISPLAY_REC_WIDTH)
        self.gui_draw_rectangle(parentFrame, DISPLAY_REC_WIDTH, DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_X + DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_Y + DISPLAY_REC_WIDTH)
        self.gui_draw_rectangle(parentFrame, DISPLAY_REC_WIDTH, DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_X + 2 * DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_Y + DISPLAY_REC_WIDTH)
        self.gui_draw_rectangle(parentFrame, DISPLAY_REC_WIDTH, DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_X, DISPLAY_START_POSITION_Y + 2 * DISPLAY_REC_WIDTH)
        self.gui_draw_rectangle(parentFrame, DISPLAY_REC_WIDTH, DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_X + DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_Y + 2 * DISPLAY_REC_WIDTH)
        self.gui_draw_rectangle(parentFrame, DISPLAY_REC_WIDTH, DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_X + 2 * DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_Y + 2 * DISPLAY_REC_WIDTH)

        self.stringVarLabel1 = StringVar()
        self.stringVarLabel2 = StringVar()
        self.stringVarLabel3 = StringVar()
        self.stringVarLabel4 = StringVar()
        self.stringVarLabel5 = StringVar()
        self.stringVarLabel6 = StringVar()
        self.stringVarLabel7 = StringVar()
        self.stringVarLabel8 = StringVar()
        self.stringVarLabel9 = StringVar()

        label1= Label(parentFrame, text="111", bg="#FFFFFF", font=FONT_SIZE, width=6, textvariable = self.stringVarLabel1)
        label1.place(x=DISPLAY_START_POSITION_X + 2,y=DISPLAY_START_POSITION_Y + 2.35 * DISPLAY_REC_WIDTH)

        label2= Label(parentFrame, text="222", bg="#FFFFFF", font=FONT_SIZE, width=6, textvariable = self.stringVarLabel2)
        label2.place(x=DISPLAY_START_POSITION_X + 2,y=DISPLAY_START_POSITION_Y + 1.35 * DISPLAY_REC_WIDTH)

        label3= Label(parentFrame, text="333", bg="#FFFFFF", font=FONT_SIZE, width=6, textvariable = self.stringVarLabel3)
        label3.place(x=DISPLAY_START_POSITION_X + 2,y=DISPLAY_START_POSITION_Y + 0.35 * DISPLAY_REC_WIDTH)

        label4= Label(parentFrame, text="444", bg="#FFFFFF", font=FONT_SIZE, width=6, textvariable = self.stringVarLabel4)
        label4.place(x=DISPLAY_START_POSITION_X + DISPLAY_REC_WIDTH + 2,y=DISPLAY_START_POSITION_Y + 2.35 * DISPLAY_REC_WIDTH)

        label2= Label(parentFrame, text="555", bg="#FFFFFF", font=FONT_SIZE, width=6, textvariable = self.stringVarLabel5)
        label2.place(x=DISPLAY_START_POSITION_X + DISPLAY_REC_WIDTH + 2,y=DISPLAY_START_POSITION_Y + 1.35 * DISPLAY_REC_WIDTH)

        label3= Label(parentFrame, text="666", bg="#FFFFFF", font=FONT_SIZE, width=6, textvariable = self.stringVarLabel6)
        label3.place(x=DISPLAY_START_POSITION_X + DISPLAY_REC_WIDTH + 2,y=DISPLAY_START_POSITION_Y + 0.35 * DISPLAY_REC_WIDTH)

        label4= Label(parentFrame, text="777", bg="#FFFFFF", font=FONT_SIZE, width=6, textvariable = self.stringVarLabel7)
        label4.place(x=DISPLAY_START_POSITION_X + 2 * DISPLAY_REC_WIDTH + 2,y=DISPLAY_START_POSITION_Y + 2.35 * DISPLAY_REC_WIDTH)

        label2= Label(parentFrame, text="888", bg="#FFFFFF", font=FONT_SIZE, width=6, textvariable = self.stringVarLabel8)
        label2.place(x=DISPLAY_START_POSITION_X + 2 * DISPLAY_REC_WIDTH + 2,y=DISPLAY_START_POSITION_Y + 1.35 * DISPLAY_REC_WIDTH)

        label3= Label(parentFrame, text="999", bg="#FFFFFF", font=FONT_SIZE, width=6, textvariable = self.stringVarLabel9)
        label3.place(x=DISPLAY_START_POSITION_X + 2 * DISPLAY_REC_WIDTH + 2,y=DISPLAY_START_POSITION_Y + 0.35 * DISPLAY_REC_WIDTH)

    def gui_draw_input(self, parentFrame):

        lblName = Label(parentFrame, text="Nhập họ và tên : ", fg="black", font=FONT_SIZE)
        lblName.place(x= 100, y = 150)

        lblBirthDay = Label(parentFrame, text="Nhập ngày sinh : ", fg="black", font=FONT_SIZE)
        lblBirthDay.place(x= 100, y = 200)

        # FullName
        self.textFullName = Text(parentFrame, height = 1, width = 30, font=11)
        self.textFullName.place(x= 280, y = 150)

        # BirthDay
        self.textBirthDay = Text(parentFrame, height = 1, width = 30, font=11)
        self.textBirthDay.place(x= 280, y = 200)

        buttonCalculate = Button(parentFrame, text ="Tính toán", font=11, width=10, height = 2, command = self.callback_calculate)
        buttonCalculate.place(x= 350, y = 350)

    def callback_calculate(self):
        strFullName = self.textFullName.get("1.0",END)
        strBirthDay = self.textBirthDay.get("1.0",END)
        strNumberOutput = self.tshCal.tsh_convert_name_and_birthday_to_number(strFullName, strBirthDay)
        self.display_output(strNumberOutput)

    def display_output(self, textNumber):
        arrayNum = ['', '', '', '', '', '', '', '', '', '']
        print("textNumber: " + str(textNumber))
        for i in range(len(textNumber) - 1):
            print("textNumber[i]: " + str(textNumber[i]))
            arrayNum[int(textNumber[i])] += textNumber[i]

        self.stringVarLabel1.set(arrayNum[1])
        self.stringVarLabel2.set(arrayNum[2])
        self.stringVarLabel3.set(arrayNum[3])
        self.stringVarLabel4.set(arrayNum[4])
        self.stringVarLabel5.set(arrayNum[5])
        self.stringVarLabel6.set(arrayNum[6])
        self.stringVarLabel7.set(arrayNum[7])
        self.stringVarLabel8.set(arrayNum[8])
        self.stringVarLabel9.set(arrayNum[9])

    def init_gui(self):
        self.gui_draw_rectangle(self.root, DISPLAY_REC_WIDTH, DISPLAY_REC_WIDTH, DISPLAY_START_POSITION_X, DISPLAY_START_POSITION_Y)
        self.gui_draw_answer(self.root)
        self.gui_draw_input(self.root)
        self.root.mainloop()
