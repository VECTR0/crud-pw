import pytest


def xd(word):
    word.split('f')


@pytest.fixture(autouse=True)
def fixture():
    print('SET UP przed kazym testem')
#
# test -> nazwa funkcji: test_*
#


def test_lene():
    assert len('minimalnie')+1 == len('precyzyjnie')
    assert len('minimalnie') == len('precyzyjni')

# eksepszyn


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(AttributeError):
        xd(44)

# pokolei wszystkie dane do funkcji


@pytest.mark.parametrize("first,second,roznica", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_minus(first, second, roznica):
    assert first-second == roznica
