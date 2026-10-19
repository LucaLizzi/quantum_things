from qiskit import __version__
import numpy as np
from qiskit.visualization import array_to_latex
from IPython.display import display

print(__version__)

ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

print(ket0 / 2 + ket1 / 2)

M1 = np.array([[1, 1], [0, 0]])
M2 = np.array([[1, 0], [0, 1]])
M = M1 / 2 + M2 / 2
print(M)

print(M1 @ ket1)
print(M1 @ M2)
print(M @ M)


# display(array_to_latex(M1 @ ket1))    # TODO: strange error
# display(array_to_latex(M1 @ M2))
# display(array_to_latex(M @ M))


from qiskit.quantum_info import Statevector
from numpy import sqrt

u = Statevector([1 / sqrt(2), 1 / sqrt(2)])
v = Statevector([(1 + 2.0j) / 3, -2 / 3])
w = Statevector([1 / 3, 2 / 3])


print(u.draw("text"))
print(u.draw("latex"))
print(u.draw("latex_source"))