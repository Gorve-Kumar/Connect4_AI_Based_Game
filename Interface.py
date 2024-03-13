from tkinter.messagebox import showinfo
import tkinter as tk
import Game

YELLOW = (255, 255, 0)
GREEN = (5, 99, 41)
PURPLE = (181, 16, 165)
ORANGE = (247, 120, 57)

class Interface(list):
    def __init__(self):  # Creates Window
        self.R = tk.Toplevel()
        self.R.title("4 IN A ROW")
        self.R.geometry('825x500+250+50')
        self.R.maxsize(825, 500)
        self.R.minsize(825, 500)
        self.R.configure(bg='#1e0e78')
        self.light_blue_color = '#a5e3fa'
        self.empty_text = '        '
        self.blue_color = '#1e0e78'
        self.font1 = "Comic Sans MS"
        self.font2 = "Ariel Black"
        self.username = ""
        self.games_played = str(0)
        self.games_won = str(0)
        self.Color = YELLOW
        self.Row = 5
        self.sq_size = 60
        self.Login_Page_Func()
        self.R.mainloop()


    def Login_Page_Func(self):
        self.F1 = tk.Frame(self.R, bg=self.light_blue_color, relief='groove', borderwidth=12)
        tk.Label(self.F1, text='\nLOGIN TO YOUR ACCOUNT', font=(self.font1, 18), bg=self.light_blue_color, fg=self.blue_color).grid(row=0, column=1), tk.Label(self.F1, text=self.empty_text, font=(self.font1, 10), bg=self.light_blue_color, fg='#8E0505').grid(row=1, column=0), tk.Label(self.F1, text=self.empty_text, font=(self.font1, 10), bg=self.light_blue_color, fg='#8E0505').grid(row=1, column=3), tk.Label(self.F1, text=self.empty_text, font=(self.font1, 12), bg=self.light_blue_color, fg='#8E0505').grid(row=3, column=1), tk.Label(self.F1, text=self.empty_text, font=(self.font1, 12), bg=self.light_blue_color, fg='#8E0505').grid(row=6, column=1), tk.Label(self.F1, text=self.empty_text, font=("Comic Sans MS", 12), bg=self.light_blue_color, fg='#8E0505').grid(row=8, column=1)
        tk.Label(self.F1, text=' Enter User Name: ', font=(self.font1, 14), bg=self.light_blue_color).grid(row=2, column=1)
        tk.Label(self.F1, text=' Enter Password: ', font=(self.font1, 14), bg=self.light_blue_color).grid(row=4, column=1)

        def LOG_FUNC():
            Accounts = []
            f = open('User_Accounts.txt', 'a+')
            f.seek(0)
            for item in f:
                Accounts.append(eval(item))
            f.close()
            try:
                flag = False
                for Account in Accounts:
                    if self.E1.get() == Account[1] and self.E2.get() == Account[2]:
                        self.username = Account[1]
                        self.games_played = str(int(Account[3]))
                        self.games_won = str(Account[4])

                        showinfo("INFORMATION", message="Login Successfully.")
                        flag = True
                        self.F1.destroy()
                        self.Frame_Radio_Buttons()
                if flag == False:
                    showinfo("INFORMATION", message="Account Not Found.")
            except Exception as exception:
                pass

        def CA_FUNC(): self.F1.destroy(), self.Create_Account_Page_Func()

        self.E2 = tk.Entry(self.F1, font=(self.font1, 14), borderwidth=3, bg=self.light_blue_color)
        self.E1 = tk.Entry(self.F1, font=(self.font1, 14), borderwidth=3, bg=self.light_blue_color)
        self.E1.grid(row=2, column=2)
        self.E2.grid(row=4, column=2)

        self.button_ca = tk.Button(self.F1, text='Create Account', command=CA_FUNC, borderwidth=3, font=(self.font1, 14), fg='#FFFFFF', bg=self.blue_color)
        self.button_log = tk.Button(self.F1, text='Log In', command=LOG_FUNC, borderwidth=3, font=(self.font1, 14), fg='#FFFFFF', bg=self.blue_color)
        self.button_log.grid(row=7, column=2)
        self.button_ca.grid(row=7, column=1)

        self.F1.place(x = 80, y = 75)

    def Create_Account_Page_Func(self):
        self.F2 = tk.Frame(self.R, bg=self.light_blue_color, relief='groove', borderwidth=12)
        tk.Label(self.F2, text='\n     CREATE AN ACCOUNT', font=(self.font1, 18), bg=self.light_blue_color, fg=self.blue_color).grid(row=0, column=1)
        tk.Label(self.F2, text=self.empty_text, bg=self.light_blue_color).grid(row=1, column=0)
        tk.Label(self.F2, text=self.empty_text, font=(self.font1, 15), bg=self.light_blue_color).grid(row=1, column=3)
        tk.Label(self.F2, text=self.empty_text, bg=self.light_blue_color).grid(row=3, column=1)
        tk.Label(self.F2, text=self.empty_text, bg=self.light_blue_color).grid(row=5, column=1)
        tk.Label(self.F2, text=self.empty_text, bg=self.light_blue_color).grid(row=7, column=1)
        tk.Label(self.F2, text=self.empty_text, bg=self.light_blue_color).grid(row=9, column=1)
        tk.Label(self.F2, text=' Set First Name: ', font=(self.font1, 14), bg=self.light_blue_color).grid(row=2, column=1)
        tk.Label(self.F2, text=' Set Last Name:  ', font=(self.font1, 14), bg=self.light_blue_color).grid(row=4, column=1)
        tk.Label(self.F2, text=' Set Password:   ', font=(self.font1, 14), bg=self.light_blue_color).grid(row=6, column=1)

        def create_my_account():
            showinfo("INFORMATION", message="Account Created Successfully.")
            if self.E1.get() != '' and self.E2.get() != '' and self.E3.get() != '':
                ID = self.Set_ID()
                Name = self.E1.get() + " " + self.E2.get()
                Pswd = self.E3.get()
                self.username = Name
                self.append([ID, Name, Pswd, 0, 0])
                f = open('User_Accounts.txt', 'a+')  # Saving Account.
                for item in self:
                    f.write(str(item) + '\n')
                f.close()
            self.F2.destroy()
            self.Frame_Radio_Buttons()

        def back_to_login_page(): self.F2.destroy(), self.Login_Page_Func()

        self.btn_CA_New = tk.Button(self.F2, text='Create Account', command=create_my_account, borderwidth=3, font=(self.font1, 14), fg='#FFFFFF', bg=self.blue_color)
        self.btn_back = tk.Button(self.F2, text='Back To Login Page', command=back_to_login_page, borderwidth=3, font=(self.font1, 14), fg='#FFFFFF', bg=self.blue_color)
        self.E1 = tk.Entry(self.F2, font=(self.font1, 14), borderwidth=3, bg=self.light_blue_color)
        self.E2 = tk.Entry(self.F2, font=(self.font1, 14), borderwidth=3, bg=self.light_blue_color)
        self.E3 = tk.Entry(self.F2, font=(self.font1, 14), borderwidth=3, bg=self.light_blue_color)
        self.E1.grid(row=2, column=2)
        self.E2.grid(row=4, column=2)
        self.E3.grid(row=6, column=2)
        self.btn_CA_New.grid(row=8, column=2)
        self.btn_back.grid(row=8, column=1)
        self.F2.place(x = 85, y = 65)

    def Frame_Radio_Buttons(self):
        self.F3 = tk.Frame(self.R, bg=self.light_blue_color, padx=8, pady=8, relief='groove', borderwidth=10)
        self.F4 = tk.Frame(self.R, bg=self.light_blue_color, padx=8, pady=8, relief='groove', borderwidth=10)

        tk.Label(self.F3, text='SELECT YOUR ', font=("Bebas Neue", 16), bg=self.light_blue_color, fg=self.blue_color).grid(row=1, column=0)
        tk.Label(self.F3, text='PIECE COLOR', font=("Bebas Neue", 16), bg=self.light_blue_color, fg=self.blue_color).grid(row=1, column=1)
        tk.Label(self.F3, text=self.empty_text, font=(self.font2, 10), bg=self.light_blue_color).grid(row=2, column=0)
        self.var_color = tk.IntVar()
        V1 = tk.Radiobutton(self.F3, text="Yellow ", font=(self.font2, 12), fg='#000000', bg=self.light_blue_color, variable=self.var_color, value=1)
        V2 = tk.Radiobutton(self.F3, text="Green  ", font=(self.font2, 12), fg='#000000', bg=self.light_blue_color, variable=self.var_color, value=2)
        V3 = tk.Radiobutton(self.F3, text="Orange ", font=(self.font2, 12), fg='#000000', bg=self.light_blue_color, variable=self.var_color, value=3)
        V4 = tk.Radiobutton(self.F3, text="Purple ", font=(self.font2, 12), fg='#000000', bg=self.light_blue_color, variable=self.var_color, value=4)
        V1.grid(row=3, column=0)
        V2.grid(row=4, column=0)
        V3.grid(row=3, column=1)
        V4.grid(row=4, column=1)

        tk.Label(self.F4, text=' SELECT FRAME', font=("Bebas Neue", 16), bg=self.light_blue_color, fg=self.blue_color).grid(row=1, column=0)
        tk.Label(self.F4, text=' GRID SIZE   ', font=("Bebas Neue", 16), bg=self.light_blue_color, fg=self.blue_color).grid(row=1, column=1)

        self.var_size = tk.IntVar()
        R1 = tk.Radiobutton(self.F4, text=" 5 X 5 ", font=(self.font2, 12), fg='#000000', bg=self.light_blue_color, variable=self.var_size, value=1)
        R2 = tk.Radiobutton(self.F4, text=" 6 X 6  ", font=(self.font2, 12), fg='#000000', bg=self.light_blue_color, variable=self.var_size, value=2)
        R3 = tk.Radiobutton(self.F4, text=" 7 X 7 ", font=(self.font2, 12), fg='#000000', bg=self.light_blue_color, variable=self.var_size, value=3)
        R4 = tk.Radiobutton(self.F4, text=" 8 X 8 ", font=(self.font2, 12), fg='#000000', bg=self.light_blue_color, variable=self.var_size, value=4)
        R5 = tk.Radiobutton(self.F4, text=" 9  X 9  ", font=(self.font2, 12), fg='#000000', bg=self.light_blue_color, variable=self.var_size, value=5)
        R6 = tk.Radiobutton(self.F4, text=" 10 X 10  ", font=(self.font2, 12), fg='#000000', bg=self.light_blue_color, variable=self.var_size, value=6)
        R7 = tk.Radiobutton(self.F4, text=" 11 X 11 ", font=(self.font2, 12), fg='#000000', bg=self.light_blue_color, variable=self.var_size, value=7)
        R8 = tk.Radiobutton(self.F4, text=" 12 X 12 ", font=(self.font2, 12), fg='#000000', bg=self.light_blue_color, variable=self.var_size, value=8)
        R1.grid(row=2, column=0)
        R2.grid(row=3, column=0)
        R3.grid(row=4, column=0)
        R4.grid(row=5, column=0)
        R5.grid(row=2, column=1)
        R6.grid(row=3, column=1)
        R7.grid(row=4, column=1)
        R8.grid(row=5, column=1)

        def game_now():
            f = open('User_Accounts.txt', 'a+')
            f.seek(0)
            for record in f:
                self.append(eval(record))
            f.close()
            for user in self:
                if user[1] == self.username:
                    self.append([user[0], user[1], user[2], int(user[3]) + 1, user[4]])
                    self.remove(user)
                    f = open('User_Accounts.txt', 'w+')
                    for record in self:
                        f.write(str(record) + '\n')
                    f.close()
                    break
            self.R.destroy()
            Game.Connect_4(self.Handle_Radio_Button2(), self.Handle_Radio_Button2(), self.sq_size, self.Handle_Radio_Button1())


        self.usernameLabel = tk.Label(self.R, text='Hey!! '+ self.username, font=(self.font1, 18), fg='#FFFFFF', bg=self.blue_color)
        self.games_played = tk.Label(self.R, text="No. Of Games Played: " + self.games_played, font=(self.font1, 18), fg='#FFFFFF', bg=self.blue_color)
        self.games_won = tk.Label(self.R, text="No. Of Games Won: " + self.games_won, font=(self.font1, 18), fg='#FFFFFF', bg=self.blue_color)
        self.play = tk.Button(self.R, text="LET'S PLAY THE GAME", command=game_now, borderwidth=6, font=("Comic Sans MS", 12), fg='#FFFFFF', bg=self.blue_color)


        self.usernameLabel.place(x = 60, y = 60)
        self.games_played.place(x = 100, y = 140)
        self.games_won.place(x = 100, y = 190)
        self.play.place(x = 120, y = 300)
        self.F3.place(x = 400, y = 60)
        self.F4.place(x = 400, y = 220)

    @staticmethod
    def Set_ID():
        f = open('User_ID.txt')  # Loading ID.
        ID = eval(f.read()) + 1
        f = open('User_ID.txt', 'w')
        f.write(str(ID))
        f.close()
        return ID

    def Handle_Radio_Button1(self):
        color = int(self.var_color.get())

        if color == 1:
            self.Color = YELLOW
        if color == 2:
            self.Color = GREEN
        if color == 3:
            self.Color = ORANGE
        if color == 4:
            self.Color = PURPLE
        return self.Color

    def Handle_Radio_Button2(self):
        x = int(self.var_size.get())
        if x == 1:
            self.Row = 5
            self.sq_size = 80
        if x == 2:
            self.Row = 6
            self.sq_size = 75
        if x == 3:
            self.Row = 7
            self.sq_size = 70
        if x == 4:
            self.Row = 8
            self.sq_size = 65
        if x == 5:
            self.Row = 9
            self.sq_size = 60
        if x == 6:
            self.Row = 10
            self.sq_size = 55
        if x == 7:
            self.Row = 11
            self.sq_size = 50
        if x == 8:
            self.Row = 12
            self.sq_size = 45
        return self.Row

