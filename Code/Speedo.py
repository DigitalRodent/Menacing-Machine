from microbit import *

# =========================================================
# Original Maqueen - real-time "speed" display
# =========================================================
# The ORIGINAL Maqueen has no wheel encoders or speed sensor, so there's
# no way to measure its actual real-world speed (cm/s). The best we can
# do is track and display the motor power level (PWM, 0-255) you're
# commanding it to run at, which acts as a stand-in for "speed" -
# higher PWM = faster.
#
# This shows that value live on the 5x5 LED display as a bar graph,
# and you can adjust it in real time with buttons A/B.
# =========================================================

MOTOR_ADDR = 0x10  # Maqueen motor driver I2C address

def set_motor(left_speed, right_speed):
    """
    Set motor speed, range -255 to 255 (negative = reverse).
    Uses Maqueen's standard I2C motor driver protocol.
    """
    def motor_bytes(motor_id, speed):
        direction = 0 if speed >= 0 else 1
        speed = min(255, abs(speed))
        return bytes([motor_id, direction, speed])

    i2c.write(MOTOR_ADDR, motor_bytes(0, left_speed))   # left motor
    i2c.write(MOTOR_ADDR, motor_bytes(1, right_speed))  # right motor

def show_speed_bar(speed_value, max_value=255):
    """Renders speed as a vertical bar graph across the 5x5 LED matrix."""
    display.clear()
    level = int((speed_value / max_value) * 25)  # scale to 0-25 LEDs
    level = max(0, min(25, level))

    for i in range(level):
        col = i % 5
        row = 4 - (i // 5)
        display.set_pixel(col, row, 9)

# --- Main ---
CURRENT_SPEED = 150  # starting motor power (0-255)
set_motor(CURRENT_SPEED, CURRENT_SPEED)
show_speed_bar(CURRENT_SPEED)

while True:
    changed = False

    if button_a.was_pressed():
        CURRENT_SPEED = max(0, CURRENT_SPEED - 25)
        changed = True

    if button_b.was_pressed():
        CURRENT_SPEED = min(255, CURRENT_SPEED + 25)
        changed = True

    if changed:
        set_motor(CURRENT_SPEED, CURRENT_SPEED)
        show_speed_bar(CURRENT_SPEED)

    sleep(50)