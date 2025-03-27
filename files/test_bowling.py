from bowling import bowling

def test_all_strikes():
    assert bowling("X|X|X|X|X|X|X|X|X|X||XX") == 300
    
def test_strikes_and_numbers():
    assert bowling("X|X|X|X|X|X|X|X|X|X||X6") == 296
    
def test_strikes_and_spares():
    assert bowling("X|X|X|X|X|X|X|X|X|X||4/") == 284
    
def test_miss_and_spare():
    assert bowling("X|X|-/|X|X|X|X|X|X|X||4/") == 254
    
def test_final_combination():
    assert bowling("X|7/|9-|X|-8|8/|-6|X|X|X||81") == 167

    
    
    