from tkinter import *
from tkinter import messagebox
import time
import threading
import random

global lst1, lst2, lst3, lst4, lst5, lst6, lst7, lst8, lst9, lst10, lst11, lst12, ochki, HP_pers, gold
lst1, lst2, lst3, lst4, lst5, lst6, lst7, lst8, lst9, lst10, lst11, lst12, lst13 = [],[],[],[],[],[],[],[],[],[],[],[], []
ochki=0
HP_pers=10
gold=5

coint_n=0


class Monsters:
    def __init__(self, HP_m, gold):
        self.HP_m=HP_m
        self.gold=gold
  
def pal_lst():
    global lst1, lst2, lst3, lst4, lst5, lst6, lst7, lst8, lst9, lst10, lst11, lst12, lst13, spisok, i
    spisok = [lst1, lst2, lst3, lst4, lst5, lst6, lst7, lst8, lst9, lst10, lst11, lst12, lst13]
    index=0
    for i in spisok:
        for x in range(1,13):
            i.append('_')
        i.insert(index,'l')
        index+=1

def anim():
    global count, i
    count=0
    while True:
        global spisok
        if count==0:
            vpravo()
        elif count==1:
            vlevo()
                
def vpravo():
    global count, i
    for i in spisok[0:12:1]:
        lbl.configure(text=i)
        time.sleep(0.1)
    count=1

def vlevo():
    global count, i
    for i in spisok[13:0:-1]:
        lbl.configure(text=i)
        time.sleep(0.1)
    count=0

def mein():
    m1=threading.Thread(target=anim)
    m1.start()
    m2=threading.Thread(target=igra)
    m2.start()

def igra():
    global i, lst1, lst2, lst3, lst4, lst5, lst6, lst7, lst8, lst9, lst10, lst11, lst12, lst13, spisok, ochki, HP_pers, gold, ran_m, coint_n
    if i == lst7:
        lbl1.configure(text='Идеально\n(5 урона)')
        ochki+=5
        lbl2.configure(text=f'Очки {ochki}', font=("Arial Bold", 16))
        if ran_m==1:
            goblin.HP_m-=5
            lbl6.configure(text=f'Монстр имеет {goblin.HP_m} HP и даёт {goblin.gold} золота', font=("Arial Bold", 16))
            if goblin.HP_m<=0:
                gold+=goblin.gold
                lbl6.configure(text=f'Монстр {monsters[ran_m]} побеждён и даёт {goblin.gold} золота', font=("Arial Bold", 16))
                lbl4.configure(text=f'Золото {gold}', font=("Arial Bold", 16))
                ran_m=0
        elif ran_m==2:
            wolk.HP_m-=5
            lbl6.configure(text=f'Монстр имеет {wolk.HP_m} HP и даёт {wolk.gold} золота', font=("Arial Bold", 16))
            if wolk.HP_m<=0:
                gold+=wolk.gold
                lbl6.configure(text=f'Монстр {monsters[ran_m]} побеждён и даёт {wolk.gold} золота', font=("Arial Bold", 16))
                lbl4.configure(text=f'Золото {gold}', font=("Arial Bold", 16))
                ran_m=0
        elif ran_m==3:
            payk.HP_m-=5
            lbl6.configure(text=f'Монстр имеет {payk.HP_m} HP и даёт {payk.gold} золота', font=("Arial Bold", 16))
            if payk.HP_m<=0:
                gold+=payk.gold
                lbl6.configure(text=f'Монстр {monsters[ran_m]} побеждён и даёт {payk.gold} золота', font=("Arial Bold", 16))
                lbl4.configure(text=f'Золото {gold}', font=("Arial Bold", 16))
                ran_m=0
    elif i == lst4 or i==lst5 or i==lst6 or i==lst8 or i==lst9 or i==lst10:
        lbl1.configure(text='Хорошо\n(1 урона)')
        ochki+=1
        lbl2.configure(text=f'Очки {ochki}', font=("Arial Bold", 16))
        if ran_m==1:
            goblin.HP_m-=1
            lbl6.configure(text=f'Монстр имеет {goblin.HP_m} HP и даёт {goblin.gold} золота', font=("Arial Bold", 16))
            if goblin.HP_m<=0:
                gold+=goblin.gold
                lbl6.configure(text=f'Монстр {monsters[ran_m]} побеждён и даёт {goblin.gold} золота', font=("Arial Bold", 16))
                lbl4.configure(text=f'Золото {gold}', font=("Arial Bold", 16))
                ran_m=0
        elif ran_m==2:
            wolk.HP_m-=1
            lbl6.configure(text=f'Монстр имеет {wolk.HP_m} HP и даёт {wolk.gold} золота', font=("Arial Bold", 16))
            if wolk.HP_m<=0:
                gold+=wolk.gold
                lbl6.configure(text=f'Монстр {monsters[ran_m]} побеждён и даёт {wolk.gold} золота', font=("Arial Bold", 16))
                lbl4.configure(text=f'Золото {gold}', font=("Arial Bold", 16))
                ran_m=0
        elif ran_m==3:
            payk.HP_m-=1
            lbl6.configure(text=f'Монстр имеет {payk.HP_m} HP и даёт {payk.gold} золота', font=("Arial Bold", 16))
            if payk.HP_m<=0:
                gold+=payk.gold
                lbl6.configure(text=f'Монстр {monsters[ran_m]} побеждён и даёт {payk.gold} золота', font=("Arial Bold", 16))
                lbl4.configure(text=f'Золото {gold}', font=("Arial Bold", 16))
                ran_m=0
    elif i == lst1 or i==lst2 or i==lst3 or i==lst11 or i==lst12 or i==lst13 :
        if coint_n==0:
            lbl1.configure(text='')
            coint_n+=1
        else:
            lbl1.configure(text='Плохо\n(Получено 1 урона)')
            ochki-=1
            lbl2.configure(text=f'Очки {ochki}', font=("Arial Bold", 16))
            HP_pers-=1
            lbl3.configure(text=f'HP {HP_pers}', font=("Arial Bold", 16))           
            if HP_pers<=0:
                messagebox.showinfo('Оповещение', 'Вы умерли')  
                time.sleep(0.5)
                window.destroy()
            else:
                pass

