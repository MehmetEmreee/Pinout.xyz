<!--
---
name: 3v3 Power
class: interface
type: pinout
description: T3 Gemstone O1 3.3 V header supply pins
pincount: 2
pin:
  '1':
  '17':
-->
# 3.3 V Power

Physical pins 1 and 17 provide the header's regulated 3.3 V supply. GPIO logic also operates at 3.3 V.

The public documentation does not currently state a safe combined accessory-current budget for these pins. Do not infer Raspberry Pi current limits; verify the T3-GEM-O1 power-tree rating before powering a substantial load.
