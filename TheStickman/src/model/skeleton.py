from limb import Limb
from bone import Bone
from joint import Joint

class Stickman:
    def __init__(self):

        # מפרק מרכזי של בטן
        self.core = Joint("core", x=200, y=200)

        # הראש יכול להיות עצם אחת
        self.head = Bone("head", self.core, length=30)

        # איברים
        self.limbs = {
            "right_arm": Limb("right_arm", 40, 35),
            "left_arm": Limb("left_arm", 40, 35),
            "right_leg": Limb("right_leg", 50, 45),
            "left_leg": Limb("left_leg", 50, 45),
        }
