import joint
import math
class Bone:
    def __init__(self, name, parent_joint, length, angle=0):
        self.name = name
        self.parent_joint = parent_joint
        self.length = length
        self.angle = angle
        self.child_joint = None   # נוסיף בהמשך

    #יחזיר לך את נקודת הציר ההתחלתית של
    # החלק העליון או התחתון של היד או הרגל 
    #החלק שקרוב יותר למרכז הגוף
    def get_start_point(self):
        return(self.parent_joint)
    
    #יחזיר את הנקודה הסופית של החלק המסויים באיבר
    def get_end_Point():
        