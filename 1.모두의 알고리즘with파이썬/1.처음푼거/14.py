def find_same_name(a):
    name_dict={}
    for name in a:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result

name = ["tom","jerry","mike","tom"]
print(find_same_name(name))

name = ["tom","jerry","mike","tom","jerry"]
print(find_same_name(name))

def find_same_name(a):
    name_dict={}
    for name in a:
        if name in name_dict:
            name_n
