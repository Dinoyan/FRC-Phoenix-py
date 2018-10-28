import robot_constant
import auto_actions


class AutonomousModeHandler():

    def __init__(self, drivetrain, sensors, elevator, intake):
        self.sensors = sensors
        self.drivetrain = drivetrain
        self.elevator = elevator
        self.intake = intake

    def AutoModeSelect(self, position, gameData):

        if (position == robot_constant.LEFT_POS):

            if (gameData[1] == 'L'):
                auto_actions.driveForward(self.drivetrain, self.sensors, 10);
                auto_actions.turnRight(self.drivetrain, self.sensors, 45);
                auto_actions.driveForward(self.drivetrain, self.sensors, 2);
                auto_actions.liftCubeScale(self.elevator);
                auto_actions.dropCube(self.intake);

            else:
                auto_actions.driveForward(self.drivetrain, self.sensors, 5);


        elif(position == robot_constant.RIGHT_POS):
            if (gameData[1] == 'R'):
                auto_actions.driveForward(self.drivetrain, self.sensors, 10);
                auto_actions.turnLeft(self.drivetrain, self.sensors, 45);
                auto_actions.driveForward(self.drivetrain, self.sensors, 2);
                auto_actions.liftCubeScale(self.elevator);
                auto_actions.dropCube(self.intake);
            else:
                auto_actions.driveForward(self.drivetrain, self.sensors, 5);

        elif(position == robot_constant.LEFT_POS):
            if (gameData[0] == 'L'):
                auto_actions.driveForward(self.drivetrain, self.sensors, 2);
                auto_actions.turnLeft(self.drivetrain, self.sensors, 45);
                auto_actions.driveForward(self.drivetrain, self.sensors, 2);
                auto_actions.turnRight(self.drivetrain, self.sensors, 0);
                auto_actions.driveForward(self.drivetrain, self.sensors, 2);
                auto_actions.liftCubeSwitch(self.elevator);
                auto_actions.dropCube(self.intake);
           
            else:
                pass

        else:
            pass
