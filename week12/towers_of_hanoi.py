def move_tower(h, src, dest, aux):
    if h == 1:
        print('Moving disk from {} -> {}'.format(src[-1], dest[-1]))
        dest.insert(0, src.pop(0))
        return 1
    else:
        return move_tower(h - 1, src, aux, dest) + move_tower(1, src, dest, aux) + move_tower(h - 1, aux, dest, src)

if __name__ == '__main__':
    h = int(input('Enter tower height: '))

    src = list(range(1, h + 1))
    dest = []
    aux = []

    src.append('A')
    dest.append('B')
    aux.append('C')

    n = move_tower(h, src, dest, aux)
    print(dest, n)