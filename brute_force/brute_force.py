import itertools
import time
import string


def common_guess(word: str) -> str | None:
    with open('best15.txt', 'r') as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):

        if match == word:
            return f'Common match: {match} (#{i})'


def brute_force(word: str, length: int, digits: bool = False, symbol: bool = False) ->str| None:
    chars: str = string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbol:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = ''.join(guess)

        if guess == word:
            return f'"{word}" was created in {attempts:,} guesses'


        print(guess, attempts)

def main():
    print('searching...')
    password: str = 'bag'

    start_time: float = time.perf_counter()

    if common_match := common_guess(password):
        print(common_match)
    else:
        if cracked := brute_force(password, length=len(password), digits=True, symbol=True):
            print(cracked)
        else:
            print('there was no match')

    end_time: float = time.perf_counter()

    print(round(end_time - start_time, 2) , 's')



if __name__ == "__main__":
    main()