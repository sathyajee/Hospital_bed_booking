import csv
import smtplib
import ssl
import gspread
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope=["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client=gspread.authorize(creds)
sheet=client.open("Bed_Booking_Form").sheet1

count=0

with open('Hospital_list.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
        if line[0]=="PANACEA":
            panacea=int(line[2])
        if line[0]=="FORTIS":
            fortis=int(line[2])
        if line[0]=="KC_GENERAL":
            kc_general=int(line[2])
        if line[0]=="BOWRING":
            bowring=int(line[2])
        if line[0]=="ESI_KA_02":
            esi_ka_02=int(line[2])
        if line[0]=="VICTORIA":
            victoria=int(line[2])
        if line[0]=="COLUMBIA_ASIA":
            columbia_asia=int(line[2])
        if line[0]=="APOLLO":
            apollo=int(line[2])
        if line[0]=="MS_RAMAIAH":
            ms_ramaiah=int(line[2])
        if line[0]=="MALLIGE":
            mallige=int(line[2])
        if line[0]=="MANIPAL":
            manipal=int(line[2])
            
        #FORMAT 1R --> Register with Hospital Name
        """
        if line[0]=="<#HOSPITAL#>":
            <#hospital#>=int(line[2])
        if line[0]=="<#HOSPITAL#>":
            <#hospital#>=int(line[2])
        """

#GETTING LENGTH OF GSHEET AND OVERWRITTING LAST READ
data=sheet.get_all_records()
n=len(data)
with open('last_read.txt') as f:
    lines = f.readlines()
    j=int(lines[0])
nfp=open("last_read.txt","w")
nfp.write(str(n))
nfp.close()

#ITERATING IN G SHEET
for i in range(j+1,n+1):
    name=sheet.cell(i+1,2).value
    email_person=sheet.cell(i+1,4).value
    pincode=sheet.cell(i+1,7).value

    #FORMAT 2R --> Register with Hospital's pincode
    #Replace <#PINCODE#> with 6-digit integer
    #Replace <#hospital#> with hospital name(lower case) and <#HOSPITAL#> with upper case
    """
    if pincode=="<#PINCODE#>":  #HOSPITALS in <#PINCODE#>
        
        if <#hospital#>!=0:
            <#hospital#>-=1
            
            text="Dear "+name+" you have been alloted in <#HOSPITAL#> HOSPITAL for COVID-19 treatment. Please get admitted within 2 days to avoid Cancellation of bed. Follow the map for the Hospital"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1
            continue

        else:
            text="Dear "+name+", presently there are NO beds available in your area limits. Please fill the following form once again and wait for the further updates. https://docs.google.com/forms/d/e/1FAIpQLSdjtvYei6Su81WSTUtyQtW09kH-ljMxjf66YkDFnOYPUli9jA/viewform?usp=pp_url"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
    """
    
    if pincode=="560072":  #HOSPITALS in 560072
        
        if panacea!=0:
            panacea-=1
            
            text="Dear "+name+" you have been alloted in PANACEA HOSPITAL for COVID-19 treatment. Please get admitted within 2 days to avoid Cancellation of bed. Location for the Hospital is provided here https://www.google.com/maps/place/Panacea+Hospital+Nagarabhavi,+Panacea+Hospital+%23+611+%2F612,+Nagarabhavi+Main+Road+2nd+Stage+Vinayaka+Layout,+Nagarabhavi+Bangalore+-+560+072,+80+Feet+Main+Rd,+2+Stage,+Naagarabhaavi,+Bengaluru,+Karnataka+560056/@12.9612955,77.5095113,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae3e81963b7b59:0x173b445df1908291!8m2!3d12.9612903!4d77.5117"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1
            continue
            
        if fortis!=0:
            fortis-=1
            text="Dear "+name+" you have been alloted in FORTIS HOSPITAL for COVID-19 treatment. Please get admitted within 2 days to avoid Cancellation of bed. Location for the Hospital is provided here https://www.google.com/maps/place/Fortis+Hospital,+Nagarbhavi,+Bangalore/@12.9595991,77.5089953,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae16773c548eed:0xff00fb1e264b6969!8m2!3d12.9595939!4d77.511184"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1
            continue
            
        else:
            text="Dear "+name+", presently there are NO beds available in your area limits. Please fill the following form once again and wait for the further updates. https://docs.google.com/forms/d/e/1FAIpQLSdjtvYei6Su81WSTUtyQtW09kH-ljMxjf66YkDFnOYPUli9jA/viewform?usp=pp_url"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1

    if pincode=="560003":  #HOSPITALs in 560003

        if kc_general!=0:
            kc_general-=1
            text="Dear "+name+" you have been alloted in KC GENERAL HOSPITAL for COVID-19 treatment. Please get admitted within 2 days to avoid Cancellation of bed. Location for the Hospital is provided here https://www.google.com/maps/place/K.C.+General+Hospital/@12.9961428,77.5671693,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae1624498c8b85:0xd95533c6e2c6bddb!8m2!3d12.9961428!4d77.569358"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1
            continue

        else:
            text="Dear "+name+", presently there are NO beds available in your area limits. Please fill the following form once again and wait for the further updates. https://docs.google.com/forms/d/e/1FAIpQLSdjtvYei6Su81WSTUtyQtW09kH-ljMxjf66YkDFnOYPUli9jA/viewform?usp=pp_url"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1

    if pincode=="560001":  #HOSPITALS in 560001

        if bowring!=0:
            bowring-=1
            text="Dear "+name+" you have been alloted in BOWRING AND LADY CURZON HOSPITAL for COVID-19 treatment. Please get admitted within 2 days to avoid Cancellation of bed. Location for the Hospital is provided here https://www.google.com/maps/place/Bowring+and+Lady+Curzon+Hospital/@12.9821932,77.6018685,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae1663b446cb89:0x2a8952c4f01fa407!8m2!3d12.982188!4d77.6040572"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1
            continue

        if mallige!=0:
            mallige-=1
            text="Dear "+name+" you have been alloted in MALLIGE HOSPITAL for COVID-19 treatment. Please get admitted within 2 days to avoid Cancellation of bed. Location for the Hospital is provided here https://www.google.com/maps/place/Mallige+Hospital/@12.9853173,77.5781693,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae16142b8d7fff:0x28d52520c417efe3!8m2!3d12.9853121!4d77.580358"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1
            continue

        else:
            text="Dear "+name+", presently there are NO beds available in your area limits. Please fill the following form once again and wait for the further updates. https://docs.google.com/forms/d/e/1FAIpQLSdjtvYei6Su81WSTUtyQtW09kH-ljMxjf66YkDFnOYPUli9jA/viewform?usp=pp_url"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1

    if pincode=="560010":  #HOSPITALS in 560010

        if esi_ka_02!=0:
            esi_ka_02-=1
            text="Dear "+name+" you have been alloted in ESI HOSPITAL RAJAJINAGAR for COVID-19 treatment. Please get admitted within 2 days to avoid Cancellation of bed. Location for the Hospital is provided here https://www.google.com/maps/place/ESI+Hospital+Main+Rd,+Rajajinagar,+Bengaluru,+Karnataka+560010/@12.9899746,77.5511987,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae3d8d7c4761ed:0xa5cf60e99210d46a!8m2!3d12.9899694!4d77.5533874"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1
            continue

        else:
            text="Dear "+name+", presently there are NO beds available in your area limits. Please fill the following form once again and wait for the further updates. https://docs.google.com/forms/d/e/1FAIpQLSdjtvYei6Su81WSTUtyQtW09kH-ljMxjf66YkDFnOYPUli9jA/viewform?usp=pp_url"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1

    if pincode=="560002":  #HOSPITALS in 560002

        if victoria!=0:
            victoria-=1
            text="Dear "+name+" you have been alloted in VICTORIA HOSPITAL for COVID-19 treatment. Please get admitted within 2 days to avoid Cancellation of bed. Location for the Hospital is provided here https://www.google.com/maps/place/Victoria+Hospital/@12.9635721,77.5716187,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae15e2d61081e7:0x6e7d0833b6fa721e!8m2!3d12.9635669!4d77.5738074"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1
            continue

        else:
            text="Dear "+name+", presently there are NO beds available in your area limits. Please fill the following form once again and wait for the further updates. https://docs.google.com/forms/d/e/1FAIpQLSdjtvYei6Su81WSTUtyQtW09kH-ljMxjf66YkDFnOYPUli9jA/viewform?usp=pp_url"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1

    if pincode=="560055":  #HOSPITALS in 560055

        if columbia_asia!=0:
            columbia_asia-=1
            text="Dear "+name+" you have been alloted in COLUMBIA ASIA HOSPITAL for COVID-19 treatment. Please get admitted within 2 days to avoid Cancellation of bed. Location for the Hospital is provided here https://www.google.com/maps/place/Columbia+Asia+Referral+Hospital+%E2%80%93+Yeshwanthpur/@13.0141953,77.5538781,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae162a55555555:0x886d228d64097005!8m2!3d13.0141901!4d77.5560668"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1
            continue

        else:
            text="Dear "+name+", presently there are NO beds available in your area limits. Please fill the following form once again and wait for the further updates. https://docs.google.com/forms/d/e/1FAIpQLSdjtvYei6Su81WSTUtyQtW09kH-ljMxjf66YkDFnOYPUli9jA/viewform?usp=pp_url"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1

    if pincode=="560020":  #HOSPITALS in 560020

        if apollo!=0:
            apollo-=1
            text="Dear "+name+" you have been alloted in APOLLO HOSPITAL for COVID-19 treatment. Please get admitted within 2 days to avoid Cancellation of bed. Location for the Hospital is provided here https://www.google.com/maps/place/Apollo+Hospitals+Sheshadripuram+Bangalore/@12.9883074,77.5704992,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae17ddf4a463e3:0x415a988bfb0b66c8!8m2!3d12.9883022!4d77.5726879"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1
            continue

        else:
            text="Dear "+name+", presently there are NO beds available in your area limits. Please fill the following form once again and wait for the further updates. https://docs.google.com/forms/d/e/1FAIpQLSdjtvYei6Su81WSTUtyQtW09kH-ljMxjf66YkDFnOYPUli9jA/viewform?usp=pp_url"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1

    if pincode=="560054":  #HOSPITALS in 560054

        if ms_ramaiah!=0:
            ms_ramaiah-=1
            text="Dear "+name+" you have been alloted in MS RAMAIAH HOSPITAL for COVID-19 treatment. Please get admitted within 2 days to avoid Cancellation of bed. Location for the Hospital is provided here https://www.google.com/maps/place/Ramaiah+Memorial+Hospital/@13.0282606,77.5682037,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae17dc7777e56d:0x3bfb44b6b12ec9d0!8m2!3d13.0282554!4d77.5703924"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1
            continue

        else:
            text="Dear "+name+", presently there are NO beds available in your area limits. Please fill the following form once again and wait for the further updates. https://docs.google.com/forms/d/e/1FAIpQLSdjtvYei6Su81WSTUtyQtW09kH-ljMxjf66YkDFnOYPUli9jA/viewform?usp=pp_url"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1

    if pincode=="560017":  #HOSPITALS in 560017

        if manipal!=0:
            manipal-=1
            text="Dear "+name+" you have been alloted in MANIPAL HOSPITAL for COVID-19 treatment. Please get admitted within 2 days to avoid Cancellation of bed. Location for the Hospital is provided here https://www.google.com/maps/place/Manipal+Hospital/@12.9583963,77.6466477,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae13c0c0c6206b:0x12d8d4c39197c7dd!8m2!3d12.9583911!4d77.6488364"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1
            continue

        else:
            text="Dear "+name+", presently there are NO beds available in your area limits. Please fill the following form once again and wait for the further updates. https://docs.google.com/forms/d/e/1FAIpQLSdjtvYei6Su81WSTUtyQtW09kH-ljMxjf66YkDFnOYPUli9jA/viewform?usp=pp_url"
            send_email=email_person
            msg=MIMEMultipart()
            msg['From']='nationalcovidportal@gmail.com'
            msg['To']=send_email
            msg['Subject']="HOSPITAL ALLOTMENT FOR COVID-19 TREATMENT"
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server=smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login('nationalcovidportal@gmail.com','shashsatyavir')
            server.sendmail('nationalcovidportal@gmail.com',send_email,text)

            server.quit()
            count=1

#UPDATING FILE
with open('Hospital_list.csv','r') as csvfile:
        reader=csv.reader(csvfile)
        with open('newfile.csv','w',newline='') as newfile:
            writer = csv.writer(newfile, delimiter=',')
            for line in reader:
                if line[0]=="PANACEA":
                    writer.writerow([line[0],line[1],panacea])
                if line[0]=="FORTIS":
                    writer.writerow([line[0],line[1],fortis])
                if line[0]=="KC_GENERAL":
                    writer.writerow([line[0],line[1],kc_general])
                if line[0]=="BOWRING":
                    writer.writerow([line[0],line[1],bowring])
                if line[0]=="ESI_KA_02":
                    writer.writerow([line[0],line[1],esi_ka_02])
                if line[0]=="VICTORIA":
                    writer.writerow([line[0],line[1],victoria])
                if line[0]=="COLUMBIA_ASIA":
                    writer.writerow([line[0],line[1],columbia_asia])
                if line[0]=="APOLLO":
                    writer.writerow([line[0],line[1],apollo])
                if line[0]=="MS_RAMAIAH":
                    writer.writerow([line[0],line[1],ms_ramaiah])
                if line[0]=="MALLIGE":
                    writer.writerow([line[0],line[1],mallige])
                if line[0]=="MANIPAL":
                    writer.writerow([line[0],line[1],manipal])

                #FORMAT 3R
                #Replace <#HOSPITAL#> with upper case
                """
                if line[0]=="<#HOSPITAL#>":
                    writer.writerow([line[0],line[1],<#hospital#>])
                if line[0]=="<#HOSPITAL#>":
                    writer.writerow([line[0],line[1],<#hospital#>])
                """

os.remove('Hospital_list.csv')
os.rename('newfile.csv','Hospital_list.csv')

if count==0:
    print("            NO UPDATES IN THE BED BOOKING GOOGLE FORM")
if count==1:
    print("            HOSPITAL ALLOTMENT MAIL SENT SUCCESSFULLY!")
z=input("Enter any key to CONTINUE.....")
