import wpilib
import Joystick_handler
import robot_map

class Intake():

	def __init__(self):
		self.openIntake = wpilib.Solenoid(robot_map.OPEN_INTAKE)
		self.closeIntake = wpilib.Solenoid(robot_map.CLOSE_INTAKE)

		self.rightIntake = wpilib.Talon(robot_map.RIGHT_INTAKE)
		self.leftIntake = wpilib.Talon(robot_map.LEFT_INTAKE)


	def operateIntake(self):
		pass


	def vomitCube(self):
		self.controlIntakeMotors(-0.5)

	def dropIntake(self):
		pass

	def controlIntakeSolenoids(state):
		self.operateIntake.set(state)
		self.closeIntake.set(!state)

	def controlIntakeMotors(speed):
		self.rightIntake.set(speed)
		self.leftIntake.set(-speed)


