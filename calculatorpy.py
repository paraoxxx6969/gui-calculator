#! /usr/bin/env python

import tkinter as tk
from tkinter import ttk
import base64
from icons import icon_string


class TkGUI(tk.Tk):
    FONT_LARGE = ("Calibri", 12)
    FONT_MED = ("Calibri", 10)

    MAX_ROW = 4
    MAX_COLUMN = 5
    i = 0
    NEW_OPERATION = False

    def __init__(self):
        super().__init__()

        self.title('Calculator')
        self.resizable(width=False, height=False)

        style = ttk.Style(self)
        style.theme_use('clam')

        icon_data = base64.b64decode(icon_string)
        self.icon = tk.PhotoImage(data=icon_data)
        self.tk.call('wm', 'iconphoto', self._w, self.icon)

        for row in range(self.MAX_ROW):
            self.columnconfigure(row, pad=3)

        for column in range(self.MAX_COLUMN):
            self.rowconfigure(column, pad=3)

        self.display = tk.Entry(self, font=("Calibri", 13))
        self.display.grid(row=1, columnspan=6, sticky=tk.W + tk.E)

        self._init_ui()

    def _init_ui(self):
        # Numbers
        for i in range(1, 10):
            tk.Button(self, text=str(i),
                      command=lambda x=i: self.get_variables(x),
                      font=self.FONT_LARGE).grid(row=2 + (i-1)//3, column=(i-1) % 3)

        tk.Button(self, text="0", command=lambda: self.get_variables(0),
                  font=self.FONT_LARGE).grid(row=5, column=1)

        # Basic buttons
        tk.Button(self, text="AC", command=self.clear_all,
                  font=self.FONT_LARGE, fg="red").grid(row=5, column=0)

        tk.Button(self, text="=", command=self.calculate,
                  font=self.FONT_LARGE, fg="red").grid(row=5, column=2)

        # Operations
        ops = ["+", "-", "*", "/"]
        for i, op in enumerate(ops):
            tk.Button(self, text=op,
                      command=lambda x=op: self.get_operation(x),
                      font=self.FONT_LARGE).grid(row=2+i, column=3)

        # Extra
        tk.Button(self, text="%", command=lambda: self.get_operation("%"),
                  font=self.FONT_LARGE).grid(row=3, column=4)

        tk.Button(self, text="(", command=lambda: self.get_operation("("),
                  font=self.FONT_LARGE).grid(row=4, column=4)

        tk.Button(self, text=")", command=lambda: self.get_operation(")"),
                  font=self.FONT_LARGE).grid(row=4, column=5)

        tk.Button(self, text="^2", command=lambda: self.get_operation("**2"),
                  font=self.FONT_MED).grid(row=5, column=5)

        tk.Button(self, text="exp", command=lambda: self.get_operation("**"),
                  font=self.FONT_MED).grid(row=5, column=4)

        tk.Button(self, text="pi", command=lambda: self.get_operation("3.14"),
                  font=self.FONT_LARGE).grid(row=2, column=4)

        tk.Button(self, text="<-", command=self.undo,
                  font=self.FONT_LARGE, fg="red").grid(row=2, column=5)

        tk.Button(self, text="x!", command=self.factorial,
                  font=self.FONT_LARGE).grid(row=3, column=5)

    # -------- Functions --------

    def factorial(self):
        try:
            number = int(self.display.get())
            fact = 1
            while number > 0:
                fact *= number
                number -= 1
            self.clear_all()
            self.display.insert(0, str(fact))
        except:
            self.clear_all()
            self.display.insert(0, "Error")

    def clear_all(self, new_operation=True):
        self.display.delete(0, tk.END)
        self.i = 0
        self.NEW_OPERATION = new_operation

    def get_variables(self, num):
        if self.NEW_OPERATION:
            self.clear_all(new_operation=False)
        self.display.insert(self.i, num)
        self.i += 1

    def get_operation(self, operator):
        self.display.insert(self.i, operator)
        self.i += len(operator)

    def undo(self):
        whole_string = self.display.get()
        if len(whole_string):
            new_string = whole_string[:-1]
            self.clear_all(new_operation=False)
            self.display.insert(0, new_string)
        else:
            self.clear_all()
            self.display.insert(0, "Error")

    def calculate(self):
        whole_string = self.display.get()
        try:
            result = eval(whole_string)   # ✅ FIXED (removed parser)
            self.clear_all()
            self.display.insert(0, str(result))
        except:
            self.clear_all()
            self.display.insert(0, "Error!")

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = TkGUI()
    app.run()