


class PhoneBook(object):
    def __init__(self):
        self.contacts = {}
        self.book_opt = {}

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(['{}={}'.format(name, msisdn) for name, msisdn in self.__dict__.items()])
        )

    def add_contact(self, *param):
        self.contacts[param[0]] = param[1]
        return self.contacts.get(param[0])

    def find_contact(self, name):
#        print '{}: {}'.format(name, self.contacts.get(name))
        try:
            return self.contacts.get(name)
        except:
            raise NameError('Not found')

    def update_contact(self, name, msisdn):
        try:
            self.contacts[self._find_contact(name)] = msisdn
        except:
            print 'X'

    def delete_contact(self, name):
        return

    def _show_options(self):
        k = 0
        for i in self.__dict__:
            if not str(i).startswith('___'):
                k += 1
                self.book_opt[str(k)] = i
                print '{}. {}'.format(k, i)




