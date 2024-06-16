import random
import string

def random_id():
    return ''.join(random.choices(string.ascii_lowercase, k=5))

# Example usage
print(random_id())
