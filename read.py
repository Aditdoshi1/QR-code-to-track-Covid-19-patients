from PIL import Image
from pyzbar.pyzbar import decode
import sqlite3
import re

conn = sqlite3.connect('pythonDB.db') 
cur = conn.cursor()

def dec():
	data = decode(Image.open('19235.png'))
	data1 = str(data[ 0 : 20 ])
	data2 = str(re.findall(r'b\'\d{1,10}', data1))
	data_final = str(data2[4:-2])
	print(data_final)

	cur.execute("SELECT * FROM patient_details1 where id=?", (data_final,))	
	rows = cur.fetchall()
	for row in rows:
		print(row)
	conn.commit()
	cur.close()
	conn.close()
			

dec()

