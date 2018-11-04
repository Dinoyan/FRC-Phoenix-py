import wpilib
import robot_map


class Intake():

    def __init__(self, sensors, joystick):
        self.openIntake = wpilib.Solenoid(robot_map.OPEN_INTAKE)
        self.closeIntake = wpilib.Solenoid(robot_map.CLOSE_INTAKE)

        self.rightIntake = wpilib.Talon(robot_map.RIGHT_INTAKE)
        self.leftIntake = wpilib.Talon(robot_map.LEFT_INTAKE)

        self.sensors = sensors
        self.joystick = joystick

        self.pdp = wpilib.PowerDistributionPanel()

    def operateIntake(self):

        if (self.joystick.getCubeStick().getRawButton(1)):
            controlIntakeSolenoids(True)
        elif(self.joystick.getCubeStick().getRawButton(2)):
            controlIntakeSolenoids(False)

        if (self.joystick.getDriveStick().getRawAxis(2) > 0.3):
            controlIntakeSolenoids(True)
        else:
            controlIntakeSolenoids(False)

        while (self.joystick.getCubeStick().getRawButton(6) == True):
            controlIntakeMotors(-0.3)

        if(self.joystick.getDriveStick().getRawButton(3) > 0.1):
            controlIntakeMotors(
                self.joystick.getDriveStick().getRawAxis(3) - 0.3)

            if (self.pdp.getCurrent(3) > 15.5 or self.pdp..getCurrent(13) > 14.5):
                controlIntakeMotors(0)
                controlIntakeSolenoids(True)

        elif(self.joystick.getCubeStick().getRawAxis(2) > 0.1):
            controlIntakeMotors(
                (-self.joystick.getCubeStick().getRawAxis(2)) - 0.5)

        else:
            controlIntakeMotors(0)

    def vomitCube(self):
        self.controlIntakeMotors(-0.5)

    def dropIntake(self):
        pass

    def controlIntakeSolenoids(state):
        self.operateIntake.set(state)
        self.closeIntake.set(not state)

    def controlIntakeMotors(speed):
        self.rightIntake.set(speed)
        self.leftIntake.set(-speed)
