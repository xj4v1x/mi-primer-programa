
number_to_guess = int((((((((2*5)/3)*8)/2)*7)-(8*3))))

print("El objetivo del juego es adivinar un número entre 1 y 100, tienes 5 intentos")
number_user = int(input("Adivina el número: "))

if number_user == number_to_guess:
    print ("Has acertado!!!")
else:
    if number_to_guess < number_user:
        print("Has fallado, el número a adivinar es menor")
    else:
        print("Has fallado, el número a adivinar es mayor")
    number_user = int(input("Adivina el número: "))
    if number_user == number_to_guess:
        print("Has acertado!!!")
    else:
        if number_to_guess < number_user:
            print("Has fallado, el número a adivinar es menor")
        else:
            print("Has fallado, el número a adivinar es mayor")
        number_user = int(input("Adivina el número: "))
        if number_user == number_to_guess:
            print("Has acertado!!!")
        else:
            if number_to_guess < number_user:
                print("Has fallado, el número a adivinar es menor")
            else:
                print("Has fallado, el número a adivinar es mayor")
            number_user = int(input("Adivina el número: "))
            if number_user == number_to_guess:
                print("Has acertado!!!")
            else:
                if number_to_guess < number_user:
                    print("Has fallado, el número a adivinar es menor")
                else:
                    print("Has fallado, el número a adivinar es mayor")
                number_user = int(input("Adivina el número: "))
                if number_user == number_to_guess:
                    print("Has acertado!!!")
                else:
                    print("Has perdido el juego")
