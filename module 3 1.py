calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple_

def is_contains(string, list_to_search):
    flag = True
    for item in list_to_search:
        if item.lower() == string.lower():
            flag = True
        elif item.lower() != string.lower():
            flag = False
    count_calls()
    return flag




print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)