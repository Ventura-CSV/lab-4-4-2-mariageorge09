def main():
    while True:
        try:
            user_num = int(input('Enter a number: '))
            number = user_num
        except ValueError:
            print ('Input must be numeric')
            continue
        else:
            print ('Output: ')
            print (number)
            break
        
        


    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
