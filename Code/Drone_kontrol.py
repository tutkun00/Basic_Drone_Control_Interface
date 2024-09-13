import dronekit 
import time

drone = dronekit.connect("127.0.0.1:14550", wait_ready=True)
while True:
    print("DRONU ARM ETME VE KALDIRMA(1)")
    print("DRONE'U HAREKET ETTİRME(2)")
    print("LAND MODE VE KAPATMA(3)")
    print("ÇIKIŞ(4)")
    msecim=input("Hangi seçeneği seçiyorsunuz?:")
    #DRONE'U ARM ETME VE KALKIŞ
    if msecim=="1":
        while True:
           if drone.is_armable is True: 
            drone.mode=dronekit.VehicleMode("GUIDED")
            time.sleep(2)
            print("GUIDED mod'a alındı.")
            drone.armed=True
            print("Drone arm ediliyor...")
            while drone.armed is False:         
                time.sleep(1)
            if drone.armed is True:
             while True: 
                att=input("Drone'un başlangıç yüksekliğini giriniz:")
                try:
                    att=float(att)
                    if att>150 or att<=0:
                        raise Exception("Kalkış yüksekliği 0 değerinden küçük veya 150 değerinden büyük olamaz!")
                except ValueError:
                    print("Lütfen pozitif bir sayi giriniz!")
                    continue
                except Exception as ex:
                    print(ex)
                    continue   
                else:
                    break 
             drone.armed=True       
             drone.simple_takeoff(att)
             print("Drone belirtilen yüksekliğe çıkıyor...")
             while drone.location.global_relative_frame.alt<att*0.99:
                print(f"Yükseklik:{drone.location.global_relative_frame.alt}")
                time.sleep(1)
             print("Drone belirtilen yüksekliğe çıktı.") 
             print("Ana menüye dönülüyor...")
             time.sleep(1.5)
             break  
            else:   
               continue  

           else:
              while drone.is_armable is False:
                 print("Drone arm edilebilir hale getiriliyor...")
                 time.sleep(1) 


    #DRONE'U BELİRLİ BİR KONUMA HAREKET ETTİRME
    elif msecim=="2":
      while True:
        if drone.armed is False or drone.location.global_relative_frame.alt<=0:
           print("Drone arm edilmiş durumda değil veya kaldırılmamış!")
           print("Lütfen ilk 1.işlemi deneyin!")
           print("Ana menüye dönülüyor...")
           time.sleep(1.5)
           break
        else:
          while True: 
           konumx=input("Drone'un gideceği konumun x koordinatını(Enlem) giriniz:")
           konumy=input("Drone'un gideceği konumun y koordinatını(Boylam) giriniz:")
           konumz=input("Drone'un gideceği konumun z koordinatını(Yükseklik) giriniz:")
           try:
              konumx=float(konumx)
              konumy=float(konumy)
              konumz=float(konumz)
              if konumx==drone.location.global_relative_frame.lat and konumy==drone.location.global_relative_frame.lon and konumz==drone.location.global_relative_frame.alt:
                 raise Exception("LÜtfen drone'un anlık konumundan farklı bir konum giriniz!")
              if konumx<-90 or konumx>90:
                 raise Exception("Enlem değeri (-90,90) aralığında olmalıdır!")
              if konumy<-180 or konumy>180:
                 raise Exception("Boylam değeri (-180,180) arasında olmalıdır!")
              if konumz<0:
                 raise Exception("Yükseklik değeri 0'dan küçük olamaz!")
           except ValueError:
              print("Lütfen konum değerlerini bir sayi olarak giriniz!")
              continue   
           except Exception as ex2:
              print(ex2)
              continue
           else:
              break
          konum=dronekit.LocationGlobalRelative(konumx,konumy,konumz) 
          drone.simple_goto(konum) 
          print("Drone belirtilen konuma gidiyor...")
          while abs(konumx-drone.location.global_relative_frame.lat)>0.5 or abs(konumy-drone.location.global_relative_frame.lon)>0.5 or abs(konumz-drone.location.global_relative_frame.alt)>0.5:
             print(f"Drone'un anlık konumu x:{drone.location.global_relative_frame.lat} y:{drone.location.global_relative_frame.lon} z:{drone.location.global_relative_frame.alt}")
             time.sleep(1) 
          print("Drone belirtilen konuma ulaştı.")   
          print("Ana menüye dönülüyor...") 
          time.sleep(1.5)
          break     
    #LAND MODU VE KAPATMA         
    elif msecim=="3":
      print("Drone LAND moduna alınıyor...")
      drone.mode=dronekit.VehicleMode("LAND")
      print("Drone yere iniyor...")
      time.sleep(1)
      while drone.location.global_relative_frame.alt>0.5:
        print(f"Drone yüksekliği: {drone.location.global_relative_frame.alt}")
        time.sleep(1) 
      while drone.armed==True: 
       drone.armed=False
       time.sleep(1)
       if drone.armed==False:
         print("Drone arm durumundan çıkarıldı!")
      time.sleep(1)   
      print("Ana menüye dönülüyor...") 
      time.sleep(1.5)
      
        
    #ANA MENÜDEN ÇIKIŞ     
    elif msecim=="4":
     if drone.armed==True:
      print("Drone hala arm edilmiş durumda,lütfen ilk 3.işlemi yapınız!")
      print("Ana menüye dönülüyor...")
      time.sleep(1.5)
     else:  
      print("Menüden çıkılıyor...")
      time.sleep(2)
      break
    else:
        print("Geçersiz seçenek seçtiniz!")
