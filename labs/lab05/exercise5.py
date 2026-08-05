test_score1 = int(input("Enter the first test score: "))
test_score2 = int(input("Enter the second test score: "))
test_score3 = int(input("Enter the third test score: "))

total_score = int(test_score1 + test_score2 + test_score3)
average_score = float(total_score / 3)

print(f"Test Score 1: {test_score1}")
print(f"Test Score 2: {test_score2}")   
print(f"Test Score 3: {test_score3}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score}")