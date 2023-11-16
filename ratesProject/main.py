import tkinter as tk
from requests import get
from module import Buttons, potw_wartosc

if __name__ == '__main__':
    # preparing my interface
    root = tk.Tk()
    root.title("Kursy walut")
    root.geometry("550x500")

    value = 0

    # getting rates data from polish bank api
    response = get("http://api.nbp.pl/api/exchangerates/tables/a?format=json").json()

    data = response[0]
    rates = data["rates"]
    rates_table = [rate for rate in rates]

    # variables usefull for positioning and saving properties in buttons 
    row = 0
    col = 0
    i = 0

    # tables with usefull data
    codes = [rate['code'] for rate in rates_table]
    currency = [rate['currency'] for rate in rates_table]
    mid = [rate['mid'] for rate in rates_table]

    btns_usage = []

    # creating buttons
    for rate in range(len(codes)):
        if col == 16:
            col = 0
            row += 1
        if row == 2:
            break
        btn = Buttons(root, codes[i],mid[i],currency[i], row, col,i,value)
        btn.create_btn()
        btns_usage.append(btn)
        i += 1
        col += 1

    # positioning gui
    pole_lab = tk.Label(root, text="Ile złotych polskich chcesz zamienić na dowolną walutę na świecie?",font="Arial 12")
    pole_lab.place(x=30, y=100)

    pole_wartosc = tk.Entry(root,font="Arial 12")
    pole_wartosc.place(x=180,y=140)

    wartosc_btn = tk.Button(root, text="Potwierdź", command=lambda: potw_wartosc(pole_wartosc, btns_usage))
    wartosc_btn.place(x=240, y = 200)
    
    root.mainloop()




