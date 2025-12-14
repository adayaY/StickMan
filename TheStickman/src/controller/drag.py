import math




def calculate_new_angle(bone, drag_x, drag_y):
    # נקודת הציר/התחלה (parent_joint) של העצם
    x0 = bone.parent_joint.x
    y0 = bone.parent_joint.y

    # חישוב הדלתא ב-X וב-Y
    dx = drag_x - x0
    dy = drag_y - y0

    # שימוש בפונקציית atan2 לחישוב זווית בראדיאנים
    # atan2 מטפל נכון בכל הרביעים (quadrants)
    rad = math.atan2(dy, dx)

    # המרה מראדיאנים למעלות (0-360)
    degrees = math.degrees(rad)

    # נרמול לטווח 0-360 מעלות
    return (degrees + 360) % 360