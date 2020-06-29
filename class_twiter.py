class twiter_user:
    num_of_employees= 0
    raise_ammount = 1.5

    def __init__(self, salary, phone_num, country, name, last_name):
        self.phone_num = phone_num 
        self.salary = salary
        self.country = country
        self.name = name
        self.last_name = last_name
        twiter_user.num_of_employees += 1


    def fullname(self):
        return '{} {}'.format(self.name, self.last_name)


    def salary_add(self):
        self.salary = self.salary * self.raise_ammount


# user1 = twiter_user(799556633, 'Afghanistan', 'Reza', 'hafizi')
# user1.phone_num = int(788556633)
# print(user1.country, user1.name, user1.phone_num, user1.fullname())

user2 = twiter_user(773334135, 'USA', 'john', 'Cohen', 500)
print(user2.country, user2.name, user2.salary_add())

#user3 = twiter_user(777555334, 'Germany', 'Hassan', 'akbari')


#print('Number of Employees: ', twiter_user.num_of_employees)
    


