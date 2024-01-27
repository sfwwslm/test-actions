from src import t, f


class Testa:
    def test_smoke(self):
        assert t() is True

    def test_smoke2(self):
        assert f() is False
