<!--
---
name: GPIO
page_url: gpio
description: T3 Gemstone O1 genel amaçlı 3,3 V GPIO pinleri
-->
# GPIO - Genel Amaçlı Giriş/Çıkış

T3-GEM-O1 üzerindeki 40 pin başlık, 3,3 V seviyesinde çalışan genel amaçlı dijital giriş/çıkış pinleri sunar. Bir GPIO giriş, çıkış veya AM67A pin çoklama sistemi üzerinden çevresel bir işlev olarak yapılandırılabilir.

Raspberry Pi'ye özel GPIO kütüphaneleri yerine `gpioinfo`, `gpiofind`, `gpioget` ve `gpioset` gibi Linux `libgpiod` araçlarını kullanın. Denetleyici ve hat numaraları çekirdek ya da device tree sürümleri arasında değişebileceğinden, hattı sistemdeki adıyla çözümleyin.

> **Elektriksel uyarı:** GPIO pinlerine doğrudan 5 V lojik uygulamayın. Herkese açık dokümantasyon pin başına veya toplam kaynak/çekme akımını, pull yapılandırmasını ve açılışta garanti edilen seviyeyi belirtmiyor. GPIO çıkışlarını kontrol sinyali olarak değerlendirin; LED, röle, buzzer veya motoru doğrudan sürmeyin, uygun direnç, sürücü, tampon ya da seviye dönüştürücü kullanın.

PWM ve diğer çevresel işlevlerin gerektirdiği pin çoklama değişiklikleri `/boot/uEnv.txt` içindeki T3-GEM-O1 device tree overlay'leriyle uygulanır.
