from tkinter import *
import tkinter.messagebox

class atm:
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(100 * blank_space + "C&S Bank ATM System")
        self.root.geometry("810x635+280+0")
        self.root.configure(background="gainsboro")
        # =============================================== Frames ===============================================
        MainFrame = Frame(self.root, bd=20, width=784, height=700, relief=RIDGE)
        MainFrame.grid()
        TopFrame1 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame1.grid(row=1, column=0, padx=5)
        TopFrame2 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame2.grid(row=0, column=0, padx=5)

        TopFrame2Left = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Left.grid(row=0, column=0, padx=3)
        TopFrame2Mid = Frame(TopFrame2, bd=5, width=200, height=300, relief=RIDGE)
        TopFrame2Mid.grid(row=0, column=1, padx=5)
        TopFrame2Right = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Right.grid(row=0, column=2, padx=5)

        # =============================================== Functions =============================================
        def enter_Pin():
            pinNo = self.txtReceipt.get("1.0", "end-1c")

            if (pinNo == str("2021")) or (pinNo == str("4444")) or (pinNo == str("6666")):
                self.txtReceipt.delete("1.0", END)

                self.txtReceipt.insert(END, '\t\t ATM' + "\n\n")
                self.txtReceipt.insert(END, 'Withdraw Cash\t\t\t\t Loan' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'Cash with Receipt\t\t\t\t Deposit' + "\n\n\n\n\n")
                self.txtReceipt.insert(END, 'Balance Cash\t\t\t Request New Pin' + "\n\n\n\n\n")
                self.txtReceipt.insert(END, 'Mini Statement\t\t\t Print Statement' + "\n\n\n\n")

                self.button_right1 = Button(TopFrame2Right, width=24, height=4, state=NORMAL, text="<-------<<",
                                            command=Loan)
                self.button_right1.grid(row=0, column=0, padx=2, pady=2)
                self.button_right2 = Button(TopFrame2Right, width=24, height=4, state=NORMAL, text="<-------<<",
                                            command=deposit)
                self.button_right2.grid(row=1, column=0, padx=2, pady=2)
                self.button_right3 = Button(TopFrame2Right, width=24, height=4, state=NORMAL, text="<-------<<",
                                            command=request_nrw_pin)
                self.button_right3.grid(row=2, column=0, padx=2, pady=2)
                self.button_right4 = Button(TopFrame2Right, width=24, height=4, state=NORMAL, text="<-------<<",
                                            command=statement)
                self.button_right4.grid(row=3, column=0, padx=2, pady=2)

                self.button_left1 = Button(TopFrame2Left, width=24, height=4, state=NORMAL, text=">>------->",
                                           command=withdrawcash)
                self.button_left1.grid(row=0, column=0, padx=2, pady=2)
                self.button_left2 = Button(TopFrame2Left, width=24, height=4, state=NORMAL, text=">>------->",
                                           command=withdrawcash)
                self.button_left2.grid(row=1, column=0, padx=2, pady=2)
                self.button_left3 = Button(TopFrame2Left, width=24, height=4, state=NORMAL, text=">>------->",
                                           command=balance)
                self.button_left3.grid(row=2, column=0, padx=2, pady=2)
                self.button_left4 = Button(TopFrame2Left, width=24, height=4, state=NORMAL, text=">>------->",
                                           command=statement)
                self.button_left4.grid(row=3, column=0, padx=2, pady=2)
            else:
                self.txtReceipt.delete("1.0", END)
                self.txtReceipt.insert(END, 'invalid pin number' + "\n\n")

        def clear():
            self.txtReceipt.delete("1.0", END)
            self.button_left1 = Button(TopFrame2Left, width=24, height=4, state=DISABLED, text=">>------->")
            self.button_left1.grid(row=0, column=0, padx=2, pady=2)
            self.button_left2 = Button(TopFrame2Left, width=24, height=4, state=DISABLED, text=">>------->")
            self.button_left2.grid(row=1, column=0, padx=2, pady=2)
            self.button_left3 = Button(TopFrame2Left, width=24, height=4, state=DISABLED, text=">>------->")
            self.button_left3.grid(row=2, column=0, padx=2, pady=2)
            self.button_left4 = Button(TopFrame2Left, width=24, height=4, state=DISABLED, text=">>------->")
            self.button_left4.grid(row=3, column=0, padx=2, pady=2)

            # =================================================widget right===================================
            self.button_right1 = Button(TopFrame2Right, width=24, height=4, state=DISABLED, text="<-------<<")
            self.button_right1.grid(row=0, column=0, padx=2, pady=2)
            self.button_right2 = Button(TopFrame2Right, width=24, height=4, state=DISABLED, text="<-------<<")
            self.button_right2.grid(row=1, column=0, padx=2, pady=2)
            self.button_right3 = Button(TopFrame2Right, width=24, height=4, state=DISABLED, text="<-------<<")
            self.button_right3.grid(row=2, column=0, padx=2, pady=2)
            self.button_right4 = Button(TopFrame2Right, width=24, height=4, state=DISABLED, text="<-------<<")
            self.button_right4.grid(row=3, column=0, padx=2, pady=2)

        def insert0():
            value0 = 0
            self.txtReceipt.insert(END, value0)
        def insert1():
            value1 = 1
            self.txtReceipt.insert(END, value1)
        def insert2():
            value2 = 2
            self.txtReceipt.insert(END, value2)
        def insert3():
            value3 = 3
            self.txtReceipt.insert(END, value3)
        def insert4():
            value4 = 4
            self.txtReceipt.insert(END, value4)
        def insert5():
            value5 = 5
            self.txtReceipt.insert(END, value5)
        def insert6():
            value6 = 6
            self.txtReceipt.insert(END, value6)
        def insert7():
            value7 = 7
            self.txtReceipt.insert(END, value7)
        def insert8():
            value8 = 8
            self.txtReceipt.insert(END, value8)
        def insert9():
            value9 = 9
            self.txtReceipt.insert(END, value9)
        def cancel():
            Cancel = tkinter.messagebox.askyesno("ATM", "Confirm if you want to cancel")
            if Cancel > 0:
                self.root.destroy()
                return
        def withdrawcash():
            enter_Pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.focus_set()
        def Loan():
            enter_Pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END, 'Loan $')
            self.txtReceipt.focus_set()
        def deposit():
            enter_Pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.focus_set()
        def request_nrw_pin():
            enter_Pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END, '\t    Welcome to C&S Bank' + '\n')
            self.txtReceipt.insert(END, '    New pin will be send to your home address\n')

            self.txtReceipt.insert(END, 'Withdraw Cash\t\t\t Loan' + "\n\n\n\n")
            self.txtReceipt.insert(END, 'Cash with Receipt\t\t\t Deposit' + "\n\n\n\n\n")
            self.txtReceipt.insert(END, 'Balance Cash\t\t\t Request New Pin' + "\n\n\n\n\n")
            self.txtReceipt.insert(END, 'Mini Statement\t\t\t Print Statement' + "\n\n\n\n")
            self.txtReceipt.insert(END, '\t\tThans for using C&S Bank\n')

        def balance():
            enter_Pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END, '\tWelcome to C&S Bank')
            self.txtReceipt.insert(END, ' 1296$' + "\n")
            self.txtReceipt.insert(END, 'Withdraw Cash\t\t\t Loan' + "\n\n\n\n")
            self.txtReceipt.insert(END, 'Cash with Receipt\t\t\t Deposit' + "\n\n\n\n\n")
            self.txtReceipt.insert(END, 'Balance Cash\t\t\t Request New Pin' + "\n\n\n\n\n")
            self.txtReceipt.insert(END, 'Mini Statement\t\t\t Print Statement' + "\n\n\n\n")
            self.txtReceipt.insert(END, '\t\tThans for using C&S Bank\n')

        def statement():
            pinNo1 = str(self.txtReceipt.get("1.0", "end-1c"))
            pinNo2 = str(pinNo1)
            pinNo3 = float(pinNo2)
            pinNo4 = float(1296 - (pinNo3))
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END, '\n\t' + str(pinNo4) + '\t\t')
            self.txtReceipt.insert(END, ' 1294$' + "\n")
            self.txtReceipt.insert(END, '\t\t\n\n Account Balance $' + str(pinNo4) + "\t\t\n\n")
            self.txtReceipt.insert(END, 'Rent\t\t\t\t 1200 $' + "\n\n")
            self.txtReceipt.insert(END, 'Tesco\t\t\t\t 79.36 $' + "\n\n")
            self.txtReceipt.insert(END, 'Rent\t\t\t\t 1200 $' + "\n\n")
            self.txtReceipt.insert(END, 'Student Loan\t\t\t\t 69.72 $' + "\n\n")

        # =============================================== Widget left ===============================================

        self.txtReceipt = Text(TopFrame2Mid, height=18, width=42, bd=12, font=('arial', 9, 'bold'))
        self.txtReceipt.grid(row=0, column=0)

        self.button_left1 = Button(TopFrame2Left, width=24, height=4, state=DISABLED, text="LOGIN",
                                   command=withdrawcash)
        self.button_left1.grid(row=0, column=0, padx=2, pady=2)
        self.button_left2 = Button(TopFrame2Left, width=24, height=4, state=DISABLED, text="LOGIN",
                                   command=withdrawcash)
        self.button_left2.grid(row=1, column=0, padx=2, pady=2)
        self.button_left3 = Button(TopFrame2Left, width=24, height=4, state=DISABLED, text="LOGIN", command=balance)
        self.button_left3.grid(row=2, column=0, padx=2, pady=2)
        self.button_left4 = Button(TopFrame2Left, width=24, height=4, state=DISABLED, text="LOGIN", command=statement)
        self.button_left4.grid(row=3, column=0, padx=2, pady=2)

        # ================================================= widget right ============================================
        self.button_right1 = Button(TopFrame2Right, width=24, height=4, state=DISABLED, text="LOGIN", command=Loan)
        self.button_right1.grid(row=0, column=0, padx=2, pady=2)
        self.button_right2 = Button(TopFrame2Right, width=24, height=4, state=DISABLED, text="LOGIN", command=deposit)
        self.button_right2.grid(row=1, column=0, padx=2, pady=2)
        self.button_right3 = Button(TopFrame2Right, width=24, height=4, state=DISABLED, text="LOGIN",
                                    command=request_nrw_pin)
        self.button_right3.grid(row=2, column=0, padx=2, pady=2)
        self.button_right4 = Button(TopFrame2Right, width=24, height=4, state=DISABLED, text="LOGIN", command=statement)
        self.button_right4.grid(row=3, column=0, padx=2, pady=2)

        # ================================================= Number Button=======================================
        self.button1 = Button(TopFrame1, width=24, height=3, text="1", font=('arial', 9, 'bold'),command=insert1)
        self.button1.grid(row=2, column=0, padx=4, pady=4)
        self.button2 = Button(TopFrame1, width=24, height=3, text="2",font=('arial', 9, 'bold'), command=insert2)
        self.button2.grid(row=2, column=1, padx=4, pady=4)
        self.button3 = Button(TopFrame1, width=24, height=3, text="3",font=('arial', 9, 'bold'), command=insert3)
        self.button3.grid(row=2, column=2, padx=4, pady=4)
        self.buttonCE = Button(TopFrame1, width=24, height=3, text="CANCEL",font=('arial', 9, 'bold'), command=cancel)
        self.buttonCE.grid(row=2, column=3, padx=4, pady=4)

        # =======================================================================================================
        self.button4 = Button(TopFrame1, width=24, height=3, text="4",font=('arial', 9, 'bold'), command=insert4)
        self.button4.grid(row=3, column=0, padx=4, pady=4)
        self.button5 = Button(TopFrame1, width=24, height=3, text="5",font=('arial', 9, 'bold'), command=insert5)
        self.button5.grid(row=3, column=1, padx=4, pady=4)
        self.button6 = Button(TopFrame1, width=24, height=3, text="6",font=('arial', 9, 'bold'), command=insert6)
        self.button6.grid(row=3, column=2, padx=4, pady=4)
        self.buttonCl = Button(TopFrame1, width=24, height=3, text="CLEAR",font=('arial', 9, 'bold'), command=clear)
        self.buttonCl.grid(row=3, column=3, padx=4, pady=4)

        # =======================================================================================================
        self.button7 = Button(TopFrame1, width=24, height=3, text="7",font=('arial', 9, 'bold'), command=insert7)
        self.button7.grid(row=4, column=0, padx=4, pady=4)
        self.button8 = Button(TopFrame1, width=24, height=3, text="8",font=('arial', 9, 'bold'), command=insert8)
        self.button8.grid(row=4, column=1, padx=4, pady=4)
        self.button9 = Button(TopFrame1, width=24, height=3, text="9",font=('arial', 9, 'bold'), command=insert9)
        self.button9.grid(row=4, column=2, padx=4, pady=4)
        self.buttonEnter = Button(TopFrame1, width=24, height=3, text="ENTER",font=('arial', 9, 'bold'), command=enter_Pin)
        self.buttonEnter.grid(row=4, column=3, padx=4, pady=4)

        # ======================================================================================================
        self.buttonSp1 = Button(TopFrame1, width=24, height=3, text="")
        self.buttonSp1.grid(row=5, column=0, padx=4, pady=4)
        self.button0 = Button(TopFrame1, width=24, height=3, text="0",font=('arial', 9, 'bold'), command=insert0)
        self.button0.grid(row=5, column=1, padx=4, pady=4)
        self.buttonSp2 = Button(TopFrame1, width=24, height=3, text="")
        self.buttonSp2.grid(row=5, column=2, padx=4, pady=4)
        self.buttonSp3 = Button(TopFrame1, width=24, height=3, text="")
        self.buttonSp3.grid(row=5, column=3, padx=4, pady=4)


if __name__ == '__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()
