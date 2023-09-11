import hashlib

guesses = []
wordlist_path = "/path/to/rockyou.txt"

with open(wordlist_path, "r", encoding="utf-8") as file:
        for line in file:
            guesses.append(line)

is_correct = False

def guessAttack(__str__):
    hash_guess = hashlib.sha256(__str__.encode('utf-8')).hexdigest()
    print("Guess: ", __str__)
    print("Guesses Hash: ", hash_guess, " vs ", hash_target, "\n")
    if hash_guess == hash_target:
        return True
    else:
        return False

hash_target = input("Hash: ")

for guess in guesses:
    is_correct = guessAttack(guess)
    if is_correct:
        print(f"The original value for the hash {hash_target} is: {guess}")
        break

if not is_correct:
    print(f"No match found for the hash {hash_target}.")