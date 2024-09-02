
def check_password(password: str):
    with open('10-million-password-list-top-100000.txt', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()

    if len(password) == 0:
        print('bad password')
        return


    for i, common_passwords in enumerate(common_passwords, start=1):


        for p in list(password):
            if p == ' ':
                print('bad password')
                return

        if password == common_passwords:
            print(f'{password}: ❌ (#{i})')
            return



    print(f'{password}: ✅ (unique)')

def main():
    user_password: str = input('Enter a password  ')
    check_password(user_password)


if __name__ == "__main__":
    main()