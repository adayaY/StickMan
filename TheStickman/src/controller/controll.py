from pynput.mouse import Listener
from mouse_pos import find_bone_by_joint

with Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()