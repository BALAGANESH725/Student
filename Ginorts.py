print(*sorted(input(), key = lambda c: ord(c)+100*c.isupper() if c.isalpha() else ord(c)+1000-100*c.isdigit()*(ord(c)%2)),sep='')
