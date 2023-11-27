import random
import tkinter as tk
from tkinter import *
from random import randint
from tkinter import messagebox
import sympy as smp
from textwrap import wrap

Window = tk.Tk()
Window.geometry('1350x700')
# Window["bg"] = "DarkSeaGreen1"

# Задание1
def mask_objects():
    a = [button_task1, button_task2, button_task3, button_next, button_task4, ans1, ans2, ans3, ans4,
         button_task_sol, dicr_text, button_back, view_equation, ans_eq1, ans_eq2, button_next3, text_root1, text_root2,
         equen_text, button_solut3, button_back_main, button_back_own, own_eque, own_a, own_b, own_c, kof_b, kof_a,
         kof_c, greet, button_back3, button_back2, dicr_task_sol,  but_next_dicr, button_own, ans_dicr, button_start,
         button_solution, button_next4, root1, root2, ans_root1, ans_root2, button_solut4, button_task5, ans_eq,
         button_solut5, button_next5, button_back4, equen_text5, ans_root3, ans_root4, button_back5]
    for x in a:
        x.place_forget()


def back_main():
    mask_objects()
    button_start.place(x=235, y=220)
    button_own.place(x=235, y=450)
    greet.place(x=50, y=10)


def main_window():
    mask_objects()
    button_task1.place(x=285, y=30)
    button_task2.place(x=285, y=135)
    button_task3.place(x=285, y=245)
    button_task4.place(x=285, y=350)
    button_task5.place(x=285, y=450)
    button_back_main.place(x=285, y=565)


def own():
    mask_objects()
    own_eque.place(x=320, y=10)
    kof_a.place(x=100, y=100)
    own_a.place(x=180, y=125, width=120, height=30)
    kof_b.place(x=100, y=180)
    own_b.place(x=180, y=205, width=120, height=30)
    kof_c.place(x=100, y=260)
    own_c.place(x=180, y=285, width=120, height=30)
    button_back_own.place(x=550, y=650)
    button_solution.place(x=480, y=550)


def own_equent():
    global root2, root1, x12, x21, text_root1, text_root2, d, root_no
    a = int(own_a.get())
    b = int(own_b.get())
    c = own_c.get()
    root_no = tk.Label(Window, text='Корней нет', font='Times 40', bg="DarkSeaGreen1", fg='medium blue')
    if int(a) > 0 and int(b) > 0 and int(c) > 0:
        tasks = ['{}x^2 + {}x + {} = 0 ']
        t = tasks[0]
        p = t.format(own_a.get(), own_b.get(), own_c.get())
    elif int(a) > 0 and int(b) < 0 and int(c) < 0:
        tasks = ['{}x^2 {}x {} = 0 ']
        t = tasks[0]
        p = t.format(own_a.get(), own_b.get(), own_c.get())
    elif int(a) == 1:
        tasks = ['x^2 {}x {} = 0 ']
        t = tasks[0]
        p = t.format(own_a.get(), own_b.get(), own_c.get())
    else:
        tasks = ['{}x^2 {}x {} = 0 ']
        t = tasks[0]
        p = t.format(own_a.get(), own_b.get(), own_c.get())
    tasks = ['Дискриминант равен: {}**2 - 4 * {} * {} = {} ']
    t = tasks[0]
    if int(own_b.get()) == 0:
        D = - (4 * int(own_a.get()) * int(own_c.get()))
    else:
        D = (int(own_b.get()) ** 2) - (4 * int(own_a.get()) * int(own_c.get()))
    d = t.format(own_b.get(), own_a.get(), own_c.get(), D)
    if D > 0:
        root_no.destroy()
        x1_own = (-b - smp.sqrt(D)) / (2 * a)
        x2_own = (-b + smp.sqrt(D)) / (2 * a)
        root1 = tk.Label(Window, text=x1_own, font='Times 40', bg="DarkSeaGreen1", fg='medium blue')
        root2 = tk.Label(Window, text=x2_own, font='Times 40', bg="DarkSeaGreen1", fg='medium blue')
        root1.place(x=525, y=250)
        root2.place(x=525, y=350)
        text_root1.place(x=400, y=250)
        text_root2.place(x=400, y=350)
    elif D == 0:
        x1_own = int(-b / (2*a))
        root1 = tk.Label(Window, text=x1_own, font='Times 40', bg="DarkSeaGreen1", fg='medium blue')
        root1.place(x=500, y=250)
        text_root.place(x=400, y=250)
    else:
        root_no.place(x=500, y=270)
    global dicr
    dicr = tk.Label(Window, text=d, font='Times 30', bg="DarkSeaGreen1", fg='medium blue')
    dicr.place(x=350, y=200)
    global equent
    equent = tk.Label(Window, text=p, font='Times 50', bg="DarkSeaGreen1", fg='medium blue')
    equent.place(x=450, y=100)


