from impresso.structures import AND, OR


def test_and_or_chain():
    a = AND("apple", "banana")
    b = OR("one", "two")
    c = AND("red", "green")

    abc = a & b & c

    print(abc, abc.chain)
    assert abc.chain == [b, a]
    assert set(abc) == set(c)
