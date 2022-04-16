from sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self,file_name):
        in_f = open(file_name, "r")
        for line in in_f.readlines():
            self.sales_people.append(line.replace("\n",""))
        in_f.close()

    def quota_report(self,quota):
        desired_list = []
        for employee_index in range(len(self.sales_people)):

            the_data = self.sales_people[employee_index].split(", ")
            emp_id = eval(the_data[0])
            emp_name = the_data[1]
            emp_all_sales = the_data[2]

            sale_list = emp_all_sales.split(" ")
            total_sale = 0
            for i in sale_list:
                i = eval(i)
                total_sale += i

            did_quota = (total_sale >= quota)

            desired_list.append([emp_id,emp_name,total_sale,did_quota])
        return desired_list

    def top_seller(self):
        #turn all employees into sales person objects
        all_info = self.quota_report(0)
        sales_ppl_list = []
        all_sales = []

        for i in range(len(self.sales_people)):
            new_id = all_info[i][0]
            new_person = all_info[i][1]
            sales_ppl_list.append(SalesPerson(new_id,new_person))

        for i in range(len(sales_ppl_list)):
            my_sale = all_info[i][2]
            sales_ppl_list[i].enter_sale(my_sale)
            all_sales.append(sales_ppl_list[i].get_sales())

        highest = sales_ppl_list[0]

        for i in range(len(sales_ppl_list)):
            if sales_ppl_list[i].get_sales() > highest.get_sales():
                highest = sales_ppl_list[i]
        return highest

    def individual_sales(self,employee_id):
        all_info = self.quota_report(0)
        sales_ppl_list = []

        for i in range(len(self.sales_people)):
            new_id = all_info[i][0]
            new_person = all_info[i][1]
            sales_ppl_list.append(SalesPerson(new_id,new_person))

        for i in sales_ppl_list:
            if i.get_id() == employee_id:
                return i
        return None

    def get_sale_frequencies(self):
        pass