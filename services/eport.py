"""
--- eport.py ---
This file initializes connection with ePort
And defines functions to send commands
"""
import serial
import threading

PORT = "COM4"
BAUDRATE = 115200
PROMPT = b"eSeries V1.3 > "

_lock = threading.Lock()

def send_command(command):
    with _lock:
        with serial.Serial(PORT, BAUDRATE, timeout=5) as ser:
            ser.reset_input_buffer()
            ser.write((command + '\r').encode("ascii"))

            response = ser.read_until(PROMPT)

            if not response.endswith(PROMPT):
                raise TimeoutError("ePort Timeout")
