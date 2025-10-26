from utils import run_script


def test_prints_structure_of_one_node_btree():
    # Build insert commands for 3, 1, 2
    script = [
        "insert 3 user3 person3@example.com",
        "insert 1 user1 person1@example.com",
        "insert 2 user2 person2@example.com",
        ".btree",
        ".exit",
    ]

    result = run_script(script)

    expected = [
        "db > Executed.",
        "db > Executed.",
        "db > Executed.",
        "db > Tree:",
        "leaf (size 3)",
        "- 0 : 1",
        "- 1 : 2",
        "- 2 : 3",
        "db >",
    ]

    assert result == expected
