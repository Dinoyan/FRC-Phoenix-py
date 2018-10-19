import wpilib
import logging
import drivetrain
import elevator
import intake
import joystick_handler
import robot_constant
import sensor_handler
import autonomous_mode_handler
from wpilib.drive import DifferentialDrive


class MyRobot(wpilib.IterativeRobot):
    '''Main robot class'''

    def robotInit(self):
        '''Robot-wide initialization code should go here'''
        self.drivetrain = drivetrain.Drivetrain()
        self.sensors = sensor_handler.sensorHandler()
        self.joystick = joystick_handler.JoystickHandler()
        self.elevator = elevator.Elevator()
        self.intakeHandler = intake.Intake(self.sensors, self.joystick)
        self.auto = Autonomous_mode_handler.AutonomousModeHandler(
            self.drivetrain, self.sensors, self.elevator, self.intakeHandler)

        self.chooser = wpilib.SendableChooser()
        self.chooser.addObject('center', 'robot_constant.CENTER_POS')
        self.chooser.addObject('left', 'robot_constant.LEFT_POS')
        self.chooser.addObject('right', 'robot_constant.RIGHT_POS')
        self.chooser.addObject('default', 'robto_constant.DEFAULT')
        wpilib.SmartDashboard.putData('Auto Mode', self.chooser)

        logging.basicConfig(filename = 'robotLogs.log', level=logging.DEBUG)
        logging.info("Init robot")


    def autonomousInit(self):
        '''Called only at the beginning of autonomous mode'''
        self.sensors.driveEncReset()
        self.sensors.elevEncReset()

        self.value = self.chooser.getSelected()
        self.gameData = wpilib.DriverStation.getInstance().getGameSpecificMessage()

        logging.info("Auto init")

    def autonomousPeriodic(self):
        '''Called every 20ms in autonomous mode'''
        if(wpilib.RobotState.isAutonomous()):
            self.auto.AutoModeSelect(self.value, self.gameData)

    def disabledInit(self):
        '''Called only at the beginning of disabled mode'''
        pass

    def disabledPeriodic(self):
        '''Called every 20ms in disabled mode'''
        pass

    def teleopInit(self):
        '''Called only at the beginning of teleoperated mode'''

        logging.info("Teleop init")

    def teleopPeriodic(self):
        '''Called every 20ms in teleoperated mode'''

        if(wpilib.RobotState.isOperatorCOntrol()):
            self.drivetrain.driveRobot()
            self.intakeHandler.operateIntake()
            self.elevator.operateElevator()

    def updateDashboard(self):
        pass


if __name__ == '__main__':
    wpilib.run(MyRobot)
