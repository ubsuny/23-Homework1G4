# Quantum Circuit Visualization Using IBM Quantum Widgets

In this example, we will create a quantum circuit and visualize it using the IBM Quantum Experience's `ibm_quantum_widgets` library and Qiskit.

## Importing Libraries

```python
from ibm_quantum_widgets import CircuitComposer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

CircuitComposer is used for visualizing the quantum circuit.
QuantumRegister and ClassicalRegister are used to define quantum and classical registers.
QuantumCircuit is used to create a quantum circuit.
numpy is imported to use the value of pi.

Quantum Register and Classical Register Initialization
qreg_q0 = QuantumRegister(3, 'q0')
creg_c0 = ClassicalRegister(1, 'c0')
qreg_q0 is a quantum register named 'q0' with 3 qubits.
creg_c0 is a classical register named 'c0' with 1 bit.

Quantum Circuit Initialization
circuit = QuantumCircuit(qreg_q0, creg_c0)
circuit is an instance of the QuantumCircuit class created using the quantum and classical registers.

Quantum Circuit Operations
circuit.reset(qreg_q0[0])
circuit.reset(qreg_q0[1])
circuit.reset(qreg_q0[2])
circuit.x(qreg_q0[1])
circuit.ccx(qreg_q0[0], qreg_q0[1], qreg_q0[2])
circuit.measure(qreg_q0[2], creg_c0[0])
reset(q) initializes qubits to the |0⟩ state.
x(q) applies an X gate (bit-flip gate) to qubit q.
ccx(q1, q2, q3) applies a controlled-controlled-X (Toffoli) gate, where q1 and q2 are control qubits, and q3 is the target qubit.
measure(q, c) measures the state of qubit q and stores the result in classical register bit c.

Circuit Visualization
editor = CircuitComposer(circuit=circuit)
editor
CircuitComposer is used to create a visual representation of the quantum circuit.
editor is an instance of CircuitComposer initialized with the circuit.
Running editor will display the quantum circuit in a visual interface.



