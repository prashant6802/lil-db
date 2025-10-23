from utils import run_script


def test_inserts_and_retrieves_row():
    result = run_script([
        "insert 1 user1 person1@example.com",
        "select",
        ".exit"
    ])

    expected = [
        "db > Executed.",
        "db > (1, user1, person1@example.com)",
        "Executed.",
        "db >"
    ]
    assert result == expected
