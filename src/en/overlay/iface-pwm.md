<!--
---
name: PWM
class: interface
type: pinout
description: T3 Gemstone O1 hardware PWM-capable header pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/pwm
pin:
  '8':
    name: PWM-0B
  '12':
    name: PWM-ECAP2
  '29':
    name: PWM-0A
  '31':
    name: PWM-1A
  '32':
    name: PWM-ECAP0
  '33':
    name: PWM-1B
  '36':
    name: PWM-ECAP1
-->
# PWM - Pulse-width Modulation

The 40-pin header exposes seven hardware PWM options: PWM-ECAP0 on GPIO 12, PWM-ECAP1 on GPIO 16, PWM-ECAP2 on GPIO 18, PWM-0A on GPIO 5, PWM-0B on GPIO 14, PWM-1A on GPIO 6 and PWM-1B on GPIO 13.

Each PWM function must be selected with its T3-GEM-O1 device-tree overlay in `/boot/uEnv.txt`. PWM-0A and PWM-0B share a period, as do PWM-1A and PWM-1B; duty cycles can be configured independently within each pair.

The controllers are exposed through `/sys/class/pwm`. See the official PWM guide for the exact overlay names and `pwmchip` mapping.
