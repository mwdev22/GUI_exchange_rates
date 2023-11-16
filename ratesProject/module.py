import tkinter as tk

# class, helps me save the properties of my buttons
class Buttons:
    def __init__(self, win, rate_code, mid, currency, row_num, col_num, id, value) -> None:
        self.win = win
        self.rate_code = rate_code
        self.row_num = row_num
        self.col_num = col_num
        self.mid = mid
        self.currency = currency
        self.ID = id
        self.value = value
    def create_btn(self):
        btn = tk.Button(self.win, text = self.rate_code,command=self.btn_clicked)
        btn.grid(row=self.row_num, column=self.col_num)

    def btn_clicked(self):
        clear = tk.Label(self.win,text=' '*550)
        clear.place(x= 50,y = 300)
        res = self.value/self.mid
        pole_odp = tk.Label(self.win, text=f'{self.value} złotych po przeliczeniu na {self.currency} wynosi {round(res, 2)}',font="Arial 10 bold")
        pole_odp.place(x=30, y=300)
        
# function that allows me to get value from user by pressing button
def potw_wartosc(pole_wartosc, btns_usage):
    value = pole_wartosc.get()
    for btn in btns_usage:
        btn.value = float(value)
        if btn.currency == "rand (Republika Południowej Afryki)":
            btn.currency = "rand (RPA)"
