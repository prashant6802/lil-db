from utils import run_script


def test_too_long_strings():
    long_username = "a" * 33
    long_email = "a" * 255

    script = [
        f"insert 1 {long_username} {long_email}",
        "select",
        ".exit",
    ]

    result = run_script(script)

    expected = [
        "db > String is too long.",
        "db > Executed.",
        "db >",
    ]

    assert result == expected
