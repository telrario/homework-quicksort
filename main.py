from seed import make_grades
from quicksort import quicksort

grades = make_grades(30)
print('unsorted grades: ', grades)
print('sorted grades:', quicksort(grades, 'grade'))
