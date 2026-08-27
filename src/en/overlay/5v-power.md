<!--
---
name: 5v Power
class: interface
type: pinout
description: T3 Gemstone O1 5 V header supply pins
url: https://docs.t3gemstone.org/en/boards/o1/peripherals/introduction
pincount: 2
pin:
  '2':
  '4':
-->
# 5 V Power

Physical pins 2 and 4 provide the header's 5 V supply rail.

The available accessory current depends on the board power source, the T3-GEM-O1 load and the power-tree limits.

> **Back-power warning:** Header back-power behaviour and protection are not publicly specified. Do not feed power into pins 2 or 4 unless T3 documentation explicitly approves the method. Motors, heaters, large LED arrays and servo power should use a correctly rated external supply with a shared ground where required.
