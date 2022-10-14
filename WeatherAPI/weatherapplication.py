import tkinter
from tkinter import Message, messagebox
import requests
from PIL import ImageTk, Image  
from datetime import date

root = tkinter.Tk()
root.title('Weather Application')
root.geometry('600x400')

ngaythang = date.today()

label0 = tkinter.Label(root,text='Weather Report',width=85,height=2,fg='white',bg='blue').place(x=0,y=0)

label1 = tkinter.Label(root,text='City or Country name').place(x=190,y=70)

label2 = tkinter.Label(root,height=2,width=15,text='NA-/',fg='white',bg='blue')
label2.place(x=0,y=0)

label3 = tkinter.Label(root,height=2,width=10,text=ngaythang,fg='white',bg='blue').place(x=480,y=0)

label4 = tkinter.Label(root,text='Weather Report',width=85,height=2,fg='white',bg='blue').place(x=0,y=180)


var1 = tkinter.StringVar()
textbox1 = tkinter.Entry(root,textvariable=var1).place(x=190,y=100)



image1 = ImageTk.PhotoImage(Image.open('D:\HocLapTrinh\PythonAPI\WeatherAPI\icon.png'))
image2 = ImageTk.PhotoImage(Image.open('D:\HocLapTrinh\PythonAPI\WeatherAPI\icon2.png'))
image3 = ImageTk.PhotoImage(Image.open('D:\HocLapTrinh\PythonAPI\WeatherAPI\icon3.png'))
image4 = ImageTk.PhotoImage(Image.open('D:\HocLapTrinh\PythonAPI\WeatherAPI\icon4.png'))
image5 = ImageTk.PhotoImage(Image.open('D:\HocLapTrinh\PythonAPI\WeatherAPI\icon5.png'))

panel1 = tkinter.Label(root,image=image1).place(x=50,y=50)

panel2 = tkinter.Label(root,image=image2).place(x=50,y=250)

panel3 = tkinter.Label(root,image=image3).place(x=200,y=250)

panel4 = tkinter.Label(root,image=image4).place(x=350,y=250)

panel5 = tkinter.Label(root,image=image5).place(x=500,y=250)


plabel1 = tkinter.Label(root,text='NA-/')
plabel1.place(x=55,y=300)

plabel2 = tkinter.Label(root,text='NA-/')
plabel2.place(x=205,y=300)

plabel3 = tkinter.Label(root,text='NA-/')
plabel3.place(x=355,y=300)

plabel4 = tkinter.Label(root,text='NA-/')
plabel4.place(x=505,y=300)


def loi():
    if var1.get() == '':
        messagebox.showerror('Vui lòng nhập tên thành phố')

def start():
    loi()
    url = 'http://api.openweathermap.org/data/2.5/weather?q='
    city = var1.get()
    apikey = 'fe53bfd100e8ca1c2ca47f202a2e9b9c'
    truelink = url + city + '&appid=' + apikey
    data = requests.get(truelink).json()
    if data['cod']=='404':
        messagebox.showerror('Không tìm thấy thành phố')
    else:
        label2.config(text=data['name']+ ', '+ data['sys']['country'])
        plabel1.config(text=(data['weather'][0]['main']))
        plabel2.config(text = str(round(data['main']['temp']-273.15,0)) + "°C" + "\n" + str(round(data['main']['temp'])) + "°F")
        plabel3.config(text=str(data['main']['humidity'])+'%')
        plabel4.config(text=data['main']['sea_level'])

def reset():
    label2.config(text='NA-/')
    plabel1.config(text='NA-/')
    plabel2.config(text='NA-/')
    plabel3.config(text='NA-/')
    plabel4.config(text='NA-/')

button1 = tkinter.Button(root,text='Select',command=lambda:start())
button1.place(x=400,y=100)

button2 = tkinter.Button(root,text='Reset',command=reset)
button2.place(x=500,y=100)

root.mainloop()