<!--
---
name: GPIO
class: interface
type: pinout
description: T3 Gemstone O1 general-purpose 3.3 V GPIO pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/gpio
pin:
  '3':
  '5':
  '7':
  '8':
  '10':
  '11':
  '12':
  '13':
  '15':
  '16':
  '18':
  '19':
  '21':
  '22':
  '23':
  '24':
  '26':
  '27':
  '28':
  '29':
  '31':
  '32':
  '33':
  '35':
  '36':
  '37':
  '38':
  '40':
-->
# GPIO - General Purpose Input/Output

The T3-GEM-O1 40-pin header exposes 3.3 V general-purpose digital I/O. A GPIO can be configured as an input, driven as an output, or switched to a peripheral function through the AM67A pinmux.

Use Linux `libgpiod` tools such as `gpioinfo`, `gpiofind`, `gpioget` and `gpioset` instead of relying on Raspberry Pi-specific GPIO libraries. Resolve a line by its system-provided name before using it; GPIO controller and line numbers may change between kernel or device-tree versions.

> **Electrical warning:** Do not apply 5 V logic directly to a GPIO pin. Public documentation does not specify per-pin or combined source/sink current, pull configuration, or a guaranteed level during boot. Treat GPIO outputs as control signals and use an appropriate resistor, driver, buffer or level shifter; do not directly drive LEDs, relays, buzzers or motors.

Pinmux changes required by PWM and other peripherals are applied with T3-GEM-O1 device-tree overlays listed in `/boot/uEnv.txt`.
