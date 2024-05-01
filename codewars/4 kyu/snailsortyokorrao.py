def snail(snail_map):

    snail_return = []
    length_group_arrays = len(snail_map)
    count_end_array = 0
    ## First step 
    for x in snail_map[0]:
        snail_return.append(x)
        count_end_array += 1
        if count_end_array == len(snail_map[0]):
            ##Start from 1 to len(snail_map)
            for y in range(1,length_group_arrays):
                snail_return.append(snail_map[y][-1])
                if y == length_group_arrays  - 1:

                    third_snail_list = snail_map[y]
                    third_snail_list.reverse()

                    snail_return.append(third_snail_list[1:])

                    snail_return.append(snail_map[y - 1 ][:len(snail_map[y - 1]) - 1])




    final_numbers = []

    for x in snail_return:
        if isinstance(x,list):
            for n in x:
                final_numbers.append(n)
        else:
            final_numbers.append(x)

    return final_numbers