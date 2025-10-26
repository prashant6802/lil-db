from utils import run_script

def test_duplicate_id_error():
    script = [
        "insert 1 user1 person1@example.com",
        "insert 1 user1 person1@example.com",
        "select",
        ".exit",
    ]

    result = run_script(script)

    expected = [
        "db > Executed.",
        "db > Error: Duplicate key.",
        "db > (1, user1, person1@example.com)",
        "Executed.",
        "db >",
    ]

    assert result == expected
