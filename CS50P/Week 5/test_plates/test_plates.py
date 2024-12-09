from plates import is_valid

def test_begintwoletters():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5") == False


def test_length():
    assert is_valid("AER134")== True
    assert is_valid("C")== False
    assert is_valid("ARI3040")==False
    assert is_valid("CS")==True


def test_num():
    assert is_valid("CS50")== True
    assert is_valid("CS050")== False
    assert is_valid("CS5S0")== False

def test_punct():
    assert is_valid("CS_50")== False