def dest_own():
    equent.destroy()
    dicr.destroy()
    root_no.destroy()


def clean_own():
    own_a.delete(0, END)
    own_b.delete(0, END)
    own_c.delete(0, END)


def task_1():
    mask_objects()
    view_equation.place(x=320, y=10)
    update()
    ans1.place(x=50, y=200)
    ans2.place(x=50, y=245)
    ans3.place(x=50, y=285)
    ans4.place(x=50, y=330)
    button_task_sol.place(x=720, y=400)
    button_next.place(x=230, y=400)
    button_back.place(x=550, y=650)


def back():
    mask_objects()
    main_window()


def update():
    global right_ans
    right_ans = 0
    tasks = ['{} {}x^{} {} {}x {} {} = 0 ']
    t = tasks[0]
    sign_a = random.choice(['-', '+'])
    a = randint(1, 100)
    def_ = randint(1, 10)
    sign_b = random.choice(['-', '+'])
    b = randint(1, 100)
    sign_c = random.choice(['-', '+'])
    c = randint(1, 100)
    if b == 0:
        tasks = ['{}{}x^{} {}{} = 0 ']
        t = tasks[0]
        p = t.format(sign_a, a, def_, sign_b, sign_c, c)
    elif b == 1 or b == -1:
        tasks = ['{}{}x^{} {}x {}{} = 0 ']
        t = tasks[0]
        p = t.format(sign_a, a, def_, sign_b, sign_c, c)
    elif a == 1 or a == -1:
        tasks = ['{}x^{} {}{}x {}{} = 0 ']
        t = tasks[0]
        p = t.format(sign_a, def_, sign_b, b, sign_c, c)
    elif a == 0:
        tasks = ['{}{}x {}{} = 0 ']
        t = tasks[0]
        p = t.format(sign_b, b, sign_c, c)
    elif sign_a == '+':
        tasks = ['{}x^{} {}{}x {}{} = 0 ']
        t = tasks[0]
        p = t.format(a, def_, sign_b, b, sign_c, c)
    else:
        p = t.format(sign_a, a, def_, sign_b, b, sign_c, c)
    if def_ == 2:
        right_ans = 2
    elif def_ == 3:
        right_ans = 1
    elif def_ >= 4:
        right_ans = 3
    elif def_ == 1:
        right_ans = 4
    global text_view
    text_view = tk.Label(Window, text=p, font='Times 50', bg="DarkSeaGreen1", fg='medium blue')
    text_view.place(x=350, y=100)

def del_():
    text_view.destroy()


var = IntVar()


def solution1():
    if var.get() == right_ans:
        messagebox.showinfo('information', 'Правильный ответ')
    elif var.get() == 0:
        messagebox.showerror('information', 'Выберите ответ')
    else:
        messagebox.showerror('information', 'Неправильный ответ')


def res():
    var.set(0)
    var3.set(0)


def output():
    global sign_a, sign_c, sign_b, a,b,c,p
    tasks = ['{} {}x^2 {} {}x {} {} = 0 ']
    t = tasks[0]
    sign_a = random.choice(['-', '+'])
    a = randint(1, 30)
    sign_b = random.choice(['-', '+'])
    b = randint(1, 30)
    sign_c = random.choice(['-', '+'])
    c = randint(1, 30)
    if b == 0:
        tasks = ['{}{}x^{} {}{} = 0 ']
        t = tasks[0]
        p = t.format(sign_a, a, sign_b, sign_c, c)
    elif b == 1 or b == -1:
        tasks = ['{}{}x^2 {}x {}{} = 0 ']
        t = tasks[0]
        p = t.format(sign_a, a, sign_b, sign_c, c)
    elif a == 1 or a == -1:
        tasks = ['{}x^2 {}{}x {}{} = 0 ']
        t = tasks[0]
        p = t.format(sign_a, sign_b, b, sign_c, c)
    elif sign_a == '+':
        tasks = ['{}x^2 {}{}x {}{} = 0 ']
        t = tasks[0]
        p = t.format(a, sign_b, b, sign_c, c)
    else:
        p = t.format(sign_a, a, sign_b, b, sign_c, c)


