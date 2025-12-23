import pygame
import math

class InputHandler:
    list_join_pose= ""
    #TODO להשלים את רשימת המפרקים

    """הפונגציה שמטפלת בקלט מהעכבר מקבלת שלושה פרמטרים
     self התייחסות לאובייקט הנוכחי של המחלקה 
     , mouse_event האובייקט מכיל את המידע של מה שקרה בעכבר 
    ו model אוביקט מסוג StickMan שעליו ארצה לפקוד כלומר לשנות את זויותיו לפי הערך שקיבלתי מהמקלדת """

    def handle_mouse(self,mouse_event,model:'StickMan'):
        for event in pygame.event.get(): # שולף את כל האירועים שהתרחשו מאז הפריים הקודם
            if event.type == pygame.MOUSEBUTTONDOWN: # זיהוי לחיצת עכבר
                mouse_click_pos = event.pos # משתנה event.pos של pygame נוצר רק שיש לחיצה מכיל tuple של (x, y)
                self.selected_joint = check_mouse_on_joint(mouse_click_pos, list_join_pose) # check_mouse_on_joint משתנה מסוג אובייקט מפרק ששומר את מה שהפונגציה החזירה

            elif event.type==pygame.MOUSEBUTTONUP: #כלומר ההעבר הפסיק את הלחיצה
             self.selected_joint =None # ברגע שהפסקנו ללחוץ על העכבר נשחרר את האובייקט כלומר המפרק

        if self.selected_joint is not None: # שהמשתנה שונה מNone זה אומר שיש מפרק שצריך להוזיז בהתאם
            self.selected_joint.x, self.selected_joint.y = pygame.mouse.get_pos() # קביעת מיקום המפרק בהתאם למיקום העכבר
# משנה את שדות הx,y של המפרק הנוכחי בהתאם לx,y של העכבר
#pygame.mouse.get_pos זו פונגצה שמחזירה את מיקום העבר בכל פרייםככה שכל תזוזת עכבר תעכדכן את מיקום העכבר


"""פונגציה שמקבלת את מיקום העכבר כלומרר איפה לחץ רשימה של מפרקים ומרחק בטיחות
ובודקם את העבר שלי נמצא על או במרחק של מרחק הבטיחות מהמפרקים שלי
ותחזיר -1 אם העכבר לא לחץ באזור שיש בו מפרים
אחרת תחזיר את המפרק שעליו נמצא העכבר"""

# אני יוצאת מנקודת הנחה שיש לי מערך או רשימה של המפרקים שומרים לי איפה כל מפרק נמצא עכשיו

def check_mouse_on_joint(mouse_click_pos,list_join_pose,safe_dis=10):
      mouse_x=mouse_click_pos.x # הכנסת מיקום העבר לפרמטרים נוחים לעבודה
      mouse_y=mouse_click_pos.y

      for joint in list_join_pose: # מעבר על הרשימה וחילוץ מיקום המפרק
          joint_x=joint.x
          joint_y=joint.y
            # עבור כל מפרק
          distance = math.hypot(mouse_x - joint_x, mouse_y - joint_y) # חישוב המרחק בין מיקון העבר לנק של המפרק פיתורס רגיל

        if distance<=safe_dis: # אם המרחק באמת בתחום הנכון אז נחזיר מיהו המפרק
            return joint
      return None # אחרתצ נחזיר None אם העכבר לא לוחץ בשום מקום
