import csv
import time
import os

def update(panacea,fortis,kc_general,bowring,mallige,esi_ka_02,victoria,columbia_asia,apollo,ms_ramaiah,manipal):
    with open('Hospital_list.csv','r') as csvfile:
        reader=csv.reader(csvfile)
        with open('newfile.csv','w',newline='') as newfile:
            writer = csv.writer(newfile, delimiter=',')
            for line in reader:
                if line[0]=="PANACEA":
                    writer.writerow(line[0],line[1],panacea)
                if line[0]=="FORTIS":
                    writer.writerow(line[0],line[1],fortis)
                if line[0]=="KC_GENERAL":
                    writer.writerow(line[0],line[1],kc_general)
                if line[0]=="BOWRING":
                    writer.writerow(line[0],line[1],bowring)
                if line[0]=="ESI_KA_02":
                    writer.writerow(line[0],line[1],esi_ka_02)
                if line[0]=="VICTORIA":
                    writer.writerow(line[0],line[1],victoria)
                if line[0]=="COLUMBIA_ASIA":
                    writer.writerow(line[0],line[1],columbia_asia)
                if line[0]=="APOLLO":
                    writer.writerow(line[0],line[1],apollo)
                if line[0]=="MS_RAMAIAH":
                    writer.writerow(line[0],line[1],ms_ramaiah)
                if line[0]=="MALLIGE":
                    writer.writerow(line[0],line[1],mallige)
                if line[0]=="MANIPAL":
                    writer.writerow(line[0],line[1],manipal)
                        
