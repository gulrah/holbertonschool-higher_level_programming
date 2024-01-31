def only_diff_elements(set_1, set_2):
    # Use symmetric difference to get elements present in only one set
    return set_1 ^ set_2

# Example usage:
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))
