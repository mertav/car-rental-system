from ast import Pass
from distutils import command
from tkinter import *
from tkinter import ttk
from turtle import heading, left, width
from PIL import Image, ImageTk
import mysql.connector as SQLC
import mysql.connector 
from mysql.connector import connection
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox
from tkinter import messagebox

class AracOto():
    
    def __init__(self):
        self.pencere=Tk()
        self.pencere.geometry("600x600")
        self.pencere.title("Araç-Kiralama-Otomasyonu")
        self.pencere.resizable(False, False)
        self.pencere.config(background="lightblue")
        self.databaseOlustur()

        #?------------------İlk Pencere Label ----------------------------
        label2=Label(self.pencere, text="Araç Kiralama Otomasyon Uygulaması ", fg="White",bg="lightblue", font="Fixedsys 22 bold" )
        label2.place(x=3,y=50)

        framebuton=Frame(self.pencere, bg="white")
        framebuton.place(relx=0.2, rely=0.2, relwidth=0.60, relheight=0.60)

        #?------------------İlk Pencere Buton ----------------------------
        musteributon = Button(framebuton,bd=5, fg="white", font=('Fixedsys', 14, 'bold'), width=14, text="Müşteri Kayıt", bg="black", cursor="hand2", overrelief="groove", height=3,command=self.musterikayit)
        musteributon.pack(side=TOP,expand=TRUE)

        aracbuton  = Button(framebuton,bd=5, fg="white", font=('Fixedsys', 14, 'bold'), width=14, text="Araç Kayıt", bg="black", cursor="hand2", overrelief="groove", height=3,command=self.arackayit)
        aracbuton.pack(side=TOP,expand=TRUE)

        kiraArac = Button(framebuton, bd=5, fg="white", font=('Fixedsys', 14, 'bold'), width=14, text="Araç Kirala", bg="black",  cursor="hand2", overrelief="groove", height=3,command=self.aracKirala  )
        kiraArac.pack(side=TOP,expand=TRUE)

        listeleKiralanan = Button(framebuton,bd=5, fg="white", font=('Fixedsys', 14, 'bold'), width=14, text="Kiralama Bilgi", bg="black", cursor="hand2", overrelief="groove", height=3,command=self.kiralanmıs_pencere)
        listeleKiralanan.pack(side=BOTTOM,expand=TRUE)



    #*##########################################################################################################
    #!-----------------DATABASE VE TABLO OLUSTURMA------------------
    def databaseOlustur(self):
        try:
            DataBase=SQLC.connect(
                host="localhost",
                user="admin",
                password="deneme"
            )
            Cursor=DataBase.cursor()
            Cursor.execute("CREATE DATABASE 90200000195mert")
            print("90200000195mert", "Adlı Database Oluşturuldu")
        except:
            print("Database Halihazırda Mevcut")
        try:
            dataBase=mysql.connector.connect(
                host="localhost",
                user="admin",
                passwd="deneme",
                database="90200000195mert")

            CursorObject=dataBase.cursor()
            arac_90200000195_Record="""CREATE TABLE musteribilgi(
                TC_NO VARCHAR(11) NOT NULL PRIMARY KEY,
                AD VARCHAR(40) NULL,
                SOYAD VARCHAR(40) NULL,
                DOGUM_TARİHİ VARCHAR(40) NULL,
                ADRES VARCHAR(40) NULL,
                TELEFON VARCHAR(11) NULL,
                MESLEK VARCHAR(40) NULL,
                EHLİYET VARCHAR(40) NULL,
                MEDENİ_DURUM VARCHAR(40) NULL,
                EGİTİM_DURUMU VARCHAR(45) NULL
            )"""
            CursorObject.execute(arac_90200000195_Record)
        except:
            
            print("1.Tablo Halihazırda Mevcut")
        try:
            dataBase=mysql.connector.connect(
                host="localhost",
                user="admin",
                passwd="deneme",
                database="90200000195mert")

            CursorObject1=dataBase.cursor()

            arac_90200000195_Record2="""CREATE TABLE aracbilgi(
                SasiNo VARCHAR(17) NOT NULL PRIMARY KEY,
                AracTuru VARCHAR(40) NULL,
                Marka VARCHAR(40) NULL,
                Model VARCHAR(40) NULL,
                UretimYili VARCHAR(40) NULL,
                YakitTuru VARCHAR(40) NULL,
                Vites VARCHAR(40) NULL,
                MotorGucu VARCHAR(40) NULL,
                KasaTipi VARCHAR(40) NULL,
                MotorHacmi VARCHAR(40) NULL,
                Cekis VARCHAR(40) NULL,
                Kapi VARCHAR(40) NULL,
                Renk VARCHAR(40) NULL,
                MotorNo VARCHAR(17) NULL,
                GunlukKiraBedel VARCHAR(40) NULL,
                Kiradami VARCHAR(40) NULL,
                KullanimDisimi VARCHAR(40) NULL
            )"""
            CursorObject1.execute(arac_90200000195_Record2)
        except:
            print("2.Tablo Halihazırda Mevcut")
        try:
            dataBase=mysql.connector.connect(
                host="localhost",
                user="admin",
                passwd="deneme",
                database="90200000195mert")
            CursorObject2=dataBase.cursor()
            arac_90200000195_Record3="""CREATE TABLE kira(
                MusteriTCNo VARCHAR(11) NOT NULL PRIMARY KEY,
                Ad VARCHAR(40) NOT NULL,
                Soyad VARCHAR(40) NOT NULL,
                Telefon VARCHAR(40) NOT NULL,
                AracSaseNo VARCHAR(17) NOT NULL,
                Marka VARCHAR(40) NOT NULL,
                Model VARCHAR(40) NOT NULL,
                Yakıt VARCHAR(40) NULL,
                Yolculuk VARCHAR(40) NOT NULL,
                KacGun VARCHAR(40) NOT NULL,
                KiraBedeli VARCHAR(40) NOT NULL,
                KiraDurumu VARCHAR(40) NOT NULL
            )"""
            CursorObject2.execute(arac_90200000195_Record3)
        except:
            print("3.Tablo Halihazırda Mevcut")

    #*##########################################################################################################
    #!-----------------MUSTERİ KAYIT FRAME--------------------------
    def musterikayit(self):
        print("çalıştı")
        self.pencereMusteri=Toplevel()
        self.pencereMusteri.title("Müşteri Kayıt ")
        self.pencereMusteri.geometry("1200x500")
        self.pencereMusteri.resizable(False, False)

        self.Ad=StringVar()
        self.Soyad=StringVar()
        self.TcKimlik=StringVar()
        self.DogumTarih=StringVar()
        self.Adres=StringVar()
        self.Telefon=StringVar()
        self.Meslegi=StringVar()
        self.EhliyetSinifi=StringVar()
        self.MedeniDurumu=StringVar()
        self.EgitimDurumu=StringVar()

        canvas=Canvas(self.pencereMusteri, height=500, width=1200, bg="white")
        canvas.pack()
        #?------------------ İKİNCİ EKRAN FRAME ----------------
        framebilgi=Frame(canvas, bg="lightblue")
        framebilgi.place(relx=0.01, rely=0.01, relwidth=0.25 , relheight=0.6)

        framebuton2=Frame(canvas, bg="lightblue")
        framebuton2.place(relx=0.01, rely=0.63, relwidth=0.25, relheight=0.33)

        frameveri=Frame(canvas, bg="lightblue")
        frameveri.place(relx=0.27, rely=0.01, relwidth=0.72, relheight=0.94)
        #?---------------------------İKİNCİ EKRAN LABEL -----------------------
        musteribaslık=Label(framebilgi, text="Müşteri Kayıt",font="Arial 10 bold", bg="lightblue",pady=3)
        musteribaslık.grid(row=0, column=0)

        
        tcLabel=Label(framebilgi, text="Tc No  *:", font="Arial 10 bold", bg="lightblue",pady=3)
        tcLabel.grid(row=1, column=0)
        
        adLabel=Label(framebilgi, text="Ad *:", font="Arial 10 bold", bg="lightblue",pady=3)
        adLabel.grid(row=2, column=0)

        soyadLabel=Label(framebilgi, text="Soyad  *:", font="Arial 10 bold", bg="lightblue",pady=3 )
        soyadLabel.grid(row=3, column=0)

        dtLabel=Label(framebilgi, text="Doğum Tarihi *:", font="Arial 10 bold", bg="lightblue",pady=3)
        dtLabel.grid(row=4, column=0)

        adresLabel=Label(framebilgi, text="Adress :", font="Arial 10 bold", bg="lightblue",pady=3)
        adresLabel.grid(row=5, column=0)

        tlfLabel=Label(framebilgi, text="Telefon :", font="Arial 10 bold", bg="lightblue",pady=3)
        tlfLabel.grid(row=6, column=0)

        meslekLabel=Label(framebilgi, text="Mesleği :", font="Arial 10 bold", bg="lightblue",pady=3)
        meslekLabel.grid(row=7, column=0)

        ehliyetLabel=Label(framebilgi, text="Ehliyet Sınıfı *:", font="Arial 10 bold", bg="lightblue",pady=3)
        ehliyetLabel.grid(row=8, column=0)

        medeniLabel=Label(framebilgi, text="Medeni Durumu :", font="Arial 10 bold", bg="lightblue",pady=3)
        medeniLabel.grid(row=9, column=0)

        egitimLabel=Label(framebilgi, text="Eğitim Durumu  *:", font="Arial 10 bold", bg="lightblue",pady=3)
        egitimLabel.grid(row=10, column=0)

        #?------------- İKİNCİ EKRAN ENTRY ---------------------
        self.tcEntry=Entry(framebilgi,textvariable=self.TcKimlik,bd=3)
        self.tcEntry.grid(row=1, column=1)
        
        self.adEntry=Entry(framebilgi, textvariable=self.Ad,bd=3)
        self.adEntry.grid(row=2, column=1)

        self.soyadEntry=Entry(framebilgi,textvariable=self.Soyad,bd=3)
        self.soyadEntry.grid(row=3, column=1)

        self.dtEntry=Entry(framebilgi,textvariable=self.DogumTarih,bd=3)
        self.dtEntry.grid(row=4, column=1)

        self.adresEntry=Entry(framebilgi,textvariable=self.Adres,bd=3 )
        self.adresEntry.grid(row=5, column=1)

        self.tlfEntry=Entry(framebilgi,textvariable=self.Telefon,bd=3)
        self.tlfEntry.grid(row=6, column=1)

        self.meslekEntry=Entry(framebilgi,textvariable=self.Meslegi,bd=3)
        self.meslekEntry.grid(row=7, column=1)

        self.ehliyetEntry=Entry(framebilgi,textvariable=self.EhliyetSinifi,bd=3)
        self.ehliyetEntry.grid(row=8, column=1)  

        self.medeniEntry=Entry(framebilgi,textvariable=self.MedeniDurumu,bd=3)
        self.medeniEntry.grid(row=9, column=1)  

        self.egitimEntry=Entry(framebilgi,textvariable=self.EgitimDurumu,bd=3)
        self.egitimEntry.grid(row=10, column=1)  

        #?----------------------İKİNCİ EKRAN BUTON -------------
        butonkayıt=Button(framebuton2, bd=2, relief=SUNKEN,command=self.musteriVeri,text="Kayıt Et", bg="black", fg="white", font="Arial 10 bold", width=25, height=1, overrelief="groove", cursor="hand2")
        butonkayıt.grid(row=0, column=1, columnspan=2,padx=40, pady=3)

        butonkayıtsil=Button(framebuton2, bd=2, relief=SUNKEN, command=self.musteriVeriSil, text="Kayıt Sil ", bg="black", fg="white", font="Arial 10 bold", width=25, height=1, overrelief="groove", cursor="hand2")
        butonkayıtsil.grid(row=1, column=1, columnspan=2,padx=15, pady=3)

        butonkayıtguncel=Button(framebuton2, bd=2, relief=SUNKEN,command=self.guncelle, text="Kayıt Güncelle ", bg="black", fg="white", font="Arial 10 bold", width=25, height=1, overrelief="groove", cursor="hand2")
        butonkayıtguncel.grid(row=2, column=1, columnspan=2,padx=15, pady=3)

        butontemizle=Button(framebuton2, bd=2, relief=SUNKEN,command=self.musteriGirdiTemizle, text="Kayıt Temizle ", bg="black", fg="white", font="Arial 10 bold", width=25, height=1, overrelief="groove", cursor="hand2")
        butontemizle.grid(row=3, column=1, columnspan=2,padx=15, pady=3)

        butoncikisMusteri=Button(framebuton2, bd=2, relief=SUNKEN,command=self.musteriCikis, text="Çıkış", bg="black", fg="white", font="Arial 10 bold", width=20, height=1, overrelief="groove", cursor="hand2")
        butoncikisMusteri.grid(row=4, column=1, columnspan=2,padx=15, pady=1)
        
        #?----------------------BİLGİ EKRANI;(TREWİEV)--------------------------
        scroollx=Scrollbar(frameveri, orient=HORIZONTAL)
        scroolly=Scrollbar(frameveri, orient=VERTICAL)
        self.musteribilgiTablo=ttk.Treeview(frameveri, column=("TcKimlik","Ad","Soyad",
        "DogumTarihi","Adres","Telefon","Mesleği","EhliyetSinifi","MedeniDurumu","EgitimDurumu"),xscrollcommand=scroollx.set,yscrollcommand=scroolly.set)
        
        scroollx.pack(side=BOTTOM, fill=X)
        scroolly.pack(side=RIGHT, fill=Y)

        scroollx.config(command=self.musteribilgiTablo.xview)
        scroolly.config(command=self.musteribilgiTablo.yview)
        
        
        self.musteribilgiTablo.heading("TcKimlik", text="TC NO")
        self.musteribilgiTablo.heading("Ad", text="AD")
        self.musteribilgiTablo.heading("Soyad", text="SOYAD")
        self.musteribilgiTablo.heading("DogumTarihi", text="Dogum tarihi"),
        self.musteribilgiTablo.heading("Adres", text="Adress")
        self.musteribilgiTablo.heading("Telefon", text="Telefon No")
        self.musteribilgiTablo.heading("Mesleği", text="Meslek")
        self.musteribilgiTablo.heading("EhliyetSinifi", text="Ehliyet")
        self.musteribilgiTablo.heading("MedeniDurumu", text="Medeni Hal")
        self.musteribilgiTablo.heading("EgitimDurumu", text="Egitim Hali")

        self.musteribilgiTablo["show"]="headings"

        self.musteribilgiTablo.column("TcKimlik", width=100)
        self.musteribilgiTablo.column("Ad", width=100)
        self.musteribilgiTablo.column("Soyad", width=100)
        self.musteribilgiTablo.column("DogumTarihi", width=100)
        self.musteribilgiTablo.column("Adres", width=100)
        self.musteribilgiTablo.column("Telefon", width=100)
        self.musteribilgiTablo.column("Mesleği", width=100)
        self.musteribilgiTablo.column("EhliyetSinifi", width=100)
        self.musteribilgiTablo.column("MedeniDurumu", width=100)
        self.musteribilgiTablo.column("EgitimDurumu", width=100)


        self.musteribilgiTablo.pack(fill=BOTH, expand=1)
        self.musteribilgiTablo.bind("<ButtonRelease-1>",self.imlecYazdirmusteri)
        self.fatch_veri()
    def musteriVeri(self):
        if len(self.TcKimlik.get())<11 or len(self.TcKimlik.get())>=12 :
            messagebox.showerror("Hata","Tc No 11 hane olmalıdır")
        elif len(self.DogumTarih.get())<10:
                messagebox.showerror("Hata","Doğum tarihini 'GÜN/AY/YILL' şeklinde giriniz")
        elif len(self.Ad.get())<2 or len(self.Soyad.get())<2 or len(self.EgitimDurumu.get())<1 or len(self.EhliyetSinifi.get())<1:
                messagebox.showerror("Hata","Zorunlu olan yerleri doldurunuz (*)")
        elif len(self.Telefon.get())<11 and len(self.Telefon.get())>12:
            messagebox.showerror("Hata","Telefon Numarası 11 haneli olmalıdır")
        else:
            conn =mysql.connector.connect(host="localhost", username="admin", password="deneme", database="90200000195mert")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO musteribilgi values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.TcKimlik.get(),
                                                                                            self.Ad.get(),
                                                                                            self.Soyad.get(),
                                                                                            self.DogumTarih.get(),
                                                                                            self.Adres.get(),
                                                                                            self.Telefon.get(),
                                                                                            self.Meslegi.get(),
                                                                                            self.EhliyetSinifi.get(),
                                                                                            self.MedeniDurumu.get(),
                                                                                            self.EgitimDurumu.get()))

            conn.commit()
            self.fatch_veri()
            conn.close()
            messagebox.showinfo("Başarılı","Kayıt Başarıyla Gerçekleştirildi")

            self.adEntry.delete(0, END)
            self.soyadEntry.delete(0, END)
            self.tcEntry.delete(0, END)
            self.dtEntry.delete(0, END)
            self.adresEntry.delete(0, END)
            self.tlfEntry.delete(0, END)
            self.meslekEntry.delete(0, END)
            self.ehliyetEntry.delete(0, END)
            self.medeniEntry.delete(0, END)
            self.egitimEntry.delete(0, END)      
    def guncelle(self):
        conn =mysql.connector.connect(host="localhost", username="admin", password="deneme", database="90200000195mert")
        my_cursor=conn.cursor()
        my_cursor.execute("update musteribilgi set AD=%s, SOYAD=%s, DOGUM_TARİHİ=%s, ADRES=%s, TELEFON=%s, MESLEK=%s, EHLİYET=%s, MEDENİ_DURUM=%s, EGİTİM_DURUMU=%s where TC_NO=%s",(
                                                                                                                                                                            self.Ad.get(),
                                                                                                                                                                            self.Soyad.get(),
                                                                                                                                                                            self.DogumTarih.get(),
                                                                                                                                                                            self.Adres.get(),
                                                                                                                                                                            self.Telefon.get(),
                                                                                                                                                                            self.Meslegi.get(),
                                                                                                                                                                            self.EhliyetSinifi.get(),
                                                                                                                                                                            self.MedeniDurumu.get(),
                                                                                                                                                                            self.EgitimDurumu.get(),
                                                                                                                                                                            self.TcKimlik.get(),
                                                                                                                                                                            ))
        conn.commit()
        self.fatch_veri()
        conn.close()      
        messagebox.showinfo("Başarılı","Bilgiler başarılı bir şekilde güncellendi") 

        self.TcKimlik.set("")
        self.Ad.set("")
        self.Soyad.set("")
        self.DogumTarih.set("")
        self.Adres.set("")
        self.Telefon.set("")
        self.Meslegi.set("")
        self.EhliyetSinifi.set("")
        self.MedeniDurumu.set("")
        self.EgitimDurumu.set("")
    def fatch_veri(self):
        conn =mysql.connector.connect(host="localhost", username="admin", password="deneme", database="90200000195mert")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from musteribilgi")        
        rows=my_cursor.fetchall()
        if len(rows) !=0:
            self.musteribilgiTablo.delete(*self.musteribilgiTablo.get_children())
            for i in rows:
                self.musteribilgiTablo.insert("", END, values=i)
            conn.commit()
        conn.close()
    def imlecYazdirmusteri(self, event=""):
        imlec_satir=self.musteribilgiTablo.focus()
        icerik=self.musteribilgiTablo.item(imlec_satir)
        satir=icerik["values"]
        self.TcKimlik.set(satir[0])
        self.Ad.set(satir[1])
        self.Soyad.set(satir[2])
        self.DogumTarih.set(satir[3])
        self.Adres.set(satir[4])
        self.Telefon.set(satir[5])
        self.Meslegi.set(satir[6])
        self.EhliyetSinifi.set(satir[7])
        self.MedeniDurumu.set(satir[8])
        self.EgitimDurumu.set(satir[9])      
    def musteriVeriSil(self):
        conn=mysql.connector.connect(host="localhost", username="admin", password="deneme", database="90200000195mert")
        my_cursor=conn.cursor()
        sorgu="DELETE FROM musteribilgi WHERE TC_NO=%s"
        value=(self.TcKimlik.get(),)
        my_cursor.execute(sorgu,value)
        conn.commit()
        conn.close()
        self.fatch_veri()
        messagebox.showinfo("Silindi","Müşteri kaydı başarıyla silindi")
    def musteriGirdiTemizle(self):

        self.adEntry.delete(0, END)
        self.soyadEntry.delete(0, END)
        self.tcEntry.delete(0, END)
        self.dtEntry.delete(0, END)
        self.adresEntry.delete(0, END)
        self.tlfEntry.delete(0, END)
        self.meslekEntry.delete(0, END)
        self.ehliyetEntry.delete(0, END)
        self.medeniEntry.delete(0, END)
        self.egitimEntry.delete(0, END)  
    def musteriCikis(self):
        cikis=messagebox.askyesno("Musteri Cikis Yapılsın mı?", "Çıkışı onaylıyor musunuz ?")
        if cikis>0:
            self.pencereMusteri.destroy()
            return
    #*##########################################################################################################
    #!-----------------ARAC KAYIT FRAME.---------------------------
    def arackayit(self):
        print("çalıştı")
        self.pencereAraba=Toplevel()
        self.pencereAraba.title("Araç Kayıt Pencere")
        self.pencereAraba.geometry("1500x700")
        self.pencereAraba.resizable(False, False)

        self.SasiNo=StringVar()
        self.AracTuru=StringVar()
        self.Marka=StringVar()
        self.Model=StringVar()
        self.UretimYili=StringVar()
        self.YakitTuru=StringVar()
        self.Vites=StringVar()
        self.MotorGucu=StringVar()
        self.KasaTipi=StringVar()
        self.MotorHacmi=StringVar()
        self.Cekis=StringVar()
        self.Kapi=StringVar()
        self.Renk=StringVar()
        self.MotorNo=StringVar()
        self.GKiralamaBedeli=StringVar()
        self.Kiradami=StringVar()
        self.KullanimDisimi=StringVar()



        canvas=Canvas(self.pencereAraba, height=700, width=1500, bg="white")
        canvas.pack()
        #?------------------ ARABA BİLGİ EKRAN FRAME ----------------
        framebilgiAraba=Frame(canvas, bg="lightblue")
        framebilgiAraba.place(relx=0.01, rely=0.01, relwidth=0.35 , relheight=0.6)

        framebutonAraba=Frame(canvas, bg="lightblue")
        framebutonAraba.place(relx=0.01, rely=0.63, relwidth=0.35, relheight=0.32)

        frameveriAraba=Frame(canvas, bg="lightblue")
        frameveriAraba.place(relx=0.37, rely=0.01, relwidth=0.62, relheight=0.94)

        #?-------------------İKİNCİ EKRAN LABEL--------------------------
        aracbaslık=Label(framebilgiAraba, text="Müşteri Kayıt",font="Arial 11 bold", bg="lightblue",pady=3)
        aracbaslık.grid(row=0, column=0)

        labelSasiNo=Label(framebilgiAraba,text="Şasi No :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelSasiNo.grid(row=1, column=0) 

        labelAracTuru=Label(framebilgiAraba,text="Araç Türü :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelAracTuru.grid(row=2, column=0) 

        labelMarka=Label(framebilgiAraba,text="Marka :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelMarka.grid(row=3, column=0)

        labelModel=Label(framebilgiAraba,text="Model :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelModel.grid(row=4, column=0) 
    
        labelUretimYili=Label(framebilgiAraba,text="Üretim Yılı :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelUretimYili.grid(row=5, column=0) 

        labelYakitTuru=Label(framebilgiAraba,text="Yakıt Türü :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelYakitTuru.grid(row=6, column=0) 
    
        labelVites=Label(framebilgiAraba,text="Vites :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelVites.grid(row=7, column=0)

        labelMotorGucu=Label(framebilgiAraba,text="Motor Gücü :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelMotorGucu.grid(row=8, column=0) 

        labelKasaTipi=Label(framebilgiAraba,text="Kasa Tipi :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelKasaTipi.grid(row=9, column=0) 

        labelMotorHacmi=Label(framebilgiAraba,text="Motor Hacmi :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelMotorHacmi.grid(row=1, column=2)

        labelCekis=Label(framebilgiAraba,text="Çekiş  :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelCekis.grid(row=2, column=2) 

        labelKapi=Label(framebilgiAraba,text="Kapı  :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelKapi.grid(row=3, column=2)

        labelRenk=Label(framebilgiAraba,text="Renk :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelRenk.grid(row=4, column=2) 

        labelMotorNo=Label(framebilgiAraba,text="Motor No :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelMotorNo.grid(row=5, column=2)

        labelKiraBedeli=Label(framebilgiAraba,text="Kira Bedeli(Gün) :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelKiraBedeli.grid(row=6, column=2)

        labelKiradami=Label(framebilgiAraba,text="Kirada mı? :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelKiradami.grid(row=7, column=2) 

        labelKullanımDisi=Label(framebilgiAraba,text="Kullanım Dışımı :",font="Arial 11 bold", bg="lightblue",pady=3)
        labelKullanımDisi.grid(row=8, column=2) 

      

         #?------------- İKİNCİ EKRAN ENTRY ---------------------

        self.sasiNoEntry=Entry(framebilgiAraba,bd=3, textvariable=self.SasiNo)
        self.sasiNoEntry.grid(row=1, column=1,pady=5)  

        self.AracTuruEntry=Entry(framebilgiAraba,textvariable=self.AracTuru,bd=3)
        self.AracTuruEntry.grid(row=2, column=1,pady=5)
        
        self.MarkaEntry=Entry(framebilgiAraba,textvariable=self.Marka,bd=3)
        self.MarkaEntry.grid(row=3, column=1,pady=5)

        self.ModelEntry=Entry(framebilgiAraba,textvariable=self.Model,bd=3)
        self.ModelEntry.grid(row=4, column=1)

        self.UretimYilEntry=Entry(framebilgiAraba,textvariable=self.UretimYili,bd=3)
        self.UretimYilEntry.grid(row=5, column=1,pady=5)

        self.YakitTurEntry=Combobox(framebilgiAraba,textvariable=self.YakitTuru,state="readonly",width=18)
        self.YakitTurEntry["values"]=("Benzin","Dizel","Elektrik","LPG")
        self.YakitTurEntry.grid(row=6, column=1,pady=5)

        self.VitesEntry=Entry(framebilgiAraba,bd=3, textvariable=self.Vites)
        self.VitesEntry.grid(row=7, column=1,pady=5)

        self.MotorGucuEntry=Entry(framebilgiAraba,bd=3, textvariable=self.MotorGucu)
        self.MotorGucuEntry.grid(row=8, column=1,pady=5)

        self.KasaTipiEntry=Combobox(framebilgiAraba,width=18, textvariable=self.KasaTipi)
        self.KasaTipiEntry["values"]=("Hatchback","Station Wagon", "Cabrio", "Pick Up", "SUV")
        self.KasaTipiEntry.grid(row=9, column=1,pady=5)  

        self.MotorHacmiEntry=Entry(framebilgiAraba,bd=3, textvariable=self.MotorHacmi)
        self.MotorHacmiEntry.grid(row=1, column=3,pady=5)  

        self.cekisEntry=Combobox(framebilgiAraba, width=18, textvariable=self.Cekis)
        self.cekisEntry["values"]=("Önden Çekiş","Arkadan Çekiş","")
        self.cekisEntry.grid(row=2, column=3,pady=5)

        self.kapiEntry=Entry(framebilgiAraba,bd=3, textvariable=self.Kapi)
        self.kapiEntry.grid(row=3, column=3,pady=5)  

        self.renkEntry=Entry(framebilgiAraba,bd=3, textvariable=self.Renk)
        self.renkEntry.grid(row=4, column=3,pady=5)  

        self.motorNoEntry=Entry(framebilgiAraba,bd=3, textvariable=self.MotorNo)
        self.motorNoEntry.grid(row=5, column=3,pady=5)  
        
        self.kiraBedeliEntry=Entry(framebilgiAraba,bd=3, textvariable=self.GKiralamaBedeli)
        self.kiraBedeliEntry.grid(row=6, column=3,pady=5)  

        self.kiradamiEntry=Combobox(framebilgiAraba, width=18, textvariable=self.Kiradami,state="readonly")
        self.kiradamiEntry["values"]=("Evet","Hayır")
        self.kiradamiEntry.grid(row=7, column=3,pady=5)  

        self.kullanimDisimiEntry=Combobox(framebilgiAraba, width=18, textvariable=self.KullanimDisimi,state="readonly")
        self.kullanimDisimiEntry["values"]=("Evet","Hayır")
        self.kullanimDisimiEntry.grid(row=8, column=3,pady=5) 

    #?----------------------ARAC EKRANI BUTON ----------------------
        butonkayıtArac=Button(framebutonAraba,command=self.aracVeri, bd=2, relief=SUNKEN,text="Kayıt Et", bg="black", fg="white", font="Arial 12 bold", width=35, height=2, overrelief="groove", cursor="hand2")
        butonkayıtArac.grid(row=0, column=1, columnspan=2,padx=80, pady=3)

        butonkayıtsilArac=Button(framebutonAraba,command=self.aracVeriSil, bd=2, relief=SUNKEN,  text="Kayıt Sil ", bg="black", fg="white", font="Arial 12 bold", width=35, height=2, overrelief="groove", cursor="hand2")
        butonkayıtsilArac.grid(row=1, column=1, columnspan=2,padx=15, pady=3)

        butonkayıtguncelArac=Button(framebutonAraba,command=self.aracGuncelle, bd=2, relief=SUNKEN, text="Kayıt Güncelle ", bg="black", fg="white", font="Arial 12 bold", width=35, height=2, overrelief="groove", cursor="hand2")
        butonkayıtguncelArac.grid(row=2, column=1, columnspan=2,padx=15, pady=3)

        butontemizleArac=Button(framebilgiAraba,command=self.aracGirdiTemizle, bd=2, relief=SUNKEN, text="Temizle", bg="black", fg="white", font="Arial 12 bold", width=10, height=2, overrelief="groove", cursor="hand2")
        butontemizleArac.grid(row=11, column=3, pady=3)

        butoncikisMusteriArac=Button(framebutonAraba,command=self.aracCikis, bd=2, relief=SUNKEN, text="Çıkış", bg="black", fg="white", font="Arial 12 bold", width=35, height=2, overrelief="groove", cursor="hand2")
        butoncikisMusteriArac.grid(row=4, column=1, columnspan=3,padx=20, pady=1)
    #?--------------------------ARAÇ BİLGİ EKRANI-------------------
        scroollxArac=Scrollbar(frameveriAraba, orient=HORIZONTAL)
        scroollyArac=Scrollbar(frameveriAraba, orient=VERTICAL)
        self.aracbilgiTablo=ttk.Treeview(frameveriAraba, column=("SasiNo","AracTuru","Marka","Model","UretimYili","YakitTuru","Vites","MotorGucu","KasaTipi","MotorHacmi","Cekis","Kapi","Renk","MotorNo","GunlukKiraBedeli","Kiradami","KullanimDisimi"),xscrollcommand=scroollxArac.set,yscrollcommand=scroollyArac.set)

        scroollxArac.pack(side=BOTTOM, fill=X)
        scroollyArac.pack(side=RIGHT, fill=Y)

        scroollxArac.config(command=self.aracbilgiTablo.xview)
        scroollyArac.config(command=self.aracbilgiTablo.yview)

        self.aracbilgiTablo.heading("SasiNo", text="Şasi No")
        self.aracbilgiTablo.heading("AracTuru", text="Araç Türü")
        self.aracbilgiTablo.heading("Marka", text="Marka")
        self.aracbilgiTablo.heading("Model", text="Model")
        self.aracbilgiTablo.heading("UretimYili", text="Üretim Yılı")
        self.aracbilgiTablo.heading("YakitTuru", text="Yakıt Türü")
        self.aracbilgiTablo.heading("Vites", text="Vites")
        self.aracbilgiTablo.heading("MotorGucu", text="Motor Gücü")
        self.aracbilgiTablo.heading("KasaTipi", text="Kasa Tipi")
        self.aracbilgiTablo.heading("MotorHacmi", text="Motor Hacmi")
        self.aracbilgiTablo.heading("Cekis", text="Çekiş")
        self.aracbilgiTablo.heading("Kapi", text="Kapı")
        self.aracbilgiTablo.heading("Renk", text="Renk")
        self.aracbilgiTablo.heading("MotorNo", text="Motor No")
        self.aracbilgiTablo.heading("GunlukKiraBedeli", text="Günlük Kira Bedeli")
        self.aracbilgiTablo.heading("Kiradami", text="Kira Durumu")
        self.aracbilgiTablo.heading("KullanimDisimi", text="Kullanım Dışımı")

        self.aracbilgiTablo["show"]="headings"

        self.aracbilgiTablo.column("SasiNo", width=100)
        self.aracbilgiTablo.column("AracTuru", width=100)
        self.aracbilgiTablo.column("Marka", width=100)
        self.aracbilgiTablo.column("Model",width=100)
        self.aracbilgiTablo.column("UretimYili", width=100)
        self.aracbilgiTablo.column("YakitTuru", width=100)
        self.aracbilgiTablo.column("Vites", width=100)
        self.aracbilgiTablo.column("MotorGucu", width=100)
        self.aracbilgiTablo.column("KasaTipi", width=100)
        self.aracbilgiTablo.column("MotorHacmi",width=100)
        self.aracbilgiTablo.column("Cekis", width=100)
        self.aracbilgiTablo.column("Kapi", width=100)
        self.aracbilgiTablo.column("Renk", width=100)
        self.aracbilgiTablo.column("MotorNo", width=100)
        self.aracbilgiTablo.column("GunlukKiraBedeli", width=100)
        self.aracbilgiTablo.column("Kiradami", width=100)
        self.aracbilgiTablo.column("KullanimDisimi", width=100)

        self.aracbilgiTablo.pack(fill=BOTH, expand=1)
        self.aracbilgiTablo.bind("<ButtonRelease-1>",self.imlecYazdirArac)
        self.arac_fatch_veri()
    def aracVeri(self):
        if self.AracTuru.get()=="" or self.Marka.get=="" or self.Model.get()=="" or self.UretimYili.get()=="" or self.YakitTuru.get()=="" or self.Vites.get()=="" or self.MotorGucu.get()=="" or self.KasaTipi=="" or self.MotorHacmi.get()=="" or self.Cekis.get()=="" or self.Kapi.get()=="" or self.Renk.get()=="" or self.MotorNo.get()=="" or self.KiraBedeli.get()=="" or self.Kiradami.get()=="":
            messagebox.showerror("Hata","Tüm alanları(*) doldurunuz")
        elif len(self.SasiNo.get())<17 or len(self.MotorNo.get())<17 or len(self.SasiNo.get())>17 or len(self.MotorNo.get())>17:
            messagebox.showerror("Hata","Şase No ve Motor No 17 hane olmalıdır")
        else:
            print("çalıştı")
            conn =mysql.connector.connect(host="localhost", username="admin", password="deneme", database="90200000195mert")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO aracbilgi VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.SasiNo.get(),
                                                                                                                self.AracTuru.get(),
                                                                                                                self.Marka.get(),
                                                                                                                self.Model.get(),
                                                                                                                self.UretimYili.get(),
                                                                                                                self.YakitTuru.get(),
                                                                                                                self.Vites.get(),
                                                                                                                self.MotorGucu.get(),
                                                                                                                self.KasaTipi.get(),
                                                                                                                self.MotorHacmi.get(),
                                                                                                                self.Cekis.get(),
                                                                                                                self.Kapi.get(),
                                                                                                                self.Renk.get(),
                                                                                                                self.MotorNo.get(),
                                                                                                                self.GKiralamaBedeli.get(),
                                                                                                                self.Kiradami.get(),
                                                                                                                self.KullanimDisimi.get()
                                                                                        ))
                                                                                
            conn.commit()
            self.arac_fatch_veri()
            conn.close()
            messagebox.showinfo("Başarılı","Kayıt Başarıyla Gerçekleşti")
            self.AracTuruEntry.delete(0,END)
            self.MarkaEntry.delete(0,END)
            self.ModelEntry.delete(0,END)
            self.UretimYilEntry.delete(0,END)
            self.YakitTuru.set(" ")
            self.VitesEntry.delete(0,END)
            self.MotorGucuEntry.delete(0,END)
            self.KasaTipiEntry.delete(0,END)
            self.MotorHacmiEntry.delete(0,END)
            self.cekisEntry.delete(0,END)
            self.kapiEntry.delete(0,END)
            self.renkEntry.delete(0,END)
            self.motorNoEntry.delete(0,END)
            self.sasiNoEntry.delete(0,END)
            self.kiraBedeliEntry.delete(0,END)
            self.kiradamiEntry.delete(0,END)
            self.kullanimDisimiEntry.delete(0,END)
    def aracGuncelle(self):
        conn =mysql.connector.connect(host="localhost", username="admin", password="deneme", database="90200000195mert")
        my_cursor=conn.cursor()
        my_cursor.execute("update aracbilgi set AracTuru=%s, Marka=%s, Model=%s, UretimYili=%s, YakitTuru=%s, Vites=%s, MotorGucu=%s, KasaTipi=%s, MotorHacmi=%s, Cekis=%s, Kapi=%s, Renk=%s, MotorNo=%s, GunlukKiraBedel=%s, Kiradami=%s, KullanimDisimi=%s where SasiNo=%s",(
                                                                                                            self.AracTuru.get(),
                                                                                                            self.Marka.get(),
                                                                                                            self.Model.get(),
                                                                                                            self.UretimYili.get(),
                                                                                                            self.YakitTuru.get(),
                                                                                                            self.Vites.get(),
                                                                                                            self.MotorGucu.get(),
                                                                                                            self.KasaTipi.get(),
                                                                                                            self.MotorHacmi.get(),
                                                                                                            self.Cekis.get(),
                                                                                                            self.Kapi.get(),
                                                                                                            self.Renk.get(),
                                                                                                            self.MotorNo.get(),
                                                                                                            self.GKiralamaBedeli.get(),
                                                                                                            self.Kiradami.get(),
                                                                                                            self.KullanimDisimi.get(),
                                                                                                            self.SasiNo.get()
                                                                                                                                                                            ))
        conn.commit()
        self.arac_fatch_veri()
        conn.close() 
    def arac_fatch_veri(self):
        conn =mysql.connector.connect(host="localhost", username="admin", password="deneme", database="90200000195mert")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from aracbilgi")        
        rows=my_cursor.fetchall()
        if len(rows) !=0:
            self.aracbilgiTablo.delete(*self.aracbilgiTablo.get_children())
            for i in rows:
                self.aracbilgiTablo.insert("", END, values=i)
            conn.commit()
        conn.close()
    def imlecYazdirArac(self, evenet=""):
        imlec_satir=self.aracbilgiTablo.focus()
        icerik=self.aracbilgiTablo.item(imlec_satir)
        satir=icerik["values"]
        self.SasiNo.set(satir[0])
        self.AracTuru.set(satir[1])
        self.Marka.set(satir[2])
        self.Model.set(satir[3])
        self.UretimYili.set(satir[4])
        self.YakitTuru.set(satir[5])
        self.Vites.set(satir[6])
        self.MotorGucu.set(satir[7])
        self.KasaTipi.set(satir[8])
        self.MotorHacmi.set(satir[9])
        self.Cekis.set(satir[10])
        self.Kapi.set(satir[11])
        self.Renk.set(satir[12])
        self.MotorNo.set(satir[13])
        self.GKiralamaBedeli.set(satir[14])
        self.Kiradami.set(satir[15])
        self.KullanimDisimi.set(satir[16])
    def aracVeriSil(self):
        conn=mysql.connector.connect(host="localhost", username="admin", password="deneme", database="90200000195mert")
        my_cursor=conn.cursor()
        sorgu="DELETE FROM aracbilgi WHERE SasiNo=%s"
        value=(self.SasiNo.get(),)
        my_cursor.execute(sorgu,value)
        conn.commit()
        conn.close()
        self.arac_fatch_veri()
        messagebox.showinfo("Silindi","Araç kaydı başarıyla silindi")
    def aracGirdiTemizle(self):
        self.SasiNo.set("")
        self.AracTuru.set("")
        self.Marka.set("")
        self.Model.set("")
        self.UretimYili.set("")
        self.YakitTuru.set("")
        self.Vites.set("")
        self.MotorGucu.set("")
        self.KasaTipi.set("")
        self.MotorHacmi.set("")
        self.Cekis.set("")
        self.Kapi.set("")
        self.Renk.set("")
        self.MotorNo.set("")
        self.GKiralamaBedeli.set("")
        self.Kiradami.set("")
        self.KullanimDisimi.set("")
    def aracCikis(self):
        cikis=messagebox.askyesno("Araç Penceresinden Cikis Yapılsın mı?", "Çıkışı onaylıyor musunuz ?")
        if cikis>0:
            self.pencereAraba.destroy()
            return
    #*##########################################################################################################
    #!-----------------ARAC KiRALAMA FRAME.------------------------
    def aracKirala(self):
        print("çalıştı")
        self.pencereAracKirala=Toplevel()
        self.pencereAracKirala.title("Araç Kirala ")
        self.pencereAracKirala.geometry("1500x700")
        self.pencereAracKirala.resizable(False, False)

        self.Ad=StringVar()
        self.Soyad=StringVar()
        self.TcKimlik=StringVar()
        self.Telefon=StringVar()
        self.SasiNo=StringVar()
        self.Marka=StringVar()
        self.Model=StringVar()
        self.YakitTuru=StringVar()
        self.Yolculuk=StringVar()
        self.KacGun=StringVar()
        self.KiraBedeli=StringVar()
        self.KiraDurumu=StringVar()
        self.KullanimDisimi=StringVar()


        canvas=Canvas(self.pencereAracKirala, height=700, width=1500, bg="white")
        canvas.pack()

        #?------------------ ARAC KİRALAMA BİLGİ EKRAN FRAME ----------------
        frameMusteriTablo=LabelFrame(canvas, bg="lightblue",font=('arial', 10, 'bold'),text="Müşteri Tablosu")
        frameMusteriTablo.place(relx=0.01, rely=0.01, relwidth=0.48 , relheight=0.35)

        frameAracTablo=LabelFrame(canvas, bg="lightblue",font=('arial', 10, 'bold'),text="Araç Bilgi Tablosu")
        frameAracTablo.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.35)

        frameAracButon=LabelFrame(canvas, bg="lightblue",font=('arial', 10, 'bold'),text="Kayıt Buton")
        frameAracButon.place(relx=0.01, rely=0.37, relwidth=0.98, relheight=0.23)

        frameKiraTablo=LabelFrame(canvas, bg="lightblue",font=('arial', 10, 'bold'),text="Kira Tablosu")
        frameKiraTablo.place(relx=0.01, rely=0.61, relwidth=0.98, relheight=0.35)

        #?-------------------ARAC KİRALAMA BUTON ------------------------------
        boslukLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="  ",bg="lightblue")
        boslukLabel.grid(row=0,column=12)
        boslukLabel1=Label(frameAracButon,font=('arial', 11, 'bold'),text="  ",bg="lightblue")
        boslukLabel1.grid(row=1,column=12)

        yaziTemizleButon=Button(frameAracButon,command=self.temizle,bd=5, fg="white", font=('arial', 10, 'bold'), width=12, text="Temizle", bg="black", cursor="hand2", overrelief="groove", height=2)
        yaziTemizleButon.grid(row=3, column=5)

        çikisButon= Button(frameAracButon,command=self.aracKiralaCikis,bd=5, fg="white", font=('arial', 10, 'bold'), width=12, text="Çıkış", bg="black", cursor="hand2", overrelief="groove", height=2)
        çikisButon.grid(row=3,column=13,padx=1,pady=2)

        kiraKayitButon = Button(frameAracButon,command=self.araciKirala,bd=5, fg="white", font=('arial', 10, 'bold'), width=12, text="Kirala", bg="black", cursor="hand2", overrelief="groove", height=2)
        kiraKayitButon.grid(row=3,column=1,padx=1)

        teslimButon=Button(frameAracButon, command=self.teslimEdildi, bd=5, fg="white", font=('arial', 10, 'bold'), width=12, text="Teslim al", bg="black", cursor="hand2", overrelief="groove", height=2 )
        teslimButon.grid(row=3,column=3,padx=5, pady=10)

        #?-------------------ARAC KİRALA LABEL---------------------------------
        musteriTcLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="Müşteri TC :",bg="lightblue",)
        musteriTcLabel.grid(row=0,column=0,pady=9)
        musteriTcEntry=Entry(frameAracButon,textvariable=self.TcKimlik,bd=3,width=15,state=DISABLED)
        musteriTcEntry.grid(row=0,column=1,pady=9)
        
        adMusteriLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="Adı :",bg="lightblue")
        adMusteriLabel.grid(row=0,column=2)
        adMusteriLabel=Entry(frameAracButon,textvariable=self.Ad,bd=3,width=15,selectborderwidth=3,state=DISABLED)
        adMusteriLabel.grid(row=0,column=3)

        soyadMusteriLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="Soyad : ",bg="lightblue")
        soyadMusteriLabel.grid(row=0,column=4)
        soyadMusteriEntry=Entry(frameAracButon,textvariable=self.Soyad,bd=3,width=15,selectborderwidth=3,state=DISABLED)
        soyadMusteriEntry.grid(row=0,column=5)

        musteriTelefonLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="Telefon :",bg="lightblue")
        musteriTelefonLabel.grid(row=0,column=6)
        musteriTelefonLabel=Entry(frameAracButon,textvariable=self.Telefon,bd=3,width=15,selectborderwidth=3,state=DISABLED)
        musteriTelefonLabel.grid(row=0,column=7)

        kacGunLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="Kaç Gün :",bg="lightblue")
        kacGunLabel.grid(row=0,column=12)
        kacGunEntry=Entry(frameAracButon,textvariable=self.KacGun,bd=3,width=15,selectborderwidth=3)
        kacGunEntry.grid(row=0,column=13)

        kiraBedelLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="Kira Bedeli :",bg="lightblue")
        kiraBedelLabel.grid(row=0,column=10)
        kiraBedelEntry=Entry(frameAracButon,textvariable=self.KiraBedeli,bd=3,width=15,selectborderwidth=3)
        kiraBedelEntry.grid(row=0,column=11)

        aracSaseLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="AraçŞase :",bg="lightblue")
        aracSaseLabel.grid(row=1,column=0,rowspan=2)
        aracSaseLabel=Entry(frameAracButon,textvariable=self.SasiNo,bd=3,width=15,selectborderwidth=3,state=DISABLED)
        aracSaseLabel.grid(row=1,column=1,rowspan=2)

        MarkaLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="Marka :",bg="lightblue")
        MarkaLabel.grid(row=1,column=2)
        MarkaEntry=Entry(frameAracButon,textvariable=self.Marka,bd=3,width=15,selectborderwidth=3,state=DISABLED)
        MarkaEntry.grid(row=1,column=3)

        ModelLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="Model  :",bg="lightblue")
        ModelLabel.grid(row=1,column=4)
        ModelEntry=Entry(frameAracButon,textvariable=self.Model,bd=3,width=15,selectborderwidth=3,state=DISABLED)
        ModelEntry.grid(row=1,column=5)

        yakıtLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="Yakıt :",bg="lightblue")
        yakıtLabel.grid(row=1,column=6)
        yakıtEntry=Entry(frameAracButon,textvariable=self.YakitTuru,bd=3,width=15,selectborderwidth=3,state=DISABLED)
        yakıtEntry.grid(row=1,column=7)

        kiraDurumuLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="Kira Durumu :",bg="lightblue")
        kiraDurumuLabel.grid(row=1,column=8)
        kiraDurumuEntry=Entry(frameAracButon,textvariable=self.KiraDurumu,bd=3,width=15,selectborderwidth=3,state=DISABLED)
        kiraDurumuEntry.grid(row=1,column=9)

        yolculukLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="Yolculuk  :",bg="lightblue")
        yolculukLabel.grid(row=1,column=10)
        yolculukEntry=Entry(frameAracButon,textvariable=self.Yolculuk,bd=3,width=15,selectborderwidth=3)
        yolculukEntry.grid(row=1,column=11)

        kullanımDisimiLabel=Label(frameAracButon,font=('arial', 11, 'bold'),text="Kullanım Dışımı?  :",bg="lightblue")
        kullanımDisimiLabel.grid(row=0,column=8)
        kullanımDisimiEntry=Entry(frameAracButon,textvariable=self.KullanimDisimi,bd=3,width=15,selectborderwidth=3,state=DISABLED)
        kullanımDisimiEntry.grid(row=0,column=9)


        #?----------------------------ARAC KİRALA TREEVİEW-------------------
        scroollx=Scrollbar(frameMusteriTablo, orient=HORIZONTAL)
        scroolly=Scrollbar(frameMusteriTablo, orient=VERTICAL)
        self.musteribilgiTablo=ttk.Treeview(frameMusteriTablo, column=("TcKimlik","Ad","Soyad",
        "DogumTarihi","Adres","Telefon","Mesleği","EhliyetSinifi","MedeniDurumu","EgitimDurumu"),xscrollcommand=scroollx.set,yscrollcommand=scroolly.set)
        
        scroollx.pack(side=BOTTOM, fill=X)
        scroolly.pack(side=RIGHT, fill=Y)

        scroollx.config(command=self.musteribilgiTablo.xview)
        scroolly.config(command=self.musteribilgiTablo.yview)
        
        
        self.musteribilgiTablo.heading("TcKimlik", text="TC NO")
        self.musteribilgiTablo.heading("Ad", text="AD")
        self.musteribilgiTablo.heading("Soyad", text="SOYAD")
        self.musteribilgiTablo.heading("DogumTarihi", text="Dogum tarihi"),
        self.musteribilgiTablo.heading("Adres", text="Adress")
        self.musteribilgiTablo.heading("Telefon", text="Telefon No")
        self.musteribilgiTablo.heading("Mesleği", text="Meslek")
        self.musteribilgiTablo.heading("EhliyetSinifi", text="Ehliyet")
        self.musteribilgiTablo.heading("MedeniDurumu", text="Medeni Hal")
        self.musteribilgiTablo.heading("EgitimDurumu", text="Egitim Hali")

        self.musteribilgiTablo["show"]="headings"

        self.musteribilgiTablo.column("TcKimlik", width=100)
        self.musteribilgiTablo.column("Ad", width=100)
        self.musteribilgiTablo.column("Soyad", width=100)
        self.musteribilgiTablo.column("DogumTarihi", width=100)
        self.musteribilgiTablo.column("Adres", width=100)
        self.musteribilgiTablo.column("Telefon", width=100)
        self.musteribilgiTablo.column("Mesleği", width=100)
        self.musteribilgiTablo.column("EhliyetSinifi", width=100)
        self.musteribilgiTablo.column("MedeniDurumu", width=100)
        self.musteribilgiTablo.column("EgitimDurumu", width=100)


        self.musteribilgiTablo.pack(fill=BOTH, expand=1)
        self.musteribilgiTablo.bind("<ButtonRelease-1>",self.imlecYazdirAracKira)
        self.fatch_veri()


    #*##########################################################################################################

        scroollxArac=Scrollbar(frameAracTablo, orient=HORIZONTAL)
        scroollyArac=Scrollbar(frameAracTablo, orient=VERTICAL)
        self.aracbilgiTablo=ttk.Treeview(frameAracTablo, column=("SasiNo","AracTuru","Marka","Model","UretimYili","YakitTuru","Vites","MotorGucu","KasaTipi","MotorHacmi","Cekis","Kapi","Renk","MotorNo","GunlukKiraBedeli","Kiradami","KullanimDisimi"),xscrollcommand=scroollxArac.set,yscrollcommand=scroollyArac.set)

        scroollxArac.pack(side=BOTTOM, fill=X)
        scroollyArac.pack(side=RIGHT, fill=Y)

        scroollxArac.config(command=self.aracbilgiTablo.xview)
        scroollyArac.config(command=self.aracbilgiTablo.yview)

        self.aracbilgiTablo.heading("SasiNo", text="Şasi No")
        self.aracbilgiTablo.heading("AracTuru", text="Araç Türü")
        self.aracbilgiTablo.heading("Marka", text="Marka")
        self.aracbilgiTablo.heading("Model", text="Model")
        self.aracbilgiTablo.heading("UretimYili", text="Üretim Yılı")
        self.aracbilgiTablo.heading("YakitTuru", text="Yakıt Türü")
        self.aracbilgiTablo.heading("Vites", text="Vites")
        self.aracbilgiTablo.heading("MotorGucu", text="Motor Gücü")
        self.aracbilgiTablo.heading("KasaTipi", text="Kasa Tipi")
        self.aracbilgiTablo.heading("MotorHacmi", text="Motor Hacmi")
        self.aracbilgiTablo.heading("Cekis", text="Çekiş")
        self.aracbilgiTablo.heading("Kapi", text="Kapı")
        self.aracbilgiTablo.heading("Renk", text="Renk")
        self.aracbilgiTablo.heading("MotorNo", text="Motor No")
        self.aracbilgiTablo.heading("GunlukKiraBedeli", text="Günlük Kira Bedeli")
        self.aracbilgiTablo.heading("Kiradami", text="Kira Durumu")
        self.aracbilgiTablo.heading("KullanimDisimi", text="Kullanım Dışımı")

        self.aracbilgiTablo["show"]="headings"

        self.aracbilgiTablo.column("SasiNo", width=100)
        self.aracbilgiTablo.column("AracTuru", width=100)
        self.aracbilgiTablo.column("Marka", width=100)
        self.aracbilgiTablo.column("Model",width=100)
        self.aracbilgiTablo.column("UretimYili", width=100)
        self.aracbilgiTablo.column("YakitTuru", width=100)
        self.aracbilgiTablo.column("Vites", width=100)
        self.aracbilgiTablo.column("MotorGucu", width=100)
        self.aracbilgiTablo.column("KasaTipi", width=100)
        self.aracbilgiTablo.column("MotorHacmi",width=100)
        self.aracbilgiTablo.column("Cekis", width=100)
        self.aracbilgiTablo.column("Kapi", width=100)
        self.aracbilgiTablo.column("Renk", width=100)
        self.aracbilgiTablo.column("MotorNo", width=100)
        self.aracbilgiTablo.column("GunlukKiraBedeli", width=100)
        self.aracbilgiTablo.column("Kiradami", width=100)
        self.aracbilgiTablo.column("KullanimDisimi", width=100)

        self.aracbilgiTablo.pack(fill=BOTH, expand=1)
        self.aracbilgiTablo.bind("<ButtonRelease-1>",self.imlecYazdirAracKira1)
        self.arac_fatch_veri()
 
  
           
        #*##########################################################################################################

        scroollKirax=Scrollbar(frameKiraTablo, orient=HORIZONTAL)
        scroollKiray=Scrollbar(frameKiraTablo, orient=VERTICAL)

        self.aracKiraTablo=ttk.Treeview(frameKiraTablo, column=("MüşteriTc","Adı","Soyad","Telefon","AracSase","Marka","Model","Yakıt","Yolculuk","KacGun","KİraBedel","KiraDurum"),xscrollcommand=scroollKirax.set,yscrollcommand=scroollKiray.set)

        scroollKirax.pack(side=BOTTOM,fill=X)
        scroollKiray.pack(side=RIGHT, fill=Y)

        scroollKirax.config(command=self.aracKiraTablo.xview)
        scroollKiray.config(command=self.aracKiraTablo.yview)

        self.aracKiraTablo.heading("MüşteriTc", text="Müşteri TC Numarası")
        self.aracKiraTablo.heading("Adı",text="Adı")
        self.aracKiraTablo.heading("Soyad",text="Soyadı")
        self.aracKiraTablo.heading("Telefon",text="Telefon")
        self.aracKiraTablo.heading("AracSase",text="Araç Şaşe Numarası")
        self.aracKiraTablo.heading("Marka",text="Marka")
        self.aracKiraTablo.heading("Model",text="Model")
        self.aracKiraTablo.heading("Yakıt",text="Yakıt")
        self.aracKiraTablo.heading("Yolculuk",text="Yolculuk")
        self.aracKiraTablo.heading("KacGun",text="Kaç Gün")
        self.aracKiraTablo.heading("KİraBedel", text="Kira Bedeli")
        self.aracKiraTablo.heading("KiraDurum", text="Kira Durumu")
        
        self.aracKiraTablo["show"]="headings"

        self.aracKiraTablo.column("MüşteriTc", width=100)
        self.aracKiraTablo.column("Adı",  width=100)
        self.aracKiraTablo.column("Soyad",  width=100)
        self.aracKiraTablo.column("Telefon",  width=100)
        self.aracKiraTablo.column("AracSase",   width=100)
        self.aracKiraTablo.column("Marka",  width=100)
        self.aracKiraTablo.column("Model",  width=100)
        self.aracKiraTablo.column("Yakıt",  width=100)
        self.aracKiraTablo.column("Yolculuk",  width=100)
        self.aracKiraTablo.column("KacGun",  width=100)
        self.aracKiraTablo.column("KİraBedel",  width=100 )
        self.aracKiraTablo.column("KiraDurum",  width=100)

        self.aracKiraTablo.pack(fill=BOTH, expand=1) 
        self.aracKiraTablo.bind("<ButtonRelease-1>",self.imlecYazdirAracKira2)        
        self.kira_fatch_veri()
    def imlecYazdirAracKira2(self, event=""):
        imlec_satir=self.aracKiraTablo.focus()
        icerik=self.aracKiraTablo.item(imlec_satir)
        satir=icerik["values"]
        self.TcKimlik.set(satir[0])
        self.Ad.set(satir[1])
        self.Soyad.set(satir[2])
        self.Telefon.set(satir[3])        
        self.SasiNo.set(satir[4])
        self.Marka.set(satir[5])
        self.Model.set(satir[6])
        self.YakitTuru.set(satir[7])    
    def imlecYazdirAracKira1(self, evenet=""):
        imlec_satir=self.aracbilgiTablo.focus()
        icerik=self.aracbilgiTablo.item(imlec_satir)
        satir=icerik["values"]
        self.SasiNo.set(satir[0])
        self.Marka.set(satir[2])
        self.Model.set(satir[3])
        self.YakitTuru.set(satir[5]) 
        self.KiraDurumu.set(satir[15])
        self.KullanimDisimi.set(satir[16])   
    def imlecYazdirAracKira(self, evenet=""):
        imlec_satir=self.musteribilgiTablo.focus()
        icerik=self.musteribilgiTablo.item(imlec_satir)
        satir=icerik["values"]
        self.TcKimlik.set(satir[0])
        self.Ad.set(satir[1])
        self.Soyad.set(satir[2])
        self.Telefon.set(satir[5])
    def teslimEdildi(self):
        conn=mysql.connector.connect(host="localhost",username="admin",password="deneme", database="90200000195mert")
        
        my_cursor=conn.cursor()
        sql="DELETE FROM kira WHERE AracSaseNo=%s"
        val=(self.SasiNo.get(),) 
        my_cursor.execute(sql,val)
        conn.commit()
        
        my_cursor=conn.cursor()
        sql="UPDATE aracbilgi SET Kiradami='Hayır' WHERE SasiNo=%s"
        val=(self.SasiNo.get(),)
        my_cursor.execute(sql,val)
        conn.commit()

        self.kira_fatch_veri()
        self.arac_fatch_veri()
        conn.close()
        messagebox.showinfo("Başarılı","Araç Başarılı Bir Şekilde Teslim Alındı !!")
    def araciKirala(self):
        if self.KiraDurumu.get()=="Evet" or self.KullanimDisimi.get()=="Evet":
            messagebox.showerror("Hata", "Bu araç daha önceden kiralandı !")
        elif self.KiraBedeli.get()=="" or self.Yolculuk.get()=="" or self.KacGun.get()=="":
            messagebox.showerror("Hata","Boş Alanları Doldurunuz")
        else:
            conn=mysql.connector.connect(host="localhost", username="admin",password="deneme",database="90200000195mert")
            my_cursor=conn.cursor()       
            sql="INSERT INTO kira VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
            val=(self.TcKimlik.get(),self.Ad.get(),self.Soyad.get(),self.Telefon.get(),self.SasiNo.get(),self.Marka.get(),self.Model.get(),self.YakitTuru.get(),self.Yolculuk.get(),self.KacGun.get(),self.KiraBedeli.get(),self.KiraDurumu.get())
            my_cursor.execute(sql,val)
            conn.commit()

            my_cursor2=conn.cursor()
            sql="UPDATE aracbilgi SET Kiradami='Evet' WHERE SasiNo=%s"
            val=(self.SasiNo.get(),)
            my_cursor2.execute(sql,val)
            conn.commit()

            my_cursor3=conn.cursor()
            sql="UPDATE kira SET KiraDurumu='Evet' WHERE AracSaseNo=%s"
            val=(self.SasiNo.get(),)
            my_cursor3.execute(sql,val)
            conn.commit()


            self.kira_fatch_veri()
            self.arac_fatch_veri()
            conn.close()

            messagebox.showinfo("Başarılı!!", "Araç Başarılı bir şekilde kayıt edildi")
    def kira_fatch_veri(self):
        conn=mysql.connector.connect(host="localhost", username="admin", password="deneme", database="90200000195mert")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from kira")
        rows=my_cursor.fetchall()
        if len(rows) != 0:
            self.aracKiraTablo.delete(*self.aracKiraTablo.get_children())
            for i in rows:
                self.aracKiraTablo.insert("", END, values=i)
            conn.commit()
        conn.close()
    def temizle(self):
        self.Ad.set("")
        self.Soyad.set("")
        self.TcKimlik.set("")
        self.Telefon.set("")
        self.SasiNo.set("")
        self.Marka.set("")
        self.Model.set("")
        self.YakitTuru.set("")
        self.Yolculuk.set("")
        self.KacGun.set("")
        self.KiraBedeli.set("")
        self.KiraDurumu.set("")
        self.KullanimDisimi.set("")    
    def aracKiralaCikis(self):
        cikis=messagebox.askyesno("Kiralama Penceresinden Cikis Yapılsın mı?", "Çıkışı onaylıyor musunuz ?")
        if cikis>0:
            self.pencereAracKirala.destroy()
            return
    #*##########################################################################################################
    #!-----------------ARACBİLGİ TREWİEV------------------------
    def kiralanmıs_pencere(self):
        self.pencereAracKirala=Toplevel()
        self.pencereAracKirala.title("Araç Kirala ")
        self.pencereAracKirala.geometry("1500x700")
        self.pencereAracKirala.resizable(False, False)

        canvas=Canvas(self.pencereAracKirala, height=700, width=1500, bg="lightblue")
        canvas.pack()
        
        baslıkLabel=Label(canvas, text="Kiralanmış Araçlar Tablosu",font=('arial', 14, 'bold'),bg="lightblue")
        baslıkLabel.place(relx=0.01)

        kiralanmısTablo=LabelFrame(canvas, bg="lightblue",font=('arial', 10, 'bold'),text="Kira Tablosu")
        kiralanmısTablo.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.65)

        CikisKiralanmısTablo=Button(canvas,command=self.pencereAracKirala.destroy,bd=5, fg="white", font=('arial', 10, 'bold'), width=12, text="Çıkış", bg="black", cursor="hand2", overrelief="groove", height=2)
        CikisKiralanmısTablo.place(relx=0.01, rely=0.75, relwidth=0.1, relheight=0.1)
        
        scroollKirax=Scrollbar(kiralanmısTablo, orient=HORIZONTAL)
        scroollKiray=Scrollbar(kiralanmısTablo, orient=VERTICAL)

        self.aracKiraTablo=ttk.Treeview(kiralanmısTablo, column=("MüşteriTc","Adı","Soyad","Telefon","AracSase","Marka","Model","Yakıt","Yolculuk","KacGun","KİraBedel","KiraDurum"),xscrollcommand=scroollKirax.set,yscrollcommand=scroollKiray.set)

        scroollKirax.pack(side=BOTTOM,fill=X)
        scroollKiray.pack(side=RIGHT, fill=Y)

        scroollKirax.config(command=self.aracKiraTablo.xview)
        scroollKiray.config(command=self.aracKiraTablo.yview)

        self.aracKiraTablo.heading("MüşteriTc", text="Müşteri TC Numarası")
        self.aracKiraTablo.heading("Adı",text="Adı")
        self.aracKiraTablo.heading("Soyad",text="Soyadı")
        self.aracKiraTablo.heading("Telefon",text="Telefon")
        self.aracKiraTablo.heading("AracSase",text="Araç Şaşe Numarası")
        self.aracKiraTablo.heading("Marka",text="Marka")
        self.aracKiraTablo.heading("Model",text="Model")
        self.aracKiraTablo.heading("Yakıt",text="Yakıt")
        self.aracKiraTablo.heading("Yolculuk",text="Yolculuk")
        self.aracKiraTablo.heading("KacGun",text="Kaç Gün")
        self.aracKiraTablo.heading("KİraBedel", text="Kira Bedeli")
        self.aracKiraTablo.heading("KiraDurum", text="Kira Durumu")
        
        self.aracKiraTablo["show"]="headings"

        self.aracKiraTablo.column("MüşteriTc", width=100)
        self.aracKiraTablo.column("Adı",  width=100)
        self.aracKiraTablo.column("Soyad",  width=100)
        self.aracKiraTablo.column("Telefon",  width=100)
        self.aracKiraTablo.column("AracSase",   width=100)
        self.aracKiraTablo.column("Marka",  width=100)
        self.aracKiraTablo.column("Model",  width=100)
        self.aracKiraTablo.column("Yakıt",  width=100)
        self.aracKiraTablo.column("Yolculuk",  width=100)
        self.aracKiraTablo.column("KacGun",  width=100)
        self.aracKiraTablo.column("KİraBedel",  width=100 )
        self.aracKiraTablo.column("KiraDurum",  width=100)

        self.aracKiraTablo.pack(fill=BOTH, expand=1)         
        self.kira_fatch_veri()  
    def kiralanmis_fatch_veri(self):
        pass
    #*##########################################################################################################    
    #!-----------------MAİNLOOP FONKS.---------------------------
    def mainloop(self):
        self.pencere.mainloop()

app=AracOto()
app.pencere.mainloop()   
