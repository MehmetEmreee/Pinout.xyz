<!--
---
name: UART
class: interface
type: pinout
description: T3 Gemstone O1 UART0 header pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/serial
pincount: 2
pin:
  '8':
    name: UART0 TX
    direction: output
    active: high
  '10':
    name: UART0 RX
    direction: input
    active: high
-->
# UART - Universal Asynchronous Receiver/Transmitter

UART0 transmit and receive are exposed on physical pins 8 and 10. These are 3.3 V logic signals and must not be connected directly to RS-232 voltage levels or 5 V UART signals.

The board also has a separate three-pin debug serial connector. Do not assume the 40-pin UART and debug console are the same Linux device; consult the current T3-GEM-O1 serial documentation.
