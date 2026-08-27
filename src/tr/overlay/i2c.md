<!--
---
page_url: i2c
description: T3 Gemstone O1 I2C1 başlık pinleri
-->
# I2C

Harici I2C1 veri yolu fiziksel pin 3 (SDA) ve fiziksel pin 5 (SCL) üzerinden kullanılabilir. Güncel sistem imajında dokümantasyon bu denetleyiciyi `/dev/i2c-2` olarak gösterir.

Aynı iki sinyal hattına adresleri çakışmayan birden fazla I2C cihazı bağlanabilir. Veri yolunu incelemek için `i2c-tools` paketini kurup `sudo i2cdetect -y -r 2` komutunu kullanın.

Fiziksel 27 ve 28 numaralı pinler HAT kimlik EEPROM'u için ayrılmıştır; donanım ve önyükleme yapılandırması doğrulanmadan genel amaçlı I2C hattı olarak kullanılmamalıdır.
