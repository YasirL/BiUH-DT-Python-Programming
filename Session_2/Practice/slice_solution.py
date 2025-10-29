def trim(s):
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1
    
    # ’“µΩ◊Ó∫Û“ª∏ˆ∑«ø’∏Ò◊÷∑˚µƒÀ˜“˝
    end = len(s)
    while end > start and s[end-1] == ' ':
        end -= 1
    s = s[start:end]
    return s
# ≤‚ ‘:
if trim('hello ') != 'hello':
    print('≤‚ ‘ ß∞‹!')
elif trim(' hello') != 'hello':
    print('≤‚ ‘ ß∞‹!')
elif trim(' hello ') != 'hello':
    print('≤‚ ‘ ß∞‹!')
elif trim(' hello world ') != 'hello world':
    print('≤‚ ‘ ß∞‹!')
elif trim('') != '':
    print('≤‚ ‘ ß∞‹!')
elif trim(' ') != '':
    print('≤‚ ‘ ß∞‹!')
else:
    print('≤‚ ‘≥…π¶!')  