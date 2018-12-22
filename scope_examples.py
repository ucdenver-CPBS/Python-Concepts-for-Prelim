# Global scope
x = "x: I'm global"
a = "a: I'm also global"


def fun1(y):
    print("y: " + y)  # local
    print(x)  # global


class Class1:
    z = "z: I'm local"  # local
    a = "a: I was redefined locally"

    print(z)

    def fun1(self, y):
        print("y: " + y)
        print(self.z)
        print(x)
        print(a)
        print(self.a)


if __name__ == '__main__':
    print(x)
    print(a)

    c = Class1()
    c.fun1("I'm local")
    fun1("I'm also local")
    # print(y)
    # print(z)
