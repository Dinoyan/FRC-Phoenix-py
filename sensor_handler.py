import wpilib
import robot_map

class sensorHandler():

	def __init__(self):
		self.leftEnc = wpilib.Encoder(robot_map.LEFT_ENC_ONE, robot_map.LEFT_ENC_TWO, True, wpilib.Encoder.EncodingType.k4X)
		self.rightEnc = wpilib.Encoder(robot_map.RIGHT_ENC_ONE, robot_map.RIGHT_ENC_TWO, True, wpilib.Encoder.EncodingType.k4X)
		self.elevatorEnc = wpilib.Encoder(robot_map.ELEVATOR_ENC_ONE, robot_map.ELEVATOR_ENC_TWO, False, wpilib.Encoder.EncodingType.k4X)


	def driveEncReset(self):
		self.leftEnc.reset()
		self.rightEnc.reset()

	def elevEncReset(self):
		self.elevatorEnc.reset()

	def navxReset(self):
		pass

	def getAhrs(self):
		pass

	def getLeftDistance(self):
		pass

	def getRightDistance(self):
		pass

	def getElevDistance(self):
		pass

	def getElevSwitchOneStatus(self):
		pass

	def getElevSwitchTwoStatus(self):
		pass
	