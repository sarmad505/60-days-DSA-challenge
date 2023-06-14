def is_valid(s):
    stack=[]
    bracket_map = {')':'(','}':'{',']':'['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or bracket_map[char]!= stack.pop():
                return False
    return len(stack)==0

input_string = '(){}[]'
print(is_valid(input_string))


input_string = '(){]'
print(is_valid(input_string))        
