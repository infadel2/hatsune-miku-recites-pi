from matrix import Matrix
from hitobject import Object

offset = 3220      # when the first object starts
offset_add = 400   # ms to add each time digit is processed

with open('data/pi.txt', 'r', encoding='utf-8') as file:
    digits = list(file.read())
    
    for digit in digits:
        coordinates = Matrix.number(digit).split(',')
        hitcircle = Object.hitcircle(coordinates[0], coordinates[1], offset)
        
        print(hitcircle)
        offset = offset + offset_add