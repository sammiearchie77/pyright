# This sample tests that a class-scoped TypeVar used to parameterize
# a base class within a class definition cannot be covariant or
# contravariant if the base class requires an invariant type parameter.

from typing import Generic, Sequence, TypeVar

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

# This should generate an error because the type parameter for list
# is invariant, so T_co here cannot be covariant.
class Class1(list[T_co]): pass

# This should generate an error because the type parameter for list
# is invariant, so T_co here cannot be contravariant.
class Class2(list[T_contra]): pass

class Class3(Generic[T_co]): ...

class Class3_Child1(Class3[T_co]): ...
class Class3_Child2(Class3[T]): ...

# This should generate an error because T_contra isn't 
# compatible with T_co.
class Class3_Child3(Class3[T_contra]): ...

class Class4(Generic[T_contra]): ...

class Class4_Child1(Class4[T_contra]): ...
class Class4_Child2(Class4[T]): ...

# This should generate an error because T_co isn't 
# compatible with T_contra.
class Class4_Child3(Class4[T_co]): ...


class Class5(Generic[T_contra]):
    ...

class Class5_Child1(Class5[frozenset[T_contra]]):
    ...

# This should generate an error because Sequence[T_co]
# is covariant and is therefore not compatible with
# a contravariant type parameter.
class Class5_Child2(Class5[Sequence[T_co]]):
    ...

class Class5_Child3(Class5[Sequence[T]]):
    ...

class Class6(Generic[T_co, T_contra]):
    ...

class Class6_Child1(Class6[T_co, T_contra]):
    ...

# This should generate an error because T_co isn't 
# compatible with T_contra.
class Class6_Child2(Class6[T_co, T_co]):
    ...

# This should generate an error because T_contra isn't 
# compatible with T_co.
class Class6_Child3(Class6[T_contra, T_contra]):
    ...

class Class6_Child4(Class6[T, T]):
    ...

# This should generate an error because Sequence[T_co] isn't 
# compatible with T_contra.
class Class6_Child5(Class6[Sequence[T_co], Sequence[T_co]]):
    ...

