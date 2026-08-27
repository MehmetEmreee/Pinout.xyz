<!--
---
name: PCM
class: interface
type: pinout
description: T3 Gemstone O1 PCM/I2S-compatible header signals
pin:
  '12':
    name: CLK
  '35':
    name: FS
  '38':
    name: DIN
  '40':
    name: DOUT
-->
# PCM - Pulse-code Modulation

The default 40-pin assignment reserves physical pins 12, 35, 38 and 40 for PCM clock, frame sync, data input and data output respectively.

PCM/I2S software and HAT compatibility must be checked against the T3-GEM-O1 device tree and audio drivers; matching physical pins alone does not guarantee that a Raspberry Pi audio HAT will work.
