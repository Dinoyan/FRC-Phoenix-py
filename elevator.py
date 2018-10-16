import wpilib
import Joystick_handler
import robot_map


class Elevator():

    def __init__(self):
        self.elevCimOne = wpilib.Talon(robot_map.ELEV_ONE)
        self.elevCimTwo = wpilib.Talon(robot_map.ELEV_TWO)
        self.elevStick = wpilib.XboxController(1)

    def operateElevator(self):
        self.elevCimOne.set(self.elevStick.getY(0))
        self.elevCimTwo.set(self.elevStick.getY(0))

    def emergencyStop(self):
        pass
