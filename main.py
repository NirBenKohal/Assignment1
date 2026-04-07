# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


"""
def isPali(s):
    for i in range(len(s)//2): #נרוץ על חצי מחרוזת כיוון שאם החצי הראשון שווה לחצי האחרון, אז גם בדיקה מהצד השני תהיה נכונה
        if s[i] != s[-i-1]:
            return False
    return True

s = input("enter a string: ")
print(isPali(s))

#שאלה 3:
#   def replace_second_most(s):




#   שאלה 4:
def prime_factors(n):
    list1 = []
    if n == 2:
        list1.append(n)
        return list1
    else:
        is_prime = True
        for x in range(2, n+1): #מעבר על כל המספרים מ2 עד n על מנת לבדוק אם קיים מספר כזה בכלל
            if n % x == 0:
                for i in range(2, x): #בדיקה של האם המספר שמתחלק ראשוני
                    if x % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    list1.append(x)

        return list1

n = int(input("enter a number: "))
print(prime_factors(n))
"""

#שאלה 5:

def smallest_Balanced_Index(lst):
    lst = []




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
