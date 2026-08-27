<!--
---
page_url: uart
description: T3 Gemstone O1 UART-MAIN1 başlık pinleri ve isteğe bağlı UART yönlendirmeleri
-->
# UART

UART-MAIN1 gönderme ve alma sinyalleri fiziksel 8 ve 10 numaralı pinlerde `/dev/ttyS3` olarak sunulur. Bunlar 3,3 V TTL lojik sinyalleridir; RS-232 gerilim seviyelerine veya 5 V UART sinyallerine doğrudan bağlanmamalıdır.

Karttaki üç pinli ayrı debug seri bağlantısı UART-MAIN0'dır; 40 pin başlıktaki UART ile aynı arayüz değildir.

> **Pin çakışması:** GPIO14 üzerinde PWM-0B etkinleştirildiğinde UART-MAIN1 TX kapanır; UART-MAIN1 RX çalışmaya devam edebilir. İsteğe bağlı UART-MAIN6 yönlendirmesi fiziksel 7/11 numaralı pinleri kullanır ve Bluetooth'u devre dışı bırakır. UART-WKUP0 ise 26/18 numaralı pinleri kullanır ve pin 26 üzerindeki SPI-MCU0 CS2'nin yerini alır. İsteğe bağlı bir yönlendirmeyi bağlamadan önce `/boot/uEnv.txt` yapılandırmasını doğrulayıp kartı yeniden başlatın.
