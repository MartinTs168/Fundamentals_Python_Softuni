companies = {}
company_info = input().split(' -> ')
while company_info[0] != 'End':
    company_name = company_info[0]
    employee_id = company_info[1]
    if company_name not in companies.keys():
        companies[company_name] = [employee_id]
    else:
        if employee_id not in companies[company_name]:
            companies[company_name].append(employee_id)
    company_info = input().split(' -> ')
for company, workers in companies.items():
    print(f"{company}")
    for worker_id in workers:
        print(f"-- {worker_id}")
