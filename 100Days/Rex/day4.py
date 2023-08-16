from argparse import ArgumentParser


def funcs(a,b):
    if pars.o=='add':
        return a+b
    elif pars.o=='min':
        if pars.a<pars.b:
            pars.a,pars.b = pars.b,pars.a
            return pars.a-pars.b
        else:
            return pars.a-pars.b
    

parsers = ArgumentParser()

parsers.add_argument('-a',help='...' , type=int,default=0)
parsers.add_argument('-b',help='...',type=int,default=0)
parsers.add_argument('-o' ,help='...')

pars = parsers.parse_args()


if __name__=='__main__':
    print(funcs(pars.a,pars.b))
