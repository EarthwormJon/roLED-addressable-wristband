# roLED-addressable-wristband

The roLED addressable RGB wristband similarities with the watch maker of a vaguely similar name end at the 42mm case and instead features individually addressable RGB LEDs and 4 capacitive touch pad inputs.

This product was uploaded to thangs.com as part of the Hallowearables Contest hosted by [Zack Freedman](https://www.youtube.com/channel/UCUW49KGPezggFi0PGyDvcvg).

To download the STL files go to the [product page at thangs.com](https://thangs.com/Earthworm_Jon/roLED-Addressable-RGB-Wristband-27867).

## Introduction

The roLED - an Addressable LED wristband powered by the microcontroller or single board computer of your choice, featuring 4 capacitive touch pads to select between multiple modes.

**Please note that the software included is in a very basic state and only seeks to demonstrate the hardware features of the device at this time. Community contribution on both the software and hardware side of the project is very much welcomed and appreciated**

### Features:

* Supports as many neopixels / ws2812b LEDs as you can reasonably power
* 4x capacitive touch pads for input
* Compatible with most microcontrollers and single board computers
* Bracelet style wristband that can be easily adjusted to fit your wrist
* All parts printed in PLA
* Estimated print time: 4.5 to 6 hours
* Estimated assembly time: 30minutes
* Optional case for the Raspberry Pi Pico

## Background for the build:

My approach to the contest has been to keep it relatively simple, focus on the aesthetics of the 3d printed elements and above all, make sure I can deliver something before the contest deadline. I used parts that had previously been destined for other projects that never happened or failed so it was nice not to have to buy anything specifically to put this together.

Using a 3d printer meant that I could rapidly iterate through design changes as when parts only take a few minutes to export from cad, slice and print, it makes sense to work through multiple printed parts - particularly for testing tolerances and light diffusion through the plastic. I spent quite a bit of time tuning the distance of the Link Faces from the LEDs as I found that when they were too close, the light would not diffuse properly and you would just end up with a very bright spot immediately over the LED - no other manufacturing method would allow me to create and iterate so quickly.

I wanted some type of input device so that future iterations of the code could give the LED wristband some actual useful functionality but trying to find small buttons would have needed me to order something specifically for the project. I settled on the aluminium foil capacitive touch pads and was pleased to find that the touchio module was built right into Circuit Python.

If you choose to make this project for yourself, I hope you find the documentation clear and that it is fun to print and assemble. If you do have any questions, please do find me (raise an issue on the repo or find me on Zack's discord) and I will get back to you in time and if you’d like to share your take on this concept please do share your remixes on thangs.com and raise a pull request in the Github repo.

## Tools used:

* Soldering Iron
* Hot glue gun (optional)
* Side Cutters
* Wire strippers
* 3d printer

## Bill of materials:

### Electronics:

* A microcontroller or single board computer of your choice, I used a Raspberry Pi Pico but otherwise the board must support:
* * CircuitPython 7.x
* * 3.3v output for the LED strip
 
* Strip of WS2812b LEDs / Neopixels @ 60 LEDs per meter (typically sold by the meter but you’ll only need to use enough to fit your wrist)
* 10x female to male dupont connectors
* 4x  1M ohm resistors

* 3d printing filament:

* * 1.75mm filament for the pins
* * Transparent, white or at least light coloured filament for the Link Faces
* * Any other colour filament for the rest of the printed parts

* Other:

* * Aluminium foil
* * Approx 3m of light gauge wire
* * Heat shrink wrap (optional)
* * Portable USB battery bank (whatever size you want to carry around for on-the-go)
* * CA glue

## Printing

The Addressable LED wristband supports a variable number of links that make up the wristband to allow you to size it to fit your wrists. You will need to print the following:

* 9 to 15x Link Bases
* 9 to 15x Link Faces (in transparent or white material)
* 1x Latch Link
* 1x Latch Outer
* 1x Latch Inner
* 1x Case
* 2x Case Bezel (in transparent or white material)
* 1x Pico Case Lower (optional)
* 1x Pico Case Lid (optional)

The hardest print in this project are the 2mm holes for the filament pins to pass through the links. These might collapse if the print is warped or has other bed adhesion problems. Slicing the print at 0.2mm layer height seemed to result in the fewest failures but you may want to print a few more Link Bases than you would actually need to account for these.

Infill: 20%
Supports: No
Re-orientate: No

## Addressable LED Wristband Assembly:

1. Push the 1.75mm filament through the holes in the Link base parts to connect one link to another. If you have problems pushing the filament through the holes in the links, use an M2 bolt to clear out the hole of any printing debris and any other obstructions.
2. Assemble the Latch Outer and Inner parts using more 1.75mm filament.
3. Check that you’re happy with the fit of the wristband, if not, you can use a small hex key or something similar to push the filament pins out and add/remove links as required.
4. Cut and solder 3 of the dupont connectors to the led strip. I like to cut these connectors down to align with the others that we’ll use later to wire up the capacitive touch pads.
5. Close the wristband and then secure the LED strip to the wristband using either the included adhesive backing or CA glue. The input end of the LED strip should be on the link next to the Link Coupler. Try to align the first and last LED with the centre of their links.
6. Strip a small amount of insulation from the female end of 4 dupont connectors. Two should be approx 2cm longer than the other two.
7. Glue these into the cuts in the case.
8. Run the wires down the wrist strap towards the input end of the LED strip and secure in place with glue as you go.
9. You can use hot glue or more CA glue to secure the wires to the inside of the loop on the Latch Link. This will help keep the wires in place as they get pulled during normal use.
10. Cut out aluminium foil and cover the 4 touch pads on the Case
11. Place the Case Bezel over the top of the Case. You should find that friction will hold it on but use glue if not.
12. Glue Link Faces onto each of the Link Bases and if friction is not enough to secure the Case Bezel to the Case, use glue here as well.

Separately to the wristband, you should extend the remaining dupont connectors to reach the wristband from the location of the microcontroller and battery. If this is in your pocket, you could run the wires up your tshirt and down your arm. An enclosure to fit the Raspberry Pi Pico is included.

## Wiring Diagram:

Yours may vary depending upon which microcontroller or single board computer that you use. The example wiring diagram in this repo shows the Raspberry Pi Pico that I happened to use.

## Code:

Depending on the microcontroller or single board computer that you use in your project, the instructions below are for the Raspberry Pi Pico

1. If it’s your first time using Circuit Python on the Raspberry Pi Pico, I recommend following this guide to set up your Pico microcontroller to run Circuit Python 7.x (https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython), and get your computer set up with an editor.
2. Download the CircuitPython library bundle (https://circuitpython.org/libraries). 
3. Copy the neopixel.mpy library to the lib folder on your Pico. If a lib folder doesn’t exist create one..
4. Create a main.py file with the demo.py code found in this repository (https://github.com/EarthwormJon/roLED-addressable-wristband) 
5. Update any of the GP## pin numbers with the same pins you have used.
6. Reload the Raspberry Pi Pico and test pressing the capacitive touch buttons.
7. If the colours of the wristband don’t change or change without you pressing the aluminium foil pads, then you need to tune the touch_x.threshold values. I found 3000 worked best but this might vary for you.
8. You also might want to adjust the brightness of the LEDs to extend the battery life.

As you can see, the script for the LEDs is very basic at the moment and pretty much only proves that the LEDs and capacitive touch pads work. Future potential use cases for the LED wristband, depending on the microcontroller used, include:

* Get the weather forecast at a touch of a button - a few blue LEDs for light rain, many blue LEDs for heavy rain?
* Get updates on your current print job using the Octoprint API
* Link it to the number of steps you’ve taken so far today

If you want to keep up with any enhancements I make to the code or contribute your own ideas, feel free to follow the project on Github at https://github.com/EarthwormJon/roLED-addressable-wristband


