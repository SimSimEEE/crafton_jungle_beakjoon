print(*sorted(set([input() for i in range(int(input()))]), key=lambda x: (len(x), x)), sep='\n')