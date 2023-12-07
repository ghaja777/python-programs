def sum_of_divisors(n):
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def find_amicable_numbers(start, end):
    amicable_numbers = []
    for num in range(start, end + 1):
        sum1 = sum_of_divisors(num)
        sum2 = sum_of_divisors(sum1)
        if num == sum2 and num != sum1:
            amicable_numbers.append((num, sum1))
    return amicable_numbers

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

amicable_pairs = find_amicable_numbers(start_range, end_range)

if amicable_pairs:
    print("Amicable number pairs in the range", start_range, "to", end_range, "are:")
    for pair in amicable_pairs:
        print(pair[0], "and", pair[1])
else:
    print("No amicable numbers found in the range", start_range, "to", end_range)
