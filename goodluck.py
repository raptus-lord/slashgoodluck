import cryptocode
string = input('encrypted string: ')
key = input('key: ')

def solve(string, key):
    output = cryptocode.decrypt(string, key)
    return output

print(solve(string, key))