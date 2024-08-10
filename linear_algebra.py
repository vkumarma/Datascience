from typing import List, Tuple, Callable
import math
Vector = List[float] # type annotation

def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v)==len(w), "vectors must be the same length"
    return [v_i + w_i for v_i,w_i in zip(v,w)]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v)==len(w), "vectors must be the same length"
    return [v_i - w_i for v_i,w_i in zip(v,w)]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    assert vectors, "no vectors provided"

    # making sure that vectors are same size
    num_elems = len(vectors[0])
    assert all(num_elems == len(v) for v in vectors), "different sizes"

    # i-th element of the result is the sum of every vector[i]
    # (vec[i] for vec in vectors) - generator expression similar to list comprehension but returns generator object that can be iterated
    return [sum([vec[i] for vec in vectors]) for i in range(num_elems)]


def scalar_multiply(c:float, v:Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_e for v_e in v]


# this function allows component wise means of list of (same-sized) vectors
def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise mean"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


# Dot product - sum of two vectors component-wise product
def dot(v:Vector, w: Vector) -> float:
    """Computes v_i * w*i + ... + v_n * w_n"""
    assert len(v) == len(w), "Vectors must be of same length"
    return sum([v_i * w_i for v_i,w_i in zip(v,w)])


def sum_of_squares(v:Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v,v)

# magnitude (or length) of vector
def magnitude(v:Vector) -> float:
    return math.sqrt(sum_of_squares(v))


def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v,w))

def distance(v:Vector, w:Vector) -> float:
    return math.sqrt(squared_distance(v,w))


Matrix = List[List[float]]


def shape(A: Matrix) -> Tuple[int,int]:
    """Returns (# of rows of A, # cols of A)"""
    rows = len(A)
    cols = len(A[0]) if A else 0
    return rows, cols


def get_row(A: Matrix, i:int) -> Vector:
    """Returns i-th row of A (as a vector)"""
    return A[i] # i-th row


def get_column(A: Matrix, j:int) -> Vector:
    """Returns j-th col of A"""
    return [A_i[j] for A_i in A]


def make_matrix(num_rows: int, num_cols:int,entry_fn: Callable[[int,int], float]) -> Matrix:
    """returns a num_rows * num_cols matrix, whose (i,j)-th entry is entry_fn(i,j)"""
    return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]

def foo(i:int, j:int) -> int:
    if i == j: return 1
    return 0


def identity_matrix(n:int) -> Matrix:
    """Returns n*n identity matrix"""
    return make_matrix(n,n, foo)

print(identity_matrix(5))