from collections import deque

def check_for_palindrome(word_deque: deque):
    if not word_deque:
        print("Введена порожня стрічка.")
    else:
        for _ in range(0, len(word_deque) // 2):
            if word_deque.pop() != word_deque.popleft():
                print(f"Введене слово не є паліндромом.")
                return
        print(f"Введене слово є паліндромом.")

while True:
    check_for_palindrome(deque("".join(input("Введіть слово для перевірки: ").split()).lower()))