def text2():
    global right_ans
    right_ans = 0
    output()
    if sign_a == '-' and sign_c == '-':
        right_ans = str((b ** 2) - (4 * (-a) * (-c)))
    elif sign_a == '-' or sign_c == '-':
        right_ans = str((b ** 2) + (4 * a * c))
    elif sign_a == '-' and sign_c == '-':
        right_ans = str((b ** 2) - (4 * (-a) * (-c)))
    else:
        right_ans = str((b ** 2) - (4 * a * c))
    global examp_dicr
    examp_dicr = tk.Label(Window, text=p, font='Times 50', bg="DarkSeaGreen1", fg='medium blue')
    examp_dicr.place(x=350, y=100)


def solution2():
    if ans_dicr.get() == right_ans:
        messagebox.showinfo('information', 'Правильный ответ')
    elif ans_dicr.get() == '':
        messagebox.showerror('information', 'Выберите ответ')
    else:
        messagebox.showerror('information', 'Неправильный ответ')


def task_2():
    mask_objects()
    dicr_text.place(x=290, y=10)
    text2()
    ans_dicr.place(x=150, y=230, width=1000, height=30)
    dicr_task_sol.place(x=720, y=400)
    but_next_dicr.place(x=280, y=400)
    button_back2.place(x=550, y=650)


def clear():
    ans_dicr.delete(0, END)


def del2():
    examp_dicr.destroy()


# Задание 3
def text3():
    global right_ans
    right_ans = 0
    output()
    if a == 1:
        right_ans = 1
    else:
        right_ans = 2
    global eque_3
    eque_3 = tk.Label(Window, text=p, font='Times 50', bg="DarkSeaGreen1", fg='medium blue')
    eque_3.place(x=350, y=100)


def del3():
    eque_3.destroy()


def task_3():
    mask_objects()
    view_equation.place(x=290, y=10)
    text3()
    ans_eq1.place(x=50, y=200)
    ans_eq2.place(x=50, y=255)
    button_next3.place(x=280, y=400)
    button_solut3.place(x=720, y=400)
    button_back3.place(x=550, y=650)


def del_3():
    eque_3.destroy()


# Задание 4
def task_4():
    mask_objects()
    equen_text.place(x=50, y=10)
    text4()
    root1.place(x=50, y=200)
    ans_root1.place(x=250, y=200, width=150, height=30)
    root2.place(x=50, y=250)
    ans_root2.place(x=250, y=250, width=150, height=30)
    button_next4.place(x=280, y=400)
    button_solut4.place(x=720, y=400)
    button_back4.place(x=550, y=650)
    ans_eq.place(x=50, y=280)


def text4():
    global eque_4, right, x1,x2
    right = 0
    output()
    eque_4 = tk.Label(Window, text=p, bg="DarkSeaGreen1", fg='medium blue', font='Times 45')
    eque_4.place(x=350, y=100)

    if sign_a == '-' and sign_c == '-':
        discr = ((b ** 2) - (4 * a * (c)))
    elif sign_a == '-' or sign_c == '-':
        discr = ((b ** 2) + (4 * a * c))
    elif sign_a == '-' and sign_c == '-':
        discr = ((b ** 2) - (4 * (-a) * (-c)))
    else:
        discr = ((b ** 2) - (4 * a * c))

    if int(discr) > 0:
        if sign_b == '-':
            x1 = str((b + smp.sqrt(discr)) / (2 * a))
            x2 = str((b - smp.sqrt(discr)) / (2 * a))
        else:
            x1 = str((-b + smp.sqrt(discr) / (2 * a)))
            x2 = str(-b - smp.sqrt(discr) / (2 * a))
    elif discr == 0:
        if b == '-':
            x = b / (2 * a)
        else:
            x = -b / (2 * a)
    else:
        right = 4


