args = list(map(int, input().split()))


sum_negative = 0
sum_positive =  0

for things in args:

    if things < 0:
            sum_negative += things
    else:
            sum_positive += things

final_negative = abs(sum_negative)
final = 0

print(sum_negative)
print(sum_positive)

if final_negative  > sum_positive:
    final =  final_negative
    print(f"The negatives are stronger than the positives")
else:
    final = sum_positive
    print(f"The positives are stronger than the negatives")
