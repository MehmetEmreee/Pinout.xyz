<!--
---
page_url: spi
description: T3 Gemstone O1 SPI-MCU0 başlık pinleri
url: https://docs.t3gemstone.org/tr/boards/o1/peripherals/introduction
-->
# SPI

SPI-MCU0; fiziksel pin 19 (MOSI), 21 (MISO) ve 23'ü (saat) kullanır. Aktif-düşük chip-select sinyalleri pin 24 (CS0) ve 26 (CS2) üzerindedir. Uygun overlay etkinken bunlar `/dev/spidev0.0` ve `/dev/spidev0.2` olarak sunulur.

Her aygıta ayrı chip-select verildiğinde ve seçili olmayan cihaz MISO hattını serbest bıraktığında birden fazla SPI cihazı MOSI, MISO ve saat hatlarını paylaşabilir.

> **Paylaşılan veri yolu uyarısı:** Belgelenen yapılandırmalarda SPI-MCU0 kart üzerindeki sensörlerle paylaşılır. 3,3 V lojik kullanın ve bağlantıdan önce `k3-am67a-t3-gem-o1-spidev0-1cs.dtbo` veya `...-2cs.dtbo` overlay'lerinden hangisinin etkin olduğunu doğrulayın. Denetleyiciyi yeniden atamak IMU ve barometreyi Linux tarafından erişilemez hâle getirebilir.
