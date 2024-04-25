I saw an interview question where you were asked to find the number of unique partitions of a number. A partition is a list of numbers that add up to that number. For example, a partition of 5 is [1,1,3] or [2,3] or [5].

While the recursive approach works, for large numbers it can take a looong time.

Using a recurrence relation found in this article: https://en.wikipedia.org/wiki/Partition_function_(number_theory), we can find the number of partitions much faster
