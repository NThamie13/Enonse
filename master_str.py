print(     )
print("                                                  MASTER STR (index, split, replace,lower,upper,title")
print("                                  *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=* *=*=*=*=*=*=*=*          ")
print(     )

#1_Tout karakte en miniskil
mesaj = ("BonJou ToUt Moun Nan KarayiB Lan")
if any (char.isupper() for char in mesaj) :
    mesaj = mesaj.lower()
    print("1_",mesaj)
    print() 

#2_Nan yon chenn karakte, koupe chenn nan tout kote ki gen espas
espas = ("Byenvini an Amerik")
if ' ' in espas :
    print("2_",espas.split())
    print() 

#3_Nan yon chenn karakte, mete tout premye let chak mo an majiskil.
prog = "mwen renmen langaj python anpil"
maj = prog.split()
t = " "
for chak_mo in maj:
    t += chak_mo.capitalize() + " "
print("3_", t)
print() 

#4_Nan yon chenn karakte, rekipere premye let chak mo.
rekipere = "Thamar se non mwen"
dekoupe = rekipere.split()
chenn = " "
for word in dekoupe:
    chenn += word[0]
print("4_","Nouvo chenn ak tout inisyal yo se :", chenn)
print() 

#5_Ranplase tout karakte "a" ki nan yon chenn pa "@"
abite = ("Map viv lalue ak manman'm")
t = (" ")
for el in abite :
    chanje = el.replace("a","@")
    t += chanje
print("5_",t) 
print() 

#6_Mete yon chenn karakte devan deye, ansuit mete'l an majiskil
non = "Thamar"
envese = non[::-1].upper()
print("6_ Chenn karakte envese a se :", envese)
print() 

#7_Afiche endeks premye karakte "a" ki nan yon chenn. 
endeks = "Ayiti se pa'n, nou kapab ann avanse"
karakte_a = 'a'
for i in range(len(endeks)):
        pozisyon = endeks.index(karakte_a)
print("7_ Premye karakte 'a' trouvel nan pozisyon :",pozisyon)
print() 
    
#8_Afiche total tout endeks karakte "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil).
tout_endeks = "Ayiti se pa'n, kanal la pap kanpe"
pozisyon = 0 
for element in range (len(tout_endeks)):
     if tout_endeks[element] =='a' or tout_endeks[element] == 'A' :
          pozisyon += element
print("8_ Total tout endeks karakte 'a' se : ",pozisyon)
print() 

#9_Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil)
fruit = "Ananas ak mango efikas pou'n sante"
liste_fruit = []
element ='a'
compt = 0
for i in range(len(fruit)):
     if fruit[i] == 'a':
        compt = i
        liste_fruit.append(compt)
print("9_",liste_fruit)
print() 

#10_Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karakte li genyen (Pa kontwole espas yo).
p = "Ayiti se yon peyi espesyal"
konte = 0
c = ''
for al in p :
     if al != ' ':
          c += al
          konte += 1        
          kole = c + str(konte)
print("10_",kole)
print(                   )

print(         )
print("                                                MASTER LIST (Union & Intersection & Lis comprehension")
print("                                  *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=* *=*=*=*=*=*=*=*          ")
print(     )

#1_ Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
vale = 0,2,7,11,12,22,28,36,44,58,62,70
liste_element = []
for eleman in vale :
     if eleman % 2 == 0:
          liste_element.append(eleman)
print("1_Lis eleman divisib pa 2 yo se : ",liste_element)
print()

#2_Ou gen yon lis antye, konvèti l an yon lis chenn.
lis_entye = [0,4,5,11,12,13,30,55]
lis_chenn=[]
for j in lis_entye:
     lis_chenn.append(str(j))
print("2_Lis antye an vinn : ",lis_chenn)
print()

#3_Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
lis_miniskil = ["python, html, css, java, javascript, django"]
lis_majikil = []
for k in lis_miniskil:
     lis_majikil.append(k.upper())
