from pytest import approx
from shadow.polyedr import Polyedr


class TestPerimetr:

    def test_simple_1(self):
        a = Polyedr(f"data/simple_1.geom", 1)
        a.draw(None, 1)
        assert a.P == approx(0.0)

    def test_simple_2(self):
        a = Polyedr(f"data/simple_2.geom", 1)
        a.draw(None, 1)
        assert a.P == approx(15.03224)

    def test_box_simple(self):
        a = Polyedr(f"data/box_simple.geom", 1)
        a.draw(None, 1)
        assert a.P == approx(4.0)