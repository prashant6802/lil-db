import subprocess

def run_script(commands):
    """Run the compiled C database binary and capture its output lines."""
    process = subprocess.Popen(
        ['./main.exe'],  # use './main' on Linux/Mac
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate('\n'.join(commands) + '\n')
    return [line.strip() for line in stdout.strip().split('\n') if line.strip()]


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