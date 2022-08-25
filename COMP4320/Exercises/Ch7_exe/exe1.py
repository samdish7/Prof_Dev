# practices with Type hinting, this is likely to be baked in with version 4.0
def grep(needle) -> str:
    '''Only emits lines of text that contain x'''
    haystack = None
    while True:
        haystack = yield haystack

        if needle not in haystack:
            haystack = None


def sed(pattern, replacement) -> str:
    '''Replace any lines containing pattern with replacement'''
    result = None
    while True:
        result = yield result

        if pattern in result:
            result = replacement


search = grep('foo')
replace = sed('bar', 'baz')
next(search)
next(replace)

f = open("test.txt")

for line in f:
    found = search.send(line)
    if found:
        line = replace.send(line)

        print(line)