print("3_Lis chenn miniskil la vinn : ",lis_majikil)
print()

#4_Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
premye_lis = [0,2,22,38,47,54,61,74,87,98,99,100,109]
dezyem_lis=[]
for u in range(len(premye_lis)) :
     if u % 3 == 0 :
          dezyem_lis.append(premye_lis[u])
print("4_Eleman ki nan endeks divisib pa 3 yo se: ",dezyem_lis)
print()

#5_Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl.
lis = [13,14,15,16,17,18,19,20,21]
lis_de_twa =[]
for l in range(0,len(lis), 3):
     tipl = lis[l : l + 3]
     lis_de_twa.append(tuple(tipl))
print("5_Lis de 3 eleman nan yon tipl : ",lis_de_twa)
print()

#6_Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon.
doublon = [0,1,5,5,6,7,8,8,8,9,10,13,13,15,16,17,17,19,20,22,23,23]
nouvo_lis = []
for i in range(len(doublon)):
     if doublon[i-1] != doublon[i]:
          nouvo_lis.append(doublon[i])
print("6_Lis sans doublon an se : ",nouvo_lis)
print()

#7_Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.
lis_1 = [13,14,15,20,37,41,43,67,69,74,83]
lis_2 = [13,16,18,20,31,37,43,69,75,80,83,90]
lis_3 = []
for i in range (len(lis_1)):
     for j in range (len(lis_2)) :
          if lis_1[i] == lis_2[j] :
               lis_3.append(lis_2[j])
print("7_Eleman komen ant 2 lis yo se : ",lis_3)
print()

#8_Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo.
lis1 = [13,14,15,20,37,41,43,67,69,74,83]
lis2 = [13,16,18,20,31,37,43,69,75,80,83,90]
lis3 = []
for m in lis1 + lis2 :
     if m not in lis1 or m not in lis2 :
          lis3.append(m)
print("8_Eleman distenge ant 2 lis yo se : ",lis3)
print()     

#9_Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman.
dictio = {
     'Nom' : 'NINGE',
     'Prenom' : 'Thamar',
     'Niveau' : 'License'
}
new_lis_kle = []
new_lis_vale = []
new_lis_kle.append(dictio.keys())
new_lis_vale.append(dictio.values())
print("9_Ansanm de kle yo nan diksyone an se :" ,new_lis_kle)
print()
print(" _Ansanm de vale yo nan diksyone an se :", new_lis_vale)
print()

#10_Reyini 3 lis ansanm, san okenn doublon.
lis1 = [0,1,5,6,7,8,9,10,13,13,15,16,17,17,19,20,22,23,25]
lis2 = [0,2,2,3,5,6,7,8,8,9,12,13,16,17,18,19,20,21,22,24]
lis3 = [3,5,6,8,9,10,11,12,13,15,16,17,19,20,22,24,24,25]
lis4 = list(set(lis1+ lis2 + lis3))
print("10_Reunion de 3 lis san doublon : ",lis4)
print(                   )

print(         )
print("                                                      MASTER DICTIONNAIRE (insistance, eval")
print("                                  *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=* *=*=*=*=*=*=*=*          ")
print(     )

#1_Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis vale
diksyone ={'maten' : 'swa', 
           'soley' : 'lalin',
          'kontan':'fache',
          'rich': 'pov'}
vale = list(diksyone.values())
print("1_Lis vale nan diksyone an se :",vale)
print()

#2_Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak deye
valeur = input("Antre yon vale stp:")
devan = valeur.startswith('{')
deye = valeur.endswith('}')
if devan and deye :
          print ("2_Li gen akolad devan ak deye.")
          print()
elif devan :
     print("Li gen akolad devan selman")
     print()
elif deye :
     print("Li gen akolad deye selman")
     print()
else:
     print ("2_Li pa gen akolad ni devan ni deye.")
     print()
         
