from bowling import bowling

def test_all_strikes():
    assert bowling("X|X|X|X|X|X|X|X|X|X||XX") == 300
