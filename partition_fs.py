from math import sqrt,pi,exp

wiki_link = "https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations"

cache = {0:1, 1:1}#first 2 terms are 1

def subsequence(n):
    """
    Generates the correct range for partition sub-values (integers from low to high)
    see link on line 2"
    """
    low, high = -(sqrt(24*n+1)-1)/6, (sqrt(24*n+1)+1)/6
    low, high = int(low), int(high)
    while low <= high:
        yield low
        low += 1

def gen_partitions(n):
	# base case of recursion: zero is the sum of the empty list
	if n == 0:
		yield []
		return
		
	# modify partitions of n-1 to form partitions of n
	for p in gen_partitions(n-1):
		yield [1] + p
		if p and (len(p) < 2 or p[1] > p[0]):
			yield [p[0] + 1] + p[1:]
        
def partition(n):
    """
    applies recursive formula for partition function
    see link on line 2
    """
    n = int(n)
    if n < 0:
        raise IndexError("partition expects pos numbers, not ",n)
    if n in cache:
        return cache[n]
    
    total = 0
    for k in subsequence(n):
        if not k:
            continue
        total += ((-1)**(k+1)) * partition(n - (3*k**2-k)/2)

    cache[n] = total
    return total

def p_approx(n):
    if n < 0:
        raise IndexError("p_approx expects pos numbers, not ",n)
    try:
        const = 1/(4*n*sqrt(3))
    except ZeroDivisionError:
        return 1 #approx doesn't expect 0, but *shrug*
    power = exp(pi*sqrt((2*n)/3))
    return const*power

def approx_error(n):
    exact, aprx = partition(n), p_approx(n)
    return 100*(aprx-exact)/exact

if __name__ == "__main__":
    # for i in range(0,100,5):
    #     print(approx_error(i))
    num = 25
    count = 0
    for i in gen_partitions(num):
         print(i)
         count += 1
    print(f'There are {count} partitions of {num}')
    print(f'The partition function expected {partition(num)} partitions')