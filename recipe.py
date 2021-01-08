print("""
Many recipe books still use cups, tablespoons and teaspoons to describe the volumes of ingredients used
when cooking or baking. While such recipes are easy enough to follow if you have the appropriate
measuring cups and spoons, they can be difficult to double, triple or quadruple when cooking Christmas
dinner for the entire extended family. For example, a recipe that calls for 4 tablespoons of an ingredient
requires 16 tablespoons when quadrupled. However, 16 tablespoons would be better expressed (and
easier to measure) as 1 cup.
Write a function that expresses an imperial volume using the largest units possible. The function will take
the number of units as its first parameter, and the unit of measure (cup, tablespoon or teaspoon) as its
second parameter. Return a string representing the measure using the largest possible units as the
function’s only result.
For example, if the function is provided with parameters representing 59 teaspoons then it should return
the string “1 cup, 3 tablespoons, 2 teaspoons”.
Hint: One cup is equivalent to 16 tablespoons. One tablespoon is equivalent to 3 teaspoons.
Name your file as recipe.py. """)


TSP_PER_TSBP = 3
TSP_PER_CUP =48

def reduceMeasure(num , unit):
    unit = unit.lower()
unit = unit.lower()

if unit == "teaspoon" or unit == 'teaspoons':
    teaspoons = num
elif unit == "tablespoon" or unit == "tablespoons" :
    teaspoons = num * TSP_PER_TSBP
elif unit == "cup" or unit == "cups" :
    teaspoons = num * TSP_PER_CUP

cups = teaspoons // TSP_PER_CUP
teaspoons = teaspoons - cups * TSP_PER_CUP
tablespoons = teaspoons // TSP_PER_TSBP
teaspoons = teaspoons - tablespoons * TSP_PER_TSBP

result = " "

if cups > 1:
    result = result + "s"

if tablespoons > 0:

    if result != "":
        result = result + ", "

result = result + str(tablespoons)+" tablespoon"

if teaspoons > 1:
    result = result + "s"

if result == " ":
    result = "0 teaspoons"

return result

def main ():
    print("59 teaspoons is %s." % reduceMeasure(59, "teaspoons"))
    print("59 tablespoons is %s." % reduceMeasure(59, "tablespoons"))
    print("1 teaspoon is %s." % reduceMeasure(1, "teaspoon"))
    print("1 tablespoon is %s." % reduceMeasure(1, "tablespoon"))
    print("1 cup is %s." % reduceMeasure(1, "cup"))
    print("4 cups is %s." % reduceMeasure(4, "cups"))
    print("3 teaspoons is %s." % reduceMeasure(3, "teaspoons"))
    print("6 teaspoons is %s." % reduceMeasure(6, "teaspoons"))
    print("95 teaspoons is %s." % reduceMeasure(95, "teaspoons"))
    print("96 teaspoons is %s." % reduceMeasure(96, "teaspoons"))
    print("97 teaspoons is %s." % reduceMeasure(97, "teaspoons"))
    print("98 teaspoons is %s." % reduceMeasure(98, "teaspoons"))
    print("99 teaspoons is %s." % reduceMeasure(99, "teaspoons"))

main()
