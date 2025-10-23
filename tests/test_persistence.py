from utils import run_script

def test_persistence():
    # Step 1: insert and exit
    result1 = run_script([
        "insert 1 user1 person1@example.com",
        ".exit",
    ])
    assert "Executed." in result1[-2]

    # Step 2: reopen DB and select
    result2 = run_script([
        "select",
        ".exit",
    ])
    assert "(1, user1, person1@example.com)" in result2[0]
