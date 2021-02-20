def main():
    while True:
        operation = input('\n******* Welcome to the Masum Bhai Banking *******\n'
                          'These are our operations:\n'
                          '1:Take money\n'
                          '2:Put money\n'
                          '3:Money transfer\n'
                          'Q:Quitting\n')
        if operation == '1':
            balance = int(input('How much money do you have? :'))
            money = int(input('How much money do you want to take?: '))
            if balance < money:
                print("##########################################")
                print('You can not do this!\nYour balance in not enough to this operation!')
                print("##########################################")
                break
            else:
                print("##########################################")
                print("Your money: ", (balance - money), '$')
                print("##########################################")
        elif operation == '2':
            money = int(input('How much money do you want to put?: '))
            balance = int(input('How much money do you have?'))
            print("##########################################")
            print('Your new balance is now: ', (money + balance), '$')
            print("##########################################")
        elif operation == '3':
            balance = int(input('How much money do you have?'))
            transfer = int(input('How much money will you transfer?: '))
            if balance > transfer:
                print("##########################################")
                print("operation successful")
                print('You transferred :', transfer, '$')
                print('Your balance is: ', (balance - transfer), '$')
                print("##########################################")
            elif balance < transfer:
                print("##########################################")
                print('There is not enough money to do this operation')
                print("##########################################")
                break
        elif operation == 'Q' or 'q':
            print("##########################################")
            print('Quitting from application!')
            print("##########################################")
            exit()
        else:
            print("##########################################")
            print('Hey! no character type,okay?')
            print("##########################################")
            main()

if __name__ == '__main__':
    main()