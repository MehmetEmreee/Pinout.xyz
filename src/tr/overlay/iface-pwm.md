<!--
---
name: PWM
page_url: pwm
description: T3 Gemstone O1 donanımsal PWM destekli başlık pinleri
-->
# PWM - Darbe Genişlik Modülasyonu

40 pin başlık yedi donanımsal PWM seçeneği sunar: GPIO 12 üzerinde PWM-ECAP0, GPIO 16 üzerinde PWM-ECAP1, GPIO 18 üzerinde PWM-ECAP2, GPIO 5 üzerinde PWM-0A, GPIO 14 üzerinde PWM-0B, GPIO 6 üzerinde PWM-1A ve GPIO 13 üzerinde PWM-1B.

Kullanılabilir işlevler `/boot/uEnv.txt` üzerinden yüklenen T3-GEM-O1 device tree overlay'lerine bağlıdır; her PWM etiketinin mevcut açılış yapılandırmasında etkin olduğunu varsaymayın. PWM-0A ile PWM-0B aynı periyodu; PWM-1A ile PWM-1B de aynı periyodu paylaşır. Her çiftte görev döngüleri bağımsız ayarlanabilir.

Denetleyicilere `/sys/class/pwm` üzerinden erişilir. Tam overlay adları ve `pwmchip` eşlemesi için resmî PWM kılavuzuna bakın.

> **Yük uyarısı:** PWM başlık pinleri 3,3 V lojik sinyalidir; motor veya servo güç çıkışı değildir. Herkese açık dokümantasyon GPIO sürme akımını veya garanti edilen PWM frekans sınırlarını belirtmiyor. Servo ve diğer yükleri uygun kapasiteli haricî kaynaktan besleyin, uygun sürücü veya seviye dönüştürücü kullanın ve gerektiğinde toprakları ortaklayın.
