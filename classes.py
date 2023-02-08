from datetime import datetime


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def move(self):
        print("move method")

    def draw(self):
        print("draw method")

    # this __str__ method determines what happens when you print an instance of the class
    def __str__(self) -> str:
        return f"Coordinate: <{self.x},{self.y}>"

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __repr__(self):
        return "Coordinate(" + str(self.x) + "," + str(self.y) + ")"


point1 = Coordinate(3, 4)
print(point1.x)
point1.x = 2
print(point1.x)
point1.move()

origin = Coordinate(0, 0)
print(f"{origin.x} , {origin.y}")
print(f"{point1.x} , {point1.y}")
print(point1)

# both these lines do the same thing but
# calling .distance on the object (point1) means you already have the self parameter
# calling .distance on the class means you need to specify each parameter
print(point1.distance(origin))
print(Coordinate.distance(point1, origin))


class Human:
    def __init__(self, name) -> None:
        self.name = name

    def talk(self, phrase="I am a talking Human"):
        return phrase


class NamedHuman(Human):
    def __init__(self, name) -> None:
        super().__init__(name)

    def talk(self):
        return Human.talk(self) + ". My name is " + self.name + "."


class ExcitedHuman(NamedHuman):
    def __init__(self, name, excitedLevel) -> None:
        super().__init__(name)
        self.excitedLevel = excitedLevel

    def talk(self):
        # using class parents for talk to build a longer string
        return NamedHuman.talk(self) + " My excitement level is " + self.excitedLevel


# create an object fella1 from the class Person with the name Jim
fella1 = Human("Jim")
print(fella1.talk())

lady1 = NamedHuman("Wendy")
print(lady1.talk())

chap1 = ExcitedHuman("Barry", "5 out of 5!")
print(chap1.talk())


class Mammal:
    def walk(self):
        print("walking")


class Dog(Mammal):
    def speak(self):
        print("woof woof")


class Cat(Mammal):
    def speak(self):
        print("Meeeooowww")


baxter = Dog()
lilly = Cat()

baxter.walk()
baxter.speak()
lilly.walk()
lilly.speak()


class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self):
        time = "6:30"
        print(self.time)


clock = Clock("5:30")
clock.print_time()


class Fraction(object):
    def __init__(self, numer, denom) -> None:
        self.numer = numer
        self.denom = denom

    def __str__(self) -> str:
        return f"{self.numer} / {self.denom}"

    def getNumer(self):
        return self.numer

    def getDenom(self):
        return self.denom

    def __add__(self, other):
        numerNew = (
            other.getDenom() * self.getNumer() + other.getNumer() * self.getDenom()
        )
        denomNew = other.getDenom() * self.getDenom()
        return Fraction(numerNew, denomNew)

    def __sub__(self, other):
        numerNew = (
            other.getDenom() * self.getNumer() - other.getNumer() * self.getDenom()
        )
        denomNew = other.getDenom() * self.getDenom()
        return Fraction(numerNew, denomNew)

    def convert(self):
        return self.getNumer() / self.getDenom()


oneHalf = Fraction(1, 2)
twoThirds = Fraction(2, 3)

print(oneHalf)
print(twoThirds)
print(oneHalf.numer)
print(oneHalf.denom)

addingFraction = oneHalf + twoThirds
print(addingFraction)

subingFraction = twoThirds - oneHalf
print(subingFraction)

print(oneHalf.convert())


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + " not found")

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return "{" + ",".join([str(e) for e in self.vals]) + "}"

    def interlace(self, s2):
        """Returns a new intSet of two lists interlaced"""
        result = intSet()
        l1 = len(self.vals)
        l2 = len(s2)
        if max(l1, l2) == 0:
            return result
        else:
            for i in range(max(l1, l2)):
                if i < l1:
                    result.insert(self.vals[i])
                if i < l2:
                    result.insert(s2[i])
            return result

    def intersect2(self, s2):
        """Returns a new intSet of just the common elements of two lists"""
        result = intSet()
        l1 = len(self)
        l2 = len(s2)
        if max(l1, l2) == 0:
            return result
        else:
            for i in range(max(l1, l2)):
                if i < l1:
                    if self.vals[i] in s2.vals:
                        result.insert(self.vals[i])
                if i < l2:
                    if s2.vals[i] in self.vals:
                        result.insert(s2.vals[i])
            return result

    def intersect(self, s2):
        """Returns a new intSet of just the common elements of two lists"""
        result = intSet()
        set1 = set(self.vals)
        set2 = set(s2.vals)
        setout = set1.intersection(set2)
        result.vals = list(setout)
        return result

    def __len__(self):
        """Returns the number of elements in a intSet"""
        return len(self.vals)


s1 = intSet()
s1.vals = [2, 3, 4, 5, 6]
print(s1.vals)
s2 = intSet()
s2.vals = [3, 3, -1, 7, 5, 8, -12]
print(s2.vals)

print(s1.intersect(s2))
print(s1.intersect2(s2))
print(len(s1))


class A(object):
    def __init__(self):
        self.a = 1

    def x(self):
        print("A.x")

    def y(self):
        print("A.y")

    def z(self):
        print("A.z")


class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3

    def y(self):
        print("B.y")

    def z(self):
        print("B.z")


class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5

    def y(self):
        print("C.y")

    def z(self):
        print("C.z")


class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6

    def z(self):
        print("D.z")


obj = D()

obj.x()
obj.y()
obj.z()
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)

## Extended Example::


class Person(object):
    def __init__(self, name) -> None:
        self.name = name
        self.birthday = None
        self.lastName = name.split(" ")[-1]

    def __str__(self) -> str:
        return self.name

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def getLastName(self):
        return self.lastName

    def getBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days


p1 = Person("Mark Zucks")
p2 = Person("Drew Hucks")
p3 = Person("Bill Gates")
p4 = Person("Andrew Gates")
p5 = Person("Hugo Boss")

personList = [p1, p2, p3, p4, p5]

for person in personList:
    print(person)

personList.sort()

for person in personList:
    print(person)


class MITPerson(Person):
    nextIDnum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIDnum
        MITPerson.nextIDnum += 1

    def getIDNum(self):
        return self.idNum

    def speak(self, utterance):
        return self.getLastName() + " says: " + utterance

    def __lt__(self, other):
        return self.idNum < other.idNum


class Student(MITPerson):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, "Dude, " + utterance)


s1 = Student("James Cameron", 1987)
s2 = Student("James Carr", 1999)
s3 = Student("Peppa Pig", 2005)

print(s2.speak("Where's my car?"))


def isStudent(obj):
    return isinstance(obj, Student)


print(isStudent(s2))
print(isStudent(p2))


class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        new = "In course " + self.department + " we say "
        return MITPerson.speak(self, new + utterance)

    def lecture(self, topic):
        return self.speak("it is obvious that " + topic)


proff = Professor("Larry Ersehooler", "Biofarming 101")
print(proff.speak("biomass is the next big thing!"))
print(proff.lecture("Apples are fuel."))
