from random import choices, sample
import string
import argparse as argp


def create_password(length = 8, digit = False, lower = False,
                    upper = False, pun = False):
    pool =  ''

    if upper:
        pool += string.ascii_uppercase

    if lower:
        pool += string.ascii_lowercase

    if digit:
        pool += string.digits

    if pun:
        pool += string.punctuation
    
    if pool == '':
        pool = string.ascii_letters

    return ''.join(choices(pool, k = length))

def parser():
    parser = argp.ArgumentParser(
                    prog ='PasswordCreator',
                    description = '''makes a password with [numbers, strings, 
                    and punctuation]. ''',
                    epilog = 'Text at the bottom of help')
    parser.add_argument('length', type=int, help = 'lenght of passwords')
    parser.add_argument('-d', '--digit', action='store_true')
    parser.add_argument('-l', '--lower', action = 'store_true')  # on/off flag
    parser.add_argument('-u', '--upper', action = 'store_true')      
    parser.add_argument('-p', '--pun', action='store_true')

    args = parser.parse_args()
    print(create_password(args.length, args.digit, args.lower,args.upper,
                        args.pun))
    

if __name__ == '__main__':
    parser()
