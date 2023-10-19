

def find_sums(int_list: list, obj_value: int):

 
    def find_sum(start : int,  values_stored : list, obj_value: int):
        
         #se ha encontrado una solucion
        if obj_value == 0 :
            result.append(values_stored[:])
            return
        # no se ha encontrado solucion
        if obj_value < 0 or start == len(int_list):
            return
        #busqueda 
        for index in range(start, len(int_list)):

            if index > start and int_list[index] == int_list[index-1]:
                continue

            values_stored.append(int_list[index])
            find_sum(index+1, values_stored, obj_value - int_list[index])
            values_stored.pop()

    result = []
    find_sum(0, [], obj_value)
    return result 

print(find_sums([1,5,3,2],6))



