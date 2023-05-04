from shared.image import SharedImage
from shared.value import SharedValue
from interfaces.motors import PublisherMotors

import cv2

# Define HAL functions
class HALFunctions:
    def __init__(self):
        # Initialize image variable
        self.shared_image = SharedImage("guiimage")
        self.shared_v = SharedValue("velocity")
        self.shared_w = SharedValue("angular")
        self.take_off = SharedValue("takeoff")
        self.landing = SharedValue("land")
        self.pausing = SharedValue("stop")
        self.motors = PublisherMotors("/cmd_vel", 4, 0.3)
        
    # Get image function
    def getImage(self):
        image = self.shared_image.get()
        return image

    # Send velocity function
    def sendV(self, velocity):
        self.shared_v.add(velocity)

    # Send angular velocity function
    def sendW(self, angular):
        self.shared_w.add(angular)
        
    # Send velocity function
    def takeoff(self):
        self.motors.takeoff()
        self.take_off.add(1)

    # Send angular velocity function
    def pause(self):
        self.motors.pause()
        self.pausing.add(2)
    
    def land(self):
        self.motors.land()
        self.landing.add(3)

# Define GUI functions
class GUIFunctions:
    def __init__(self):
        # Initialize image variable
        self.shared_image = SharedImage("guiimage")

    # Show image function
    def showImage(self, image):
        # Reshape to 3 channel if it has only 1 in order to display it
        if (len(image.shape) < 3):
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        self.shared_image.add(image)