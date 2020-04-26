from tech_dev import (
    data_analyst,
    data_engineer,
    ml_engineer,
    mobile_developer,
    product_manager,
    technical_leader,
    web_developer,
)
from sales import account_manager, merchandiser, sales_manager

p1 = data_analyst.DataAnalyst()
p1.set_name('Sarah', 'Berkley')
print(*p1.get_name(), p1.who_is())
p1.set_chief('Paul Gerber')

p2 = data_engineer.DataEngineer()
p2.set_name('Liam', 'Smith')
print(*p2.get_name(), p2.who_is())
p2.set_chief('Paul Gerber')

p3 = ml_engineer.MLEngineer()
p3.set_name('Marie', 'Jones')
print(*p3.get_name(), p3.who_is())
p3.set_chief('Olivia Kay')

p4 = mobile_developer.MobileDevepoler()
p4.set_name('Noah', 'Ax')
p4.set_platform('ios')
print(*p4.get_name(), p4.who_is())
p4.set_chief('Olivia Kay')

p5 = product_manager.ProductManager()
p5.set_name('Ava', 'Thomas')
print(*p5.get_name())


people = [p1, p2, p3, p4]

print('\n\n\nPaul Gerber is chief for:')
for p in people:
    if p.get_chief() == 'Paul Gerber':
        print(*p.get_name())