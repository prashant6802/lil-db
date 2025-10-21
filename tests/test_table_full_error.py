import subprocess

def run_script(commands):
    """Run the database binary and capture its output as a list of lines."""
    process = subprocess.Popen(
        ['./main.exe'],  # or './db' on Linux/Mac
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate('\n'.join(commands) + '\n')
    return [line.strip() for line in stdout.strip().split('\n') if line.strip()]


def test_table_full_error():
    # Prepare 1401 insert commands
    script = [f"insert {i} user{i} person{i}@example.com" for i in range(1, 1402)]
    script.append(".exit")

    result = run_script(script)

    # The second-to-last line should contain the table full error
    assert result[-2] == "db > Error: Table full."
