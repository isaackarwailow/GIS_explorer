import re
def markdownparser(markdown):
    h_val = re.compile('^#+\s')
    assert h_val.match(markdown), 'invalid markdown'
    # validator
    h = h_val.search(markdown)
    h_string = markdown[h.start():h.end()]
    # count hashes for h level
    num = h_string.count('#')
    string = markdown[h.end():]
    # test validation
    if h_val.match(markdown):
        html = '<h' + str(num) + '>' + string + '</h' + str(num) + '>'
        return html
    else:
        string = '#Invalid'
        return string
  

'''
# test
markdown = '### ### Double Header H3'
h_val = re.compile('^#+\s')
assert h_val.match(markdown), 'invalid markdown'
# validator
h = h_val.search(markdown)
h_string = markdown[h.start():h.end()]
# count hashes for h level
num = h_string.count('#')
string = markdown[h.end():]
# test validation
if h_val.match(markdown):
    html = '<h' + str(num) + '>' + string + '</h' + str(num) + '>'
else:
    print('#Invalid')
'''