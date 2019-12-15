from tkinter import *
import math
"""
float handling is not their
"""


class calculator:
    def __init__(self, root):
        self.root = root
        root.title("DSC CALCI")

        self.window = Text(root, state='normal', width=40, height=3,
                           background='yellow', foreground='black', relief='raised')
        self.window.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        self.equation = str()

        b1 = self.create_button(7).grid(row=1, column=0)
        b2 = self.create_button(8).grid(row=1, column=1)
        b3 = self.create_button(9).grid(row=1, column=2)
        b4 = self.create_button('mod').grid(
            row=1, column=3)
        b5 = self.create_button(4).grid(row=2, column=0)
        b6 = self.create_button(5).grid(row=2, column=1)
        b7 = self.create_button(6).grid(row=2, column=2)
        b8 = self.create_button(u"\u00F7").grid(row=2, column=3)
        b9 = self.create_button(1).grid(row=3, column=0)
        b10 = self.create_button(2).grid(row=3, column=1)
        b11 = self.create_button(3).grid(row=3, column=2)
        b12 = self.create_button('*').grid(row=3, column=3)
        b13 = self.create_button(0).grid(row=4, column=0)
        b14 = self.create_button('.').grid(row=4, column=1)
        b15 = self.create_button('+').grid(row=4, column=2)
        b16 = self.create_button('-').grid(row=4, column=3)
        b17 = self.create_button('=', None, 21).grid(
            row=5, column=0, columnspan=4)  # 34
        b18 = self.create_button(u"\u232B", None).grid(
            row=5, column=4)
        b19 = self.create_button('cos').grid(row=1, column=4)
        b20 = self.create_button('sin').grid(row=2, column=4)
        b21 = self.create_button('tan').grid(row=3, column=4)
        b22 = self.create_button('|x|').grid(row=4, column=4)

    def parse(self, equation):
        if 'mod' in self.equation:
            self.equation = self.equation.replace('mod', '%')
        if '|x|' in self.equation:
            self.equation = self.equation.replace('|x|', '')
            self.equation = str(abs(int(self.equation)))

        if 'cos' in self.equation:
            self.equation = self.equation.replace('cos', '')
            self.equation = str(math.cos(int(self.equation)))
        if 'sin' in self.equation:
            self.equation = self.equation.replace('sin', '')
            self.equation = str(math.sin(int(self.equation)))
        if 'tan' in self.equation:
            self.equation = self.equation.replace('tan', '')
            self.equation = str(math.tan(int(self.equation)))

        return str(eval(self.equation))

    def create_button(self, icon, write=True, width=7):
        return Button(self.root, text=icon, width=width, cursor='mouse',
                      command=lambda: self.click(icon, write))

    def click(self, text, write):

        if write == None:

            if text == '=' and self.equation:
                self.equation = self.equation.replace(u"\u00F7", '/')
                answer = self.parse(self.equation)
                self.clear_window()
                self.insert_window(answer, newline=True)
            elif text == u"\u232B":
                self.clear_window()

        else:
            self.insert_window(text)

    def clear_window(self):
        self.equation = ''
        self.window.configure(state='normal')
        self.window.delete('1.0', END)

    def insert_window(self, value, newline=False):
        self.window.configure(state='normal')
        self.window.insert(END, value)
        self.equation += str(value)
        self.window.configure(state='disabled')


if __name__ == "__main__":
    root = Tk()
    calculator(root)
    root.mainloop()
