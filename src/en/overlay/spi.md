<!--
---
name: SPI
class: interface
type: pinout
description: T3 Gemstone O1 SPI-MCU0 header pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/introduction
pincount: 5
pin:
  '19':
    name: SPI-MCU0 MOSI
    direction: output
    active: high
  '21':
    name: SPI-MCU0 MISO
    direction: input
    active: high
  '23':
    name: SPI-MCU0 SCLK
    direction: output
    active: high
  '24':
    name: SPI-MCU0 CS0
    direction: output
    active: low
  '26':
    name: SPI-MCU0 CS2
    direction: output
    active: low
-->
# SPI - Serial Peripheral Interface

SPI-MCU0 uses physical pins 19 (MOSI), 21 (MISO) and 23 (clock), with active-low chip selects on pins 24 (CS0) and 26 (CS2). They are exposed as `/dev/spidev0.0` and `/dev/spidev0.2` when the matching overlay is active.

Multiple SPI devices can share MOSI, MISO and the clock when each device has its own chip-select and releases MISO while not selected.

> **Shared-bus warning:** Documented configurations share SPI-MCU0 with onboard sensors. Use 3.3 V logic and verify whether `k3-am67a-t3-gem-o1-spidev0-1cs.dtbo` or `...-2cs.dtbo` is active before wiring. Reassigning the controller can make the onboard IMU and barometer unavailable to Linux.
