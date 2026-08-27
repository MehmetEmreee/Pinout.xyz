# T3 Gemstone O1 Pinout

## 40 pin genişleme başlığı için etkileşimli referans

Gemstone Pinout, T3-GEM-O1 geliştirme kartının fiziksel pinlerini, uyumluluk GPIO numaralarını ve varsayılan arayüzlerini belgeler. Başlık, bilinen Raspberry Pi 40 pin fiziksel dizilimini kullanır; ancak işlemci, pin çoklama seçenekleri ve yazılım altyapısı Texas Instruments AM67A platformuna özgüdür.

## Başlık arayüzleri

Belgelenen başlık yapılandırmasında 3,3 V GPIO pinleriyle birlikte I2C-MCU0, SPI-MCU0, UART-MAIN1 ve PCM-McASP0 bulunur. Etkin işlevler `/boot/uEnv.txt` üzerinden yüklenen device tree overlay'lerine bağlıdır; bağlantı yapmadan önce açılış yapılandırmasını doğrulayın. Yedi başlık konumu donanımsal PWM seçeneğine sahiptir.

## Uyumlu HAT ve eklentiler

Fiziksel olarak takılabilmek, elektriksel veya yazılımsal uyumluluk anlamına gelmez. [Uyumlu kartlar kataloğunda](/tr/boards) yalnızca T3-GEM-O1 pin dizilimi, gerilim gereksinimleri, pin yönleri, device-tree yapılandırması ve Linux sürücüleri incelenen kartlar yer alır.

Bir eklenti, katalogda **Doğrulandı** veya **Koşullu uyumlu** durumu gösterilmedikçe uyumlu kabul edilmez.

Uyumluluk durumları:

* **Doğrulandı:** donanım ve yazılım çalışması teyit edilmiştir.
* **Koşullu uyumlu:** belgelenen sınırlamalar veya yapılandırmayla çalışabilir.
* **Uyumsuz:** kart kullanılmamalıdır veya gerekli bir özellik mevcut değildir.

## Yetkili kaynaklar

* [T3 Gemstone O1 dokümantasyonu](https://docs.t3gemstone.org/tr/boards/o1/introduction)
* [GPIO kılavuzu](https://docs.t3gemstone.org/tr/boards/o1/peripherals/gpio)
* [PWM kılavuzu](https://docs.t3gemstone.org/tr/boards/o1/peripherals/pwm)
* [Açık donanım tasarım dosyaları](https://github.com/t3gemstone/hardware)
