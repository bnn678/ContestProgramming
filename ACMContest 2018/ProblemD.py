def IsPrime(num):
    num = int(num)
    if num == 1:
        return False
    
    for i in range( 2, int(num**.5) ):
        if num % i == 0:
            return False
    return True

p = int( input() )
inputs = []
answers = []
max_tests = 100 # BAAADDDDDD

for a in range(p):
    input_line = input()
    k = input_line.split(' ')[1]
    inputs.append(k)

    passed = False

    if IsPrime(k):
        total = 0
        
        for b in range( max_tests ):
            total = 0
            
            if len(k) > 1:
                for j in range( len(k) ):
                    total += int(k[j])**2
            else:
                total = int(k)**2

            if total == 1:
                answers.append("YES")
                passed = True
                break

            k = str(total)

    if( passed == False ):
        answers.append("NO")



for i in range( len(inputs) ):
    print( str(i+1) + " " + str(inputs[i]) + " " + answers[i] )
