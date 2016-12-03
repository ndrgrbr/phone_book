def data_in (t):
    while True:
        try:
            x = raw_input(t)
            if x != '':
                return x
                break
            raise NameError('Empty value. Try again:')
        except NameError as e:
            print e