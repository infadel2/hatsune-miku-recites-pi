from matrix import Matrix
from hitobject import Object
from writer import Writer

offset = 3220      # when the first object starts
offset_add = 400   # ms to add each time digit is processed

with open('data/pi.txt', 'r', encoding='utf-8') as file:
    digits = list(file.read())
    
    for digit in digits:
        coordinates = Matrix.number(digit).split(',')
        hitcircle = Object.hitcircle(coordinates[0], coordinates[1], offset)
        
        Writer.append(f'{hitcircle}\n', 'output.txt')
        offset = offset + offset_add