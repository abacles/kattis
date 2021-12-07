for _ in range(int(input())):
    cmd = input()
    if cmd.startswith('simon says '):
        print(cmd[10:])
    else:
        print()
