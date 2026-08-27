# T3 Gemstone O1 Pinout

## Interactive reference for the 40-pin expansion header

Gemstone Pinout documents the physical pins, compatibility GPIO numbers and default interfaces exposed by the T3-GEM-O1 development board. The header follows the familiar Raspberry Pi 40-pin physical layout, while the underlying processor, pin multiplexing and software stack are specific to the Texas Instruments AM67A platform.

## Header interfaces

The default header configuration exposes I2C1, SPI0, UART0 and PCM alongside general-purpose 3.3 V GPIO. Seven GPIOs can be switched to PWM functions with T3-GEM-O1 device-tree overlays configured in `/boot/uEnv.txt`.

## Compatible HATs and add-ons

Physical fit does not guarantee electrical or software compatibility. The [compatible boards catalogue](/boards) lists only add-ons reviewed against the T3-GEM-O1 pin assignment, voltage requirements, pin direction, device-tree configuration and Linux driver availability.

Compatibility states are:

* **Verified:** hardware and software operation have been confirmed.
* **Conditionally compatible:** the board can work with documented limitations or configuration.
* **Incompatible:** the board must not be used, or a required feature is unavailable.

## Authoritative resources

* [T3 Gemstone O1 documentation](https://docs.t3gemstone.org/en/boards/o1/introduction)
* [GPIO guide](https://docs.t3gemstone.org/en/boards/o1/peripherals/gpio)
* [PWM guide](https://docs.t3gemstone.org/en/boards/o1/peripherals/pwm)
* [Open hardware design files](https://github.com/t3gemstone/hardware)
