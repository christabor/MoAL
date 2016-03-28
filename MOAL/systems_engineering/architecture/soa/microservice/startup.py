"""Startup."""

import os

if __name__ == '__main__':
    opt = raw_input('Enter an option: [billing | inventory | shipping] ')
    opt = opt.strip()
    print('You chose: {}'.format(opt))
    cwd = os.getcwd()

    if opt == 'billing':
        print('Starting billing service')
        os.system('python {}/billing_svc/app.py'.format(cwd))
    elif opt == 'inventory':
        print('Starting inventory service')
        os.system('python {}/inventory_svc/app.py'.format(cwd))
    elif opt == 'shipping':
        print('Starting shipping service')
        os.system('python {}/shipping_svc/app.py'.format(cwd))
