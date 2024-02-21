test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
print(test_dict['month'])

res = dict(zip(test_dict['month'], test_dict['name']))
print(res)