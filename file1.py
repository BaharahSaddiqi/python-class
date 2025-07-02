
#file opnen und lesen 

with open("C:/Users/xy/Documents/My_Project/PCAP/PCAP/data.txt", "r", encoding="UTF-8")as file:
    content=file.read()
    print(content)
    #file öfnnen und shreiben 
    #lätste zeil wird gelöchen mit(w) 
with open("C:/Users/xy/Documents/My_Project/PCAP/PCAP/data.txt", "w", encoding="UTF-8")as file:
   file.write("chara khat gabli ro pak mikoni ? ")   



with open("C:/Users/xy/Documents/My_Project/PCAP/PCAP/data.txt", "a", encoding="UTF-8")as file:
    file.write("ich lerne gerade python\n")   

#file als bainary lesen und und die summe erhalten 
file= open ("C:/Users/xy/Documents/My_Project/PCAP/PCAP/data.txt","rb")  
summe=0
for line in file:
    print(len(line))
    summe+=len(line)
print("gesmat",summe)
file.close()


#
with open("C:/Users/xy/Documents/My_Project/PCAP/PCAP/data.txt", "w+")as file:
    file.write("ich lerne gerade python\n")   
    file.seek(0)# erste file zu lesen 
    text=file.read()
    print(text.strip())