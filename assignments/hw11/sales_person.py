class SalesPerson:
    def __init__(self, employee_id,name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def enter_sale(self,sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for num in self.sales:
            total += num
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self,quota):
        return self.total_sales() <= quota

    def compare_to(self,other):
        if other.total_sales() > self.total_sales():
            return -1
        elif other.total_sales() < self.total_sales():
            return 1
        else:
            return 0

    def __str__(self):
        return "{:0}-{:1}: {:2}".format(self.employee_id,self.name,self.total_sales())