def HP_rerturn():
    global HP_pers, gold
    if gold<=0:
        messagebox.showinfo('Оповещение', 'Не хватает денег')
    else:
        gold-=1
        HP_pers+=1
        lbl3.configure(text=f'HP {HP_pers}', font=("Arial Bold", 16))
        lbl4.configure(text=f'Золото {gold}', font=("Arial Bold", 16))

def rand_monster():
    global monsters, ran_m, goblin, wolk, payk
    ran_m = random.randint(1, 3)
    monsters = {1:'Гоблин',
                2:'Волк',
                3:'Паук'
        }
    if ran_m==1:
        gold_rand=random.randint(1, 3)
        HP_m_rand=random.randint(1, 5)
        goblin=Monsters(HP_m_rand, gold_rand)
        lbl5.configure(text=f'Вы встретили монстра {monsters[ran_m]}', font=("Arial Bold", 16))
        lbl6.configure(text=f'Монстр имеет {goblin.HP_m} HP и даёт {goblin.gold} золота', font=("Arial Bold", 16))
    elif ran_m==2:
        gold_rand=random.randint(1, 3)
        HP_m_rand=random.randint(3, 7)
        wolk=Monsters(HP_m_rand, gold_rand)
        lbl5.configure(text=f'Вы встретили монстра {monsters[ran_m]}', font=("Arial Bold", 16))
        lbl6.configure(text=f'Монстр имеет {wolk.HP_m} HP и даёт {wolk.gold} золота', font=("Arial Bold", 16))
    elif ran_m==3:
        gold_rand=random.randint(1, 3)
        HP_m_rand=random.randint(5, 10)
        payk=Monsters(HP_m_rand, gold_rand)
        lbl5.configure(text=f'Вы встретили монстра {monsters[ran_m]}', font=("Arial Bold", 16))
        lbl6.configure(text=f'Монстр имеет {payk.HP_m} HP и даёт {payk.gold} золота', font=("Arial Bold", 16))


window = Tk()
window.title("Типа игра")
window.geometry('800x250')

lbl = Label(window, text='', font=("Arial Bold", 16))
lbl.grid(column=0, row=0)

btn = Button(window, text="Нажать", font=("Arial Bold", 14), command=igra)  
btn.grid(column=0, row=1)
lbl1 = Label(window, text='', font=("Arial Bold", 16))
lbl1.grid(column=1, row=1)

lbl2 = Label(window, text=f'Очки {ochki}', font=("Arial Bold", 16))
lbl2.grid(column=2, row=1)
lbl3 = Label(window, text=f'HP {HP_pers}', font=("Arial Bold", 16))
lbl3.grid(column=2, row=2)
lbl4 = Label(window, text=f'Золото {gold}', font=("Arial Bold", 16))
lbl4.grid(column=2, row=3)
btn2 = Button(window, text="Восстановить HP", font=("Arial Bold", 14), command=HP_rerturn)  
btn2.grid(column=2, row=4)

btn3 = Button(window, text="Встретить монстра", font=("Arial Bold", 14), command=rand_monster)  
btn3.grid(column=0, row=4)
lbl5 = Label(window, text='', font=("Arial Bold", 16))
lbl5.grid(column=0, row=5)
lbl6 = Label(window, text='', font=("Arial Bold", 16))
lbl6.grid(column=0, row=6)

pal_lst()
mein()

window.mainloop()
