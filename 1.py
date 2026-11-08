def calculate_savings(monthly_deposit, target_amount):
     current_savings = 0
     month = 1
     while current_savings < target_amount:
         current_savings += monthly_deposit

         if month % 6 == 0:
            current_savings =- 5000

         print("Месяц", month)
         print("Накоплено", current_savings)
         month += 1
     return current_savings

print("Начинаем расчёт накоплений...")

calculate_savings(10000, 100000)
