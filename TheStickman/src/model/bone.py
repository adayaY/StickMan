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
    def get_end_Point(self):
        return(self.child_joint)
    
    #
    def get_end_Point2(self):
        x0, y0 = self.get_start()
        # חישוב פשוט: נקודת הקצה לפי אורך וזווית
        rad = math.radians(self.angle) #המרת זווית לראדיאנים
        x_end = x0 + math.cos(rad) * self.length
        y_end = y0 + math.sin(rad) * self.length
        return (x_end, y_end)