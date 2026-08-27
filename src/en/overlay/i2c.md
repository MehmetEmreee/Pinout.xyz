<!--
---
name: I2C
class: interface
type: pinout
description: T3 Gemstone O1 I2C1 header pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/i2c
pin:
  '3':
    name: I2C1 SDA
    direction: both
    active: high
  '5':
    name: I2C1 SCL
    direction: both
    active: high
  '27':
    name: ID SDA
    direction: both
    active: high
  '28':
    name: ID SCL
    direction: both
    active: high
-->
# I2C - Inter-Integrated Circuit

The external I2C1 bus is available on physical pin 3 (SDA) and physical pin 5 (SCL). The board documentation identifies this controller as `/dev/i2c-2` in the current software image.

I2C supports multiple devices on the same two signal lines, provided their addresses do not conflict. Install `i2c-tools` and use `sudo i2cdetect -y -r 2` to inspect the bus.

Physical pins 27 and 28 are reserved for the HAT identification EEPROM interface. Do not treat them as a general-purpose I2C connector unless the hardware and boot configuration have been explicitly verified.
