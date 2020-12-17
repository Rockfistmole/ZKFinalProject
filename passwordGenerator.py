'''
Author:  Zaeem Khan
Class:   CIS 2531
Descr:
This is a random password generator
'''

import random
import pyperclip
import string
import tkinter as tk
from tkinter import ttk, filedialog


class randomPassGen:
    '''This class will generate the random password'''
    
    def setLetters(self, letters):
        self.__letters = random.choice(letters)
    def getLetters(self):
        return self.__letters
    def setNumbers(self, numbers):
        self.__numbers = random.choice(numbers)
    def getNumbers(self):
        return self.__numbers
    def setSymbols(self, symbols):
        self.__symbols = random.choice(symbols)
    def getSymbols(self):
        return self.__symbols
    
    def determineStrength(self):
        # clear out the entry
        self.entry.delete(0, tk.END)
        # check the listbox for the length of password
        length = self.listBox.get(tk.ACTIVE)
        password = ""
        alpha = string.ascii_letters
        digits = string.digits
        punc = string.punctuation
        
        # if the radio button is on low, generate a weak password
        if self.var.get() == 1:
            for i in range (length):
               self.setLetters(alpha)
               password += self.getLetters()
            return password
        # Medium password
        elif self.var.get() == 0:
            for i in range (0, length, 2):
                self.setLetters(alpha)
                self.setNumbers(digits)
                password += self.getLetters() + self.getNumbers()
            return password
        elif self.var.get() == 3:
            for i in range(0, length, 3):
                self.setLetters(alpha)
                self.setNumbers(digits)
                self.setSymbols(punc)
                password += self.getLetters() + self.getNumbers() + self.getSymbols()
            return password
        else:
            errorMessage = tk.messagebox.showerror(title='Error', message='Must select a length option')
            return errorMessage
    
    def generatePassword(self):
        self.entry.config(state=tk.NORMAL)
        passwordGen = self.determineStrength()
        self.entry.insert(1, passwordGen)
        self.entry.config(state=tk.DISABLED, fg='black')
    
    def copyPassword(self):
        randomPassword = self.entry.get()
        pyperclip.copy(randomPassword)
        
    def save_file(self):
        fileName = tk.filedialog.asksaveasfilename(filetypes = [('Text Files', '*.txt'),
                                                                ('All Files', '*.*')],
                                                   title = 'Select File',
                                                   defaultextension = '*.txt')
        if len(fileName) != 0:
            self.fileVar = open(fileName, 'w')
            self.fileVar.write(self.entry.get())
            self.fileVar.close()
    
    def __init__(self, letters, numbers, symbols):
        ''' The __init__ function will setup the values for generating '''
        self.__letters = letters
        self.__numbers = numbers
        self.__symbols = symbols
        
        # GUI Setup
        self.main_window = tk.Tk()
        self.var = tk.IntVar()
        self.varOne = tk.IntVar()
        self.main_window.title('ZK -- Random Password Gen.')
        self.main_window.config(bg='#6D8A96')
            
        # Menu Bar
        self.menuBar = tk.Menu(self.main_window)
        self.main_window.config(menu = self.menuBar)
        self.fileMenu = tk.Menu(self.menuBar, tearoff = 0)
        self.menuBar.add_cascade(label='File', menu = self.fileMenu)
        self.fileMenu.add_command(label='Save Password to File', command=self.save_file)
        self.fileMenu.add_separator
        self.fileMenu.add_command(label='Exit', command=self.main_window.destroy)
            
        # password label
        passwordLabel = tk.Label(self.main_window, text='Password', bg='#6D8A96', padx=20, pady=10, font=('Times New Roman', 12))
        passwordLabel.grid(row=0)
        self.entry = tk.Entry(self.main_window, width=30, font=('Times New Roman', 12), state=tk.DISABLED)
        self.entry.grid(row=0, column=1)
            
        # length label
        lengthLabel = tk.Label(self.main_window, text='Length', bg='#6D8A96',padx=20, pady=10, font=('Times New Roman', 12))
        lengthLabel.grid(row=1)
            
        # Copy and Generate buttons
        self.btnCopy = tk.Button(self.main_window, text='Copy', command=self.copyPassword, padx=20, pady=10, font=('Times New Roman', 12))
        self.btnCopy.grid(row=0, column=4)
        self.btnGen = tk.Button(self.main_window, text='Generate', command=self.generatePassword, padx=20, pady=10, font=('Times New Roman', 12))
        self.btnGen.grid(row=0, column=5)
            
        # Listbox and Scrollbar
        self.scrollBar = tk.Scrollbar(self.main_window, orient=tk.VERTICAL)
        self.listBox = tk.Listbox(self.main_window, yscrollcommand = self.scrollBar.set, selectmode='SINGLE', font=('Times New Roman', 12))
        self.scrollBar.config(command = self.listBox.yview)
        values = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
        for item in range(values[0], values[17]):
            self.listBox.insert(tk.END,item)
        self.listBox.grid(row=1, column=1)
        self.scrollBar.grid(row=1, column=2)
    
        # Radio buttons
        self.radioLow = tk.Radiobutton(self.main_window, text='Low', variable=self.var, value=1, padx=20, pady=10, font=('Times New Roman', 12))
        self.radioLow.grid(row=1, column=3, sticky='E') 
        self.radioMiddle = tk.Radiobutton(self.main_window, text="Medium", variable=self.var, value=0, padx=20, pady=10, font=('Times New Roman', 12)) 
        self.radioMiddle.grid(row=1, column=4, sticky='E') 
        self.radioStrong = tk.Radiobutton(self.main_window, text="Strong", variable=self.var, value=3, padx=20, pady=10, font=('Times New Roman', 12)) 
        self.radioStrong.grid(row=1, column=5, sticky='E') 
        
        self.main_window.mainloop()
        

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!@#$%^&*()"
myGUI = randomPassGen(letters, digits, symbols)  