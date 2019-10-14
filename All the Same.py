from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    is_bool = True

    #print(len(elements))
    if len(elements) == 1 or len(elements) == 0:
        return is_bool
    
    #type
    #for el in elements:
    #    if type(el) != int:
    #       is_no_indx = True
    #        break
    #        #print(elements, "not int")
     

    #zero
    #elements_2 = elements[:]
    #elements_2.append(1)
    

    
    #many
    first_el = elements[0]    
    for el in elements:
        if first_el != el:
            is_bool = False
            break
    return is_bool


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
