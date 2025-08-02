"""Day8 30 days of Python Programming"""
#1
dog=dict()
#2
dog['name']='Police'
dog['color']='fauve'
dog['breed']='Chien baoulé'
dog['legs']=4
dog['age']=2
#3
student={}
student['first_name']='Mpo'
student['last_name']='Frank'
student['gender']='Male'
student['age']=25
student['marital_status']='single'
student['skills']=['Python', 'PHP', 'k8s', 'Git', 'Linux', 'Postgres', 'Docker']
student['country']='Benin'
student['city']='Abomey-Calavi'
student['address']='Aitchedji, L281s N°c'
#4
print(len(student))
#5
print(student.get('skills'))
print(type(student['skills']))
#6
student['skills'].append('SQL')
student['skills'].append('HTMX')
#7
student_keys=student.keys()
#8
student_values=student.values()
#9
student_tpl=student.items()
#10
del student['address']
#11
del dog
