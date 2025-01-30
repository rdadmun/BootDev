def deduplicate_lists(lst1, lst2, reverse=False):
    combined = lst1 +lst2
    uniques = list(set(combined))
    return sorted(uniques, reverse=reverse)

# OR

def deduplicate_oneline(lst1, lst2, reverse = False):
    return sorted(set(lst1 + lst2, reverse=reverse))