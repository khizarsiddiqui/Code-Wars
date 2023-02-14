  

                                                                   # CODE WARS SOLUTIONS

# splitting numbers and squaring them individualy and forming a string array of the sum

# def split_num(num):
#   s_num=str(num)
#   res=''
#   for i in range(len(s_num)):
#     res+= str(int(s_num[i])**2)
#   return int(res)


# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)

# num=9119
# print(split_num(num))

# COUNTING NUMBER OF 'X' AND 'O' IN A LIST

# def xo(s):
#   s = s.lower()
#   if s.count('x') == s.count('o'):
#     return True
#   else:
#     return False

# s='sdad'
# print(xo(s))


# SPLITTING ARRAY IN THE PAIR OF 2 AND REPLACING THE LAST REMAINING ODD ONE WITH A '_'

# def solution(s):
#     list_s=list(s)
#     res=[]
#     for i in range(0,len(s)):
#         if list_s[i]==0:
#             continue
#         if len(s) %2 ==0:
#             if i==len(s)-1:
#                 break
#             else:
#                 res.append(list_s[i]+list_s[i+1])
#                 list_s[i]=0
#                 list_s[i+1]=0
#         elif len(list_s) %2 != 0:
#             if i == len(list_s)-1:
#                 res.append(list_s[i]+'_')
#                 break
#             else:
#                 res.append(list_s[i]+list_s[i+1])
#                 list_s[i]=0
#                 list_s[i+1]=0      
#     return res

# s = 'abcdefg'
# print(solution(s))

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
# pairs = {'A':'T','T':'A','C':'G','G':'C'}
# def DNA_strand(dna):
#     return ''.join([pairs[x] for x in dna])

# dna = "ATTGC"
# print(DNA_strand(dna))


# An ATM ran out of 10 dollar bills and only has 100, 50 and 20 dollar bills. Given an amount between 40 and 10000 dollars (inclusive) 
# and assuming that the ATM wants to use as few bills as possible,  determinate the minimal number of 100, 50 and 20 dollar bills the ATM needs to dispense (in that order).

# def withdraw(n):
#     n50 = 0
#     n20, r = divmod(n, 20)
#     # print(n20,r)
#     if r == 10:
#         n20 -= 2
#         n50 += 1
#     n100, n20 = divmod(n20, 5)
#     return [n100, n50, n20]
# n = (60)
# print (withdraw(n))



# Your task is to write a function maskify, which changes all but the last four characters into '#'.

# def maskify(cc):
#     strlen=len(cc)
#     str1 = cc.replace(cc, '#' * strlen)
#     str1 = str1[:-4]
#     # print(str1)
#     str2=cc[-4:]  
#     # print(str2)
#     return "".join([str1,str2])


# def maskify2(cc):
#     return "#"*(len(cc)-4) + cc[-4:]

# cc = "SF$SDfgsd2eA"
# print(maskify2(cc))