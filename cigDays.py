from tkinter import ttk, Tk
from datetime import datetime


class CigDays:
    def __init__(self, master):
        master.title('Cig Days')
        master.geometry('200x200')
        self.daysTill = 0
        self.calcDaysTill()

        self.dayLabel = ttk.Label(
            master, text=self.daysTill, font=('Helvetica', 52))
        self.dayLabel.pack(padx=2, pady=2)

        self.resetButton = ttk.Button(
            master, text='Reset', command=lambda: self.setLastDay())
        self.resetButton.pack(padx=2, pady=2)

    def getLastDay(self):
        try:
            with open('last_day.txt', 'r') as file:
                self.lastDay = file.read()
                return self.lastDay
        except FileNotFoundError:
            return self.setLastDay()

    def setLastDay(self):
        with open('last_day.txt', 'w') as file:
            now = datetime.now()
            self.lastDay = now.strftime('%d-%m-%Y')
            file.write(self.lastDay)
        self.calcDaysTill()
        self.dayLabel.configure(text=self.daysTill)
        return self.lastDay

    def calcDaysTill(self):
        self.daysTill = datetime.now()-datetime.strptime(self.getLastDay(), '%d-%m-%Y')
        self.daysTill = self.daysTill.days


def main():
    root = Tk()
    CigDays(root)
    root.mainloop()


if __name__ == '__main__':
    main()
