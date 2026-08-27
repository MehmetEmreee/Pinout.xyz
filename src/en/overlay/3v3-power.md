<!--
---
name: 3v3 Power
class: interface
type: pinout
description: T3 Gemstone O1 3.3 V header supply pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/introduction
pincount: 2
pin:
  '1':
  '17':
-->
# 3.3 V Power

Physical pins 1 and 17 provide the header's regulated 3.3 V supply. GPIO logic also operates at 3.3 V.

> **Undocumented limit:** The public documentation does not state a safe combined accessory-current budget or whether this rail may be back-powered. Do not infer Raspberry Pi limits, inject an external voltage or power a substantial load until the T3-GEM-O1 power-tree rating is confirmed.
