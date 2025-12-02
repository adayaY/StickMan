from bone import Bone
from joint import Joint

class Limb:
    def __init__(self, name, length_upper, length_lower):
        self.name = name
        
        # מפרקים
        self.joint_start = Joint(name + "_start")
        self.joint_mid = Joint(name + "_mid")
        self.joint_end = Joint(name + "_end")
        
        # עצמות
        self.upper = Bone(name + "_upper", self.joint_start, length_upper)
        self.lower = Bone(name + "_lower", self.joint_mid, length_lower)
        
        # קישורים לוגיים
        self.upper.child_joint = self.joint_mid
        self.lower.child_joint = self.joint_end
    
    def get_start_joint():
        return           
