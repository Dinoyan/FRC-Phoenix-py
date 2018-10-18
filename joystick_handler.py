import wpilib
import robot_map


class JoystickHandler():

    def __init__(self):
        self.driveStick = wpilib.Joystick(robot_map.DRIVE_STICK)
        self.cubeStick = wpilib.Joystick(robot_map.CUBE_STICK)

    def getDriveStick(self):
        return self.driveStick

    def getCubeStick(self):
        return self.cubeStick

    def vibrateDriveStick():
    	self.driveStick.setRumble(RumbleType.kRightRumble, 1)

    def vibrateCubeStick():
    	self.cubeStick.setRumble(RumbleType.kRightRumble, 1)
