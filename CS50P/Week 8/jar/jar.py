class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity
        self.size=0


    def __str__(self):
        return "🍪" * self.size


    def deposit(self, n):
        if n<0:
            raise ValueError("Not negative")
        if self._size+n>self._capacity:
            raise ValueError("Out of capacity")
        self._size+=n


    def withdraw(self, n):
        if n>self._size:
            raise ValueError("Not enough")
        self._size-=n

    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self, value):
        if value<1:
            raise ValueError("@capacity.setter error")
        self._capacity=value


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if size<0:
            raise ValueError("@size.setter error")
        if size>self._capacity:
            raise ValueError("@size.setter error")

        self._size=size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)

if __name__=="__main__":
    main()
