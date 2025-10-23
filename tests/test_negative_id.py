from utils import run_script


def test_negative_id():

    script = [
        "insert -1 cstack foo@bar.com",
        "select",
        ".exit",
    ]

    result = run_script(script)

    expected = [
        "db > ID must be positive.",
        "db > Executed.",
        "db >"
    ]

    assert result == expected