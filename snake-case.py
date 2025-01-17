# https://python.30secondsofcode.org/list
# Converts a string to snake case. Break the string into words and combine them adding _ as a separator, using a regexp.

import re

def snake(s):
    return '_'.join(re.sub('([A-Z][a-z]+)', r' \1',
    re.sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()

# EXAMPLES
# snake('camelCase') # 'camel_case'
# snake('some text') # 'some_text'
# snake('some-mixed_string With spaces_underscores-and-hyphens') # 'some_mixed_string_with_spaces_underscores_and_hyphens'
# snake('AllThe-small Things') # "all_the_smal_things"