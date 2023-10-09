a_set = set([int(i) for i in range(1,int(input())+1)])
while True:
    b_answer = input()
    if b_answer == 'HELP':
        break
    a_answer = input()
    b_set = set([int(i) for i in (b_answer.split())])
    if a_answer == 'YES':
        a_set &= b_set
    else:
        a_set -= b_set
print(*[str(i) for i in a_set])