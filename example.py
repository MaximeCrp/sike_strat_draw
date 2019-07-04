from sike_strat_draw import drawer
import random

if __name__ == "__main__":

    dw = drawer.Drawer()
    dw.init_drawing()
    
    for i in range(10):
        isogeny = bool(random.getrandbits(1))
        if isogeny:
            dw.draw_isogeny()
        else:
            dw.draw_doubling()

    dw.end_tree()

    dw.save_drawing()

    dw.end_drawing()
