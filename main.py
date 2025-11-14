#successfully pushed to git 
import tabulate
import datetime
import csv
import os
print('Welcome to your personal expense tracker:')
print('1. Add expense')
print('2. View expenses')
print('3. Remove expense')
print('4. Show total expense')
print('5. Quit')

os.makedirs('/home/tathagatkr/Documents/expense_tracker', exist_ok=True)

def write_header():
    if not os.path.exists('/home/tathagatkr/Documents/expense_tracker/data.csv'):
        with open('/home/tathagatkr/Documents/expense_tracker/data.csv','w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['date','category','amount','note'])

def add_expense():
    time=datetime.datetime.now().date()
    category=input('Enter category:')
    amount=float(input('Enter amount:'))
    note=input('Enter note:')
    with open('/home/tathagatkr/Documents/expense_tracker/data.csv','a') as f:
        file=csv.writer(f)
        file.writerow([time,category,amount,note])
    print('Saved an expense...')
def view_expense():
    with open('/home/tathagatkr/Documents/expense_tracker/data.csv','r') as f:
        data=list(csv.reader(f))
        if not data[1:]:
            print('No expense is added.')
            return
        table=[[i,*row] for i,row in enumerate(data)]
        print(tabulate.tabulate(table[1:],headers=data[0],tablefmt='fancy-grid'))

def remove_expense():
    with open('/home/tathagatkr/Documents/expense_tracker/data.csv','r') as f:
        data=list(csv.reader(f))
        if not data[1:]:
            print('No expense is added.')
            return
        required_row=input('Enter the number of row to remove:')
        if int(required_row)>=1:
            try:
                data.pop(int(required_row))
            except IndexError:
                print('Index is not valid')

        else:
            print('please enter a valid row to remove')

    with open('/home/tathagatkr/Documents/expense_tracker/data.csv','w') as f:
        file=csv.writer(f)
        file.writerows(data)
def total_expense():
    total=0
    with open('/home/tathagatkr/Documents/expense_tracker/data.csv','r') as f:
        data=list(csv.reader(f))
        expenses=data[1:]
        for expense in expenses:
            total+=float(expense[2])
    print(total)
def main():
    write_header()
    while True:
        try:
            choice=input('Enter choice:')
            if choice=='1':
                add_expense()
            elif choice=='2':
                view_expense()
            elif choice=='3':
                remove_expense()
            elif choice=='4':
                total_expense()
            elif choice.lower() in ['5', 'quit', 'Quit', 'EXIT']:
                print('exiting...')
                break
        except (ValueError,IndexError,TypeError) as error:
            print(f'Error occured {error}')
            continue

main()

