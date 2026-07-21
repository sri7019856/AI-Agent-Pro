def test_uppercase():
    assert "agent".upper() == "AGENT"


def test_lowercase():
    assert "AI".lower() == "ai"


def test_strip():
    assert "  hello  ".strip() == "hello"
