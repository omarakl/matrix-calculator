from tkinter import *

root = Tk()
root.geometry('650x550')
root.configure(background = 'powder blue')
root.title("Matrix Operator")

color = "powder blue"

label_title = Label(root , text = "Matrix Operator" , bg = 'powder blue' , fg = 'red')
label_title.pack()


def Addition():
    a = int(entry1.get()) + int(entry_a.get())
    label_a = Label(root ,text = a , bg = color)
    label_a.place(x = 40 , y = 370)

    b = int(entry2.get()) + int(entry_b.get())
    label_b = Label(root , text = b , bg = color)
    label_b.place(x = 90 , y = 370)

    c = int(entry3.get()) + int(entry_c.get())
    label_c = Label(root , text = c , bg = color)
    label_c.place(x = 140 , y = 370)

    d = int(entry4.get()) + int(entry_d.get())
    label_d = Label(root , text = d , bg = color)
    label_d.place(x = 40 , y = 420)

    e = int(entry5.get()) + int(entry_e.get())
    label_e = Label(root , text = e , bg = color)
    label_e.place(x = 90 , y = 420)

    f = int(entry6.get()) + int(entry_f.get())
    label_f = Label(root , text = f , bg = color)
    label_f.place(x = 140 , y = 420)

    g = int(entry7.get()) + int(entry_g.get())
    label_g = Label(root , text = g , bg = color)
    label_g.place(x = 40 , y = 470)

    h = int(entry8.get()) + int(entry_h.get())
    label_h = Label(root , text = h , bg = color)
    label_h.place(x = 90 , y = 470)

    i = int(entry9.get()) + int(entry_i.get())
    label_i = Label(root , text = i , bg = color)
    label_i.place(x = 140, y = 470)


def Subtrsction():

    j = int(entry1.get()) - int(entry_a.get())
    label_j = Label(root, text = j , bg = color)
    label_j.place(x = 250, y = 370)

    k = int(entry2.get()) - int(entry_b.get())
    label_k = Label(root, text = k , bg = color)
    label_k.place(x = 300, y = 370)

    l = int(entry3.get()) - int(entry_c.get())
    label_l = Label(root, text=l , bg = color)
    label_l.place(x=350, y=370)

    m = int(entry4.get()) - int(entry_d.get())
    label_m = Label(root, text=m , bg = color)
    label_m.place(x=250, y=420)

    n = int(entry5.get()) - int(entry_e.get())
    label_n = Label(root, text=n , bg = color)
    label_n.place(x=300, y=420)

    o = int(entry6.get()) - int(entry_f.get())
    label_o = Label(root, text=o , bg = color)
    label_o.place(x=350, y=420)

    p = int(entry7.get()) - int(entry_g.get())
    label_p = Label(root, text=p , bg = color)
    label_p.place(x=250, y=470)

    q = int(entry8.get()) - int(entry_h.get())
    label_q = Label(root, text=q , bg = color)
    label_q.place(x=300, y=470)

    r = int(entry9.get()) - int(entry_i.get())
    label_r = Label(root, text=r , bg = color)
    label_r.place(x=350, y=470)

