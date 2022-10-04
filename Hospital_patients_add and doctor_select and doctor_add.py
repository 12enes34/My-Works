#video nun url si
# https://www.youtube.com/watch?v=y5AMBSZb9YM

#Enes Ünver 214210118 b gurubu



doktor_liste=[]
hasta_liste=[]
#ana class
class hastane:
    def __init__(self,hastane_ismi='short time'):
        hastane_ismi='short time hastanesi'
        self.hastane_ismi=hastane_ismi
        

class doktor(hastane):
    def __init__(self,doktor_ismi,unvan,uzm_alanı,hastane_ismi):
        super().__init__(hastane_ismi)
        self.doktor_ismi=doktor_ismi
        self.unvan=unvan
        self.uzm_alanı=uzm_alanı

    def doktorlistele(self):
        print(self.unvan,self.doktor_ismi,'uzmanlık alanı:',self.uzm_alanı)

    def doktoradı(self):
        return(self.doktor_ismi)

    
    
    
class hasta(hastane):
    def __init__(self,hasta_ismi,hastalık,ilaç,ilaç_veren_doktor,hastane_ismi):
        super().__init__(hastane_ismi)
        self.hasta_ismi=hasta_ismi
        self.hastalık=hastalık
        self.ilaç=ilaç
        self.ilaç_veren_doktor=ilaç_veren_doktor

    def hastalistele(self):
        print(self.hastane_ismi,'hastanesi ',self.hasta_ismi,' isimli hastanın hastalığı:',self.hastalık,'doktoru:',self.ilaç_veren_doktor,'verilen ilaç:',self.ilaç)
    @staticmethod
    def mesaj():
        print('geçmiş olsun')
        


def doktorekle(x):
    doktor_ismi=input('eklenecek doktor adını giriniz:')
    unvan=input('eklenecek doktorun unvanı:')
    uzm_alanı=input('eklenecek doktorun uzmanlık alanı:')
    hastane_ismi=x
    doktor_liste.append(doktor(doktor_ismi,unvan,uzm_alanı,hastane_ismi))
    


def hastaekle(x):
    hasta_ismi=input('hasta ismi:')
    hastalık=input('hastalik ismi:')
    ilaç=input('ilacı:')
    print('Doktor seçiniz:')
    
    for i in range(len(doktor_liste)):
        doktor_liste[i].doktorlistele()
        print(f'ıcın {i} ye basınız')
    x=int(input())
    for z in range(len(doktor_liste)):
        if x==z:
            ilaç_veren_doktor=doktor_liste[i].doktoradı()

    hastane_ismi=x
    hasta_liste.append(hasta(hasta_ismi,hastalık,ilaç,ilaç_veren_doktor,hastane_ismi))


a=90
while a!=0:
    a=int(input('cikis icin 0 a basiniz,doktor eklemek ıcın 1 e basınız,hasta eklemek için 2 ye basınız,doktor listelemek için 3 e basınız,hasta listelemek icin 4 e basınız,'))
    
    if a==1:
        doktorekle(hastane)
    elif a==2:
        hastaekle(hastane)
    elif a==3:
        for i in range(len(doktor_liste)):
            doktor_liste[i].doktorlistele()
    elif a==4:
        for i in range(len(hasta_liste)):
            hasta_liste[i].hastalistele()

hasta.mesaj()

























