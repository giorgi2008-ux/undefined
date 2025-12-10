def get_volume_of_cuboid(length, width, height):
    return length * width * height
print(get_volume_of_cuboid(2,5,6))

print("-----------------------")

def points(games):
    total = 0
    for game in games:
        x = int(game[0])  
        y = int(game[2])   
        
        if x > y:
            total += 3
        elif x == y:
            total += 1
        
        
    return total


print("-----------------------")

def other_angle(a, b):
    return 180 - (a + b)
