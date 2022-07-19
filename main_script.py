

# print(m)

# for mm in m[0]:
#     print(mm)



def bubble_sort(l):
    list_length = len(l)
    for x in range(list_length):
        already_sorted = True

        for i in range(list_length - x - 1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]

                already_sorted = False
        if already_sorted:
            return l


def insertion_sort(l):
    for i in range(1, len(l)):
        key_item = l[i]
        j = i - 1

        while j >= 0 and l[j] > key_item:
            l[j], l[j+1] = key_item, l[j]
            j -= 1
    return l

def merge_sort(left, right):

    if(len(left) == 0):
        return right

    if(len(right) == 0):
        return left

    result = []
    left_index = right_index = 0

    while len(result) < len(left) + len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1


        if left_index == len(left):
            result += right[right_index:]
            break

        if right_index == len(right):
            result += left[left_index:]
            break

    return result


def merge(l):
    if len(l) < 2:
        return l

    midpoint = len(l) // 2

    return merge_sort(
        left = merge(l[:midpoint]),
        right = merge(l[midpoint:])
    )

# from collections import Counter
#
# s1 = 'worldd'
# s2 = 'worlddds'
#
# def scramble(s1, s2):
#
#     ct1 = Counter(s1)
#     ct2 = Counter(s2)
#
#     for i, j in ct2.items():
#         if j > ct1[i]:
#             return False
#     return True



from base64 import b64decode, b64encode

original = 'u!@4@Kh6daBmTbES'
# original = '1cTvFOizXmg2lkkQBvJEUZFdV7dC5jWs'
# print(original)
encoded = b64encode(original.encode('utf-8'))
print(encoded)
# decoded = b64decode(encoded).decode('utf-8')
# print(decoded)

user = 'cn=authdevproxymanager'
# proxypw = 'dSFANEBLaDZkYUJtVGJFUw=='
# dmppw = 'MWNUdkZPaXpYbWcybGtrUUJ2SkVVWkZkVjdkQzVqV3M='
print(b64decode(test).decode('utf-8'))
searchAttribute = 'uid'

# print(len(file_to_list))
# print(len(file_to_list_no_duplicate))

# with open('cfa_cfaone_20220421081401', 'w') as outputFile:
#     csvWriter = csv.writer(outputFile, delimiter='|', quoting=csv.QUOTE_NONE, escapechar='\\')
#     csvWriter.writerow(["CUSTID", "FNAME", "LNAME", "STREET", "SECONDARY", "CITY", "STATE", "POSTAL", "EMAIL", "PHONE",
#                         "CFAONE_SIGNUP_DATE"])
#
#     # read the lines into a list
#     lines = file_to_list_no_duplicate
#
#     # split the list into chunks of 1000
#     total_count = len(lines)
#     for i in range(0, len(lines), 1000):
#         chunk = lines[i:i + 1000]
#         if i % 1000000 == 0:
#             print("processed: {count} of {total}".format(count=i, total=total_count))
#         # Build the search filter
#         searchFilter = '(|'
#         for line in chunk:
#
#             # clean the data
#             inputSeparator = ''
#             if inputSeparator:
#                 searchValue = line.split(inputSeparator)[0]  # in case there are other values on the line
#             else:
#                 searchValue = line
#
#             inputCharsToStrip = ''
#             if inputCharsToStrip:
#                 for c in inputCharsToStrip:
#                     searchValue = searchValue.replace(c, "")
#
#             searchFilter += '({0}={1})'.format(searchAttribute, searchValue)
#         searchFilter += ')'
#         print(searchFilter)
import json
import pandas as pd
#
data_list = [{'mail': 'cateringAutomationTest@mailinator.com', 'givenName': 'Eric', 'mobile': '+1404 123 1234', 'sn': 'Stevens', 'zip': '30307', 'city': 'Atlanta', 'street': '123 Some St.', 'street2': 'Attn Eric', 'st': 'GA', 'uid': 'CFAID-0P1YU678J8D36PSV', 'loyaltyRegistrationDate': '20191121201734.305Z'}, {'mail': 'cateringAutomationTest2@mailinator.com', 'givenName': 'Eric', 'mobile': '+1404 123 1234', 'sn': 'Stevens', 'zip': '30307', 'city': 'Atlanta', 'street': '123 Some St.', 'street2': 'Attn Eric', 'st': 'GA', 'uid': 'CFAID-0PE3KD0PDBKCXL0Z', 'loyaltyRegistrationDate': None}, {'sn': 'familyName', 'givenName': 'firstName', 'uid': 'CFAID-5V9A5K9K17KWPGU7', 'mail': 'Auto9e49148a@cfatest.mailinator.com', 'street': '', 'street2': '', 'city': '', 'st': '', 'zip': '', 'mobile': '', 'loyaltyRegistrationDate': ''}]
# print(type(data_list))
# loyalty = data_list[0]['loyaltyRegistrationDate']
# print(loyalty)
# loyalty = loyalty.split('.')[0]+' UTC'
# print(loyalty)
#
df = pd.DataFrame(data_list)
# print(df[ (df['loyaltyRegistrationDate'].str.len() <= 0) | (df['loyaltyRegistrationDate'].isnull())])
# print(df[['mail', 'uid', 'givenName']].head(1))


# data_to_json = [json.dumps(x) for x in data_list]
# df1 = pd.DataFrame(data_to_json)
# print(df1)

# from typing import List
#
# names = ['Allwyn Pereira', 'Zach Truman', 'Percy Khambatta', 'Silvia Lehman', 'John Adizes']
#
# def convertList(testList) -> (List, List):
#     firstList = []
#     secondList = []
#     aTom = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
#     for name in testList:
#         first, last = name.split(" ")
#         if last[0] in aTom:
#             firstList.append(name)
#         else:
#             secondList.append(name)
#
#     return (firstList, secondList)
#
# first, second = convertList(names)
# print(first)
# print(second)