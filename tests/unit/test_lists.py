def test_list_length():
    data = [1, 2, 3, 4]
    assert len(data) == 4


def test_append():
    data = []
    data.append("AI")
    assert data == ["AI"]


def test_membership():
    assert "python" in ["java", "python", "c++"]
