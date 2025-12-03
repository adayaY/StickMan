from limb import Limb
from bone import Bone
from joint import Joint
from head import Head

class Stickman:
    def __init__(self):

        # מפרק מרכזי של צוואר
        #ומפה תתחיל להצטייר הדמות
        #
        self.core = Joint("core/neck", x=200, y=200)
        #בנייה של הקו המייצג את הבטן
        self.stomach = Bone("stomach",base_joint = self.core ,length = 60 ,angel =  270 )
        # הראש יכול להיות עצם אחת
        self.head = Head( self.core)

        # איברים
        self.limbs = {
            "right_arm": Limb("right_arm", self.core, 40, 35),
            "left_arm": Limb("left_arm", self.core, 40, 35),
            "right_leg": Limb("right_leg", self.stomach.get_end_joint(), 50, 45),
            "left_leg": Limb("left_leg", self.stomach.get_end_joint(), 50, 45),
        }