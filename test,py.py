  

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