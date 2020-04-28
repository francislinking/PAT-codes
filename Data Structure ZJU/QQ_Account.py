N = int(input())

AccountDict = {}

def Login(account,psw):
    if account not in AccountDict.keys():
        print('ERROR: Not Exist')
    else:
        if AccountDict[account] != psw:
            print('ERROR: Wrong PW')
        else:
            print('Login: OK')


def Create(account,psw):
    pswLength = len(psw)
    if 6<=pswLength<=16 and ' ' not in psw:
        pswValid = psw
    else:
        print('ERROR:Wrong PW')
    
    if account in AccountDict.keys():
        print('ERROR: Exist')
    else:
        AccountDict[account] = pswValid
        print('New: OK')



for i in range(N):
    cmd, account, psw = input().split()
    # print(cmd,account,psw)
    if cmd == 'L':
        Login(account,psw)
    else:
        Create(account,psw)

    


