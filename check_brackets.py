import sys

def check_brackets(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for i, char in enumerate(content):
        if char in '({[':
            stack.append((char, i))
        elif char in ')}]':
            if not stack:
                print(f"Unmatched closing bracket {char} at index {i}")
                # Print context
                start = max(0, i - 40)
                end = min(len(content), i + 40)
                print(f"Context: ...{content[start:end]}...")
            else:
                top, pos = stack.pop()
                if top != pairs[char]:
                    print(f"Mismatched bracket {char} at index {i}, matches {top} at index {pos}")
    
    while stack:
        top, pos = stack.pop()
        print(f"Unclosed bracket {top} at index {pos}")

if __name__ == "__main__":
    check_brackets(sys.argv[1])
