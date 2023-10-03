namespace Quantum.Example {

    // Operation to prepare a qubit in an equal superposition of |0⟩ and |1⟩
    operation PrepareSuperposition(qubit: Qubit) : Unit {
        H(qubit); // Apply Hadamard gate to create superposition
    }

    // Operation to measure the qubit and return the result
    operation MeasureQubit(qubit: Qubit) : Result {
        return MResetZ(qubit); // Measure the qubit along the Z-axis and return the result
    }

    // Driver operation to run the quantum program
    operation RunProgram() : Result {
        using (qubit = Qubit()) {
            PrepareSuperposition(qubit); // Prepare the qubit in superposition
            let result = MeasureQubit(qubit); // Measure the qubit
            return result;
        }
    }
}
