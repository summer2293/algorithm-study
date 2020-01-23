def valid_skill_trees(skill, skill_trees):
    counter = 0
    for trees in skill_trees:
        pre_skill = ''
        for skill_tree in trees:
            if skill_tree in skill:
                pre_skill += skill_tree
        if skill.startswith(pre_skill):
            counter += 1
    return counter
        
    

def test_valid_skill_trees():
    assert valid_skill_trees("CBD", ["BACDE", "CBADF", "AECB", "BDA"]) == 2