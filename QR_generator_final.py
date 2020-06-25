import sqlite3
import qrcode
import PIL.Image
from tkinter import filedialog
from tkinter import *

conn = sqlite3.connect('pythonDB.db') 
cur = conn.cursor()

def senti():
	cur.execute('CREATE TABLE IF NOT EXISTS patient_details1 (ID REAL PRIMARY KEY, Name TEXT NOT NULL, Age Real NOT NULL, Address TEXT NOT NULL, tested TEXT NOT NULL, result TEXT NOT NULL, contact REAL NOT NULL, Image BLOB NOT NULL)') 
	id=id1.get()
	name1=name.get()
	age1=age.get()
	address1=address.get()
	tested1=tested.get()
	result1=result.get()
	contact1=contact.get()
	filename = filedialog.askopenfilename()
	a = filename
	print(a)
	cur.execute("INSERT INTO patient_details1 (ID, Name, Age, Address, tested, result, contact, Image) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (id, name1, age1, address1, tested1, result1, contact1, a)) 
	cur.execute("SELECT * FROM patient_details1")
	rows = cur.fetchall()
	for row in rows:
		print(row)
	conn.commit()
	cur.close()
	conn.close()
	
	data = id
	filename1 = id+".png"
	img1 = qrcode.make(data)
	img1.save(filename1)
	
	im = PIL.Image.open(filename1).convert("RGB")
	logo = PIL.Image.open(a)
	box = (135,135,170,170)
	im.crop(box)
	region = logo
	region = region.resize((box[2] - box[0], box[3] - box[1]))
	im.paste(region,box)
	im.save(id+".png")
	img = qrcode.make(data)
	img.save(filename)

	print("QR Code is generated")


r = Tk() 
r.geometry("1000x600")
r.title('Real-Time Sentimenal Analysis') 
Label(r, text='Id:').grid(row=0,pady=20)
Label(r, text='Name:').grid(row=1,pady=20)
Label(r, text='Age:').grid(row=2,pady=20)
Label(r, text='Address:').grid(row=3,pady=20)
Label(r, text='tested:').grid(row=4,pady=20)
Label(r, text='result:').grid(row=5,pady=20)
Label(r, text='Contact Details:').grid(row=6,pady=20)

id1 = Entry(r)
name = Entry(r)
age = Entry(r)
address = Entry(r)
tested = Entry(r)
result = Entry(r)
contact = Entry(r)
id1.grid(row=0, column=1,ipadx=150,ipady=5)
name.grid(row=1, column=1,ipadx=150,ipady=5)
age.grid(row=2, column=1,ipadx=150,ipady=5)
address.grid(row=3, column=1,ipadx=150,ipady=5)
tested.grid(row=4, column=1,ipadx=150,ipady=5)
result.grid(row=5, column=1,ipadx=150,ipady=5)
contact.grid(row=6, column=1,ipadx=150,ipady=5)

buttonP = Button(r, text='Generate QR code', width=25, command=senti) 
buttonP.grid(row=10,padx=10,ipadx=40,ipady=10)
buttonS = Button(r, text='Exit', width=25, command=r.destroy) 
buttonS.grid(row=10,column=1,padx=120,ipadx=40,ipady=10)

r.mainloop()