from phone_dict import PhoneBook
from input_module import data_in

print 'Welcome to phone-book!'.center(50)
print 'Options:'.center(50)

phone_book = PhoneBook()

phone_book.contacts = {'olya': '543', 'dima': '321', 'alla': '123'}


def f():
    return

print type(phone_book._show_options)
print type(phone_book._show_options())

while True:
    phone_book._show_options()
    print phone_book.book_opt
    print phone_book.__dict__
    print phone_book.book_opt.keys()
    a=raw_input('Choose option:')

    if a in phone_book.book_opt.keys():
        phone_book.book_opt[a](data_in('Enter name'), data_in('Enter msisdn'))
    elif a == 'exit':
        break
    else:
        print 'Choose correct option: {}'.format(phone_book.book_opt.keys())

#    print '--------------------------------------------'
#    print '1. Create contact'
#    print '2. Find contact'
#   print '3. Update contact by name'
#    print '4. Delete contact by name'
#   print '5. List all contacts'
#    print ''
#    print '6. Save in file\n7. Load from file\n8. Exit'
#
#    a=raw_input('Choose option:')#
#if a == '1':
