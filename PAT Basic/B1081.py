N = int(input())

for i in range(N):
    psw = input()
    l =len(psw)

    if l < 6:
        print('Your password is tai duan le.')
    else:
        invalid = 0
        hasAlpha = 0
        hasDigital = 0
        for ch in psw:
            if ch.isalnum() or ch == '.':
                if ch.isalpha():
                    hasAlpha = 1
                elif ch.isdigit():
                    hasDigital = 1
            else:
                invalid = 1 

        if invalid == 1:
            print('Your password is tai luan le.')
        elif hasDigital == 0:
            print('Your password needs shu zi.')
        elif hasAlpha == 0:
            print('Your password needs zi mu.')
        else:
            print('Your password is wan mei.')