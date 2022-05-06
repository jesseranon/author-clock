# Raspberry Pi Author Clock
This is a DIY version of The  Author Clock.  The underlying script is written in Python and deployed on Raspberry Pi with a Waveshare e-paper display, mounted on a normal picture frame.

**Link to project:** Blog coming soon

 

## How It's Made:

**Tech used:** Raspberry Pi Zero WH, Waveshare e-paper display, Python

Aside from Waveshare's e-paper software that controls the display, the script that runs the clock is written in python. It uses a Cron job to start the Python script every day, as it is set to stop at a certain time every day because it is in a classroom.

Gathered quotes from multiple sources including:
https://github.com/solarkennedy/epaper-watch/

e-paper hat
https://www.waveshare.com/7.5inch-e-paper-hat.htm
https://github.com/waveshare/e-Paper/

## Lessons Learned:

Python library CSV reader - I learned to use this to parse through a .csv file with the necessary quotes with their information and corresponding times.

Python library PIL - I learned to use this to generate image files for display on the e-paper display.

I also learned that there needs to be some sort of time checking against a service to keep machine time in sync with actual time, as the clock has fallen out of sync.  Being that the clock doesn't have access to the wifi in the building it is in, this is another problem to figure out.  But overall this was a really fun project and it got me to fall in love with coding all over again.
