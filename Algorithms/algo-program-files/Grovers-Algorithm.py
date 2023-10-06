# Grover's algorithm is a quantum algorithm that is used for searching an unsorted database or 
# solving certain black-box search problems with a quadratic speedup compared to classical algorithms.
# pip install qiskit

from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram
import numpy as np

def initialize_state(circuit, n):
    for qubit in range(n):
        circuit.h(qubit)
    return circuit

def oracle(circuit, target):
    circuit.z(target)
    circuit.cz(0, target)
    return circuit

def diffusion_operator(circuit, n):
    for qubit in range(n):
        circuit.h(qubit)
    for qubit in range(n):
        circuit.x(qubit)
    circuit.cz(0, n-1)
    for qubit in range(n):
        circuit.x(qubit)
    for qubit in range(n):
        circuit.h(qubit)
    return circuit

def grover_algorithm(n, target):
    circuit = QuantumCircuit(n, n)
    
    # Step 1: Initialize the superposition state
    initialize_state(circuit, n)
    
    # Step 2: Apply Grover's iterations
    iterations = int(np.pi/4 * np.sqrt(2**n))
    for _ in range(iterations):
        oracle(circuit, target)
        diffusion_operator(circuit, n)
    
    # Measure the qubits
    circuit.measure(range(n), range(n))
    
    return circuit

# Define the number of qubits and the target value to search for
n = 3  # Number of qubits (can be adjusted)
target = 5  # Target value to search for (0 to 2^n-1)

# Create the Grover's algorithm circuit
grover_circuit = grover_algorithm(n, target)

# Visualize the circuit
grover_circuit.draw(output='mpl')

# Simulate the circuit to see the probability distribution
simulator = Aer.get_backend('qasm_simulator')
job = execute(grover_circuit, simulator, shots=1024)
result = job.result()
counts = result.get_counts()
plot_histogram(counts)
