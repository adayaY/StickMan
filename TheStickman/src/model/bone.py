from joint import Joint
import math
class Bone:
    """
    מייצגת עצם בסטיקמן. כל עצם מחוברת למפרק אחד ויוצאת ממנו בזווית מסוימת ובאורך קבוע.

    Attributes:
        name (str): שם העצם (לוגי בלבד, לצורכי זיהוי).
        parent_joint (Joint): המפרק שממנו העצם מתחילה.
        length (float): האורך של העצם בפיקסלים.
        angle (float): הזווית הנוכחית של העצם במעלות.
        child_joint:המפרק שבו העצם מסתיימת.
    """

    def __init__(self, name, parent_joint, length, angle):
        self.name = name
        self.parent_joint = parent_joint
        self.length = length
        self.angle = angle
        self.child_joint = None   # נוסיף בהמשך

    #יחזיר לך את נקודת הציר ההתחלתית של
    # החלק העליון או התחתון של היד או הרגל 
    #החלק שקרוב יותר למרכז הגוף
    def get_bone_start(self):
        return self.parent_joint
    
    def set_angle(self, new_angle):
        self.angle=new_angle
        
    # יחזיר את הנקודה הסופית של החלק המסויים באיבר
    def get_bone_end(self):
        # אם אין child_joint, נחשב וניצור אותו
        if self.child_joint is None:
            self.get_end_joint()
        return self.child_joint
    
    #פונ עזר לחישוב מיקום סופי של המפרק הסופי של העצם
    def calculate_end_joint_position(self):
        x0 = self.parent_joint.x
        y0 = self.parent_joint.y

        rad = math.radians(self.angle) # המרת זווית לראדיאנים
        x_end = x0 + math.cos(rad) * self.length
        y_end = y0 + math.sin(rad) * self.length

        if self.child_joint is None:
            # יצירת מפרק חדש אם הוא לא קיים
            self.child_joint = Joint(f"{self.name}_end", x_end, y_end, self.angle)
        else:
            # עדכון מפרק קיים
            self.child_joint.x = x_end
            self.child_joint.y = y_end
    
    #כמו הפונקצייה הקודמת אבל רק עם חישוב לפי אורך עצם וזווית בראדיאנים
    def get_end_joint(self):
        
        return self.calculate_end_joint_position()
    
    
    def update_angle_and_chain(self, new_angle):
        self.set_angle(new_angle)

        # הפעלת חישוב המיקום החדש למפרק הסופי של העצם הזו
        self.calculate_end_joint_position() 

        # אם יש עצם נוספת שמחוברת למפרק הסופי הזה (כמו lower bone), צריך לעדכן גם אותה.
        # זה דורש לוגיקה ב-Limb או ב-Stickman שתטפל בשרשור.
        # כרגע, בגלל מבנה ה-Limb שלך, נסתפק בקריאה לפונקציית העדכון של ה-Limb:
        # (מניח ש-drag.py ידאג לקרוא ל-limb.update_joints_position() לאחר השינוי)