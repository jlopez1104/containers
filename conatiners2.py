musicians = []
for i in range(4):
    name = input('Enter artist: ')
    musicians.append(name)
print(musicians)
name2 = input('name person to see if they are on list: ')
if name2 in musicians:
    print('this fruit is in the list')
else:
    print ('fruit is not in the list')
