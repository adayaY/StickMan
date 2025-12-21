import pygame

"""הפונגציה מקבלת שלושה פרמטרים
 self התייחסות לאובייקט הנוכחי של המחלקה 
 , key_event האובייקט מכיל את המידע של מה שקרה במקלדת 
ו model אוביקט מסוג StickMan שעליו ארצה לפקוד כלומר לשנות את זויותיו לפי הערך שקיבלתי מהמקלדת """

class InputHandler:
    def handle_key(self,key_event,model:'StickMan'):
     if key_event.type==pygame.KEYDOWN:
        if key_event.key==pygame.K_a:
            current_angle=model.get_joint_angle("right_elbow")
            new_angle=current_angle+5
            model.set_joint_angle('right_elbow',new_angle)

        elif          key_event.key==pygame.K_d :
            current_angle=model.get_joint_angle("left_elbow")
            new_angle=current_angle+5
            model.set_joint_angle('left_elbow',new_angle)






#get_joint_angle  פונגציה ממחלקת model  שמקבלת מחרוזת שמייצגת את שם המפרק ומחזירה במספר את הזוית הנוכחית שהמפרק נמצא בה כרגע
#model.set_joint_angle פונגציה ממחלקת model שמשנה את הזוית הנוכחית