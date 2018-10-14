import wpilib
import robot_map
import Joystick_handler

class Drivetrain():

	def __init__(self):
		self.l_motor1 = wpilib.Talon(robot_map.LEFT_DRIVE1)
		self.l_motor2 = wpilib.Talon(robot_map.LEFT_DRIVE2)
		self.r_motor1 = wpilib.Talon(robot_map.RIGHT_DRIVE1)
		self.r_motor2 = wpilib.Talon(robot_map.RIGHT_DRIVE2)
		self.driveStick = Joystick_handler.JoystickHandler().getDriveStick()


	def driveRobot(self):
		right = self.driveStick.getRawAxis(5)
		left = self.driveStick.getRawAxis(1)

		self.moveRobot(left, right)


	def moveRobot(self, leftSpeed, rightSpeed):

		self.l_motor1.set(leftSpeed)
		self.l_motor2.set(leftSpeed)

		self.r_motor1.set(rightSpeed)
		self.r_motor2.set(rightSpeed)


	def autoMove(self):
		pass

		
