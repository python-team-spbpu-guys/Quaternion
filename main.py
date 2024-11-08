import numpy as np
import quaternion
import math


class QuaternionOps:
    def __init__(self, scalar, i, j, k):
        self.scalar = scalar
        self.i = i
        self.j = j
        self.k = k

    # операция умножения кватернионов
    def __mul__(self, other):
        s = self.scalar * other.scalar - self.i * other.i - self.j * other.j - self.k * other.k
        i = self.scalar * other.i + self.i * other.scalar + self.j * other.k - self.k * other.j
        j = self.scalar * other.j - self.i * other.k + self.j * other.scalar + self.k * other.i
        k = self.scalar * other.k + self.i * other.j - self.j * other.i + self.k * other.scalar
        return QuaternionOps(s, i, j, k)

    # операция сложения кватернионов
    def __add__(self, other):
        return QuaternionOps(
            self.scalar + other.scalar,
            self.i + other.i,
            self.j + other.j,
            self.k + other.k
        )

    # операция разности кватернионов
    def __sub__(self, other):
        return QuaternionOps(
            self.scalar - other.scalar,
            self.i - other.i,
            self.j - other.j,
            self.k - other.k
        )

    # комплексно-сопряженный кватернион
    def conjugate(self):
        return QuaternionOps(self.scalar, -self.i, -self.j, -self.k)

    # норма кватерниона
    def magnitude(self):
        return math.sqrt(self.scalar**2 + self.i**2 + self.j**2 + self.k**2)

    # обратный кватернион
    def reciprocal(self):
        conj = self.conjugate()
        mag_sq = self.magnitude()**2
        return QuaternionOps(conj.scalar / mag_sq, conj.i / mag_sq,
                             conj.j / mag_sq, conj.k / mag_sq)

    # поворот вектора с нулевой действительной частью в соответствии с кватернионом
    def rotate_vec(self, vec):
        vec_quat = QuaternionOps(0, *vec)
        rotated_vec = self * vec_quat * self.reciprocal()
        return (round(rotated_vec.i,8), round(rotated_vec.j,8), round(rotated_vec.k,8))

    def __str__(self):
        return f"QuaternionOps({self.scalar}, {self.i}, {self.j}, {self.k})"


# Пример использования
q_custom1 = QuaternionOps(1, 0, 1, 2)
q_custom2 = QuaternionOps(1, 1, 2, 0)

q_lib1 = np.quaternion(1, 0, 1, 2)
q_lib2 = np.quaternion(1, 1, 2, 0)

# Multiplication
print(f"Multiplication of {q_custom1} and {q_custom2}:\n\nResult for class implementation: {q_custom1 * q_custom2}")
print(f"Result for quaternion library: {q_lib1 * q_lib2}\n")

# Addition
print(f"Addition of {q_custom1} and {q_custom2}:\n\nResult for class implementation: {q_custom1 + q_custom2}")
print(f"Result for quaternion library: {q_lib1 + q_lib2}\n")

# Vector rotation
vec = (1, 0, 0)  # vector with zero real part
rotated_vec = q_custom1.rotate_vec(vec)
print(f"Rotation of vector {vec}:\n\nResult for class implementation: {rotated_vec}")

print(f"Result for quaternion library: {quaternion.rotate_vectors(q_lib1, vec)}\n")