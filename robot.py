import wpilib
import drivetrain
import elevator
import sensor_handler
from wpilib.drive import DifferentialDrive

class MyRobot(wpilib.IterativeRobot):
    '''Main robot class'''


    def robotInit(self):
        '''Robot-wide initialization code should go here'''
        self.drivetrain = drivetrain.Drivetrain()
        self.sensors = sensor_handler.sensorHandler()

        # object that handles basic drive operations


    def autonomousInit(self):
        '''Called only at the beginning of autonomous mode'''
        self.sensors.driveEncReset()
        self.sensors.elevEncReset()

    def autonomousPeriodic(self):
        '''Called every 20ms in autonomous mode'''

    def disabledInit(self):
        '''Called only at the beginning of disabled mode'''
        pass
            
    def disabledPeriodic(self):
        '''Called every 20ms in disabled mode'''
        pass

    def teleopInit(self):
        '''Called only at the beginning of teleoperated mode'''
        self.drivetrain.driveRobot()


    def teleopPeriodic(self):
        '''Called every 20ms in teleoperated mode'''
        

if __name__ == '__main__':
    wpilib.run(MyRobot)
