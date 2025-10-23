from utils import run_script


def test_table_full_error():
    # Prepare 1401 insert commands
    script = [f"insert {i} user{i} person{i}@example.com" for i in range(1, 1402)]
    script.append(".exit")

    result = run_script(script)

    # The second-to-last line should contain the table full error
    assert result[-2] == "db > Error: Table full."
