# alignment_laser
How to build a simple alignment laser for typical optical alignment tasks
## Overview:
This alignment laser is fast and simple to build, and easy to move around the lab. It can be used for most alignment tasks, from simple arrangements (e.g. placing a few mirrors) to complex systems (e.g. building sophisticated microscopes).

**Note:** It is not essential to copy this exact design, the key features and methods shown here can be applied to other setups.

![social_preview](https://github.com/amsikking/alignment_laser/blob/main/social_preview.jpg)

## Features:
- **A 532nm laser diode:** this sits in the middle of the visible spectrum (~380-750nm), and is good for aligning to the central wavelength of typical achromatic lenses. Also, the human eye is sensitive to the bright green color which helps during alignment.
- **A round ~3.5mm diameter beam profile:** elliptical or otherwise asymmetric beams are difficult to work with, a round beam is usually best.
- **A power of 4.5mW:** bright enough for most tasks, but not excessive.
- **A 5x beam expander with collimation adjustment:** this gives a ~17.5mm diameter beam which is enough for most 1 inch optical alignment tasks (and exceeds most objective back focal plane diameters).
- **A variable iris:** this allows easy beam diameter adjustment in the range of ~1-17.5mm. Small diameter beams (e.g. 1mm) are good for checking back reflections and beam deviations from lenses or other optics. Large diameter beams (e.g. >5mm) are good for checking collimation and have a long propagation distance.
- **Balanced mechanics:** the assembly is easy to move around and bolt down in different positions. When paired with 2 adjustable mirrors, the alignment laser is fast to deploy in most situations.

## Build:
Go to the [cad](https://github.com/amsikking/alignment_laser/tree/main/cad) folder and open [alignment_laser_v1.0.pdf](https://github.com/amsikking/alignment_laser/blob/main/cad/alignment_laser_v1.0.PDF)
- Get the parts and screw them together (see the other CAD files for details).

## Test:
Download the repository, go to the [photos](https://github.com/amsikking/alignment_laser/tree/main/photos) folder and follow the numbered photos:

0) **Check parts**: to follow exactly you’ll need these extra parts from Thorlabs:
    - Absorptive ND filter wheel (or filter set) for beam attenuation: NDC-100S-4M or NEK01 (or both).
    - A camera for looking at the beam profile: e.g. CS165MU1/M
    - Some shear plates for checking collimation: SI100 (5-10mm beams), SI050P (2.5-5mm beam plate) and SI254P (10-25.4mm beam plate).
    - **Note:** If you don’t have these parts, you can do something similar with other tricks (e.g. alternative beam attenuation and profiling methods, and checking collimation with distance).
1) **Check laser collimation:** attenuate the beam and use the 2.5-5mm shear plate to check the laser output is collimated.
2) **Optional -> measure beam profile:** use a camera and compare the measured beam profile to the specification. Attenuate with ND filters on the camera and use the back reflection to align. See the [beam_profile_example](https://github.com/amsikking/alignment_laser/tree/main/beam_profile_example) folder and the [gaussian_beam_profiler](https://github.com/amsikking/gaussian_beam_profiler) repository for more.
3) **Add target:** use an alignment card (or similar) and center the beam on a target.
4) **Add 5x beam expander:** the large beam (iris open) should have a nice smooth profile over ~17.5mm.
5) **Check beam deviation:** with a small ~1mm beam (iris closed), check the position of the beam on the target. A small deviation of a few mm is normal after adding the beam expander since we are relying on the mechanical alignment of the parts.
6) **Add large shear plate:** With a small ~1mm beam, add the 10-25.4mm shear plate and use the double reflections to align the plate with the line on the frosted screen.
7) **Check collimation:** Open the iris to ~17.5mm and check the collimation with the shear plate.
8) **Adjust collimation:** use the beam expander adjuster to set the collimation with the shear plate.
9) **Re-check collimation:** use the 5-10mm shear plate to double check collimation, then fix the position of the beam expander adjuster with the set screw.

If the testing goes smoothly, the portable alignment laser is now ready to use!

## Acknowledgments:
Inspired by, or with contributions from: [jlazzaridean](https://github.com/jlazzaridean), [fadero](https://github.com/fadero) and [AndrewGYork](https://github.com/AndrewGYork).
