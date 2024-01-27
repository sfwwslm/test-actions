from src import t, f
import pytest


@pytest.mark.smoke
class Testa:
    def test_smoke(self):
        assert t(), True

    def test_smoke2(self):
        assert f(), True
