
import functions as func
figure = input('Введіть назву фігури для пошуку площі(Квадрат, Коло, Прямокутник) : ')
if figure == 'Квадрат':
    a = int(input('Введіть довжину сторони : '))
    func.square(a)
elif figure == 'Коло':
    a = int(input('Введіть довжину радіуса : '))
    func.circle(a)
elif figure == 'Прямокутник':
    a = int(input('Ведіть довжину : '))
    b = int(input('Введіть ширину : '))
    func.rectangle(a,b)