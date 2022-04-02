def splited_email(email):
    username = email.split('@')[0]
    domain = email.split('@')[1]
    print('username', username)
    print('domain', domain)

splited_email(input("Enter your email: "))

