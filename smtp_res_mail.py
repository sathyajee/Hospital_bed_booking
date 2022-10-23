import csv
import smtplib
import ssl
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

UPR=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
DGTS=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

subject="RTPCR RESULT"
passw="shashsatyavir"
count=0
with open('record.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    with open('waste.csv','w',newline='') as newfile:
        writer=csv.writer(newfile, delimiter=',')
        for line in reader:
            if line[5]=="0":
                if line[4]=='positive':
                    BU_N=""
                    for x in range(3):
                        BU_N+=random.choice(UPR)
                    BU_N+="-"
                    for y in range(4):
                        BU_N+=random.choice(DGTS)
                    text="Dear "+line[0]+" your COVID-19 Swab test is POSITIVE.And your BU Number is "+BU_N+" You are advised to isolate yourself and be under medication. If Hospital is really neessary for you please fill the form provided with appropriate and correct details.GOVERNMENT OF PES https://docs.google.com/forms/d/e/1FAIpQLSdjtvYei6Su81WSTUtyQtW09kH-ljMxjf66YkDFnOYPUli9jA/viewform?usp=pp_url "
                    send_email=line[3]
                    msg=MIMEMultipart()
                    msg['From']='nationalcovidportal@gmail.com'
                    msg['To']=send_email
                    msg['Subject']=subject
                    msg.attach(MIMEText(text,"plain"))
                    text=msg.as_string()

                    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
                    server.login('nationalcovidportal@gmail.com',passw)
                    server.sendmail('nationalcovidportal@gmail.com',send_email,text)

                    server.quit()
                    count=1

                    writer.writerow([line[0],line[1],line[2],line[3],line[4],"1"])

            if line[5]=="0":
                if line[4]=='negative':
                    text="Dear "+line[0]+", your COVID-19 Swab test is NEGATIVE. Stay Safe. Call 1991 if any symptoms. GOVERNMENT OF PES"
                    send_email=line[3]
                    msg=MIMEMultipart()
                    msg['From']='rb9993848@gmail.com'
                    msg['To']=send_email
                    msg['Subject']=subject
                    msg.attach(MIMEText(text,"plain"))
                    text=msg.as_string()

                    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
                    server.login('nationalcovidportal@gmail.com',passw)
                    server.sendmail('nationalcovidportal@gmail.com',send_email,text)

                    server.quit()
                    count=1

                    writer.writerow([line[0],line[1],line[2],line[3],line[4],"1"])
                    
            if line[5]=="1":
                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5]])

os.remove('record.csv')
os.rename('waste.csv','record.csv')
print("---------------------------------------------------------------")
print()
if count==0:
    print("             NO NEW RESULTS UPDATED TO SEND MAIL")
if count==1:
    print("             MAIL HAS BEEN SENT SUCCESSFULLY")
a=input("Press any key to CONTINUE...")
