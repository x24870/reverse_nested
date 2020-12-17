def reverse_nested(nested_input):
    if not any(nested_input) or not isinstance(nested_input, dict):
        return nested_input

    key = next(iter(nested_input))
    val = nested_input[key]
    sub_dict = reverse_nested(val)

    if not isinstance(sub_dict, dict):
        return {sub_dict: key}
    else:
        # find the Innermost dictionary
        innermost_dict = sub_dict
        while 1:
            ret_key = next(iter(innermost_dict))
            ret_val = innermost_dict[ret_key]
            if not isinstance(ret_val, dict): break
            innermost_dict = ret_val

        # replace innermost dictionary value to new dictionary
        innermost_key = next(iter(innermost_dict))
        innermost_val = innermost_dict[innermost_key]
        innermost_dict[innermost_key] = {innermost_val: key}
        return sub_dict