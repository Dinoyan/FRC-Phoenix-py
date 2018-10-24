import math
import wpilib
import os.path
import pickle

import pathfinder as pf

class AutoPath():

	WHEEL_DIAMETER = 0.5 # 6 inches
	ENCODER_COUNTS_PER_REV = 256

	MAX_VELOCITY = 6 #ft/s
	MAX_ACCELERATION = 5

	def __init__(self, sensors, drivetrain):
		self.sensors = sensors
		self.drivetrain = drivetrain


	def path_init(self):

		# Set up the trajectory
        points = [
            pf.Waypoint(0, 0, 0),
            pf.Waypoint(6, -6, 0),
            pf.Waypoint(11, -6, 0),
            pf.Waypoint(8, 0, math.radians(-90)),
            #pf.Waypoint(23.5, 8, 0),

        ]
        
        info, trajectory = pf.generate(points, pf.FIT_HERMITE_CUBIC, pf.SAMPLES_HIGH,
                                       dt=self.getPeriod(),
                                       max_velocity=self.MAX_VELOCITY,
                                       max_acceleration=self.MAX_ACCELERATION,
                                       max_jerk=120.0)

           # because of a quirk in pyfrc, this must be in a subdirectory
        # or the file won't get copied over to the robot
        pickle_file = os.path.join(os.path.dirname(__file__), 'trajectory.pickle')

        if wpilib.RobotBase.isSimulation():
            # generate the trajectory here

            # and then write it out
            with open(pickle_file, 'wb') as fp:
                pickle.dump(trajectory, fp)
        else:
             with open('fname', 'rb') as fp:
                    trajectory = pickle.load(fp)

        # Wheelbase Width = 2 ft
        modifier = pf.modifiers.TankModifier(trajectory).modify(2.0)

        # Do something with the new Trajectories...
        left = modifier.getLeftTrajectory()
        right = modifier.getRightTrajectory()
        
        leftFollower = pf.followers.EncoderFollower(left)
        leftFollower.configureEncoder(self.l_encoder.get(), self.ENCODER_COUNTS_PER_REV, self.WHEEL_DIAMETER)
        leftFollower.configurePIDVA(1.0, 0.0, 0.0, 1 / self.MAX_VELOCITY, 0)
        
        rightFollower = pf.followers.EncoderFollower(right)
        rightFollower.configureEncoder(self.r_encoder.get(), self.ENCODER_COUNTS_PER_REV, self.WHEEL_DIAMETER)
        rightFollower.configurePIDVA(1.0, 0.0, 0.0, 1 / self.MAX_VELOCITY, 0)
        
        self.leftFollower = leftFollower
        self.rightFollower = rightFollower


	def run(self):


