from tkinter import *
from tkinter import ttk
from Adafruit_IO import Client,Data
from PIL import Image,ImageTk
aio = Client('ak47av', 'bda36d622b874920902764079deb0631')

class product:

    def __init__(self, name, price, quantity):
        self.price = price
        self.name = name
        self.quantity = quantity

    def adagetdata(self):
        Quantity = aio.receive(self.name)
        Price = aio.receive((self.name+'price'))
        self.quantity = IntVar()
        self.quantity.set(Quantity.value)
        self.price = IntVar()
        self.price.set(Price.value)

product1 = product('lays',10,10)
product2 = product('coke',25,25)
product3 = product('candy',1,50)

win = Tk()
win.geometry('1386x250')
win.title('Update Vending Details')

def main():

    product1.adagetdata()
    product2.adagetdata()
    product3.adagetdata()

    fr1 = Frame(win).grid(row=0,column=0)
    #Display existing attributes
    ttk.Separator(fr1, orient=VERTICAL).grid(row=0,column=3,rowspan=5,sticky='ns')
    ttk.Separator(fr1, orient=VERTICAL).grid(row=0,column=8,rowspan=5,sticky='ns')
    load = Image.open('/home/akav/Downloads/Spark-Logo_Navin.png')
    load = load.resize((150, 150), Image.ANTIALIAS)
    sparkimg = ImageTk.PhotoImage(load)
    spark = Label(fr1,image = sparkimg)
    spark.image = sparkimg
    spark.grid(row=0,rowspan=5,column=9,padx=10)

    #display update options

    prodlabel = Label(fr1,text='   Products   ').grid(row=0,column=0,padx=10,pady=10)
    pricelabel = Label(fr1,text='   Prices   ').grid(row=0,column=1)
    quantitylabel = Label(fr1,text=' Quantity Available ').grid(row=0,column=2)

    p1 = Label(fr1,text=(product1.name)).grid(row=1,column=0)
    price1 = Label(fr1,textvariable = str(product1.price)).grid(row=1,column=1)
    q1 = Label(fr1,textvariable=str(product1.quantity)).grid(row=1,column=2)

    p2 = Label(fr1, text=(product2.name)).grid(row=2, column=0)
    price2 = Label(fr1, textvariable=str(product2.price)).grid(row=2, column=1)
    q2 = Label(fr1, textvariable=str(product2.quantity)).grid(row=2, column=2)

    p3 = Label(fr1, text=(product3.name)).grid(row=3, column=0)
    price3 = Label(fr1, textvariable=str(product3.price)).grid(row=3, column=1)
    q3 = Label(fr1, textvariable=str(product3.quantity)).grid(row=3, column=2)


    def updateprice1():
        product1.price.set(pr1.get())
        data = Data(value=product1.price.get())
        aio.create_data((product1.name+'price'),data)
        print('Updated !')
        pr1.set(0)

    def updatequan1():
        product1.quantity.set(product1.quantity.get()+quantity1.get())
        data1 = Data(value=product1.quantity.get())
        aio.create_data(product1.name,data1)
        print('Updated !')
        quantity1.set(0)

    def updateprice2():
        product2.price.set(pr2.get())
        data = Data(value=product2.price.get())
        aio.create_data((product2.name+'price'), data)
        print('Updated !')
        pr2.set(0)

    def updatequan2():
        product2.quantity.set(product2.quantity.get()+quantity2.get())
        data1 = Data(value=product2.quantity.get())
        aio.create_data(product2.name, data1)
        print('Updated !')
        quantity2.set(0)

    def updateprice3():
        product3.price.set(pr3.get())
        data = Data(value=product3.price.get())
        aio.create_data((product3.name+'price'), data)
        print('Updated !')
        pr3.set(0)

    def updatequan3():
        product3.quantity.set(product3.quantity.get()+quantity3.get())
        data1 = Data(value=product3.quantity.get())
        aio.create_data(product3.name, data1)
        print('Updated !')
        quantity3.set(0)

    editPrice = Label(fr1,text='  Edit Prices  ').grid(row=0,column=4,padx=10)
    editQuantity = Label(fr1,text='  Add Quantity  ').grid(row=0,column=5)

    pr1 = IntVar()
    pre1 = Entry(fr1,textvariable=str(pr1)).grid(row=1,column=4,padx=20)
    quantity1 = IntVar()
    quan1 = Entry(fr1,textvariable=str(quantity1)).grid(row=1,column=5,padx=10)
    okprice1 = Button(fr1,text='Update Price',command=updateprice1).grid(row=1,column=6,padx=15)
    okquan1 = Button(fr1,text='Update Quantity',command=updatequan1).grid(row=1,column=7,padx=15)

    pr2 = IntVar()
    pre2 = Entry(fr1,textvariable=str(pr2)).grid(row=2, column=4)
    quantity2 = IntVar()
    quan2 = Entry(fr1,textvariable=str(quantity2)).grid(row=2, column=5)
    okprice2 = Button(fr1, text='Update Price',command=updateprice2).grid(row=2, column=6, padx=15)
    okquan2 = Button(fr1, text='Update Quantity',command=updatequan2).grid(row=2, column=7, padx=15)

    pr3 = IntVar()
    pre3 = Entry(fr1,textvariable=str(pr3)).grid(row=3, column=4)
    quantity3 = IntVar()
    quan3 = Entry(fr1,textvariable=str(quantity3)).grid(row=3, column=5)
    okprice3 = Button(fr1, text='Update Price',command=updateprice3).grid(row=3, column=6, padx=15)
    okquan3 = Button(fr1, text='Update Quantity',command=updatequan3).grid(row=3, column=7, padx=15)

    refresh = Button(fr1,text='Refresh Contents',command=main).grid(row=4,column=3)

main()

win.mainloop()