<!--
---
name: I2C
class: interface
type: pinout
description: T3 Gemstone O1 I2C-MCU0 and reserved I2C-WKUP0 header pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/i2c
pin:
  '3':
    name: I2C-MCU0 SDA
    direction: both
    active: high
  '5':
    name: I2C-MCU0 SCL
    direction: both
    active: high
  '27':
    name: I2C-WKUP0 SDA (Reserved)
    direction: both
    active: high
  '28':
    name: I2C-WKUP0 SCL (Reserved)
    direction: both
    active: high
-->
# I2C - Inter-Integrated Circuit

The external I2C-MCU0 bus is available on physical pin 3 (SDA) and physical pin 5 (SCL).

The official pages show both `/dev/i2c-1` and `/dev/i2c-2` under different image or overlay configurations. Do not hard-code the bus number: run `ls /dev/i2c-*`, identify the active controller for the installed image, then inspect that bus with `i2cdetect`.

> **Electrical warning:** Use only 3.3 V-compatible devices. The public documentation does not publish the header pull-up values; verify existing pull-ups and total bus loading before adding resistors. Every device sharing the bus must use a non-conflicting address.

> **Reserved pins:** Physical pins 27 and 28 belong to I2C-WKUP0 and are reserved for HAT identification EEPROM. The official guide says to leave them unconnected when no HAT is present; do not treat them as general-purpose I2C or GPIO without explicit validation.
