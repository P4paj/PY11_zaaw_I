#przykład 1 - użycie TypedDict

from typing import TypedDict

class User(TypedDict):
    name:str
    age:int
    email:str

def print_user_info(user:User) -> None:
    print(f"Name: {user['name']}, Age: {user['age']}, e-mail: {user['email']}")

user_data = {'name':'Leon','age':40,'email':'leonion@abc.pl'}
print_user_info(user_data)

#przykład 2 - złożone aliasy typów

from typing import List,Tuple,Union

Coordinate = Tuple[float,float]
Path = List[Coordinate]
CoordinateError = Union[Coordinate,str]

def validate_coordinate(coord:CoordinateError)->bool:
    if isinstance(coord,str):
        print(f"Error: {coord}")
        return False
    return True

example_path = [(0.0,1.0),(2.5,3.5),(4.0,-1.2),('True',True)]
print(validate_coordinate(example_path[0]))
print(validate_coordinate("invalide coordinate"))
print("_"*70)
print(validate_coordinate(example_path[3][0]))
print(validate_coordinate(example_path[3][1]))
