from os import path
from sys import argv

def Nerum(Class, Args=()):
    
    if len(argv) < 2:
        print('usage: {} func_name [args]'.
        format(path.basename(argv[0])))
        return

    func = Class.__getattribute__(Class, argv[1])
    try:
        ret = eval('func(Class(*Args),{})'.
        format(''.join(argv[2:])))
    except Exception as e:
        print('error: {}'.format(e))
        return
    print(ret)
