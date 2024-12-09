class Person:
    def __init__(self, name: str, age: int, job: str) -> None:
        self.name = name
        self.age = age
        self.job = job

    def get_details(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}"


class Student(Person):
    def __init__(self, name: str, age: int, job: str, grade: str) -> None:
        super().__init__(name, age, job)
        self.grade = grade

    def get_details(self) -> str:
        return (
            f"Name: {self.name}, Age: {self.age}, Job: {self.job}, Grade: {self.grade}"
        )


class Professor(Person):
    def __init__(self, name: str, age: int, job: str, courses: list[str]) -> None:
        super().__init__(name, age, job)
        self.courses = courses

    def get_details(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}, Courses: {self.courses}"


class Employee(Person):
    def __init__(self, name: str, age: int, job: str, department: str) -> None:
        super().__init__(name, age, job)
        self.department = department

    def get_details(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}, Department: {self.department}"


class StudentProfessor(Student, Professor):
    def __init__(
        self, name: str, age: int, job: str, courses: list[str], grade: str
    ) -> None:
        Person.__init__(self, name, age, job)
        self.courses = courses
        self.grade = grade

    def get_details(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}, Courses: {self.courses}, Grade: {self.grade}"


class Location:
    __slots__ = ["name", "latitude", "longitude"]

    def __init__(self, name: str, latitude: float, longitude: float) -> None:
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_coordinates(self) -> tuple[float, float]:
        return (self.latitude, self.longitude)
