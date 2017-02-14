keypad = {2: list('abc'),
          3: list('def'),
          4: list('ghi'),
          5: list('jkl'),
          6: list('mno'),
          7: list('pqrs'),
          8: list('tuv'),
          9: list('wxyz')}
words = raw_input().split(',')
for word in words:
    w = word.split('-')
    result = list()
    for char in w:
        ch = char.split('.')
        result.append(keypad[int(ch[0])][int(ch[1]) - 1])
    print ''.join(result),
