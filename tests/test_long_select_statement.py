from utils import run_script


def test_prints_all_rows_in_multi_level_tree():
    script = [f"insert {i} user{i} person{i}@example.com" for i in range(1, 16)]
    script += ["select", ".exit"]

    result = run_script(script)

    # In Ruby, result[15...result.length] means: from index 15 to the end
    # So we slice from index 15 onward in Python too.
    expected_output = [
        "db > (1, user1, person1@example.com)",
        "(2, user2, person2@example.com)",
        "(3, user3, person3@example.com)",
        "(4, user4, person4@example.com)",
        "(5, user5, person5@example.com)",
        "(6, user6, person6@example.com)",
        "(7, user7, person7@example.com)",
        "(8, user8, person8@example.com)",
        "(9, user9, person9@example.com)",
        "(10, user10, person10@example.com)",
        "(11, user11, person11@example.com)",
        "(12, user12, person12@example.com)",
        "(13, user13, person13@example.com)",
        "(14, user14, person14@example.com)",
        "(15, user15, person15@example.com)",
        "Executed.",
        "db >",
    ]

    assert result[15:] == expected_output
