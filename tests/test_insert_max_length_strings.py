from utils import run_script


def test_allows_inserting_max_length_strings():
    long_username = "a" * 32
    long_email = "a" * 255

    script = [
        f"insert 1 {long_username} {long_email}",
        "select",
        ".exit",
    ]

    result = run_script(script)

    expected = [
        "db > Executed.",
        f"db > (1, {long_username}, {long_email})",
        "Executed.",
        "db >",
    ]

    assert result == expected
