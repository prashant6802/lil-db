from utils import run_script


def test_print_3_leaf_node_btree_structure():
    # Generate insert commands for 1..14
    script = [f"insert {i} user{i} person{i}@example.com" for i in range(1, 15)]
    # Add tree inspection and one more insert
    script += [
        ".btree",
        "insert 15 user15 person15@example.com",
        ".exit",
    ]

    result = run_script(script)

    expected = [
        "db > Tree:",
        "- internal (size 1)",
        "- leaf (size 7)",
        "- 1",
        "- 2",
        "- 3",
        "- 4",
        "- 5",
        "- 6",
        "- 7",
        "- key 7",
        "- leaf (size 7)",
        "- 8",
        "- 9",
        "- 10",
        "- 11",
        "- 12",
        "- 13",
        "- 14",
        "db > Executed.",
        "db >",
    ]

    # The original Ruby test compares only from the 15th line onward
    assert result[14:] == expected
