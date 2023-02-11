def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local   # pake return karna ada value yang kita minta


def write_todos(filepath, var):   # karna yang bakal berubah cuma nama file sama var nya itu
    with open(filepath, 'w') as file:
        file.writelines(var)   # gapakereturn karna ada value yang kita butuhkan

if __name__=='__main__':
    print(get_todos()) #supaya dia ga kebaca di mainpy, taroh di ifelse