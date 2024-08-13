from tkinter import *
root=Tk()
root.geometry("615x400")
root.title("Application")
option_frame=Frame(root,bg="#c3c3c3")

def hide_indicate():
    first_indicate.config(bg="#c3c3c3")
    second_indicate.config(bg="#c3c3c3")
    third_indicate.config(bg="#c3c3c3")

def first_page():
    first_frame=Frame(main_frame)
    lb=Label(first_frame,text="alsdhfkshfushdfjdhfkasdjhg")
    lb.pack()
    first_frame.pack()

def second_page():
    second_frame=Frame(main_frame)
    lb=Label(second_frame,text="alsdhfkshfushdfjdhfkasdjhg")
    lb.pack()
    second_frame.pack()

def third_page():
    third_frame=Frame(main_frame)
    lb=Label(third_frame,text="alsdhfkshfushdfjdhfkasdjhgdlfhkhfksdjhf sdfksdj fhskdhf sdkfh askldhglkasjhgkjashg")
    lb.pack()
    third_frame.pack()

def delate_page():
    for frame in main_frame.winfo_children():
        frame.destroy()
def indicate(lb,page):
    hide_indicate()
    lb.config(bg="#158aff")
    delate_page()
    page()

first_button=Button(option_frame,text="1py homework",
                    bg="#c3c3c3",fg="black",borderwidth=0,command=lambda:indicate(first_indicate,first_page))
first_button.place(x=10,y=50)

first_indicate=Label(option_frame,text="",bg="#c3c3c3",
                     fg="black")
first_indicate.place(x=3,y=50)

second_button=Button(option_frame,text="2py homework",
                    bg="#c3c3c3",fg="black",borderwidth=0,command=lambda:indicate(second_indicate, second_page))
second_button.place(x=10,y=150)

second_indicate=Label(option_frame,text="",bg="#c3c3c3",
                     fg="black") #3333333333
second_indicate.place(x=3,y=150)

third_button=Button(option_frame,text="3py homework",
                    bg="#c3c3c3",fg="black",borderwidth=0,command=lambda:indicate(third_indicate, third_page))
third_button.place(x=10,y=250)

third_indicate=Label(option_frame,text="",bg="#c3c3c3",
                     fg="black")
third_indicate.place(x=3,y=250)

option_frame.pack(side=LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=115,height=400)

main_frame=Frame(root,highlightbackground="black",
                 highlightthickness=2)
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=500,height=400)

root.mainloop()








option_frame=Frame(windows,bg="#c3c3c3")
option_frame.pack(side=RIGHT)
option_frame.pack_propagate(False)
option_frame.configure(width=150,height=800)

main_frame=Frame(windows,highlightbackground="black",
                 highlightthickness=2)
main_frame.pack(side=RIGHT)
main_frame.pack_propagate(False)
main_frame.configure(width=900,height=800)

first_button=Button(option_frame,text="1.PY Homework",bg="#c3c3c3",
                    fg="black",borderwidth=0,command=lambda:indicate(first_indicate,first_page))
first_button.place(x=10,y=50)
first_indicate=Label(option_frame,text="",bg="#c3c3c3",fg="black")
first_indicate.place(x=3,y=50)

second_button=Button(option_frame,text="2.PY Homework",bg="#c3c3c3",
                     fg="black",borderwidth=0,command=lambda:indicate(second_indicate,second_page))
second_button.place(x=10,y=150)
second_indicate=Label(option_frame,text="",bg="#c3c3c3",fg="black")
second_indicate.place(x=3,y=150)

third_button=Button(option_frame,text="3.PY Homework",bg="#c3c3c3",
                     fg="black",borderwidth=0,command=lambda:indicate(third_indicate,third_page))
third_button.place(x=10,y=250)
third_indicate=Label(option_frame,text="",bg="#c3c3c3",fg="black")
third_indicate.place(x=3,y=250)

delete_all_button=Button(option_frame,text="Clean the Board",bg="#c3c3c3",
                     fg="black",borderwidth=0,command=lambda:indicate(delete_indicate,delete_all))
delete_all_button.place(x=10,y=400)
delete_indicate=Label(option_frame,text="",bg="#c3c3c3",fg="black")
delete_indicate.place(x=3,y=400)

def hide_indicate():
    first_indicate.config(bg="#c3c3c3")
    second_indicate.config(bg="#c3c3c3")
    third_indicate.config(bg="#c3c3c3")
    delete_all_button.config(bg="#c3c3c3")

def indicate(lb,page):
    hide_indicate()
    lb.config(bg="#158aff")
    delete_page()
    page()


def first_page():
    first_frame=Frame(main_frame)
    lb=Label(first_frame,text=""" def factorial(n):
    if n==0:
        return 1
    elif n ==1:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter a number to find the factorial of it: "))
print(factorial(n)) """)
    lb.pack()
    first_frame.pack()

def second_page():
    second_frame=Frame(main_frame)
    lb=Label(second_frame,text=""" def fibonancy(m):
    if m==0:
        return 0
    elif m==1:
        return 1
    else:
        return fibonancy(m) + fibonancy(m-1)
m=int(input("Enter the number to find the fibonancy of it: "))
print(fibonancy(m))""")
    lb.pack()
    second_frame.pack()

def third_page():
    third_frame=Frame(main_frame)
    lb=Label(third_frame,text="dlhsdhkshhsafhdhflasdhflkasd"
                              "fjsdlflsdhsdhglhsdalghsdhgshdgsd"
                              "dlgas;ldg;lsdhg;lshdg;ldshg;lshdg;l"
                              "###################################")
    lb.pack()
    third_frame.pack()


def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()

def delete_all():
    for frame in main_frame.winfo_children():
        frame.destroy()