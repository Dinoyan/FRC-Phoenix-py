import wpilib
import robot_map
from navx import AHRS

class sensorHandler():

	def __init__(self):
		self.leftEnc = wpilib.Encoder(robot_map.LEFT_ENC_ONE, robot_map.LEFT_ENC_TWO, True, wpilib.Encoder.EncodingType.k4X)
		self.rightEnc = wpilib.Encoder(robot_map.RIGHT_ENC_ONE, robot_map.RIGHT_ENC_TWO, True, wpilib.Encoder.EncodingType.k4X)
		self.elevatorEnc = wpilib.Encoder(robot_map.ELEVATOR_ENC_ONE, robot_map.ELEVATOR_ENC_TWO, False, wpilib.Encoder.EncodingType.k4X)
		self.ahrs = AHRS.create_i2c()


	def driveEncReset(self):
		self.leftEnc.reset()
		self.rightEnc.reset()

	def elevEncReset(self):
		self.elevatorEnc.reset()

	def navxReset(self):
		self.ahrs.reset()

	def getAhrs(self):
		return self.ahrs

	def getCurrentAngle(self):
		return ahrs.getAngle()

	def getLeftDistance(self):
		return self.rightEnc.getDistance()

	def getRightDistance(self):
		return self.leftEnc.getDistance()

	def getElevDistance(self):
		return self.elevatorEnc.getDistance()

	def getElevSwitchOneStatus(self):
		pass

	def getElevSwitchTwoStatus(self):
		pass
	