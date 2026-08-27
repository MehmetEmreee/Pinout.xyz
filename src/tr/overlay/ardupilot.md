<!--
---
name: ArduPilot
page_url: ardupilot
description: ArduPilot tarafından kullanılan T3 Gemstone O1 başlık işlevleri
url: https://docs.t3gemstone.org/tr/projects/ardupilot
pin:
  '27':
    name: Ayrılmış I2C SDA
  '28':
    name: Ayrılmış I2C SCL
-->
# ArduPilot başlık bağlantıları

Bu görünüm, gerekli device tree overlay'leri etkinleştirildikten sonra resmî T3 Gemstone ArduPilot yapılandırmasının 40 pin başlığa atadığı işlevleri gösterir.

## Seyrüsefer ve kontrol

* **GPS ve haricî pusula:** 7 (UART-MAIN6 RX), 11 (UART-MAIN6 TX), 3 (I2C-MCU0 SDA) ve 5 (I2C-MCU0 SCL) numaralı pinler.
* **RC girişi:** 10 numaralı pin (UART-MAIN1 RX) SBUS kabul eder.
* **RC çıkışları:** 29, 8, 31, 33, 32, 36 ve 12 numaralı pinler sırasıyla RCOut 1–7 çıkışlarını sağlar.
* **Telemetri:** 18 (UART-WKUP0 TX) ve 26 (UART-WKUP0 RX) numaralı pinler.

## Atanmış diğer pinler

19, 21, 23 ve 24 numaralı pinler SPI-MCU0 arayüzünü oluşturur. 27 ve 28 numaralı pinler I2C-WKUP0 için ayrılmıştır; 37 numaralı pin ise haricî buzzer'a atanmıştır.

> **SBUS uyarısı:** SBUS terslenmiş seri sinyal kullanır. Alıcı ile 10 numaralı pin arasına haricî bir sinyal tersleyici bağlanmalıdır; standart SBUS çıkışını doğrudan bağlamayın.

> **Güç ve lojik uyarısı:** RCOut pinleri yalnızca 3,3 V PWM lojik sinyali taşır; servoya güç sağlamaz. Servo ve diğer yükleri ortak topraklı, uygun kapasiteli haricî kaynaktan besleyin; gerektiğinde sürücü veya seviye dönüştürücü kullanın. GPS ve telemetri sinyal seviyelerinin bağlantıdan önce 3,3 V olduğunu doğrulayın.

> **Buzzer uyarısı:** Herkese açık dokümantasyon haricî buzzer çıkışı için güvenli doğrudan sürme akımını belirtmiyor. Seçilen buzzer ve kart sınırı açıkça doğrulanmadıkça transistör veya uygun bir sürücü kullanın.

> **Kaynak çakışması:** GPS için kullanılan UART-MAIN6 overlay'i Bluetooth'u devre dışı bırakır. UART-WKUP0 telemetrisi fiziksel pin 26 üzerindeki SPI-MCU0 CS2'nin yerini aldığından ArduPilot SPI yapılandırması yalnızca CS0'ı sunar.

Çevre birimlerini bağlamadan önce resmî ArduPilot kılavuzundaki tüm overlay'leri etkinleştirin. Kılavuzda Linux aygıt yolları, servis kurulumu ve QGroundControl bağlantısı da açıklanır.
