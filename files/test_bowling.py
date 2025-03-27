from bowling import bowling

def test_all_strikes():
    assert bowling("X|X|X|X|X|X|X|X|X|X||XX") == 300
    
def test_strikes_and_numbers():
    assert bowling("X|X||X|X|X|X|X|X|X||X6") == 296
