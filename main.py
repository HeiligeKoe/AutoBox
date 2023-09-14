import pyautogui
import tkinter as tk

window = tk.Tk()
window.geometry('500x500')

class AutoBoxBot:
    def __init__(self):
        self.block = 'block.png'
        self.text = tk.Label(text='Idle Slayer RB Bot')
        self.button = tk.Button(text='activate', padx=200, pady=150, bg='green', command=self.change_button)
        self.activated = False

    def auto_block(self):
        while self.activated:
            position = pyautogui.locateOnScreen(self.block, confidence=.7)
            try:
                if position[0] < 220:
                    pyautogui.press('space')

            except:
                pass

    def change_button(self):
        if not self.activated:
            self.activated = True
            self.button.configure(text='deactivate',bg='red')
            self.auto_block()




    def layout(self):
        self.text.grid(row=2)
        self.button.grid()




bot = AutoBoxBot()
bot.layout()

window.mainloop()
