import unittest

def get_value(obj, key_path):
    keys = key_path.split('/')
    current = obj

    for key in keys:
        if key in current:
            current = current[key]
        else:
            return None  # Key not found

    return current

class TestGetValue(unittest.TestCase):
    def test_existing_key(self):
        obj = {"a":{"b":{"c":"d"}}}
        key = "a/b/c"
        result = get_value(obj, key)
        self.assertEqual(result, "d")

    def test_nested_key(self):
        obj = {"x":{"y":{"z":"a"}}}
        key = "x/y/z"
        result = get_value(obj, key)
        self.assertEqual(result, "a")

    def test_nonexistent_key(self):
        obj = {"a":{"b":{"c":"d"}}}
        key = "x/y/z"
        result = get_value(obj, key)
        self.assertIsNone(result)

    def test_partial_key(self):
        obj = {"a":{"b":{"c":"d"}}}
        key = "a/b"
        result = get_value(obj, key)
        self.assertEqual(result, {"c": "d"})

if __name__ == "__main__":
    unittest.main()
