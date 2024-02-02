
def calc_all():
    global expenses_min
    global expenses_norm
    global cur_income

#def calc_expenses():
    x1_wife = 75000
    x2_mortage = 36000
    x_all = x1_wife + x2_mortage

    z1_tts = 1000
    z2_food_min = 22 * 50
    z2_food_max = 22 * 300
    z3_some_for_family = 4000
    z3_some_purchases = 4000

    expenses_min = x_all #+ z2_food_min
    expenses_norm = x_all + z1_tts + z2_food_max
    expenses_max = expenses_norm + z3_some_for_family + z3_some_purchases

    print("cur expenses min:", expenses_min)
    print("cur expenses norm:", expenses_norm)
    print("cur expenses max:", expenses_max)


#def calc_income():

    x1_salary = 106000
    x2_shir = 14500
    x3_en56 = 10500

    cur_income = x1_salary + x2_shir + x3_en56

    print("cur income:", cur_income)

    add_min = cur_income - expenses_min
    add_norm = cur_income - expenses_norm
    add_max = cur_income - expenses_max

    cur_assets = 70000

    print("add_min:", add_min)
    print("add_norm:", add_norm)
    print("add_max:", add_max)
    print("cur_assets:", cur_assets)
    print()

    k1 = cur_assets
    k2 = cur_assets
    k3 = cur_assets

    for i in range(0, 12):

        k1 += add_min
        k2 += add_norm
        k3 += add_max

        print(i+1, k1, k2, k3)

def calc_credit():
    global expenses_min
    global expenses_norm
    
    #credit = 1000000
    #pay = 22753

    credit = 720000
    pay = 15300

    for i in range(0, 60):
        dd = (pay + expenses_min)
        credit -= dd
        print(i+1, credit)

def calc_small_salary():
    global expenses_norm
    global cur_income
    
    #credit = 1000000
    #pay = 22753

    credit = 720000
    pay = 15300

    for i in range(0, 60):
        new_income = cur_income - 36000 #70k
        credit += new_income - (pay + expenses_norm)
        print(i+1, credit)

def print_title(title):

    print(";---", title, end='')
    for i in range(0, 92):
        print('-', end='')
    print("\n", end='')


def main():

    print_title("current")
    calc_all()

    print_title("calc_credit")
    calc_credit()

    #print_title("calc_small_salary")
    #calc_small_salary()


if __name__ == '__main__':
    main()
