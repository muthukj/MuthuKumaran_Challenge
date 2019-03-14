# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

p = '^[456]{1}\d{3}\-?\d{4}\-?\d{4}\-?\d{4}$'

for _ in range(int(input())):
    try:
        n = input()
        assert re.search(p,n)
        n = n.replace('-','')
        assert not re.search(r'(\d)\1{3,}',n)
    except:
        print('Invalid')
    else:
        print('Valid')