#3_Pakouri yon diksyonè, epi afiche tout kle yo
etidyan = {
     'non' : 'SIMON',
     'prenon' :'Edithe',
     'lekol' : 'Esih',
     'stati' : 'marie'
}
print(f"3_Ansanm de kle yo nan diksyone etidyan se : {etidyan.keys()}")
print()

#4_Pakouri yon diksyonè, epi afiche tout valè yo.
prof = {
     'non' : 'Lauture',
     'prenon' :'Jeanine',
     'lekol' : 'Uniq',
     'stati' : 'Selibate'
}
print(f"4_Ansanm de vale yo nan diksyone etidyan se : {prof.values()}")
print()

#5_Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.
ces= {
'Matiere' : 'Maths',
'Domaine': 'Informatique',
"Session" : "2eme",
'Professeur': 'Mr Bens Alive'
}
kopi_ces = dict(ces.copy())
print("5_Kopi de diksyone an se : ", kopi_ces)
print()

#6_Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done). Ajoute yon underscore devan ak dèyè tout valè ki se chenn yo
info = {
     "name" :"Thamie",
     "age" : 20,
     "market" : ["belmart", "Delimart"],
     "Atis" : "Rutshelle"
}
for a , b in info.items() :
     if type (b) == str :
          info[a] = ('_' + b + '_')
print("6_Ajou de underscore devan ak deye tout vale ki se chenn yo : ",info)
print()

#7_Nan yon diksyonè ki gen valè ki se chenn sèlman. Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman.
dictyo = {
     "a" : "12", "b" : "43" , "c" : "Cedrick", "s" : "Simeon"
}
new_dictyo = {}
for cle , valeur in dictyo.items():
     if valeur.isnumeric():
          new_dictyo [cle] = valeur
print("7_Nouvo diksyone ki gen digit selman:",new_dictyo)
print()

#8_Pakouri yon disksyonè, pou w mete l sou fòm lis, kote chak eleman nan disksyonè sa, vin sou fòm tipl(kle, valè) anndan lis la.
dic = {"a" : "12", "b" : "13"}
lis = []
for j , k in dic.items():
     ajout = j,k
     lis.append(ajout)
print("8_Diksyone sou fom lis",lis)
print()

#9_Pakouri yon lis tipl, pou w mete l sou fòm diksyonè. 
t = ("a",11), ("b",22), ("c",33), ("d",44)
d =dict(t)
print("9_Lis tipl sou fom diksyone :",d)
print()

#10_Kole 2 diksyonè ansanm pou fè youn, kote si gen eleman ki gen menm kle ap konkatene valè, swivan kondisyon sa yo:
#Antye: ADISYON
#Chenn, lis, set: KONKATENASYON
#Rès eleman ki pa gen valè ki gen tip sa yo, pap nan nouvo diksyonè a.
dict1 = {
     "non" : "Elie",
     "age" : 7,
     "hauteur" : 1.20,
     "nourriture" : ["Riz", "Pois"]
}
dict2 ={
     "non" : "Kyria",
     "age" : 4,
     "hauteur" : 1.10 ,
     "nourriture" : ["Pâtes", "Légumes"]
     #"boissons" : ["Coca", "MaltaH"]
}
dict3={}
for k in dict1.keys() | dict2.keys():
    rekipere1= dict1.get(k, '')
    rekipere2= dict2.get(k, '')
    if isinstance(rekipere1, int) and isinstance(rekipere2,int) :
        dict3[k] = rekipere1 + rekipere2
    elif isinstance(rekipere1, str) and isinstance(rekipere2,str) :
        dict3[k] = rekipere1 + rekipere2
    elif isinstance(rekipere1, list) and isinstance(rekipere2,list) :
        dict3[k] = rekipere1 + rekipere2
    elif isinstance(rekipere1, set) and isinstance(rekipere2,set) :
        dict3[k] = rekipere1 + rekipere2  
print("10_De diksyone yo vinn bay:" ,dict3)
print(                   )

print(         )
print("                                                               MASTER FUNCTION CONCEPT"                                                 )
print("                                  *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=* *=*=*=*=*=*=*=*          ")
print(     )

