#################################################################
#File         : NestedObj.py
#Author       : Afsal Ashraf
#Created At   : 01 - 04 - 23
#Description  : Nested Object function where you pass in the object and a key and get back the value
#################################################################

def get_value_from_nested_dict(nested_dict, key):
    # Split the key by the separator character
    key_parts = key.split('/')

    # Traverse the dictionary using the key parts
    current_dict = nested_dict
    for key_part in key_parts:
        if key_part in current_dict:
            current_dict = current_dict[key_part]
        else:
            return None

    # Return the value at the final key
    return current_dict


# Example InputFile
nested_dict = {"x": {"y": {"z": "a"}}}
key = "x/y/a"
value = get_value_from_nested_dict(nested_dict, key)
print(value)