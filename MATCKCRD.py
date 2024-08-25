import random
class Match:

    def __init__ (self,word,des):
        self.word=word
        self.des=des
        self.cardnum={}

    def ADD(self, word,des): 
   
        self.cardnum[word]=des
        return self.cardnum
    


card1= Match ("","")
nu= input("  you want to creat a card       ")

while nu!="no":
    word=input ("  entre the woerd      ")
    des= input ("entre the description     ")
    card1.ADD(word,des)
    nu= input(" do you wany tro add a new one       ")


# for j in card1.cardnum:
#     print(j)
#     wordtetst= input (" entrz the word   ")
#     if j== wordtetst:
#         continue
#     else:
#         print(" try again   ")
#     break   

Words=[] 
descri=[]
for x,y in card1.cardnum.items()   :
    Words.append(x)
    descri.append(y)
print ("how do you want to revise word by word / multiple choices  ")
way= input ("choise the way to review :    ")
match way :
    case "word by word":
        while True :
            WC= random.choice(Words)
            print (WC)
            woo= input (" entre the correct word  ")
            if card1.cardnum[WC]==woo :
               print (" you doing well ")
               continue
            else :
                print (" try again ")
                break
    case "multiple choices" :         
        WORDS2= random.sample(Words,len(Words)) 
        while True:
            for f in WORDS2:
                print(f)
                d=Words.index(f)
                ju=d
                newlis= descri[ju::1]
                trlis=random.sample(newlis,len(newlis))
                print(random.sample(trlis,len(trlis)))
                correct= input (" entre the corect  word   ")
                if card1.cardnum[f]==correct :
                    print (" you doing well  ")
                    continue
                else:
                    print (" try a nother way ")
                    break
            con=input (' do you wqnt to stqrt over ')
            if con !="no":
                continue
            else:
                break



    

# print(Words)
# k= int (input(" entre    "))

# review= random.sample(descri, k)
# print(review)        
