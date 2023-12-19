#Напишите программу которая настроит отображение
#комментария к отметке 'мне нравится' в условном посте. Список
#имен передается в кач-ве аргумента.
#Например:
#[]     -->  "no one likes this"
#["Peter"]   -->  "Peter likes this"
#["Jacob", "Alex"]  -->  "Jacob and Alex like this"
#["Max", "John", "Mark"]  -->  "Max, John and Mark like this"
#["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

name = ["Alex", "Jacob", "Mark", "Max", "Alex", "Jacob"]

if len(name) == 0:
    print("No one likes this")
elif len(name) == 1:
    print("Peter likes this")
elif len(name) == 2:
    print(name[0], "and", name[1], "ike this")
elif len(name) == 3:
    print(name[0],",", name[1], "and", name[2], "like this")
else:
    print(name[0], ",", name[1], "and", len(name) - 2, "like this")
    


