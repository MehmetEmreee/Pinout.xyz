<!--
---
name: ArduPilot
class: interface
type: pinout
description: T3 Gemstone O1 header functions used by ArduPilot
url: https://docs.t3gemstone.org/en/projects/ardupilot
pin:
  '3':
    name: GPS / ADS1115 SDA
  '5':
    name: GPS / ADS1115 SCL
  '7':
    name: GPS RX
  '8':
    name: RCOut 2
  '10':
    name: RCIn SBUS
  '11':
    name: GPS TX
  '12':
    name: RCOut 7
  '18':
    name: Telemetry TX
  '19':
    name: SPI MOSI
  '21':
    name: SPI MISO
  '23':
    name: SPI SCLK
  '24':
    name: SPI CS0
  '26':
    name: Telemetry RX
  '27':
    name: Reserved I2C SDA
  '28':
    name: Reserved I2C SCL
  '29':
    name: RCOut 1
  '31':
    name: RCOut 3
  '32':
    name: RCOut 5
  '33':
    name: RCOut 4
  '36':
    name: RCOut 6
  '37':
    name: Buzzer
-->
# ArduPilot header connections

This view shows the 40-pin header functions assigned by the official T3 Gemstone ArduPilot configuration after the required device-tree overlays are enabled.

## Navigation and control

* **GPS and external compass:** pins 7 (UART-MAIN6 RX), 11 (UART-MAIN6 TX), 3 (I2C-MCU0 SDA) and 5 (I2C-MCU0 SCL).
* **RC input:** pin 10 (UART-MAIN1 RX) accepts SBUS.
* **RC outputs:** pins 29, 8, 31, 33, 32, 36 and 12 provide RCOut 1 through RCOut 7 respectively.
* **Telemetry:** pins 18 (UART-WKUP0 TX) and 26 (UART-WKUP0 RX).

## Other assigned pins

Pins 19, 21, 23 and 24 form SPI-MCU0. Pins 27 and 28 are reserved I2C-WKUP0 lines, while pin 37 is assigned to the external buzzer.

> **SBUS warning:** SBUS uses an inverted serial signal. An external signal inverter is required between the receiver and pin 10; do not connect a standard SBUS output directly.

Enable every overlay listed in the official ArduPilot guide before wiring peripherals. The guide also documents Linux device paths, service setup and QGroundControl connectivity.
