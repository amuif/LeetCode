if __name__ == '__main__':
  
    lst = []


    num_commands = int(input())


    for _ in range(num_commands):
        command = input().split()
        
        if command[0] == 'insert':
            i, e = int(command[1]), int(command[2])
            lst.insert(i, e)
        elif command[0] == 'print':
            print(lst)
        elif command[0] == 'remove':
            e = int(command[1])
            lst.remove(e)
        elif command[0] == 'append':
            e = int(command[1])
            lst.append(e)
        elif command[0] == 'sort':
            lst.sort()
        elif command[0] == 'pop':
            lst.pop()
        elif command[0] == 'reverse':
            lst.reverse()
