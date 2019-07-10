from sike_strat_draw import drawer
import random

if __name__ == "__main__":
    """ This example has no mathematical background and just shows some features of the module """
    dw = drawer.Drawer()
    dw.init_drawing()

    dw.save_point(0, 0)
    for i in range(5):
        isogeny = bool(random.getrandbits(1))
        if isogeny:
            dw.draw_isogeny()
        else:
            dw.draw_doubling()
    dw.draw_final_dot()

    dw.restore_point(0, 0)
    for i in range(5):
        isogeny = bool(random.getrandbits(1))
        if isogeny:
            dw.draw_isogeny()
        else:
            dw.draw_doubling()
    dw.draw_final_dot()

    dw.end_tree()

    dw.save_drawing()

    dw.end_drawing()
