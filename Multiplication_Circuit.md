## The Code for the Original Ciruit that runs the Multiplication Function
```python
#import the necessary libraries for using the IBM Quantum Composer widget and the Qiskit library
#CircuitComposer allows you to create, edit, and visualize quantum circuits.
#qiskit library provides the QuantumRegister, ClassicalRegister, and QuantumCircuit classes, which are used to create and manipulate quantum circuits.
#numpy library provides the pi constant, which is used in the Hadamard gate operation.

from ibm_quantum_widgets import CircuitComposer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

#Add 3 quatnum register ans 1 clasical register
#QuantumRegister class represents a register of quantum bits
#The ClassicalRegister class represents a register of classical bits
#The QuantumCircuit class represents a quantum circuit, which is a sequence of quantum operations applied to a quantum register.

qreg_q0 = QuantumRegister(3, 'q0')
creg_c0 = ClassicalRegister(1, 'c0')
circuit = QuantumCircuit(qreg_q0, creg_c0)

#The reset() operation resets a qubit to the state |0⟩.
#The h() operation is the Hadamard gate, which puts a qubit in a superposition of the states |0⟩ and |1⟩.
#The ccx() operation is the controlled-controlled-X gate, which is a three-qubit gate that entangles the qubits in such a way that the state of the third qubit is determined by the states of the first two qubits.
#The measure() operation measures the state of a qubit and stores the result in a classical register.


circuit.reset(qreg_q0[0])
circuit.reset(qreg_q0[1])
circuit.reset(qreg_q0[2])
circuit.h(qreg_q0[0])
circuit.h(qreg_q0[1])
circuit.ccx(qreg_q0[0], qreg_q0[1], qreg_q0[2])
circuit.measure(qreg_q0[2], creg_c0[0])

#The CircuitComposer constructor takes a QuantumCircuit object as input and creates a new instance of the IBM Quantum Composer widget with the circuit displayed in it.

editor = CircuitComposer(circuit=circuit)
editor
```

## The Circuit On IBM Composer


![original-circuit-2](https://github.com/ubsuny/23-Homework1G4/assets/38404107/d12fc316-2b82-4859-ab99-64e5113c176f)


## The Truth Table, Probabilities and results are included in another Markdown

  


