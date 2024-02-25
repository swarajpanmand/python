from collections import OrderedDict

dict = OrderedDict({'swaraj':10 , 'suhani':12})

dict.update({'suhani1': 15})
dict.move_to_end('suhani1', last = False)

print(dict)
