num_of_completed_HW = '12'
num_of_hours = '1.5'
course_name = 'Pyton'
num_of_hours = float(num_of_hours)
num_of_completed_HW = float(num_of_completed_HW)
time_for_one_task = num_of_hours / num_of_completed_HW
print('Курс:', course_name,';'  ' всего задач:', num_of_completed_HW,';','затрачено часов:', num_of_hours,';', 'среднее время выполнения:', time_for_one_task, 'часа''.')