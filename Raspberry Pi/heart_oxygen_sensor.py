import time
from max30102 import MAX30102

# Create MAX30102 object
mx30 = MAX30102()

def measure_heart_rate_and_spO2():
    # Initialize MAX30102 sensor
    mx30.begin()

    # Print header
    print("Red, IR, Heart Rate, SpO2")

    try:
        while True:
            # Read sensor data
            mx30.read_sensor()

            # Print data
            print(f"{mx30.red}, {mx30.ir}, {mx30.ir_hr}, {mx30.ir_spo2}")

            time.sleep(1)  # Adjust the delay based on your requirements

    except KeyboardInterrupt:
        print("Measurement stopped by the user.")

if __name__ == "__main__":
    measure_heart_rate_and_spO2()
