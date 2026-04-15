def length(x):
    s = 0
    for i in x:
        s += 1
    return s
def safe_print_list(my_list=[], x=0):
    if isinstance(my_list,list):
        if x <= length(my_list):
            return my_list[:x]
        raise IndexError
    raise ValueError

try:
    nb_print = safe_print_list()
    print("nb_print: {:d}".format(nb_print))
except IndexError,ValueError:
    pass
