import imgkit
import os
import csv

# rollno = "CS16B045"
for filename in os.listdir('QRCodes/Proshows/'):
	rollno,ext = os.path.splitext(filename)
	nights = ""
	rock_show_file = open('list_rock.csv','rt')
	edm_night_file = open('list_edm.csv','rt')
	choreo_night_file = open('list_choreo.csv','rt')
	popular_night_file = open('list_popular.csv','rt')

	rock_show = csv.reader(rock_show_file)
	edm_night = csv.reader(edm_night_file)
	choreo_night = csv.reader(choreo_night_file)
	popular_night = csv.reader(popular_night_file)
	print(rollno)
	for row in rock_show:
		if row[2].upper()==rollno:
			# print("Yolo")
			nights += "<tr><td>%s</td><td>%s</td></tr>" % (str(row[6]),str(row[7]))
			break
	for row in edm_night:
		if row[2].upper()==rollno:
			nights += "<tr><td>%s</td><td>%s</td></tr>" % (str(row[6]),str(row[7]))
			# print("Yolo")
			break
	for row in choreo_night:
		if row[2].upper()==rollno:
			nights += "<tr><td>%s</td><td>%s</td></tr>" % (str(row[6]),str(row[7]))
			# print("Yolo")
			break
	for row in popular_night:
		if row[2].upper()==rollno:
			nights += "<tr><td>%s</td><td>%s</td></tr>" % (str(row[6]),str(row[7]))
			# print("Yolo")
			break

	# for filename in os.listdirs('QRCodes/Proshows/'):
	# 	rollno, ext = os.path.splitext(filename)
	html = """<!DOCTYPE html>
	<html>
	<head>
		<title></title>
	</head>
	<body>
		<div style="text-align: center;">	
			<img src="%s" style="height:200px;"><br>
			<p>This QR code is applicable only if you present your <strong>Institute ID card</strong> at the time of entrance.</p>
			<p><strong>Mess card not applicable.</strong></p><br>
			<img src="%s" style="height:400px;">
			<table style="display: inline-block; position: relative; bottom: 150px;">
				<tr>
					<th>Night</th>
					<th>Ticket</th>					
				</tr>
				%s
			</table>
			<p>%s</p>
		<p>In case you have lost your Institute ID card or are unable to present it, collect your ticket from <strong>Faculty Association Office, MSB</strong> from <strong>11:00 AM to 1:00 PM</strong> on the day of the show.
		<strong>Photo ID other than mess card</strong> is required to collect your ticket.</p><br>
		<p>Everyone is required to read the <strong>Security Policy</strong> from the link provided in the mail before coming.</p>
		<p>For further queries contact:<br>Uday - 8056197476<br>Uthej - 9502558377</p><br>
		<p><strong>Developed by Saarang Devops</strong></p>

	</div>
	</body>
	</html>""" % (str(os.path.dirname(os.path.abspath(__file__)))+'/saarang_logo.jpg',str(os.path.dirname(os.path.abspath(__file__)))+'/QRCodes/Proshows/'+rollno+'.png',nights,rollno)

	imgkit.from_string(html,'Attachments/'+rollno+'.jpg')

rock_show_file.close()
edm_night_file.close()
choreo_night_file.close()
popular_night_file.close()