# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

"""
# שאלה 1:
def isAngram(s,t):

    if len(s) != len(t):
        return "False"
    if sorted (s) == sorted (t):
        return "True"
    else:
        return "False"

s = input("Enter a word: ")   # recieve the first string
t = input("Enter another word: ")   # recieve the second string

print(isAngram(s, t))
"""

"""
# שאלה 2:
def isPali(s):
    for i in range(len(s)//2):   # נרוץ על חצי מחרוזת כיוון שאם החצי הראשון שווה לחצי האחרון, אז גם בדיקה מהצד השני תהיה נכונה
        if s[i] != s[-i-1]:
            return False
    return True

s = input("enter a string: ")
print(isPali(s))
"""

"""
# שאלה 3:
def replace_second_most(s):
   WordChars = [] #רשימה המייצגת את התווים במחרוזת שהתקבלה
   SecondMost = [] #רשימה של int שמכניסה את מספר הפעמים של כל תו בכל מילה
   Count = [] #רשימה של מספר הפעמים, רק בסדר עולה

   #הכנסת כל התווים לרשימה ללא תו פעמיים וסידור הרשימה
   for char in s:
      if char not in WordChars:
         WordChars.append(char)
   WordChars.sort()
   #print(WordChars)

    #הכנסה של מספר הפעמים של כל תו במחרוזת באותו מיקום שנמצא בWordChars
   for i in range(len(WordChars)):
      SecondMost.append(s.count(WordChars[i]))
      Count.append(s.count(WordChars[i]))
   Count.sort() #סידור של התדירויות ברשימה נפרדת מגדול לקטן
   #print(SecondMost)
   #print(Count)

   if len(Count) == 1: #אם יש רק אות אחת אז זו התדירות
      x = Count[0]
   else:
      x = Count[-2]
   #print(x)

   SecondChar = ''
   for i in range(len(SecondMost) - 1, -1, -1): #מעבר מהסוף להתחלה כדי למצוא את התו הכי גדול לקסיקוגרפית
      if SecondMost[i] == x:
         SecondChar = WordChars[i]
         print(SecondChar)
         break

   result = ''
   for char in s:
      if char == SecondChar:
         result += '#'
      else:
         result += char

   return result

s = input("enter a string: ")
print(replace_second_most(s))
"""

"""
# שאלה 4:
def prime_factors(n):
   list1 = []

   if n == 2:
      list1.append(n)
      return list1

   else:
      is_prime = True
      for x in range(2, n+1): #מעבר על כל המספרים מ2 עד n על מנת לבדוק אם קיים מספר כזה בכלל
         if n % x == 0:
            #print('this is',x) #לצורך הבדיקה
            for i in range(2, x): #בדיקה של האם המספר שמתחלק ראשוני
               if x % i == 0:
                  is_prime = False
                  #print(i) #לצורך הבדיקה
                  #print(x)
                  break

            if is_prime:
               list1.append(x)
   return list1

n = int(input("enter a number: "))
print(prime_factors(n))
"""


# שאלה 5:

def smallest_Balanced_Index(lst):
   lst = []


# שאלה 6:
def pascal_triangle(n):
   


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
