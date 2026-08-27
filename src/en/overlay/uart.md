<!--
---
name: UART
class: interface
type: pinout
description: T3 Gemstone O1 UART-MAIN1 header pins and optional UART routes
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/serial
pincount: 2
pin:
  '8':
    name: UART-MAIN1 TX
    direction: output
    active: high
  '10':
    name: UART-MAIN1 RX
    direction: input
    active: high
-->
# UART - Universal Asynchronous Receiver/Transmitter

UART-MAIN1 transmit and receive are exposed on physical pins 8 and 10 as `/dev/ttyS3`. These are 3.3 V TTL logic signals and must not be connected directly to RS-232 voltage levels or 5 V UART signals.

The board's separate three-pin debug serial connector is UART-MAIN0 and is not the 40-pin header UART.

> **Pin conflict:** Enabling PWM-0B on GPIO14 disables UART-MAIN1 TX; UART-MAIN1 RX can remain active. The optional UART-MAIN6 route uses physical pins 7/11 and disables Bluetooth. UART-WKUP0 uses pins 26/18 and replaces SPI-MCU0 CS2 on pin 26. Confirm `/boot/uEnv.txt` and reboot before wiring an optional route.
