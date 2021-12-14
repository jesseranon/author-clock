import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
# from lib import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

# define display function
# put everything below in it
def display_quote(o):
    try:
        write_dict = o

        # print(write_dict)

        # THIS IS THE DRAW PART OF THE DISPLAY FUNCTION
        im = Image.new('L', (800,480), 255)
        draw = ImageDraw.Draw(im)

        # draw text
        for l in list(write_dict.keys()):
            if l == 'attribution':
                k = write_dict[l]
                draw.multiline_text((k['x'], k['y']), k['text'], font=k['font'], spacing=k['spacing'], align='right', fill=0)
            else:
                wdl = write_dict[l]
                for t in wdl:
                    k = wdl[t]
                    draw.text((k['x'], k['y']), k['text'], font=k['font'], fill=0)

        # FOR TESTING save to image
        im.save(f"1.bmp")

        # draw to display
        # logging.info("Starting quote display")
        # epd = epd7in5_V2.EPD()
        
        # logging.info("init and Clear")
        # epd.init()
        # epd.Clear()

        # epd.display(epd.getbuffer(im))

        # logging.info("sending epd to sleep")
        # epd.sleep()

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        # epd7in5_V2.epdconfig.module_exit()
        exit()