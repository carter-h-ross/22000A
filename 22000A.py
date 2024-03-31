#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
LF = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
LM = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
LR = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
RF = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
RM = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)
RR = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# how much the wheels need to turn to make the bot turn 180 degrees
turn180 = 400
# controller deadzone used to avoid the bot moving when you do not want it to
deadzone = 5
# the speed that the bot will go when one of the axis is just past the deadzone
minSpeed = 50
# how far the wheels need to turn to move one inch
degToOneInch = 50

# function that uses the turn180 constant to turn the degrees you want turn the bot to the distance to turn the drivetrain
def degToVex(deg):
    return ((turn180 * deg) / 180)

def inchToDeg(inches):
    return inches * degToOneInch

def ondriver_drivercontrol_0():
    setStopCoast()

    while True:

        #|----- moving left drive -----|

        # moving left forward
        if controller_1.axis3.position() > deadzone:
            setLeftSpeed(minSpeed + controller_1.axis3.position() / (100 / minSpeed))
            driveLeftForward()

        # moving left reverse
        elif controller_1.axis3.position() < 0 - deadzone:
            setLeftSpeed(minSpeed + (0 - controller_1.axis3.position()) / (100 / minSpeed))
            driveLeftReverse()
        
        else:
            stopLeft()

        #|----- moving right drive -----|

        # moving right forward
        if controller_1.axis2.position() > deadzone:
            setRightSpeed(minSpeed + controller_1.axis2.position() / (100 / minSpeed))
            driveRightForward()

        # moving right reverse
        elif controller_1.axis2.position() < 0 - deadzone:
            setRightSpeed(minSpeed + (0 - controller_1.axis2.position()) / (100 / minSpeed))
            driveRightReverse()

        else:
            stopRight()

def onauton_autonomous_0():
    setStopBrake()
    setSpeed(100, 100)
    move(10)
    turnLeft(90)
    move(-10)
    turnRight(90)
    move(5)
 
# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()


#|----- motor velo functions -----|

def setLeftSpeed(velo):
    LF.set_velocity(velo)
    LM.set_velocity(velo)
    LR.set_velocity(velo)    

def setRightSpeed(velo):
    RF.set_velocity(velo)
    RM.set_velocity(velo)
    RR.set_velocity(velo)

def setSpeed(leftVelo, rightVelo):
    setLeftSpeed(leftVelo)
    setRightSpeed(rightVelo)

#|----- motor movement forward functions -----|

def moveLeft(dist, waiting = True):
    LF.spin_for(FORWARD, dist, DEGREES, wait=False)
    LM.spin_for(FORWARD, dist, DEGREES, wait=False)
    LR.spin_for(FORWARD, dist, DEGREES, wait=waiting)

def moveRight(dist, waiting = True):
    RF.spin_for(FORWARD, dist, DEGREES, wait=False)
    RM.spin_for(FORWARD, dist, DEGREES, wait=False)
    RR.spin_for(FORWARD, dist, DEGREES, wait=waiting)

def driveLeftForward():
    LF.spin(FORWARD)
    LM.spin(FORWARD)
    LR.spin(FORWARD)

def driveLeftReverse():
    LF.spin(REVERSE)
    LM.spin(REVERSE)
    LR.spin(REVERSE)

def driveRightForward():
    LF.spin(FORWARD)
    LM.spin(FORWARD)
    LR.spin(FORWARD)

def driveRightReverse():
    LF.spin(REVERSE)
    LM.spin(REVERSE)
    LR.spin(REVERSE)

#|----- motor stopping functions -----|

def setStopCoast():
    LF.set_stopping(COAST)
    LM.set_stopping(COAST)
    LR.set_stopping(COAST)
    RF.set_stopping(COAST)
    RM.set_stopping(COAST)
    RR.set_stopping(COAST)

def setStopBrake():
    LF.set_stopping(BRAKE)
    LM.set_stopping(BRAKE)
    LR.set_stopping(BRAKE)
    RF.set_stopping(BRAKE)
    RM.set_stopping(BRAKE)
    RR.set_stopping(BRAKE)

def stopLeft():
    LF.stop()
    LM.stop()
    LR.stop()

def stopRight():
    RF.stop()
    RM.stop()
    RR.stop()

#|----- motor movement turning functions -----|

def move(dist):
    moveLeft(inchToDeg(dist))
    moveRight(inchToDeg(dist))

def flipLeft():
    moveLeft(0-turn180)
    moveRight(turn180)

def flipRight():
    moveLeft(turn180)
    moveRight(0-turn180)

def turnLeft(deg):
    moveLeft(0-degToVex(deg))
    moveRight(degToVex(deg))

def turnRight(deg):
    moveLeft(0-degToVex(deg))
    moveRight(degToVex(deg))

# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )
