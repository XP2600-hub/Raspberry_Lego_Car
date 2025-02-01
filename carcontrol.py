from gpiozero import OutputDevice
import time
import curses

# Define the GPIO pins connected to the L298N
motor1_forward = OutputDevice(17)  # IN1
motor1_backward = OutputDevice(18)  # IN2
motor_enable = OutputDevice(22)     # ENA (optional for PWM control)

# Enable the motor
motor_enable.on()

# Get the curses window to capture keyboard input
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):  # Quit if 'q' is pressed
            break
        elif char == curses.KEY_UP:  # Move motor forward
            motor1_forward.on()
            motor1_backward.off()
            print("Motor moving forward")
        elif char == curses.KEY_DOWN:  # Move motor backward
            motor1_forward.off()
            motor1_backward.on()
            print("Motor moving backward")
        elif char == curses.KEY_LEFT:  # Stop motor
            motor1_forward.off()
            motor1_backward.off()
            print("Motor stopped")
        elif char == curses.KEY_RIGHT:  # Toggle motor direction
            motor1_forward.toggle()  # Change direction
            motor1_backward.toggle()
            print("Motor direction toggled")
        time.sleep(0.1)  # Small delay to avoid bouncing

finally:
    # Clean up GPIO states before exiting
    motor1_forward.off()
    motor1_backward.off()
    motor_enable.off()
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()