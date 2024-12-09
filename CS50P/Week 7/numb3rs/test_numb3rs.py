from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1")== True
    assert validate("dog")==False
    assert validate("555.4.2.0")==False
    assert validate("4.555.2.0")==False
    assert validate("4.2.555.0")==False
    assert validate("4.2.0.555")==False
    assert validate("555.555.555.555")==False
