### Employee Salary(using functions)


def calculate_gross_salary(basic_salary, category):
    if category == "Executive":
        da = 0.5 * basic_salary
        hra = 0.3 * basic_salary
        pf = 0.12 * basic_salary
        
        gross_salary = basic_salary + da + hra
        return gross_salary, pf
        
    elif category == "Manager":
        da = 0.9 * basic_salary
        hra = 0.3 * basic_salary
        pf = 0.4 * basic_salary
        
        gross_salary = basic_salary + da + hra
        return gross_salary, pf
    
    else:
        print("worong option!") 

def calculate_income_tax(basic_salary, category):
    gross_salary, _ = calculate_gross_salary(basic_salary, category)
    
    income_tax = 0.1 * gross_salary
    
    return income_tax

def calculate_net_salary(basic_salary, category):
    gross_salary, pf = calculate_gross_salary(basic_salary, category)
    income_tax = calculate_income_tax(basic_salary, category)
    
    net_salary = gross_salary - pf - income_tax
    
    return net_salary


basic_salary = float(input("Enter basic salary: "))
category = input("Enter category (Executive/Manager): ")

net_salary = calculate_net_salary(basic_salary, category) 
print(net_salary)






### Employee Salary(using classes)


class Employee:
    def __init__(self, basic_salary, category):
        self.basic_salary = basic_salary
        self.category = category
        
    def calculate_gross_salary(self):
        if self.category == "Executive":
            da = 0.5 * self.basic_salary
            hra = 0.3 * self.basic_salary
            pf = 0.12 * self.basic_salary
            
            gross_salary = self.basic_salary + da + hra
            return gross_salary, pf
            
        elif self.category == "Manager":
            da = 0.9 * self.basic_salary
            hra = 0.3 * self.basic_salary
            pf = 0.4 * self.basic_salary
            
            gross_salary = self.basic_salary + da + hra
            return gross_salary, pf
        
        else:
            print("Wrong option!") 
    
    def calculate_income_tax(self):
        gross_salary, _ = self.calculate_gross_salary()
        income_tax = 0.1 * gross_salary
            
        return income_tax
                    
    def calculate_net_salary(self):
        gross_salary, pf = self.calculate_gross_salary()
        income_tax = self.calculate_income_tax()
        
        net_salary = gross_salary - pf - income_tax
        return net_salary


basic_salary = float(input("Enter basic salary: "))
category = input("Enter category (Executive/Manager): ")

employee = Employee(basic_salary, category)
net_salary = employee.calculate_net_salary()

print("Net Salary:", net_salary)
