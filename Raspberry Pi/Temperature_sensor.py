import board
import busio
import adafruit_mlx90614
import time

# Set up the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the MLX90614 temperature sensor object
mlx = adafruit_mlx90614.MLX90614(i2c)

def measure_temperature():
    # Read object and ambient temperatures
    object_temp = mlx.object_temperature
    ambient_temp = mlx.ambient_temperature

    # Print the temperatures
    print(f"Object Temperature: {object_temp:.2f}°C")
    print(f"Ambient Temperature: {ambient_temp:.2f}°C")

if __name__ == "__main__":
    try:
        while True:
            measure_temperature()
            time.sleep(1)  # Adjust the delay based on your requirements

    except KeyboardInterrupt:
        print("Measurement stopped by the user.")
