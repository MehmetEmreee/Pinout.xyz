<!--
---
page_url: i2c
description: T3 Gemstone O1 I2C-MCU0 ve ayrılmış I2C-WKUP0 başlık pinleri
pin:
  '27':
    name: I2C-WKUP0 SDA (Ayrılmış)
  '28':
    name: I2C-WKUP0 SCL (Ayrılmış)
-->
# I2C

Haricî I2C-MCU0 veri yolu fiziksel pin 3 (SDA) ve fiziksel pin 5 (SCL) üzerinden kullanılabilir.

Resmî sayfalarda farklı imaj veya overlay yapılandırmaları için hem `/dev/i2c-1` hem `/dev/i2c-2` gösteriliyor. Veri yolu numarasını sabit kabul etmeyin: `ls /dev/i2c-*` ile hatları listeleyin, kurulu imajdaki etkin denetleyiciyi belirleyin ve ardından doğru hattı `i2cdetect` ile inceleyin.

> **Elektriksel uyarı:** Yalnızca 3,3 V uyumlu cihaz kullanın. Herkese açık dokümantasyon başlıktaki pull-up değerlerini yayımlamıyor; haricî direnç eklemeden önce mevcut pull-up'ları ve toplam veri yolu yükünü doğrulayın. Aynı hattı kullanan cihazların adresleri çakışmamalıdır.

> **Ayrılmış pinler:** Fiziksel 27 ve 28 numaralı pinler I2C-WKUP0'a aittir ve HAT kimlik EEPROM'u için ayrılmıştır. Resmî kılavuz HAT yoksa boş bırakılmalarını söyler; açıkça doğrulamadan genel amaçlı I2C veya GPIO olarak kullanmayın.