def clear4():
    ans_root1.delete(0, END)
    ans_root2.delete(0, END)


var3 = IntVar()


def solution4():
    if (ans_root1.get() == x1 or ans_root2.get() == x1) and (ans_root1.get() == x2 or ans_root2.get() == x2) or right == var3.get():
        messagebox.showinfo('information', 'Правильный ответ')
    elif ans_root1.get() == '' and ans_root2.get() == '':
        messagebox.showerror('information', 'Выберите ответ')
    else:
        messagebox.showerror('information', 'Неправильный ответ')


def del4():
    eque_4.destroy()


# Задание 5
def task_5():
    mask_objects()
    equen_text5.place(x=50, y=10)
    text5()
    root1.place(x=50, y=200)
    ans_root3.place(x=250, y=200, width=100, height=30)
    root2.place(x=50, y=250)
    ans_root4.place(x=250, y=250, width=100, height=30)
    button_next5.place(x=280, y=400)
    button_solut5.place(x=720, y=400)
    button_back5.place(x=550, y=650)


def clear5():
    ans_root3.delete(0, END)
    ans_root4.delete(0, END)


def text5():
    global x1_v, x2_v, eque5
    tasks = ['x^2 - 7x + 10 = 0 ', 'x^2 - 15x - 16 = 0', 'x^2 + 10x - 39 = 0', 'x^2 + 16x + 63 = 0', 'x^2 - 17x - 18 = 0',
             'x^2 + 11x + 18 = 0', 'x^2 + 7x - 18 = 0', 'x^2 + 9x + 18 = 0']
    p = random.choice(tasks)
    eque5 = tk.Label(Window, text=p, bg="DarkSeaGreen1", fg='medium blue', font='Times 45')
    if eque5["text"] == tasks[0]:
        x1_v = '2'
        x2_v = '5'
    elif eque5["text"] == tasks[1]:
        x1_v = '-1'
        x2_v = '16'
    elif eque5["text"] == tasks[2]:
        x1_v = '-13'
        x2_v = '3'
    elif eque5["text"] == tasks[3]:
        x1_v = '-9'
        x2_v = '-7'
    elif eque5["text"] == tasks[4]:
        x1_v = '-1'
        x2_v = '18'
    elif eque5["text"] == tasks[5]:
        x1_v = '-9'
        x2_v = '-2'
    elif eque5["text"] == tasks[6]:
        x1_v = '-9'
        x2_v = '2'
    elif eque5["text"] == tasks[7]:
        x1_v = '-6'
        x2_v = '-3'

    eque5.place(x=350, y=100)


def del5():
    eque5.destroy()


def solution5():
    if (ans_root3.get() == x1_v or ans_root3.get() == x2_v) and (ans_root4.get() == x1_v or ans_root4.get() == x2_v):
        messagebox.showinfo('information', 'Правильный ответ')
    elif ans_root1.get() == '' and ans_root2.get() == '':
        messagebox.showerror('information', 'Выберите ответ')
    else:
        messagebox.showerror('information', 'Неправильный ответ')


#Объекты
ans_root3 = tk.Entry(Window, bg='white', fg='#01213d', font=('Arial', 10, 'bold'))
ans_root4 = tk.Entry(Window, bg='white', fg='#01213d', font=('Arial', 10, 'bold'))
equen_text5 = tk.Label(Window, text='Решите уравнение, используя теорему Виета:', bg="DarkSeaGreen1", fg='medium blue',
                       font='Times 45')
button_next5 = tk.Button(Window, text="Следующее задание", bg="grey89", fg='medium blue', font='Times 20', padx=70,
                         pady=10, command=lambda: (del5(), task_5(), clear5()))
button_solut5 = tk.Button(Window, text="Проверить решение", bg="grey89", fg='medium blue', font='Times 20', padx=70,
                          pady=10, command=solution5)
button_task5 = tk.Button(Window, text="Задание 5", font='Times 30', padx=300, pady=5, bg="lavender", fg='medium blue',
                         command=task_5)
