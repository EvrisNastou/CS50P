from um import count

def test_count():
    assert count("Um, album.") == 1
    assert count("um") == 1
    assert count("Um, hello, um...") == 2
    assert count("Um?") == 1
