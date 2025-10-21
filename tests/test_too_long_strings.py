import subprocess

def run_script(commands):
    """Run the compiled C database binary and capture its output lines."""
    process = subprocess.Popen(
        ['./main.exe'],  # use './db' on Linux/Mac
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate('\n'.join(commands) + '\n')
    return [line.strip() for line in stdout.strip().split('\n') if line.strip()]


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
