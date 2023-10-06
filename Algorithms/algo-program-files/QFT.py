#Python code implementation of the Quantum Fourier Transform (QFT) algorithm using Qiskit
#pip install qiskit

from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
import numpy as np

def qft_circuit(n):
    # Create a quantum circuit with n qubits
    circuit = QuantumCircuit(n)

    # Apply Hadamard gates and controlled-phase gates
    for i in range(n):
        circuit.h(i)
        for j in range(i+1, n):
            circuit.cp(2*np.pi/2**(j-i+1), j, i)

    # Swap the qubits for correct output
    for i in range(n//2):
        circuit.swap(i, n-i-1)

    return circuit

# Define the number of qubits
n = 3

# Create the QFT circuit
qft = qft_circuit(n)

# Visualize the circuit
qft.draw(output='mpl')

# Simulate the circuit to see the state vector
simulator = Aer.get_backend('statevector_simulator')
job = execute(qft, simulator)
result = job.result()
statevector = result.get_statevector()
plot_bloch_multivector(statevector)

# Measure the circuit to see the probability distribution
qft.measure_all()
qft.draw(output='mpl')

# Simulate the circuit to see the histogram of outcomes
simulator = Aer.get_backend('qasm_simulator')
job = execute(qft, simulator, shots=1024)
result = job.result()
counts = result.get_counts()
plot_histogram(counts)
