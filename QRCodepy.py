import pyqrcode
# import openpyxl
import csv
from keyczar import keyczar

def qrcodegen(data,location):
	img = pyqrcode.create(str(data))
	img.png(location,scale=10)
def encryptdata(data):
	location = "keyczarkeys"
	crypter = keyczar.Crypter.Read(location)
	encrypted_data = crypter.Encrypt(data)
	decrypted_data = crypter.Decrypt(encrypted_data)
	# print(encrypted_data)
	return encrypted_data
if __name__=="__main__":
	# excel = openpyxl.load_workbook(filename = "First Year's List.xlsx")
	# excel1 = openpyxl.load_workbook(filename = "Sharavathi.xlsx")
	
	rock_show_file = open('list_rock.csv','rb')
	edm_night_file = open('list_edm.csv','rb')
	choreo_night_file = open('list_choreo.csv','rb')
	popular_night_file = open('list_popular.csv','rb')


	rock_show = csv.reader(rock_show_file)
	edm_night = csv.reader(edm_night_file)
	choreo_night = csv.reader(choreo_night_file)
	popular_night = csv.reader(popular_night_file)
	
	roll_set = set()
	for row in rock_show:
		if row[2] == 'Student Id':
			continue
		roll_set.add(row[2].upper())
	
	for row in edm_night:
		if row[2] == 'Student Id':
			continue
		roll_set.add(row[2].upper())

	for row in choreo_night:
		if row[2] == 'Student Id':
			continue
		roll_set.add(row[2].upper())

	for row in popular_night:
		if row[2] == 'Student Id':
			continue
		roll_set.add(row[2].upper())


	for roll in roll_set:
		print(roll.upper())
		ciphertext = encryptdata(str(roll).upper())
		location = str(roll).upper() + '.png'
		qrcodegen(ciphertext,location) 
		break

	rock_show_file.close()
	edm_night_file.close()
	choreo_night_file.close()
	popular_night_file.close()
	# for sheet in excel.get_sheet_names():
	# 	sheetdata = excel[sheet]
	# 	i=1
	# 	data=sheetdata.cell(row=i,column=5).value
	# 	while data not in [None,'']:
	# 		if '17B' in data:
	# 			ciphertext=encryptdata(str(data))
	# 			location = "QRCodes/Boys/" + data + ".png"
	# 			qrcodegen(ciphertext,location)
	# 		i=i+1
	# 		data=sheetdata.cell(row=i,column=5).value
	# for sheet in excel1.get_sheet_names():
	# 	sheetdata = excel1[sheet]
	# 	i=1
	# 	data=sheetdata.cell(row=i,column=4).value
	# 	while data not in [None,'']:
	# 		if "17B" in data:
	# 			ciphertext=encryptdata(str(data))
	# 			location = "QRCodes/Girls/" + data + ".png"
	# 			qrcodegen(ciphertext,location)
	# 		i=i+1
	# 		data=sheetdata.cell(row=i,column=4).value



