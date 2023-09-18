from ibm_quantum_widgets import CircuitComposer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

def create_quantum_circuit():
    """
    Create a quantum circuit with the following operations:
    1. Reset three quantum bits (q0[0], q0[1], q0[2]) to the |0⟩ state.
    2. Apply a Hadamard gate (H) to q0[0] and q0[1].
    3. Apply a Toffoli (CCX) gate to q0[0], q0[1], and q0[2].
    4. Measure the state of q0[2] and store it in a classical bit (c0[0]).

    Returns:
    QuantumCircuit: The created quantum circuit.
    """
    qreg_q0 = QuantumRegister(3, 'q0')
    creg_c0 = ClassicalRegister(1, 'c0')
    circuit = QuantumCircuit(qreg_q0, creg_c0)

    # Reset quantum bits to |0⟩ state
    circuit.reset(qreg_q0[0])
    circuit.reset(qreg_q0[1])
    circuit.reset(qreg_q0[2])

    # Apply Hadamard gates
    circuit.h(qreg_q0[0])
    circuit.h(qreg_q0[1])

    # Apply Toffoli (CCX) gate
    circuit.ccx(qreg_q0[0], qreg_q0[1], qreg_q0[2])

    # Measure q0[2] and store the result in c0[0]
    circuit.measure(qreg_q0[2], creg_c0[0])

    return circuit

# Create the quantum circuit
circuit = create_quantum_circuit()

# Create a CircuitComposer widget to visualize the circuit
editor = CircuitComposer(circuit=circuit)
editor
