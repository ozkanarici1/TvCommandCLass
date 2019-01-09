import random
import time
class Kanal():
    def __init__(self,tv_durum="açık",tv_ses=0,kanal_listesi=['atv','show','star','kanalD','Trt','Bein sport'],kanal="atv"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tv_ac(self):
        if(self.tv_durum=="açık"):
            print('tv zaten açık')
        else:
            print('tv açılıyor..')
            self.tv_durum="açık"
    def tv_kapat(self):
        if (self.tv_durum == "kapalı"):
            print('tv zaten kapalı')
        else:
            print('tv kapatılıyor.')
            self.tv_durum = "kapalı"
    def ses_ayarı(self):
        while True:
            cevap=input("sesi azalt : '<'\n Sesi arttır '>'\n Çıkış:çıkış")
            if(cevap=="<"):
                if(self.tv_ses!=0):

                    self.tv_ses -=1
                    print('ses : ',self.tv_ses)

            elif(cevap==">"):
                if(self.tv_ses!=31):
                    self.tv_ses+=1
                    print('ses : ',self.tv_ses)
            else:
                print("ses güncellendi ", self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
         print('Kanal ekleniyor..')
         time.sleep(1)
         self.kanal_listesi.append(kanal_ismi)
         print('Kanal eklendi')
    def rastgele_kanal(self):
        rasgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rasgele]
        print("şu anki kanal : ",self.kanal)
    def __len__(self):
         return len(self.kanal_listesi)
    def __str__(self):
         return "Tv durumu {} \n Tv ses {} \n Kanal listesi {} \n Şu anki kanal {} \n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
kumanda=Kanal()
while True:
             işlem=input('işlem seçiniz : ')
             if(işlem=="q"):
                 print('Programdan çıkılıyor ')
                 break
             elif(işlem=="1"):
                 kumanda.tv_ac()
             elif(işlem=="2"):
                 kumanda.tv_kapat()
             elif(işlem=="3"):
                 kumanda.ses_ayarı()
             elif(işlem=="4"):
                 kumanda.rastgele_kanal()
             elif(işlem=="5"):
                 kanalisim=input('kanal isimlerini virgülle ayırınız')
                 kanal_listesi=kanalisim.split(",")
                 for eklenecek in kanal_listesi:
                     kumanda.kanal_ekle(eklenecek)
             elif(işlem=="6"):
                 print('kanal sayısı ',len(kumanda))
             else:
                 print('Geçersiz işlem')







