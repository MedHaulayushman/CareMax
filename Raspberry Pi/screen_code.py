import time
from max30102 import MAX30102
import board
import displayio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

# Create MAX30102 object
mx30 = MAX30102()

# Set up the TFT screen
spi = board.SPI()
tft_cs = board.CE0
tft_dc = board.D25

displayio.release_displays()
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)

display = ST7735R(display_bus, width=160, height=128)

# Create a Group
g = displayio.Group()

# Create a Label
text = "Red: 0\nIR: 0\nHeart Rate: 0\nSpO2: 0%"
label_text = label.Label(displayio.BitmapFont(None), text=text, color=0xFFFFFF, x=10, y=10)
g.append(label_text)

# Show the Group
display.show(g)

def update_display(red, ir, heart_rate, spo2):
    label_text.text = f"Red: {red}\nIR: {ir}\nHeart Rate: {heart_rate}\nSpO2: {spo2}%"

if __name__ == "__main__":
    # Initialize MAX30102 sensor
    mx30.begin()

    try:
        while True:
            # Read sensor data
            mx30.read_sensor()

            # Update TFT display
            update_display(mx30.red, mx30.ir, mx30.ir_hr, mx30.ir_spo2)

            time.sleep(1)  # Adjust the delay based on your requirements

    except KeyboardInterrupt:
        print("Measurement stopped by the user.")
