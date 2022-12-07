from math import sin, cos
from pylx16a.lx16a import *
import time

LX16A.initialize("COM3", 0.1)

try:
    servo3 = LX16A(3)
    servo4 = LX16A(4)
    servo3.set_angle_limits(0, 240)
    servo4.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
while True:
    servo3.move(cos(t) * 30 + 150)
    servo4.move(sin(t) * 20 + 90)

    time.sleep(0.05)
    t += 0.1
