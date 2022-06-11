def substring(large_str, potential_substr):
    if len(potential_substr) < 1:
        return True
    for i in range(len(large_str)):
        large_str_idx, j = i, 0
        while j < len(potential_substr) and large_str_idx < len(large_str) and large_str[large_str_idx] == potential_substr[j]:
            j += 1
            large_str_idx += 1
        if j + 1 == len(potential_substr):
            return True
    return False