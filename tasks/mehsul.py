mehsullar=[ ]
class Mehsul():
    def __init__(self,_ad,_qiymet,_miqdar):
        self.ad=_ad
        self.qiymet=_qiymet
        self.miqdar=_miqdar
        mehsullar.append(self) 
    def melumatGoster(self):
        print(f'{self.ad} | {self.qiymet} | {self.miqdar}')

    # def elaveEt(self):
    #      mehsullar.append(self) 

def istehsalEt():
    ad=input('Mehsulun adi :')
    qiymet=int(input('Mehsulun qiymeti :'))
    miqdar=int(input('Mehsulun miqdari :'))
    mehsul=Mehsul(ad,qiymet,miqdar)

for say in range(3):
    istehsalEt()

def melumatlariGoster():
    for mehsul in mehsullar:
        mehsul.melumatGoster()
        

def qiymetCeminiTap():
    qiymetlerinCemi=0
    for mehsul in mehsullar:
        qiymetlerinCemi=qiymetlerinCemi+mehsul.qiymet

    print(f'Mehsullarin umumi qiymet cemi {qiymetlerinCemi} - dir')
emr=input('Mehsullari gormek ucun 1 , qiymet cemini gormek ucun 2 yazin');

if emr=='1':
    melumatlariGoster()
elif emr=='2':
    qiymetCeminiTap()        
