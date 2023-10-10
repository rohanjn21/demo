def get_value(obj, key_path):
    keys = key_path.split('/')
    current = obj

    for key in keys:
        if key in current:
            current = current[key]
        else:
            return None  # Key not found

    return current

# Example usage
obj1 = {"a":{"b":{"c":"d"}}}
key1 = "a/b/c"
result1 = get_value(obj1, key1)
print(result1)  # Output: "d"

obj2 = {"x":{"y":{"z":"a"}}}
key2 = "x/y/z"
result2 = get_value(obj2, key2)
print(result2)  # Output: "a"

obj3 = {"q":"w"}
key3 = "q"
result3 = get_value(obj3, key3)
print(result3) # Output: "w"

obj4 = {"x":{"y":{"z":""}}}
key4 = "x/y/z"
result4 = get_value(obj4, key4)
print(result4)  # Output: " "

obj5 = {"x":{"y":{"z":"a"}}}
key5 = "x/y\z"
result5 = get_value(obj5, key5)
print(result5)  # Output: None