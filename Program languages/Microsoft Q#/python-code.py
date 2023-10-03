from qiskit import QuantumCircuit, Aer, transpile, assemble

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Apply a Hadamard gate to create superposition
qc.h(0)

# Measure the qubit
qc.measure_all()

# Simulate the quantum circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = assemble(compiled_circuit)
result = simulator.run(job).result()

# Get the measurement result
counts = result.get_counts()
print(counts)
