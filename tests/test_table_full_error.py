from utils import run_script


def test_table_full_error():
    # Prepare 1401 insert commands
    script = [f"insert {i} user{i} person{i}@example.com" for i in range(1, 1402)]
    script.append(".exit")

    result = run_script(script)

    # Previously: "db > Error: Table full."
    # Now expect the last 2 lines to be:
    # "db > Executed." and "db > Need to implement updating parent after split"

    expected = [
        "db > Executed.",
        "db > Need to implement splitting internal node",
    ]

    assert result[-2:] == expected
