import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from time_quote_finder import find_time_quote
import logging
from lib import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

try:
    logging.info("Starting quote display")
    epd = epd7in5_V2.EPD()
    
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 480
    FONT_SIZE = 30
    TOP_MARGIN = 15
    SIDE_MARGIN = 15
    SPACING = 3 # padding between lines of text

    garamond = {
        'regular': ImageFont.truetype('fonts/Garamond-Regular.ttf',FONT_SIZE),
        'bold': ImageFont.truetype('fonts/Garamond-Bold.ttf',FONT_SIZE),
        'italic': ImageFont.truetype('fonts/Garamond-Italic.ttf',FONT_SIZE)
    }

    time_quote = find_time_quote()
    # time_quote = {'time-of-text': '0:00', 'text-time': 'Midnight', 'text': '"Midnight," you said. What is midnight to the young? And suddenly a festive blaze was flung Across five cedar trunks, snow patches showed, And a patrol car on our bumpy road Came to a crunching stop. Retake, retake!', 'title': 'Pale Fire', 'author': 'Vladimir Nabokov'}
    # time_quote = {'time-of-text': '0:00', 'text-time': 'twelve', 'text': 'HAMLET: What hour now? HORATIO: I think it lacks of twelve. MARCELLUS: No, it is struck.', 'title': 'Hamlet', 'author': 'William Shakespeare'}
    print(time_quote)

    def text(output_path,font_reg,font_bold,quote):
        pre_time = {'self': 'pre_time', 'font': font_reg}
        text_time = {'self': 'text_time', 'font': font_bold, 'text': quote['text-time']}
        post_time = {'self': 'post_time', 'font': font_reg}
        quote_text = quote['text'].strip()
        quote_title = quote['title'].strip()
        quote_author = quote['author'].strip()
        ttb = quote_text.find(text_time['text'])
        tte = ttb + len(text_time['text'])
        if ttb > 0:
            pre_time['text'] = quote_text[0:ttb]
        else:
            pre_time['text'] = ''
        if tte >= len(quote_text):
            post_time['text'] = ''
        else:
            post_time['text'] = quote_text[tte:]
        attribution = f"{quote_title}\n{quote_author}"

        left_margin = SIDE_MARGIN
        top_margin = TOP_MARGIN
        right_margin = DISPLAY_WIDTH - left_margin
        bottom_margin = DISPLAY_HEIGHT - top_margin

        reg_ascent, reg_descent = font_reg.getmetrics()
        (a_width, a_height), (a_offset_x, a_offset_y) = font_reg.font.getsize(quote_author)
        (t_width, t_height), (t_offset_x, t_offset_y) = font_reg.font.getsize(quote_title)
        ## other stuff here

        # set attribution width
        att_width = 0
        if t_width > a_width:
            att_width += t_width
        else:
            att_width += a_width

        # set attribution x, y
        att_x = right_margin - att_width
        att_y = bottom_margin - (reg_ascent*2) - reg_descent - SPACING

        # set quote box height
        QUOTE_BOX_HEIGHT = att_y - top_margin

        ## split the lines
        line = 1
        next_line = line + 1

        write_dict = {}

        xpix, ypix = (left_margin, top_margin)
        to_print = [pre_time, text_time, post_time]

        for t in range(0,len(to_print)):

            curr = to_print[t]
            text_buffer = [curr['text']]

            while len(text_buffer) > 0:

                while xpix + curr['font'].getlength(text_buffer[0]) > right_margin:

                    try:

                        e = text_buffer[0].rindex(' ')

                        try:

                            text_buffer[1] = text_buffer[0][e:] + text_buffer[1]

                        except IndexError:

                            text_buffer.append(text_buffer[0][e:])

                        text_buffer[0] = text_buffer[0][0:e]

                    except ValueError:
                        
                        xpix = left_margin
                        ypix += reg_ascent + SPACING
                        line += 1

                        try:
                            text_buffer[0] += text_buffer.pop(1)                        
                            
                        except IndexError:
                            
                            continue

                try:
                    write_dict[str(line)]
                except KeyError:
                    write_dict.update({
                        str(line): {}
                    })

                write_dict[str(line)].update({
                    curr['self']: {
                        'font': curr['font'],
                        'x': xpix,
                        'y': ypix,
                        'text': text_buffer[0]
                    }
                })

                if len(text_buffer) > 1: # if there is more from this text still in the buffer
                    line += 1
                    xpix =left_margin
                    ypix += reg_ascent + SPACING
                    text_buffer[1] = text_buffer[1][1:] # remove extraneous space at front.
                else:
                    xpix += curr['font'].getlength(text_buffer[0])

                text_buffer.pop(0)

        # print(write_dict)

        # draw the image
        im = Image.new('L', (800,480), 255)
        draw = ImageDraw.Draw(im)

        # draw text
        for l in write_dict:
            wdl = write_dict[l]
            for t in wdl:
                k = wdl[t]
                draw.text((k['x'], k['y']), k['text'], font=k['font'], fill=0)

        # draw attribution
        draw.multiline_text((att_x, att_y), attribution, font=font_reg, spacing=SPACING, align='right', fill=0)

        # save to image
        im.save(output_path)
        print(f"image saved to {output_path}")

    text(f"{time_quote['author']}_{time_quote['title']}_{SPACING}.bmp", garamond['regular'], garamond['bold'], time_quote)

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd7in5_V2.epdconfig.module_exit()
    exit()