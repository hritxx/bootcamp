import timeit
import time


t = timeit.timeit("sum(range(10000))", number=100)
print(f"timeit result: {t:.4f} seconds")


list_time = timeit.timeit("[x*x for x in range(1000000)]", number=1)
gen_time = timeit.timeit("(x*x for x in range(1000000))", number=1)
print(f"List comp time: {list_time:.4f}s | Generator expr time: {gen_time:.4f}s")


start = time.time()
sum(range(1000000))
end = time.time()
print(f"Manual time: {end - start:.4f} seconds")

unsorted_list = list(reversed(range(10000)))
sorted_time = timeit.timeit("sorted(unsorted_list)", globals=globals(), number=10)
print(f"Sorted time: {sorted_time:.4f} seconds")