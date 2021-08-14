---
id: circuitpython
title: Installing CircuitPython
sidebar_label: Installing CircuitPython
---

## Where do I download it from?

You can download CircuitPython from the download section of the [CircuitPython Website](https://circuitpython.org/downloads)


## What board?

You need to download the version that's built for you board.

## Which version?

PyKey needs modules that were made available with version 7.0.0.  At the time of writing, 7.0.0 is still in alpha.
Why 7.0.0? [Hear the changes that comes wth 7.0 from Scott](https://youtu.be/HaLtpXjhSMg?t=2295), the main developer on Circuitpython.

## How do I install it?

Once you have the firmware downloaded, uncompress the zip file, put your board in bootloader mode (double-press of reset for nRF52840 boards).  A mass storage device will show up on your computer. Copy the UF2 file to the controller.
The board will restart and a different mass storage device will showw up on your computer.  Your board now runs CircuitPython!

See a video example [here](https://youtu.be/1VyQ86nlFf4?list=PLjF7R1fz_OOWFqZfqW9jlvQSIUmwn9lWr).




