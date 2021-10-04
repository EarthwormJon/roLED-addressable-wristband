"""CircuitPython Capacitive Touch NeoPixel Brightness Control Example"""
import time
import board
import touchio
import neopixel

touch_a = touchio.TouchIn(board.GP7)
touch_b = touchio.TouchIn(board.GP9)
touch_c = touchio.TouchIn(board.GP10)
touch_d = touchio.TouchIn(board.GP12)

touch_a.threshold = 3000
touch_b.threshold = 3000
touch_c.threshold = 3000
touch_d.threshold = 3000

num_pixels = 11
ORDER = neopixel.GRB


pixels = neopixel.NeoPixel(board.GP28, num_pixels, auto_write=False, pixel_order=ORDER, brightness=0.5)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


touched = time.monotonic()
color = 0
while True:
    if touch_a.value:
        pixels.fill((255, 0, 0))
        pixels.show()
        time.sleep(1)

    elif touch_b.value:
        pixels.fill((0, 255, 0))
        pixels.show()
        time.sleep(1)

    elif touch_c.value:
        rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step


    elif touch_d.value:
        rainbow_cycle(0.01)  # rainbow cycle with 1ms delay per step
