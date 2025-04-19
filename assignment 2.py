class Device:
    def move(self):
        print("Device is moving...")

class Drone(Device):
    def move(self):
        print("Drone is flying through the air 🚁")

class RobotVacuum(Device):
    def move(self):
        print("Robot Vacuum is cleaning the floor 🤖🧹")

class SmartWatch(Device):
    def move(self):
        print("Smartwatch is tracking your steps ⌚👟")

# Using polymorphism
devices = [Drone(), RobotVacuum(), SmartWatch()]

for device in devices:
    device.move()