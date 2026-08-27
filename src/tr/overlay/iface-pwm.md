<!--
---
name: PWM
page_url: pwm
description: T3 Gemstone O1 donanımsal PWM destekli başlık pinleri
-->
# PWM - Darbe Genişlik Modülasyonu

40 pin başlık yedi donanımsal PWM seçeneği sunar: GPIO 12 üzerinde PWM-ECAP0, GPIO 16 üzerinde PWM-ECAP1, GPIO 18 üzerinde PWM-ECAP2, GPIO 5 üzerinde PWM-0A, GPIO 14 üzerinde PWM-0B, GPIO 6 üzerinde PWM-1A ve GPIO 13 üzerinde PWM-1B.

Her PWM işlevi `/boot/uEnv.txt` içindeki ilgili T3-GEM-O1 device tree overlay'iyle seçilmelidir. PWM-0A ile PWM-0B aynı periyodu; PWM-1A ile PWM-1B de aynı periyodu paylaşır. Her çiftte görev döngüleri bağımsız ayarlanabilir.

Denetleyicilere `/sys/class/pwm` üzerinden erişilir. Tam overlay adları ve `pwmchip` eşlemesi için resmî PWM kılavuzuna bakın.
