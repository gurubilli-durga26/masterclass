'''
#string plaindrome or not
string=input('enter:')
rev=string[::-1]
if string==rev:
    print("palindrome")
else:
    print("not palindrome")
    

Example 1:
Input: string str=”Take u forward is Awesome”
Output: 
Vowels: 10
Consonants: 11
White spaces: 4
Explanation:
'
string=input('enter a string:')
vow_count=0
con_count=0
space_count=0
for i in range(len(string)):
    if string[i] in 'AEIOUaeiou':
        vow_count+=1
    elif string[i]==' ':
        space_count+=1
    else:
        con_count+=1
print(f'vowel count is {vow_count}')
print(f'consonants count is {con_count}')
print(f'white spaces count is {space_count}')


Example 1:
Input: c = ‘A’
Output: 65
Explanation: ASCII value of A is 65

ch=input('enter:')
print(ord(ch))

Example 1:
Input: Str = “take u forward”
Output: tk  frwrd
Explanation: All vowels are removed from the given String.

string=input('enter:')
result=''
for ch in string:
    if ch not in 'AEIOUaeiou':
        result=result+ch
print(result)

Example 1:
Input: str = “Take you forward” 
Output: Takeyouforward
Explanation: After removing all the whitespaces Takeyouforward is the result

string=input('enter:')
result=''
for ch in string:
    if ch not in ' ':
        result=result+ch
print(result)

Example 1:
Input: string str = "take12% *&u ^$#forward"
Output: takeuforward
Explanation:
Characters 1,2,%,*,&,^,$,# along with whitespaces are 
removed but the order of remaining alphabets is preserved.

string=input('enter:')
result=''
for ch in string:
    if ch not in '!@#$%^&*0123456789 ':
        result=result+ch
print(result)

Examples:
INPUT: HELLO
OUTPUT: OLLEH

string=input('enter:')
reverse=''
for ch in string:
    reverse=ch+reverse
print(reverse)

Example 1:
Input: “a+((b-c)+d)”
Output: “a+b-c+d”
Explanation: Removed all the brackets in the algebric expression.

string=input('enter:')
result=''
for ch in string:
    if ch not in '()':
        result=result+ch
print(result)

Example 1:
Input: String str = "take u forward is awesome"
Output: “TakE U ForwarD IS AwesomE”
Explanation: We get the result after capitalizing the first and last character of each word of a string

string=input('enter:').title()
print(string)


Example 1:
Input: takeuforward
Output: a2 d1 e1 f1 k1 o1 r2 t1 u1 w1 
Explanation: Count of every character of string is printed.
'''

s = input("Enter a string: ")
d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
for ch in sorted(d):
    print(ch, d[ch], end=" ")