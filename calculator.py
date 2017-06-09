#calculator app
from tkinter import *
from tkinter import messagebox as msg

####################



#####################
window=Tk()
window.geometry("400x400")


#buttons list
buttons=[]
#buttons list


#numbers to be operrated
numbers_list=[]
#numbers to be operrated
exp=[]
answer=0
temp=[]
class operations:
    def __init__(self,n):
        self.it=n
    def docalc(self):
        for x in exp:
            if x=='+':
                answer=numbers_list[self.it]+numbers_list[self.it+1]
                self.it+=2
                numbers_list.append(answer)
                print(numbers_list)
opr=operations(0)
def button_click(x):
    temp_no=''
    if x in ('+','-','*','/','='):
        for e_x in temp:
            print(e_x)
            temp_no+=str(e_x)
        temp[:]=[]
        numbers_list.append(int(temp_no))
        exp.append(x)
        if x=='=':
            opr.docalc()
    else:
        temp.append(x)
###########################
def button_gen(buttons):
    nx=0
    ny=0
    for i in range(0,10):
        buttons.append(Button(window,text=i,command=lambda i=i:button_click(i),height=2,width=5))
        buttons[i].place(x=50+nx,y=50+ny)
        nx+=60
        if i%3==0:
            nx=0
            ny+=40
    buttons[0].place(x=110,y=50+ny)
    b1=Button(window,text='+',height=2,width=5,command=lambda:button_click('+'))
    b1.place(x=230,y=90)
    b2=Button(window,text='-',height=2,width=5,command=lambda:button_click('-'))
    b2.place(x=280,y=90)
    b3=Button(window,text='x',height=2,width=5,command=lambda:button_click('*'))
    b3.place(x=230,y=140)
    b4=Button(window,text='/',height=2,width=5,command=lambda:button_click('/'))
    b4.place(x=280,y=140)
    b5=Button(window,text='=',height=2,width=12,command=lambda:button_click('='))
    b5.place(x=230,y=190)
    
button_gen(buttons)

            

###########################
window.mainloop()

print(exp)
print(numbers_list)


