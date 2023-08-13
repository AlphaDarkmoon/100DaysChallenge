from argparse import ArgumentParser
import sys

def sum_of_num(number):
    if number>0:
        number_str = str(number)
        sum_num = 0
        for i in number_str:
            sum_num+=int(i)
        return sum_num
    
    else:
        return 'give value...'
    
parser = ArgumentParser()
parser.add_argument('-a',help='...',type=int,default=0)
args = parser.parse_args()


if __name__=='__main__':
    print(sum_of_num(args.a))

