import subprocess

def run_script(commands):
    """
    Run the database binary and feed it a list of commands (like insert/select/.exit).
    Capture and return the output as a list of lines.
    """
    process = subprocess.Popen(
        ['./main.exe', "test.db"],  # path to your compiled C database program
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Join commands into one string separated by newlines
    script_input = '\n'.join(commands) + '\n'
    stdout, stderr = process.communicate(script_input)

    # Split output into clean lines
    lines = [line.strip() for line in stdout.strip().split('\n')]
    return lines