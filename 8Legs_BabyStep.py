from math import sin, cos
from pylx16a.lx16a import *
import time

LX16A.initialize("COM5", 0.1)

try:
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    servo3 = LX16A(3)
    servo4 = LX16A(4)
    servo5 = LX16A(5)
    servo6 = LX16A(6)
    servo7 = LX16A(7)
    servo8 = LX16A(8)
    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
    servo3.set_angle_limits(0, 240)
    servo4.set_angle_limits(0, 240)
    servo5.set_angle_limits(0, 240)
    servo6.set_angle_limits(0, 240)
    servo7.set_angle_limits(0, 240)
    servo8.set_angle_limits(0, 240)

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
while True:
    servo1.move(sin(t) * 10 + 25 +10)
    servo2.move(cos(t) * 10 + 3 +10)
    servo3.move(cos(t) * 10 + 183 -10)
    servo4.move(sin(t) * 10 + 150 -10)
    servo5.move(-sin(t) * 10 + 23 +10)
    servo6.move(-cos(t) * 10 +1 +10)
    servo7.move(-cos(t) * 10 + 182 -10)
    servo8.move(-sin(t) * 10 + 153 -10)

    time.sleep(0.02)
    t += 0.1
