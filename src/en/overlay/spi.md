<!--
---
name: SPI
class: interface
type: pinout
description: T3 Gemstone O1 SPI0 header pins
pincount: 5
pin:
  '19':
    name: SPI0 MOSI
    direction: output
    active: high
  '21':
    name: SPI0 MISO
    direction: input
    active: high
  '23':
    name: SPI0 SCLK
    direction: output
    active: high
  '24':
    name: SPI0 CE0
    direction: output
    active: low
  '26':
    name: SPI0 CE1
    direction: output
    active: low
-->
# SPI - Serial Peripheral Interface

SPI0 uses physical pins 19 (MOSI), 21 (MISO) and 23 (clock), with active-low chip selects on pins 24 (CE0) and 26 (CE1).

Multiple SPI devices can share MOSI, MISO and the clock when each device has its own chip-select signal. Confirm the Linux device node and required device-tree configuration for the connected peripheral before use.
