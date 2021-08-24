---
id: circuitpython
title: Installing CircuitPython
sidebar_label: Installing CircuitPython
---

## Where do I download it from?

You can download CircuitPython from the download section of the [CircuitPython Website](https://circuitpython.org/downloads)


## What board?

You need to download the version that's built for your board.  If your keyboard uses a development board as its core, you will need to download CircuitPython for that development board.  If you have a keyboard that's directly supported as a board in the list, use that.

## Which version?

PyKey needs core modules that were made available with version 7.0.0.  At the time of writing, 7.0.0 is still in beta.
Why 7.0.0? [Hear the changes that comes wth 7.0 from Scott](https://youtu.be/HaLtpXjhSMg?t=2295), the main developer on Circuitpython.  The key addition needed by PyKey is the Keypad core module.  Earlier releases do not have this module.

## How do I install it?

Once you have CircuitPython for your board downloaded,  put your board in bootloader mode (double-press of reset for nRF52840 boards).  A mass storage device will show up on your computer. Copy the UF2 file to the controller.
The board will restart and a different mass storage device will showw up on your computer.  Your board now runs CircuitPython!

See a video example [here](https://youtu.be/1VyQ86nlFf4?list=PLjF7R1fz_OOWFqZfqW9jlvQSIUmwn9lWr).






