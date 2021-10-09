# book = dict()
# count = int(input())
n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break
# for i in range(count):
#     name_phone = input().split(" ")
#     book[name_phone[0]] = name_phone[1]

# for y in range(count):
#     search = input()
#     if book.get(search) == None:
#         print('Not found')
#     else:
#         print(search+'='+book[search])

# book = dict()
# string = 'teste '
# lista = string.rstrip().split(' ')
# if len(lista) < 1:
#     print('xpto')
# else:
#     print('zpto')
# fhand = open('dict_test_case.txt')
# for line in fhand:
#     name_phone = line.rstrip().split(' ')
#     name=name_phone[0].rstrip()
#     phone=''
#     if len(name_phone) <= 1:
#         book[name] = phone.rstrip()  
#     else:       
#         #print(book[name_phone[0]])
#         if not name.rstrip().isnumeric():  
#        # if not book[name_phone[0]].rstrip().isnumeric():            
#              book[name] = name_phone[1].rstrip()

# fhand2 = open('dict_test_search.txt')
# for lines in fhand2:
#     search = lines.rstrip()
#     if book.get(search) == None:
#         print('Not found')
#     else:
#         print(search+'='+book[search])