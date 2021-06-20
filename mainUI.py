from tkinter import *
from tkinter import messagebox
from Adafruit_IO import Client,Data
import serial
import time
from PIL import Image, ImageTk

ser = serial.Serial(port='/dev/ttyUSB0',baudrate = 9600,bytesize = serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, timeout=None)
aio = Client('ak47av', 'bda36d622b874920902764079deb0631')

class product:

    def __init__(self, name, price, quantity):
        self.price = price
        self.name = name
        self.quantity = quantity

    def adagetdata(self):
        Quantity = aio.receive(self.name)
        print(self.name)
        Price = aio.receive((self.name+'price'))
        print(self.name+'price')
        self.quantity = IntVar()
        self.quantity.set(Quantity.value)
        self.price = IntVar()
        self.price.set(Price.value)
        print(str(Quantity.value)+'    '+str(Price.value))


product1 = product('lays',10,10)
product2 = product('coke',25,25)
product3 = product('candy',1,50)

win = Tk()
win.title('Vending machine')
#Product Declar
frame1 = Frame(win).grid()

def main():

    product1.adagetdata()
    product2.adagetdata()
    product3.adagetdata()

    def calc1():
        cost1 = v1.get()*product1.price.get()
        return cost1

    def calc2():
        cost2 = v2.get()*product2.price.get()
        return cost2

    def calc3():
        cost3 = v3.get()*product3.price.get()
        return cost3



    nameofprod = Label(frame1,text="    Product avaliable    ",padx=80,pady=20).grid(row=0,column=0)
    quantityrequired = Label(frame1,text ='   Quantity    ',padx=20).grid(row=0,column=1)
    priceofprod = Label(frame1,text='    Price   ',padx=20).grid(row=0,column=2)
    quantityavailable = Label(frame1,text='   Quantity available    ',padx=20).grid(row=0,column=4)



    load1 = Image.open("/home/akav/Downloads/lays.jpeg")
    load1 = load1.resize((150, 150), Image.ANTIALIAS)
    lays = ImageTk.PhotoImage(load1)
    p1 = Label(frame1,image = lays,pady=30)
    p1.image = lays
    p1.grid(row=1,column=0,pady=30)
    v1 = IntVar(frame1,value=0)
    optionbox1 = OptionMenu(frame1,v1,0,1,2,3,4,5).grid(row=1,column=1)
    pricebox1 = Label(frame1,textvariable=str(product1.price)).grid(row=1,column=2)
    q1 = Label(frame1,textvariable=str(product1.quantity)).grid(row=1,column=4)


    load2 = Image.open("/home/akav/Downloads/coke.jpg")
    load2 = load2.resize((90,150), Image.ANTIALIAS)
    coke = ImageTk.PhotoImage(load2)
    p2 = Label(frame1,image = coke)
    p2.image = coke
    p2.grid(row=2,column=0,padx=30,pady=30)
    v2 = IntVar(frame1,value=0)
    optionbox2 = OptionMenu(frame1,v2,0,1,2,3,4,5).grid(row=2,column=1)
    pricebox2 = Label(frame1,textvariable=str(product2.price)).grid(row=2,column=2)
    q2 = Label(frame1,textvariable=str(product2.quantity)).grid(row=2,column=4)


    load3 = Image.open("/home/akav/Downloads/candy.jpg")
    load3 = load3.resize((120,150), Image.ANTIALIAS)
    candy = ImageTk.PhotoImage(load3)
    p3 = Label(frame1,image = candy)
    p3.image = candy
    p3.grid(row=3,column=0,padx=30,pady=20)
    v3 = IntVar(frame1,value=0)
    optionbox3 = OptionMenu(win,v3,0,1,2,3,4,5).grid(row=3,column=1)
    pricebox3 = Label(frame1,textvariable=str(product3.price)).grid(row=3,column=2)
    q3 = Label(frame1,textvariable=str(product3.quantity)).grid(row=3,column=4)

    def authorize():
        totalcost = calc1() + calc2() + calc3()
        product1.quantity.set(product1.quantity.get() - v1.get())
        for i in range(0, v1.get()):
            val = '1'
            ser.write(val.encode())
            time.sleep(1)
        data1 = Data(value=product1.quantity.get())
        aio.create_data('lays', data1)
        product2.quantity.set(product2.quantity.get() - v2.get())
        for i in range(0, v2.get()):
            val = '2'
            ser.write(val.encode())
            time.sleep(1)
        data2 = Data(value=product2.quantity.get())
        aio.create_data('coke', data2)
        product3.quantity.set(product3.quantity.get() - v3.get())
        for i in range(0, v3.get()):
            val = '3'
            ser.write(val.encode())
            time.sleep(1)
        data3 = Data(value=product3.quantity.get())
        aio.create_data('candy', data3)
        data = Data(value=totalcost)
        aio.create_data('earnings', data)
        return totalcost

    def calc():

        if((product1.quantity.get()-v1.get())<0 or (product2.quantity.get()-v2.get())<0 or (product3.quantity.get()-v3.get())<0):
            messagebox.showinfo('Not enough items','Not enough items are available , please select a quantity lesser than the quantity available')
            main()

        else :
            totalcost = calc1() + calc2() + calc3()
            msgbox = messagebox.askquestion('Payment', 'You have to pay {0:.2f}  (inclusive of tax).Click yes to pay and no to return to main screen'.format(totalcost*1.18))
            if(msgbox=='yes'):
                authorize()
            else:
                main()


    ok = Button(frame1,text="Pay",command = calc).grid(row=4)

main()

win.mainloop()

