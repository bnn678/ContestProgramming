def FindIslands(num_list):
    sub_island_list = []
    sub_island = []
    current_min = min(num_list)

    count = 0
    while( len( num_list ) > count ):
        if num_list[count] > current_min:
            while( num_list[count] > current_min ):
                sub_island.append(num_list[count])
                count += 1

                if(count == len(num_list)):
                    break
            sub_island_list.append(sub_island)
            sub_island = []

        count += 1

    return sub_island_list


test_input1 = "1 0 0 1 1 2 2 1 1 0 1 2 0"
test_input2 = "2 0 1 2 4 3 1 3 4 5 2 1 0"
test_input3 = "3 0 1 2 4 4 1 0 2 4 1 0 0"
test_input4 = "4 0 1 2 3 4 5 6 7 8 9 10 0"
p = int( input() )
answers = []

for a in range( p ):
    k = input()
    k = test_input2
    num_list_str = k.split(' ')
    num_list_str = num_list_str[1:]
    num_list = []

    for num in num_list_str:
        num_list.append(int(num))

    sub_island_list = []
    current_island = 0
    found = []

    found = FindIslands(num_list)

    for island in found:
        sub_island_list.append(island)

    while( current_island < len( sub_island_list ) ):
        found = FindIslands(sub_island_list[current_island])
        for island in found:
            sub_island_list.append(island)
        current_island += 1

    answers.append(len(sub_island_list))

for i in range(len(answers)):
    print( str(i+1) + " " + str(answers[i]) )
    
