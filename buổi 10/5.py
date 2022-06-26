names = {
'students': [
{'firstName': 'Nikki', 'lastName': 'Roysden'},
{'firstName': 'Mervin', 'lastName': 'Friedland'},
{'firstName': 'Aron', 'lastName': 'Wilkins'}
],
'teachers': [
{'firstName': 'Amberly', 'lastName': 'Calico'},
{'firstName': 'Regine', 'lastName': 'Agtarap'}
]
}
print('List of students:\n')
for i in 'students':
   print('-'+str(i['firstName'])+' '+str(i['lastName'])+'\n')