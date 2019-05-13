import re

##No 1
f = open("Indonesia.txt", "r")
teks = f.read()
pola = r"me\w+"

strings = re.findall(pola, teks)
print ("Hasilnya", strings )

##No 2
f = open("Indonesia.txt", "r")
teks = f.read()
pola = r"di\w+"

strings = re.findall(pola, teks)
print ("Hasilnya", strings)

#No3
f = open("Indonesia.txt", "r")
teks = f.read()
pola = r"di\s\w+"

strings = re.findall(pola, teks)
print ("Hasilnya", strings)

#No4
#a
f = open("KEI.html", "r", encoding = "latin1")
teks = f.read()
f.close()
pola = r"([\w+]+)</td></a>"

tup = re.findall(pola,teks)
print(tup)

#b
f = open('KEI.html','r', encoding='latin1')
teks = f.read()
f.close()
tup = re.findall(r'title="([\w+]+)">',teks)
tup = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks)
a = []
for i in tup :
    a.append((i[0], float(i[1])))
print(a)













