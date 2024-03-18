from __future__ import annotations


var: int = 1


class Duck:
    def __init__(self): ...

    def __getattr__(self, attr):
        if attr == "quack":
            return lambda: print("quack")
        elif attr == "swimlane":
            return lambda: print("swimlane")
        else:
            raise AttributeError(f"No such attribute {attr}")


duck = Duck()
duck.quack()


var: int = 1
var = "hi"


def consume_many_types(
    num: int,
    decimel: float,
    boolean: bool,
    string: str,
    binary: bytes,
    obj: object,
) -> None:
    pass


from typing import (
    List,
    Dict,
    Tuple,
    Set,
    Union,
    Type,
    Optional,
    NamedTuple,
    TypeVar,
)


nums: List[int] = []
three_dimensional_vector: Tuple[int, float, str] = (1, 2.0, "a")
n_dimensional_vector: Tuple[float, ...] = 1, 2, 3, 4, 5, 6
student_to_ages: Dict[str, int] = {
    "bobby": 25,
    "murry": 23,
    "ergub": 22,
}

fruits: Set[str] = {"apple", "orange", "preserves"}


class Animal: ...


x = Animal
fecko = x()
fecko


miscellaneous_values: List[Union[int, float, Type, str]] = [1, 1.0, "hi", object]

y: Union[int, float, Type, str]
y = "hi"

# OR
u: int | float | Type | str
u = 3

o: Optional[int] = None


def greet(name: Optional[str] = None):
    if not name:
        print("hello")
    print(f"hello {name}")


# student: Dict[str, Union[str, int]] = {
#     "name": "mary", # noqa: ERA001
#     "age": 'wqe', # doesnt care if it int or not
# }


# suing typing
# class Student(TypedDict):
#     name: str
#     age: int


# student: Student = {
#     "name": "mary",
#     "age": 24,
# }

# other_student = Student(name="Jared", age="sdf")  # the type of age creates problem.

# using the collection

# Point = namedtuple("Point", ["x", "y"])
# point2d = Point(1, 2)
# point2d.x


# using the typing
class Point(NamedTuple):
    x: int
    y: int


point2d = Point(1, 2)
point2d.x

# bob: "Student"


bob: Student

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    position: Point
    friends: List[Student]


student = Student(
    **{
        "name": "Jared",
        "age": 34,
        "position": Point(1, 2),
        "friends": [
            Student(
                **{  # type: ignore
                    "name": "Jared",
                    "age": 24,
                    "position": Point(1, 2),
                    "friends": [],
                }
            )
        ],
    }
)

print(student.friends[0].age)


# Defines a generic function to create a list of addable entities using TypeVar in Python.
TAddableEntity = TypeVar("TAddableEntity", int, float)


def make_list_of_addable(
    a: TAddableEntity,
    b: TAddableEntity,
) -> List[TAddableEntity]:
    return [a, b]


make_list_of_addable(a='t', b='s')
