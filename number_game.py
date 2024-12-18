import random
import sys

try:
    sys.stdout.write("Please enter the number min_number: ")
    sys.stdout.flush()
    n = int(sys.stdin.readline())

    sys.stdout.write("Please enter the number max_number: ")
    sys.stdout.flush()
    m = int(sys.stdin.readline())
except:
    sys.stderr.write("You must enter valid integers for 'n' and 'm'\n")
    sys.exit(1)

if n >= m:
    sys.stderr.write("You must choose 'n' which is smaller than 'm'\n")
    sys.exit(1)

correct_number = random.randint(n, m)

current_time = 0
maximum_time = 5

while True:
    if current_time >= maximum_time:
        sys.stdout.write("You are lose!\n")
        sys.stdout.flush()
        break
    sys.stdout.write(f"You can guess {maximum_time - current_time} time. Please enter your guess: ")
    sys.stdout.flush()
    guess_number = int(sys.stdin.readline())
    if guess_number == correct_number:
        sys.stdout.write("You are win!\n")
        sys.stdout.flush()
        break 
    
    current_time += 1

