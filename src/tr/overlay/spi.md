<!--
---
page_url: spi
description: T3 Gemstone O1 SPI0 başlık pinleri
-->
# SPI

SPI0; fiziksel pin 19 (MOSI), 21 (MISO) ve 23'ü (saat) kullanır. Aktif-düşük chip-select sinyalleri pin 24 (CE0) ve 26 (CE1) üzerindedir.

Her aygıta ayrı chip-select verildiğinde birden fazla SPI cihazı MOSI, MISO ve saat hatlarını paylaşabilir. Kullanmadan önce Linux aygıt düğümünü ve gerekli device-tree yapılandırmasını doğrulayın.