button_back5 = tk.Button(Window, text="Назад", bg="grey89", fg='medium blue', font='Times 20', padx=70, pady=10,
                         command=lambda: (back(), del5()))
text_root1 = tk.Label(Window, text='x1 = ', font='Times 40', bg="DarkSeaGreen1", fg='medium blue')
text_root2 = tk.Label(Window, text='x2 = ', font='Times 40', bg="DarkSeaGreen1", fg='medium blue')
text_root = tk.Label(Window, text='x = ', font='Times 40', bg="DarkSeaGreen1", fg='medium blue')
view_equation = tk.Label(Window, text='Определите вид уравнения:', font='Times 40', bg="DarkSeaGreen1",
                         fg='medium blue')
own_eque = tk.Label(Window, text='Введите коэффициенты:', font='Times 40', bg="DarkSeaGreen1",fg='medium blue')
button_solution = tk.Button(Window, text="Решить уравнение", font='Times 20', padx=70,
                            pady=10, bg="grey89", fg='medium blue', command=lambda: (own_equent(), ))
own_a = tk.Entry(Window, bg='white', fg='#01213d', font=('Arial', 10, 'bold'))
own_b = tk.Entry(Window, bg='white', fg='#01213d', font=('Arial', 10, 'bold'))
own_c = tk.Entry(Window, bg='white', fg='#01213d', font=('Arial', 10, 'bold'))
kof_a = tk.Label(Window, text='a:', bg="DarkSeaGreen1", fg='medium blue', font='Times 40')
kof_b = tk.Label(Window, text='b:', bg="DarkSeaGreen1", fg='medium blue', font='Times 40')
kof_c = tk.Label(Window, text='c:', bg="DarkSeaGreen1", fg='medium blue', font='Times 40')
ans1 = tk.Radiobutton(Window, text='Кубическое', font='Times 25', variable=var, bg="DarkSeaGreen1", fg='medium blue',
                      value=1)
ans2 = tk.Radiobutton(Window, text='Квадратное', font='Times 25', variable=var, bg="DarkSeaGreen1", fg='medium blue',
                     value=2)
ans3 = tk.Radiobutton(Window, text='Уравнение высших степеней', font='Times 25', bg="DarkSeaGreen1", fg='medium blue',
                      variable=var, value=3)
ans4 = tk.Radiobutton(Window, text='Линейное', variable=var, font='Times 25', bg="DarkSeaGreen1", fg='medium blue',
                      value=4)
button_next = tk.Button(Window, text="Следующее задание", command=lambda: (del_(), task_1(), res()), font='Times 25', padx=70,
                        pady=10, fg='medium blue', bg="grey89")
button_task1 = tk.Button(Window, text="Задание 1", font='Times 30', padx=300, pady=5, bg="lavender", fg='medium blue',
                         command=lambda: (task_1()))
button_task_sol = tk.Button(Window, text="Проверить решение", command=lambda: (solution1(),), font='Times 25', padx=70,
                            pady=10, bg="grey89", fg='medium blue')
button_back = tk.Button(Window, text="Назад", font='Times 20', padx=70, pady=10, bg="grey89", fg='medium blue',
                        command=lambda: (back(), del_()))
button_start = tk.Button(Window, text="Начать тестирование!", font=('Times New Roman', 60, 'bold', 'underline'),
        foreground='black', bg="DarkSeaGreen1",fg='medium blue', padx=10, pady=10, command=main_window)
button_start.place(x=235, y=220)
text = 'Добро пожаловать в программу-тренажер по решению квадратных уравнений!'
greet = tk.Label(Window, text=text, bg="DarkSeaGreen1", fg='dark green', font='Times 45')
greet.place(x=80,y=10)
Window.update()
width = greet.winfo_width()
button_own = tk.Button(Window, text="Решить свое уравнение", font=('Times New Roman', 58, 'bold', 'underline'),
                 foreground='black', bg="DarkSeaGreen1", fg='medium blue', padx=9, pady=10, command=lambda: (own()),)
if width > 600:
    char_width = width / len(text)
    wrapped_text = '\n'.join(wrap(text, int(1200 / char_width)))
    greet['text'] = wrapped_text
