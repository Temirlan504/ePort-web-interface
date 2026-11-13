# --- Example 1 ---
# List only serial COM ports (USB class, excluding HID, audio, etc)
# import serial.tools.list_ports

# ports = serial.tools.list_ports.comports()

# for port in ports:
#     print("Port:", port.device)
#     print("Description:", port.description)
#     print("VID:", port.vid)
#     print("PID:", port.pid)
#     print()


# --- Example 2 ---
# import serial
# import time

# with serial.Serial("COM4", 115200, timeout=1) as ser:
#     ser.reset_input_buffer()
#     ser.write(b"list\r")
#     time.sleep(0.5) # Time for device to gather and send data

#     response = ser.read_all()
#     print("Raw:", repr(response))


# --- Example 3 ---
# BUG: What if command execution is longer than 0.5s?
# SOLUTION: Use end-of-command prompt from ePort (PROMPT = b"eSeries V1.3 > ")

import serial

PROMPT = b"eSeries V1.3 > "
with serial.Serial("COM4", 115200, timeout=5) as ser:
    ser.reset_input_buffer()
    ser.write(b"list\r")

    response = ser.read_until(PROMPT)

    if not (response.endswith(PROMPT)):
        print("Timeout: prompt not received.")

    print(response.decode("ascii", errors="replace"))