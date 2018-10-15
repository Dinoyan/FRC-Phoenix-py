import robot_constant
class AutonomousActions():

	def driveForward(drivetrain, sensors, distance):
		angle1 = sensors.getCurrentAngle() + robot_constant.DRIVE_MAX_ANGLE
		angle2 = sensors.getCurrentAngle() - robot_constant.DRIVE_MAX_ANGLE

		while (sensors.getRigthDistance() < distance):
			curr_angle = sensors.getCurrentAngle
			if (curr_angle > angle1):
				drivetrain.moveRobot(-robot_constant.DRIVE_TURNING_SPEED2, -robot_constant.DRIVE_TURNING_SPEED2)
			elif (curr_angle < angle2):
				drivetrain.moveRobot(RobotConstant.DRIVE_TURNING_SPEED2, RobotConstant.DRIVE_TURNING_SPEED2)
			else:
				rivetrain.moveRobot(RobotConstant.DRIVE_DRIVING_SPEED, -RobotConstant.DRIVE_DRIVING_SPEED)

	def turnRight(drivetrain, sensors, angle):
		pass

	def turnLeft(drivetrain, sensors, angle):
		pass

	def dropCube(intake):
		pass

	def liftCubeSwitch(elev):
		pass

	def liftCubeScale(elev):
		pass

	def dropIntake(intake):
		pass

	def justMove(drivetrain):
