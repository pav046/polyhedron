# !/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ["simple_1"]:   # "ccc", "cube", "box", "king", "cow"
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        for l in range(2):
            Polyedr(f"data/{name}.geom", l).draw(tk, l)
        print()
        delta_time = time() - start_time
        print(f"Изображение полиэдра и нахождение"
              f" периметра проекций '{name}' заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")
except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()