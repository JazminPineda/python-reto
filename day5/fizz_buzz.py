for numer in range (1, 101):
    
    if numer % 3 == 0 and numer %5 ==0:
        numer= "FizzBuzz"
    elif numer % 3 == 0:
        numer = "Fizz"
      
    elif numer % 5 == 0:
        numer = "Buzz"
      
    else:
        numer
    print(numer)