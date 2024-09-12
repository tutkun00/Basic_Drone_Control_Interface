# Basic_Drone_Control_Interface
A basic drone control interface made with Python DroneKit library. Python DroneKit kütüphanesi ile yapılmış bir temel dron kontrol arayüzü.
Programın 3 işlevi vardır:
 1-Drone'u arm etme ve belirli bir yüksekliğe kaldırma.
    -Drone arm edilebilir duruma gelene kadar beklenir.Sonra drone "GUIDED" moduna alınır.Arm edilir ve kullanıcıdan gelen metre cinsinde yüksekliğe çıkar. (Buradaki önemli unsur, drone arm              edildikten sonra bekletilmeden yükseklik değerinin girilmesidir.)
 2-Drone'u belirli bir konuma gönderme.
    -Drone'un gidilmesi istenilen konumun enlem,boylam ve yükseklik değerleri sırasıyla kullanıcıdan alınır ve drone belirtilen konuma doğru hareket eder.
 3-Drone'u indirme ve arm durumundan çıkarma.
    -Drone "LAND" moduna alınır ve yere iner.Yere indiğinde arm durumundan çıkarılır.
 Not: Bütün işlemlerden sonra ana menüye geri dönülür ve istenilen işlemin yapılmasına olanak verilir.
 Not2: Bu proje 2. sınıfa yeni geçmiş bir Bilgisayar Mühendisliği öğrencisinin yaptığı bir projedir.Teknik aksaklıklar olasılıklar dahilinde bulundurulmalıdır.

The program has 3 functions:
 1-Arming the drone and lifting it to a certain height.
    -Wait until the drone becomes armable. Then the drone is put into "GUIDED" mode. It is armed and rises to the height in meters received from the user. (The important element here is to enter         the altitude value without waiting after the drone is armed.)
 2-Sending the drone to a specific location.
    -The latitude, longitude and altitude values ​​of the desired location of the drone are received from the user respectively and the drone moves towards the specified location.
 3-Landing and unarming the drone.
    -The drone is put into "LAND" mode and lands on the ground. When it lands on the ground, it is taken out of arm state.
 Note: After all operations, you can return to the main menu and perform the desired operation.
 Note2: This project is a project made by a Computer Engineering student who has just passed the 2nd year. Technical glitches should be kept within the scope of possibility.