#1_kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la.
def mot (param1) :
    return param1[::-1]
kreye = "Vanessa"
envese = mot(kreye)
print("1_Mo envese fonksyon an retounen an se:", envese )
print()

#2_kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik.
import random
import string
def aleya(k) :
    chwa = string.ascii_lowercase
    use = ''
    for _ in range(k):
        use += random.choice(chwa)
    return(use)
n = 7
use = aleya(n)
print("2_Kod aleyatwa avek karakte alfabetik yo se: ",use)
print()

#3_kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon.
import random
import string
def sansrep(r) :
    chwa = string.ascii_lowercase
    mot = ''
    while len (mot) < r :
        karakte = random.choice(chwa)
        if karakte not in mot :
            mot += karakte
    return(mot)
n = 8
use = sansrep(n)
print("3_Kod aleyatwa avek karakte alfabetik san repetisyon an se: ",use)
print()

#4_kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon.
import random
import string
def alfa(t) :
    chwa_alfanum = string.ascii_lowercase + string.digits
    kod = ''
    while len (kod) < t :
        karakte_alfanum= random.choice(chwa_alfanum)
        if karakte_alfanum not in kod :
            kod += karakte_alfanum
    return(kod)
nb = 10
tot = alfa(nb)
print("4_Kod aleyatwa avek karakte alafanimerik san repetisyon an se: ",tot)
print()

#5_Ou gen yon lis chenn. Jenere yon SLUG apati chenn nan. Nan yon SLUG, tout karaktè ki akseptab yo se: alfanimerik ak "-"
import re
def fonct_slug(lis_chenn):
    sl = []
    for opt in lis_chenn:
        slug = re.sub(r'[^a-zA-Z0-9 ]', '', opt)
        slug = slug.replace(' ', '-')
        sl.append(slug)
    return sl
lis_chenn = ["13 I am a Beautiful Woman"]
slugs = fonct_slug(lis_chenn)
print(slugs)
print()

#6_Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil
def separe (m,n) :
        sep = n.join(m)
        return(sep)
mo ="JESUS"
vigil = ','
retour = separe(mo,vigil)
print("6_Mot nan yon fonksyon ki separe ak vigil :",retour)
print()

#7_Kreye yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè.
import string
def krip (mo,alfa ):
    kriptaj = [str(alfa.index(karakt)) for karakt in mo if karakt in alfa]
    kriptaj = '-'.join(kriptaj)
    return kriptaj
alfa = string.ascii_letters
mot = krip("edithe",alfa)
print("7_Mo kripte an se: ", mot)
print()

#8_Kreye yon fonksyon ki ap dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè.
import string
def dekrip (mo, alfa):
    pozisyonlettre = [int(position) for position in mo.split("-")]
    dekriptaj = ''.join([alfa[position] for position in pozisyonlettre])
    return dekriptaj
mo = "1-14-1"
alfabe = string.ascii_lowercase
mots = dekrip(mo,alfa)
print("8_Mo dekripte an se: ",mots)
print()

#9_kreye yon fonksyon ki ap pran 2 paramet,epi ki pemite vale yo.answit li retounen tou 2 vale yo sou fom tuple
def ret(param1,param2):
    param1,param2= param2, param1
    return param1, param2
param1=13
param2="Tham"
param1,param2 = ret(param1,param2)
print("9_Vale pemite yo se :",param1,param2)
print()

#10_Kreye yon fonksyon ki ap pran yon non an paramèt, epi ki retounen inisyal yo. Atansyon ak non konpoze ak tirè yo.
def initial(non):
    re = non.split('-')
    rere = " "
    for el in re:
        nom = el.split()
        for el in nom:
            rere += el[0]
    return rere
nom = "Marie-Thamie Ninge"
inisyal = initial(nom)
print("10_Inisyal fonksyon an retounen an se :",inisyal)  
print(                  )
    







