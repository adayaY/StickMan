from pynput.mouse import Listener

def is_near_joint(joint, click_x, click_y, radius=10):
    # מחשב מרחק או ריבוע מרחק בין נקודת הלחיצה למרכז המפרק
    distance_squared = (joint.x - click_x)**2 + (joint.y - click_y)**2
    return distance_squared < radius**2

# הפונקציה סורקת את כל העצמות ומחזירה את העצם שה-child_joint שלה נלחץ.
def find_bone_by_joint(skeleton, click_x, click_y, radius=10):
    # עובר על כל האיברים (Arms, Legs)
    for limb_name, limb in skeleton.limbs.items():
        # בודק את עצם ה-Lower (זווית מרפק/ברך)
        if is_near_joint(limb.lower.child_joint, click_x, click_y, radius):
            # אם לחצו על מפרק הקצה (יד/רגל), משנים את זווית עצם ה-Lower
            return limb.lower

        # בודק את עצם ה-Upper (זווית כתף/ירך)
        # שימו לב: מפרק אמצעי הוא ה-child_joint של ה-upper bone
        if is_near_joint(limb.upper.child_joint, click_x, click_y, radius):
            # אם לחצו על המרפק/ברך, משנים את זווית עצם ה-Upper
            return limb.upper

    # ניתן גם לבדוק את עצם הבטן (stomach)
    if is_near_joint(skeleton.stomach.get_end_joint(), click_x, click_y, radius):
        return skeleton.stomach

    return None # לא נמצאה עצם רלוונטית

