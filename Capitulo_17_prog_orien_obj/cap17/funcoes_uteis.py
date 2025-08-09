def ba():
    print('\n','-' * 40,'\n', sep='')

def bar(whitch, n):
    match whitch:
        case 'ini':
            print('┌', '─' * (20 * n), '┐', sep='')
        case 'mid':
            print('├','─' * (20 * n), '┤', sep='')
        case 'end':
            print('└', '─' * (20 * n), '┘', sep='')
        case _:
            print('─' * (21 * n))

def exibe_lista(lst):
    i = 1
    for j in lst:
        print(j, end=' │ ')
        if i % 10 == 0:
            print()
        i+=1

def exb_lst_n_prvd(lst):
    i = 1
    for j in lst:
        if '__' not in j:
            print(j, end=' │ ')
            i += 1
        if i % 10 == 0:
            print()