import serial

ser = serial.Serial('COM6', 9600, timeout=1)
ser.flushInput()

while True:
    # print(ser.readline())
    # try:
    #     ser_bytes = ser.readline()
    #     decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    #     print(decoded_bytes)
    # except:
    #     print("Keyboard Interrupt")
    #     break