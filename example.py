import SIKEStrategyDrawer

if __name__ == "__main__":
    import random

    drawer = SIKEStrategyDrawer.Drawer()

    for i in range(10):
        isogeny = bool(random.getrandbits(1))
        if isogeny:
            drawer.draw_isogeny()
        else:
            drawer.draw_doubling()

    drawer.end_tree()

    drawer.save_drawing()

    drawer.end_drawing()
