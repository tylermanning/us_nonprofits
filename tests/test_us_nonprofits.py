from us_nonprofits import __version__
from us_nonprofits.constants import REGIONS


def test_version():
    assert __version__ == '0.1.0'


def test_regions():
    assert "OTHER" in REGIONS
