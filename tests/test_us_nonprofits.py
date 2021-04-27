import requests
import pytest
from us_nonprofits import __version__
from us_nonprofits.constants import REGIONS


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.parametrize("url", REGIONS.values())
def test_eobmf_data_sources(url):
    r = requests.get(url)
    assert 200 == r.status_code
