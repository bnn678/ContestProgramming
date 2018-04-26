test_input1 = "15 9010 9000 9020 9030 9040 9050 9060 9070 9070 9090 9100 9110 9120 9130 9140 9150 9160 9170 9180 9190"
test_input2 = "2 919 918 917 916 915 914 913 912 911 910 909 908 907 906 905 904 903 902 901 900"
test_input3 = "3 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919 900"
test_input4 = "4 918 917 916 915 914 913 912 911 910 909 908 907 906 905 904 903 902 901 900 919"

p = int( input() )

outputs = []
for i in range(p):
    input_line = input()
    heights_str = input_line.split(' ')
    heights_str.remove(heights_str[0])

    heights = []
    for number in heights_str:
        heights.append(int(number))

    steps = 0

    for j in range(19):
        for k in range(19):
            if heights[k] > heights[k+1]:
                temp = heights[k]
                heights[k] = heights[k+1]
                heights[k+1] = temp
                steps += 1

    outputs.append(steps)

for i in range(len(outputs)):
    print( str(i+1) + " " + str(outputs[i]))