def multiplication():
    s = int(entry1.get()) * int(entry_a.get()) + int(entry2.get()) * int(entry_d.get()) + int(entry3.get()) * int(entry_g.get())
    label_s = Label(root, text = s , bg = color)
    label_s.place(x = 460, y = 370)

    t = int(entry1.get()) * int(entry_b.get()) + int(entry2.get()) * int(entry_e.get()) + int(entry3.get()) * int(entry_h.get())
    label_t = Label(root, text=t , bg = color)
    label_t.place(x=510, y=370)

    u = int(entry1.get()) * int(entry_c.get()) + int(entry2.get()) * int(entry_f.get()) + int(entry3.get()) * int(entry_i.get())
    label_u = Label(root, text=u , bg = color)
    label_u.place(x=560, y=370)

    v = int(entry4.get()) * int(entry_a.get()) + int(entry5.get()) * int(entry_d.get()) + int(entry6.get()) * int(entry_g.get())
    label_v = Label(root, text=v , bg = color)
    label_v.place(x=460, y=420)

    w = int(entry4.get()) * int(entry_b.get()) + int(entry5.get()) * int(entry_e.get()) + int(entry6.get()) * int(entry_h.get())
    label_w = Label(root, text=w , bg = color)
    label_w.place(x=510, y=420)

    x = int(entry4.get()) * int(entry_c.get()) + int(entry5.get()) * int(entry_f.get()) + int(entry6.get()) * int(entry_i.get())
    label_x = Label(root, text=x , bg = color)
    label_x.place(x=560, y=420)

    y = int(entry7.get()) * int(entry_a.get()) + int(entry8.get()) * int(entry_d.get()) + int(entry9.get()) * int(entry_g.get())
    label_y = Label(root, text=y , bg = color)
    label_y.place(x=460, y=470)

    z = int(entry7.get()) * int(entry_b.get()) + int(entry8.get()) * int(entry_e.get()) + int(entry9.get()) * int(entry_h.get())
    label_z = Label(root, text=z , bg = color)
    label_z.place(x=510, y=470)

    z1 = int(entry7.get()) * int(entry_c.get()) + int(entry8.get()) * int(entry_f.get()) + int(entry9.get()) * int(entry_i.get())
    label_z1 = Label(root, text=z1 , bg = color)
    label_z1.place(x=560, y=470)



# Matrix 1

entry1 = Entry(root , width = 3)
entry1.place(x = 50 , y = 60)
entry2 = Entry(root , width = 3)
entry2.place(x = 120 , y = 60)
entry3 = Entry(root , width = 3)
entry3.place(x = 190 , y = 60)
entry4 = Entry(root , width = 3)
entry4.place(x = 50 , y = 120)
entry5 = Entry(root , width = 3)
entry5.place(x = 120 , y = 120)
entry6 = Entry(root , width = 3)
entry6.place(x = 190 , y = 120)
entry7 = Entry(root , width = 3)
entry7.place(x = 50 , y = 180)
entry8 = Entry(root , width = 3)
entry8.place(x = 120 , y = 180)
entry9 = Entry(root , width = 3)
entry9.place(x = 190 , y = 180)


# Matrix 2

entry_a = Entry(root , width = 3)
entry_a.place(x = 450 , y = 60)
entry_b = Entry(root , width = 3)
entry_b.place(x = 520 , y = 60)
entry_c = Entry(root , width = 3)
entry_c.place(x = 590 , y = 60)
entry_d = Entry(root , width = 3)
entry_d.place(x = 450 , y = 120)
entry_e = Entry(root , width = 3)
entry_e.place(x = 520 , y = 120)
entry_f = Entry(root , width = 3)
entry_f.place(x = 590 , y = 120)
entry_g = Entry(root , width = 3)
entry_g.place(x = 450 , y = 180)
entry_h = Entry(root , width = 3)
entry_h.place(x = 520 , y = 180)
entry_i = Entry(root , width = 3)
entry_i.place(x = 590 , y = 180)


label_1 = Label(root,text = "Matrix-1")
label_1.place(x = 110 , y = 230)
label_2 = Label(root, text = "Matrix-2")
label_2.place(x = 510 , y = 230)





button1 = Button(root , text = "ADD" , command = Addition)
button1.place(x = 305 , y = 90)
button2 = Button (root , text = "SUBTRACT" , command = Subtrsction)
button2.place(x = 290 , y = 150)
button3 = Button(root , text = "MULTIPLY" , command = multiplication)
button3.place(x = 290, y = 200)

label_line = Label(root, text = "______________________________________________________________________________________________________________________________________" , bg = "powder blue")
label_line.place(x = 0, y = 275)

label_addition = Label(root, text = "ADDITION" , bg = "powder blue" , fg = "green")
label_addition.place(x = 70, y = 320)

label_subtraction = Label(root , text = "SUBTRACTION", bg = "powder blue" , fg = "green")
label_subtraction.place(x = 260, y = 320)

label_multp = Label(root , text = "MULTIPLICATION", bg = "powder blue" , fg = "green")
label_multp.place(x = 460, y = 320)

label_author = Label(root , text = "Omar Akl", bg = "powder blue")
label_author.place(x = 590 , y = 530)

root.mainloop()