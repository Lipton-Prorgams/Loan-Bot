import customtkinter as ctk
import re
import ctypes

s = 0
n = ""
c = 0
p = ""

def v(f, x):
    return f(x)

def m(a):
    return round(int(a) * 0.15)

def s_m(event=None):
    global s, n, c, p
    u = entry.get()
    chat_box.insert(ctk.END, f"Вы: {u}\n")
    entry.delete(0, ctk.END)

    if s == 0:
        if v(lambda x: x.strip() != "" and x[0].isupper(), u):
            n = u
            chat_box.insert(ctk.END, f"Бот: Приятно познакомиться, {n}\n")
            chat_box.insert(ctk.END, "Бот: На какую сумму вы хотите взять кредит?\n")
            s = 1
        else:
            chat_box.insert(ctk.END, "Бот: Пожалуйста, введите ваше имя с большой буквы.\n")

    elif s == 1:
        if v(lambda x: x.isdigit() and 10000 <= int(x) <= 10000000, u):
            c = int(u)
            m_p = m(c)
            chat_box.insert(ctk.END, f"Бот: Хорошо, ваш кредит составляет {c} рублей под 15% годовых.\n")
            chat_box.insert(ctk.END, f"Бот: Сумма ежемесячного платежа: {m_p} рублей.\n")
            chat_box.insert(ctk.END, "Бот: Введите ваш номер телефона:\n")
            s = 2
        else:
            chat_box.insert(ctk.END, "Бот: Пожалуйста, введите сумму кредита в диапазоне от 10000 до 10000000 рублей.\n")

    elif s == 2:
        if v(lambda x: re.match(r"^\+?\d{10,15}$", x), u):
            p = u
            chat_box.insert(ctk.END, "Бот: Подтвердите, что вы согласны взять кредит, поставив галочку.\n")
            entry.pack_forget()
            checkbox.pack(pady=10)
            s = 3
        else:
            chat_box.insert(ctk.END, "Бот: Пожалуйста, введите корректный номер телефона (например, +79991234567).\n")

def cc():
    global s
    if checkbox_var.get():
        chat_box.insert(ctk.END, "Бот: Кредит подтвержден. Удачного вам дня!\n")
        chat_box.insert(ctk.END, "Бот: Диалог завершен.\n")
        s = 4
        checkbox.pack_forget()
    else:
        chat_box.insert(ctk.END, "Бот: Пожалуйста, подтвердите, что вы согласны взять кредит.\n")

root = ctk.CTk()
root.title("Кредитный бот")
root.geometry("370x385")
root.resizable(False, False)
ctk.set_appearance_mode("dark")

chat_box = ctk.CTkTextbox(root, width=380, height=300, wrap="word", font=("Arial", 12), bg_color="#1e1e1e", fg_color="#1e1e1e", text_color="#ffffff")
chat_box.pack(pady=10)

entry = ctk.CTkEntry(root, width=400, font=("Arial", 12), bg_color="#1e1e1e", fg_color="#1e1e1e", text_color="#ffffff")
entry.pack(pady=10, padx=(10, 10))

checkbox_var = ctk.BooleanVar()
checkbox = ctk.CTkCheckBox(root, text="Я согласен взять кредит", variable=checkbox_var, command=cc, font=("Arial", 12), bg_color="#1e1e1e", fg_color="#1e1e1e", text_color="#ffffff")

entry.bind("<Return>", s_m)
chat_box.insert(ctk.END, "Бот: Добрый день, ваше имя пожалуйста!\n")
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
root.mainloop()