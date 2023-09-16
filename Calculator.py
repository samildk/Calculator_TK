from tkinter import *

# initializing the frame
#----------------------------------------------------------
frame = Tk()
frame.title('Calculator')

#intializing entery
#-----------------------------------------------------------
e = Entry(frame , width=30 ,borderwidth=5)
e.grid(row=0,column=0 , columnspan=8)


def button_click(number):

    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
    

def button_clear_func():

    e.delete(0,END)
    

def button_back_func():

    current = e.get()
    e.delete(0,END)
    e.insert(0,current[0:-1])

def button_add_func():
    global first_number
    global mat
    first_number = e.get()
    mat = 'addition'
    e.delete(0,END)

def button_min_func():
    global first_number
    global mat
    first_number = e.get()
    mat = 'minus'
    e.delete(0,END)
    
def button_div_func():
    global first_number
    global mat
    first_number = e.get()
    mat = 'division'
    e.delete(0,END) 

def button_mul_func():
    global first_number
    global mat
    first_number = e.get()
    mat = 'multiply'
    e.delete(0,END)
    
def button_pow_func():
    global first_number
    global mat
    first_number = e.get()
    mat = 'power'
    e.delete(0,END)
    
def button_residual_func():
    global first_number
    global mat
    first_number = e.get()
    mat = 'residual'
    e.delete(0,END)

def button_equal_func():

    second_number = e.get()
    e.delete(0,END)

    if mat == 'addition' :
        e.insert(0, int(first_number) + int(second_number))   

    if mat == 'minus':
        e.insert(0, int(first_number) - int(second_number)) 

    if mat == 'division':
        e.insert(0, int(first_number) / int(second_number))    

    if mat == 'multiply':
        e.insert(0, int(first_number) * int(second_number))   

    if mat == 'power':
        e.insert(0, int(first_number) ** int(second_number)) 

    if mat == 'residual':
        e.insert(0, int(first_number) % int(second_number)) 



# defining the buttons
#-----------------------------------------------------------
button_1 = Button(frame,text='1',bg='red',padx=40,pady=30,command=lambda:button_click(1),)
button_2 = Button(frame,text='2',bg='blue',padx=40,pady=30,command=lambda:button_click(2))
button_3 = Button(frame,text='3',bg='green',padx=40,pady=30,command=lambda:button_click(3))
button_4 = Button(frame,text='4',bg='yellow',padx=40,pady=30,command=lambda:button_click(4))
button_5 = Button(frame,text='5',bg='purple',padx=40,pady=30,command=lambda:button_click(5))
button_6 = Button(frame,text='6',bg='yellow',padx=40,pady=30,command=lambda:button_click(6))
button_7 = Button(frame,text='7',bg='red',padx=40,pady=30,command=lambda:button_click(7))
button_8 = Button(frame,text='8',bg='blue',padx=40,pady=30,command=lambda:button_click(8))
button_9 = Button(frame,text='9',bg='white',padx=40,pady=30,command=lambda:button_click(9))
button_0 = Button(frame,text='0',bg='orange',padx=40,pady=30,command=lambda:button_click(0))


button_clear = Button(frame,text='C',padx=40,pady=30,command=button_clear_func)
button_backspace = Button(frame,text='<--',padx=35,pady=30,command=button_back_func)


button_equal    = Button(frame,text='=',bg='yellow',padx=40,pady=30,command=button_equal_func)
button_addition = Button(frame,text='+',bg='yellow',padx=40,pady=30,command=button_add_func)
button_minus    = Button(frame,text='-',bg='yellow',padx=40,pady=30,command=button_min_func)
button_division = Button(frame,text='/',bg='yellow',padx=40,pady=30,command=button_div_func)
button_multiply = Button(frame,text='x',bg='yellow',padx=40,pady=30,command=button_mul_func)
button_power    = Button(frame,text='^',bg='yellow',padx=40,pady=30,command=button_pow_func)
button_residual = Button(frame,text='%',bg='yellow',padx=40,pady=30,command=button_residual_func)

# show buttons on frame
#---------------------------------------------------------
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=4,column=1)

button_clear.grid(row=4,column=0)
button_backspace.grid(row=4,column=2)



button_addition.grid(row=1,column=3)
button_minus.grid(row=2,column=3)
button_division.grid(row=3,column=3)
button_multiply.grid(row=4,column=3)
button_power.grid(row=5,column=1)
button_residual.grid(row=5,column=2)
button_equal.grid(row=5,column=3)

 
# frame.iconbitmap(r'C:\Users\Ten\Desktop')  


frame.mainloop()