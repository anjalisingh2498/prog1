employee_details = {
    "name": "",
    "address": "",
    "pan": "",
    "basic": 0,
    "hra": 0,
    "da": 0,
    "deduct": 0,
    "tds": 0,
    "gross_salary" :0,
    "net_salary": 0
}
employee_details["name"] = input("Enter employee name: ")
employee_details["address"] = input("Enter employee address: ")
employee_details["pan"] = input("Enter employee PAN: ")
employee_details["basic"] = int(input("Enter employee basic salary: "))
employee_details["hra"] = int(input("Enter employee HRA: "))
employee_details["da"] = int(input("Enter employee DA: "))
employee_details["tds"] = int(input("Enter employee TDS: "))
employee_details["deduct"] = int(input("Enter employee other deductions: "))

employee_details["gross_salary"] = (employee_details["basic"] + employee_details["hra"] + employee_details["da"] + employee_details["tds"])
employee_details["net_salary"] = (employee_details["gross_salary"] - employee_details["deduct"])

print("\nEmployee information:")
print("Name:", employee_details["name"])
print("Address:", employee_details["address"])
print("PAN:", employee_details["pan"])
print("Basic Salary:", employee_details["basic"])
print("TDS:", employee_details["tds"])
print("HRA:", employee_details["hra"])
print("DA:", employee_details["da"])
print("Other Deductions:", employee_details["deduct"])

print("Gross Salary:", employee_details["gross_salary"])
print("Net Salary:", employee_details["net_salary"])
