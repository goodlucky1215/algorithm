def find_same_name(a):
    name_dict={}
    for name in a:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    result=set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result

name=["tom","jein",'mike','tom']
print(find_same_name(name))

name=["tom","jein",'mike','tom','jein','tom']
print(find_same_name(name))

def find_student(a,k):
    for i in a:
        if i == k:
            return a[i]

    return "?"

student={
    39:'junstin',
    14:'john',
    67:'mike',
    105:'fall'
    }
print(find_student(student,39))
print(find_student(student,23))

def find_student(a,k):
    if k in a:
        return a[k]
    else:
        return "?"

student={
    39:'junstin',
    14:'john',
    67:'mike',
    105:'fall'
    }
print(find_student(student,39))
print(find_student(student,23))
