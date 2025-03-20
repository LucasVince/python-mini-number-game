import tkinter as tk
import random

num = random.randint(1, 10)

def comparar():
    entry_value = input_entry.get()
    if int(entry_value) == num:
        text_res.config(text='parabens, voce acertou')
    elif int(entry_value) > 10:
        text_res.config(text='digite um valor menor do que 10')
    elif int(entry_value) < 1:
        text_res.config(text='digite um valor maior que 1')
    elif int(entry_value) != num:
        text_res.config(text='errou, tente denovo')
    else:
        text_res.config(text='escreva algo valido')


window = tk.Tk()

window.title('adivinha essa porra caralho')
window.geometry('500x650')
window.config(padx=20, pady=35)

text_input = tk.Label(window, text='Digite um numero abaixo:', font=('Arial', 16))
text_input.pack(pady=50)

input_entry = tk.Entry(window, font=('arial', 14))
input_entry.pack(pady=5, padx=5)

btn_matheus = tk.Button(window, text='adivinhar', font=('arial', 16), command=comparar)
btn_matheus.pack(pady=50)

text_res = tk.Label(window, text='', font=('Arial', 16))
text_res.pack(pady=50)

window.mainloop()