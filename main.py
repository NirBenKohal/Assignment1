# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# שאלה 1:
def isAngram(s,t):

    if len(s) != len(t):
        return "False"
    if sorted (s) == sorted (t):
        return "True"
    else:
        return "False"

s = 'rat'   # recieve the first string
t = 'tar'   # recieve the second string

print(isAngram(s, t))



# שאלה 2:
def isPali(s):
    SNew = s.replace(' ', '').lower()
    for i in range(len(s)//2):   # נרוץ על חצי מחרוזת כיוון שאם החצי הראשון שווה לחצי האחרון, אז גם בדיקה מהצד השני תהיה נכונה
        if SNew[i] != SNew[-i-1]:
            return False
    return True

s = 'A man a plan a canal panama'
print(isPali(s))



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

s = 'niirrr'
print(replace_second_most(s))



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
                  #print(x) #לצורך הבדיקה
                  break

            if is_prime:
               list1.append(x)
         is_prime = True
   return list1

n = 60
print(prime_factors(n))


# שאלה 5:
def smallest_Balanced_Index(lst):
   if not lst:
      return -1

   for i in range(len(lst)):
      left = sum(lst[:i])
      # print('left= ', left)

      right=1
      for num in lst[i+1:]:
         right *= num
         # print('right= ', right)

      if right == left:
         return i

   return -1

lst = [3, 2, 1, 7, 3]
print(smallest_Balanced_Index(lst))



# שאלה 6:
def pascal_traingle(n):
   if n <= 0:
      return

   triangle = []

   for i in range(n):
      current_row = []
      for j in range(i + 1):
         if j == 0 or j == i:
            current_row.append(1)
         else:
            left_number = triangle[i - 1][j - 1]
            right_number = triangle[i - 1][j]
            current_sum = left_number + right_number
            current_row.append(current_sum)

      triangle.append(current_row)

   string_rows = []

   for row in triangle:
      row_text = ""
      for num in row:
         row_text = row_text + str(num) + " "
      row_text = row_text.strip()
      string_rows.append(row_text)

   max_length = len(string_rows[-1])

   for row_text in string_rows:
      print(row_text.center(max_length))

n = 5
pascal_traingle(n)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
