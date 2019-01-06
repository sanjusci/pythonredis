import redis


class Redis(object):

    connect = None

    def __init__(self):
        self.connect = self.__connect()

    def __connect(self):
        if not self.connect:
            rc = redis.Redis(
                host='127.0.0.1',
                port=6379,
                password=''
            )
            return rc
        return self.connect

    def set(self, key, value, ex=None, px=None, nx=False, xx=False):
        """
        Function set
        :param key:
          A key that contains key.
        :param value:
          A value that contains value.
        :param ex:
          An ex sets an expire flag on key ``name`` for ``ex`` seconds.
        :param px:
          A px sets an expire flag on key ``name`` for ``px`` milliseconds.
        :param nx:
          A nx if set to True, set the value at key ``name`` to ``value`` only
            if it does not exist.
        :param xx:
          A xx if set to True, set the value at key ``name`` to ``value`` only
            if it already exists.
        :return:
        """
        r = self.connect
        r.set(key, value, ex=ex, px=px, nx=nx, xx=xx)

    def get(self, key):
        r = self.connect
        return r.get(key)


if __name__ == '__main__':
    r = Redis()
    choices = "1. SET\n2. GET\n3. Exit"
    while True:
        print(choices)
        choice = int(input("Enter your choice - "))

        if choice == 1:
            key = input("Enter key Name - ")
            value = input("Enter value - ")
            r.set(key, value)
        elif choice == 2:
            key = input("Enter key Name - ")
            print(r.get(key), '\n')
        elif choice == 3:
            break
        else:
            print("Invalid choice\n")

