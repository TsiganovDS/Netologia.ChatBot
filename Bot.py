
HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = []
today = []
tomorrow = []
owner = []

run = True
while run:
  command = input("Введите команду: ")
  if command == 'help':
      print(HELP)
  elif command == 'show':
      print(tasks)
  elif command == 'add':
      task = input("Введите название задачи: ")
      date = input("Введите дату выполнения задачи:")
      if date == "Сегодня":
          today.append(task)
      elif date == "Завтра":
          tomorrow.append(task)
      else:
          owner.append(task)
      print(f"Задача {task} добавлена")
      tasks.append(task)
  elif command == 'exit':
      print("Спасибо за использование! До свидания!")
      break
  else:
      print("Неизвестная команда")
      run = False

print("До свидания!")