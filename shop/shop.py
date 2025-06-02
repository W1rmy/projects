tovari = {
  "плов" : 6, "лепёшечка" : 9, "Ачик-чучук" : 10, "Самса" : 3, "бэляш" : 7, 
  "Шурпа" : 9, "Такмач" : 5, "Эчпочмак" : 4, "Чебурек" : 8, "Картошка" : 2,
  "Чай" : 10, "Кофе" : 10, "Молоко" : 10, "Натахтаре" : 7
}

zakas = input("Введите закас: (В конце звказа введите 'Стоп закас')")
while zakas != "Стоп закас":
  if zakas == "admin":
    password = input("введите пароль: ")
    if password == "admin":
      while True:
        panel_admina = input("Что вы хотите сделать(1 - добавить товар, 2 - удалить товар 3 - изменить количество товара, 4 - вывод каталога, выход из панели админа - adminStop): ")

        if panel_admina == 'adminStop':
          print("Вы вышли из панели админа")
          zakas = input("Введите закас: (В конце звказа введите 'Стоп закас')")
          break
          
        if panel_admina == "1":
          kakoy_tovar = input("Какой товар вы хотите добавить: ")
          skolko_tovara = int(input(f"Сколько {kakoy_tovar} вы хотите добавить: "))
  
          if kakoy_tovar in tovari:
            print("Такой товар уже есть")
          elif skolko_tovara < 0:
            print("Не правильный вод")
          else:
            tovari[kakoy_tovar] = skolko_tovara
        elif panel_admina == "2":
          del_tovar = input("Какой товар вы хотите удалить: ")
          if del_tovar in tovari:
            tovari.pop(del_tovar)
          else:
            print('')
        elif panel_admina == "3":      
          delta_tovar = input("количество какого товара вы хотите изменить: ")
          if delta_tovar in tovari:
            chto_sdelat = input('Что вы хотите сделать(1 - добавить, 2 - убавить): ')
            if chto_sdelat == "1":
              skolko_vi_xotite_dobavit = int(input("Сколько товара вы хотите добавить: "))
              tovari[delta_tovar] += skolko_vi_xotite_dobavit
            elif chto_sdelat == "2":
              skolko_vi_xotite_ybavit = int(input("Сколько товара вы хотите убавить: "))
              if skolko_vi_xotite_ybavit > tovari[delta_tovar]:
                tovari[delta_tovar] = 0
              else:
                tovari[delta_tovar] -= skolko_vi_xotite_ybavit
            else:
              print("Не правильный вод")
          else:
            print("Данного товара нет")
        elif panel_admina == "4":
          print(tovari)
        else:
          print("Данной команды нет :(") 
    else:
       print("Неверный пароль")
  else:
    if zakas in tovari:
      if tovari[zakas] > 0:
        tovari[zakas] -= 1
        print(f"Вы закали {zakas}, осталось {tovari[zakas]} штук")
      else: 
        print("Товар закончился")
    else:
      print("Данного товара нет")

    zakas = input("Введите закас: (В конце звказа введите 'Стоп закас')")
    








