
e "help", "copyright", "credits" or "license" for more information.
>>> balance = 0.0
>>> debt = 0.0
>>> daily_limit = 100
>>> daily_added = 0
>>> rides = 0
>>>
>>> operations = []  # son əməliyyatlar üçün
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>> balance = 0.0
>>> debt = 0.0
>>> daily_limit = 100
>>> daily_added = 0
>>> rides = 0
>>>
>>> operations = []  # son əməliyyatlar üçüncorrect_pin = "1234"
>>> attempts = 0
>>>
>>> while attempts < 3:
...         pin = input("PIN daxil et: ")
...
PIN daxil et:     if pin == correct_pin:
PIN daxil et:         print("Giriş uğurludur")
PIN daxil et:         break
PIN daxil et:     else:
PIN daxil et:         print("Yanlış PIN")
PIN daxil et:         attempts += 1
PIN daxil et:
PIN daxil et: if attempts == 3:
PIN daxil et:     print("3 dəfə səhv daxil etdiniz. Proqram bağlandı.")
PIN daxil et:     exit()while True:
PIN daxil et:     print("\n1) Balansı göstər")
PIN daxil et:     print("2) Balans artır")
PIN daxil et:     print("3) Gediş et")
PIN daxil et:     print("4) Son əməliyyatlar")
PIN daxil et:     print("5) Günlük statistika")
PIN daxil et:     print("6) Parametrlər")
PIN daxil et:     print("0) Çıxış")
PIN daxil et:
PIN daxil et:     choice = input("Seçim et: ")if choice == "1":
PIN daxil et:         print("Balans:", balance)elif choice == "2":
PIN daxil et:         amount = float(input("Məbləğ daxil et: "))
PIN daxil et:
PIN daxil et:         if amount <= 0:
PIN daxil et:             print("Yanlış məbləğ!")
PIN daxil et:         elif daily_added + amount > daily_limit:
PIN daxil et:             print("Limit aşılır!")
PIN daxil et:         else:
PIN daxil et:             daily_added += amount
PIN daxil et:
PIN daxil et:             if debt > 0:
PIN daxil et:                 if amount >= debt:
PIN daxil et:                     amount -= debt
PIN daxil et:                     debt = 0
PIN daxil et:                 else:
PIN daxil et:                     debt -= amount
PIN daxil et:                     amount = 0
PIN daxil et:
PIN daxil et:             balance += amount
PIN daxil et:
PIN daxil et:             operations.append(("Artırma", amount, 0, balance))
PIN daxil et:
PIN daxil et:             print("Yeni balans:", balance)elif choice == "3":
PIN daxil et:         rides += 1
PIN daxil et:
PIN daxil et:         if rides == 1:
PIN daxil et:             price = 0.40
PIN daxil et:         elif 2 <= rides <= 4:
PIN daxil et:             price = 0.36
PIN daxil et:         else:
PIN daxil et:             price = 0.30
PIN daxil et:
PIN daxil et:         if balance >= price:
PIN daxil et:             balance -= price
PIN daxil et:             operations.append(("Gediş", price, 0.40 - price, balance))
PIN daxil et:             print("Keçid edildi. Balans:", balance)
PIN daxil et:
PIN daxil et:         elif 0.30 <= balance < 0.40:
PIN daxil et:             print("Təcili keçid istifadə olundu")
PIN daxil et:             balance -= 0.30
PIN daxil et:             debt += 0.10
PIN daxil et:             operations.append(("Təcili keçid", 0.30, 0.10, balance))
PIN daxil et:         else:
PIN daxil et:             print("Balans kifayət deyil!")
PIN daxil et:             rides -= 1elif choice == "4":
PIN daxil et:         n = int(input("Neçə əməliyyat görmək istəyirsən: "))
PIN daxil et:         for op in operations[-n:]:
PIN daxil et:             print(op)elif choice == "5":
PIN daxil et:         print("Gediş sayı:", rides)
PIN daxil et:         print("Artırılan pul:", daily_added)elif choice == "0":
PIN daxil et:         print("Proqram bitdi")
PIN daxil et:         breaktotal_spent = 0
PIN daxil et: total_discount = 0
PIN daxil et: mode = "normal"  # rejimelif choice == "3":
PIN daxil et:
PIN daxil et:     if mode == "student":
PIN daxil et:         price = 0.20
PIN daxil et:         discount = 0.20
PIN daxil et:     elif mode == "pension":
PIN daxil et:         price = 0.15
PIN daxil et:         discount = 0.25
PIN daxil et:     else:
PIN daxil et:         rides += 1
PIN daxil et:         if rides == 1:
PIN daxil et:             price = 0.40
PIN daxil et:         elif 2 <= rides <= 4:
PIN daxil et:             price = 0.36
PIN daxil et:         else:
PIN daxil et:             price = 0.30
PIN daxil et:         discount = 0.40 - price
PIN daxil et:
PIN daxil et:     if balance >= price:
PIN daxil et:         balance -= price
PIN daxil et:         total_spent += price
PIN daxil et:         total_discount += discount
PIN daxil et:
PIN daxil et:         operations.append(("Gediş", price, discount, balance))
PIN daxil et:         print("Keçid edildi. Balans:", balance)
PIN daxil et:
PIN daxil et:     elif 0.30 <= balance < 0.40 and mode == "normal":
PIN daxil et:         print("Təcili keçid istifadə olundu")
PIN daxil et:         balance -= 0.30
PIN daxil et:         debt += 0.10
PIN daxil et:
PIN daxil et:         total_spent += 0.30
PIN daxil et:         total_discount += 0.10
PIN daxil et:
PIN daxil et:         operations.append(("Təcili keçid", 0.30, 0.10, balance))
PIN daxil et:     else:
PIN daxil et:         print("Balans kifayət deyil!")elif choice == "5":
PIN daxil et:     print("Gediş sayı:", rides)
PIN daxil et:     print("Ümumi ödəniş:", total_spent)
PIN daxil et:     print("Ümumi endirim:", total_discount)
PIN daxil et:     print("Artırılan pul:", daily_added)elif choice == "6":
PIN daxil et:     print("1) Limit dəyiş")
PIN daxil et:     print("2) Rejim seç")
PIN daxil et:
PIN daxil et:     p = input("Seçim: ")
PIN daxil et:
PIN daxil et:     if p == "1":
PIN daxil et:         new_limit = float(input("Yeni limit: "))
PIN daxil et:         if new_limit > 0:
PIN daxil et:             daily_limit = new_limit
PIN daxil et:             print("Limit dəyişdi")
PIN daxil et:         else:
PIN daxil et:             print("Yanlış dəyər!")
PIN daxil et:
PIN daxil et:     elif p == "2":
PIN daxil et:         print("1) Normal")
PIN daxil et:         print("2) Tələbə (0.20)")
PIN daxil et:         print("3) Pensiyaçı (0.15)")
PIN daxil et:
PIN daxil et:         m = input("Seç: ")
PIN daxil et:
PIN daxil et:         if m == "1":
PIN daxil et:             mode = "normal"
PIN daxil et:         elif m == "2":
PIN daxil et:             mode = "student"
PIN daxil et:         elif m == "3":
PIN daxil et:             mode = "pension"
PIN daxil et:         else:
PIN daxil et:             print("Yanlış seçim!")
PIN daxil et:
PIN daxil et:         print("Rejim:", mode)elif choice == "4":
PIN daxil et:     n = int(input("Neçə əməliyyat görmək istəyirsən: "))
PIN daxil et:
PIN daxil et:     for op in operations[-n:]:
PIN daxil et:         print(f"Tip: {op[0]}, Məbləğ: {op[1]}, Endirim: {op[2]}, Balans: {op[3]}")