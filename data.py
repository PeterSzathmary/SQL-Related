meno=["Chlieb","Jablko","Mrkva","Hruska","Slivka","Rozok",
"Cibula","Stehno - kuracie","Stehno - morcacie","Stehno - bravcove",
"Pomelo","Granatove jablko","Sunka - kuracia","Sunka - morcacia",
"Tlacenka - bravcova","Tlacenka - kuracia","Zemiak","Pomaranc",
"Makovnik"]

typ=["Pecivo","Ovocie","Zelenina","Ovocie","Ovocie","Pecivo",
"Zelenina","Maso","Maso","Maso","Ovocie","Ovocie","Maso",
"Maso","Maso","Maso","Zelenina","Ovocie","Pecivo"]

cena=[1.50,0.79,0.59,0.89,0.70,0.06,0.60,2.30,3.69,
4.19,2.59,0.99,7.16,10.38,4.57,5.36,0.49,0.89,1.79]

balenie=["ks","kg","kg","kg","kg","ks","kg","kg",
"kg","kg","ks","ks","kg","kg","kg","kg","kg","kg","ks"]

f = open("inserts_lidl.sql","a")
for i in range(len(meno)):
    if i < len(meno) - 1:
        f.write(f"INSERT INTO LIDL (Meno, Typ, Cena, Balenie) VALUES (\"{meno[i]}\", \"{typ[i]}\", {cena[i]}, \"{balenie[i]}\");\n")
    else:
        f.write(f"INSERT INTO LIDL (Meno, Typ, Cena, Balenie) VALUES (\"{meno[i]}\", \"{typ[i]}\", {cena[i]}, \"{balenie[i]}\");")
f.close()

meno=["Cibula","Tlacenka - bravcova","Makovnik","Paprika",
"Slivka","Rozok","Sunka - kuracia","Sunka - bravcova",
"Zemiak","Pomaranc","Chlieb","Granatove jablko","Jablko",
"Mrkva","Hruska"]

typ=["ZEL","MAS","PEC","ZEL","OVO","PEC","MAS",
"MAS","ZEL","OVO","PEC","OVO","OVO","ZEL","OVO"]

cena=[0.58,4.40,3.80,0.89,0.75,0.06,
6.30,5.70,0.05,0.72,1.49,1.09,0.79,0.59,0.89]

balenie=["kg","kg","kg","kg","kg","ks","kg","kg",
"ks","kg","ks","ks","kg","kg","kg"]

f = open("inserts_kaufland.sql","a")
for i in range(len(meno)):
    if i < len(meno) - 1:
        f.write(f"INSERT INTO KAUFLAND (Meno, Typ, Cena, Balenie) VALUES (\"{meno[i]}\", \"{typ[i]}\", {cena[i]}, \"{balenie[i]}\");\n")
    else:
        f.write(f"INSERT INTO KAUFLAND (Meno, Typ, Cena, Balenie) VALUES (\"{meno[i]}\", \"{typ[i]}\", {cena[i]}, \"{balenie[i]}\");")
f.close()

id=[]
id.extend(range(1,11))

percento=[10,12,7,15,35,60,5,10,3,12]

datum=["08.04.2022","15.04.2022","22.04.2022","29.04.2022",
"06.05.2022","13.05.2022","20.05.2022","27.05.2022","03.06.2022",
"10.06.2022"]

f = open("inserts_zlavy.sql","a")
for i in range(len(id)):
    if i < len(id) - 1:
        f.write(f"INSERT INTO ZLAVY (ID, Percento, Datum) VALUES (\"{id[i]}\", {percento[i]}, \"{datum[i]}\");\n")
    else:
        f.write(f"INSERT INTO ZLAVY (ID, Percento, Datum) VALUES (\"{id[i]}\", {percento[i]}, \"{datum[i]}\");")
f.close()