button_own.place(x=235, y=450)
button_back_main = tk.Button(Window, text="Назад", font='Times 30', padx=330, pady=5, bg="lavender", fg='medium blue',
                             command=back_main)
button_back_own = tk.Button(Window, text="Назад", font='Times 20', padx=70, pady=5, bg="grey89", fg='medium blue',
                            command=lambda: (back_main(), dest_own(), clean_own(), ))
dicr_task_sol = tk.Button(Window, text="Проверить решение", font='Times 20', padx=70, pady=10, bg="grey89",
                          fg='medium blue', command=solution2)
dicr_text = tk.Label(Window, text='Вычислите дискриминант:', bg="DarkSeaGreen1", fg='medium blue', font='Times 50')
ans_dicr = tk.Entry(Window, bg='white', width=1000, bd=0, fg='#01213d', font=('Arial', 8, 'bold'))
but_next_dicr = tk.Button(Window, text="Следующее задание", bg="grey89", fg='medium blue', font='Times 20', padx=70,
                          pady=10, command=lambda: (del2(), task_2(), clear()))
button_task2 = tk.Button(Window, text="Задание 2", font='Times 30', padx=300, pady=10, bg="lavender", fg='medium blue',
                         command=task_2)
button_back2 = tk.Button(Window, text="Назад", font='Times 20', padx=70, pady=5, bg="grey89", fg='medium blue',
                         command=lambda: (back(), del2()))
ans_eq1 = tk.Radiobutton(Window, text='Приведенное', font='Times 25', bg="DarkSeaGreen1", fg='medium blue',
                         variable=var, value=1)
ans_eq2 = tk.Radiobutton(Window, text='Неприведенное', font='Times 25', bg="DarkSeaGreen1", fg='medium blue',
                         variable=var, value=2)
button_task3 = tk.Button(Window, text="Задание 3", font='Times 30', padx=300, pady=5, bg="lavender", fg='medium blue',
                         command=task_3)
button_next3 = tk.Button(Window, text="Следующее задание", bg="grey89", fg='medium blue', font='Times 20', padx=70,
                         pady=10, command=lambda: (del_3(), task_3(), res()))
button_solut3 = tk.Button(Window, text="Проверить решение", bg="grey89", fg='medium blue', font='Times 20', padx=70,
                          pady=10, command=solution1)
button_back3 = tk.Button(Window, text="Назад", bg="grey89", fg='medium blue', font='Times 20', padx=70, pady=10,
                         command=lambda: (back(), del_3()))
ans_eq = tk.Radiobutton(Window, text='Корней нет', font='Times 25', bg="DarkSeaGreen1", fg='medium blue',
                                 variable=var3, value=4)
ans_root1 = tk.Entry(Window, bg='white', fg='#01213d', font=('Arial', 10, 'bold'))
root1 = tk.Label(Window, text='Первый корень:', bg="DarkSeaGreen1", fg='medium blue',
                 font='Times 20')
ans_root2 = tk.Entry(Window, bg='white', fg='#01213d', font=('Arial', 10, 'bold'))
root2 = tk.Label(Window, text='Второй корень:', bg="DarkSeaGreen1", fg='medium blue',
                 font='Times 20')
equen_text = tk.Label(Window, text='Решите уравнение, используя дискриминант:', bg="DarkSeaGreen1", fg='medium blue',
                      font='Times 45')
button_task4 = tk.Button(Window, text="Задание 4", font='Times 30', padx=300, pady=5, bg="lavender", fg='medium blue',
                         command=task_4)
button_next4 = tk.Button(Window, text="Следующее задание", bg="grey89", fg='medium blue', font='Times 20', padx=70,
                         pady=10, command=lambda: (del4(), task_4(), clear4(), res()))
button_solut4 = tk.Button(Window, text="Проверить решение", bg="grey89", fg='medium blue', font='Times 20', padx=70,
                          pady=10, command=solution4)
button_back4 = tk.Button(Window, text="Назад", bg="grey89", fg='medium blue', font='Times 20', padx=70, pady=10,
                         command=lambda: (back(), del4()))


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom


app = FullScreenApp(Window)
Window.mainloop()
