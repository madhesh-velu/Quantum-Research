namespace Quantum.Example {

    // Operation to prepare an electron in a superposition of spin-up and spin-down states
    operation PrepareElectronSuperposition(qubit: Qubit) : Unit {
        // Apply a Hadamard gate to create superposition
        H(qubit);
    }

    // Operation to measure the electron's spin and return the result
    operation MeasureElectronSpin(qubit: Qubit) : Result {
        return M(qubit);
    }

    // Driver operation to run the quantum program
    operation RunProgram() : (Result, Result) {
        using (qubit1 = Qubit()) {
            using (qubit2 = Qubit()) {
                PrepareElectronSuperposition(qubit1); // Prepare the first electron in superposition
                PrepareElectronSuperposition(qubit2); // Prepare the second electron in superposition

                let result1 = MeasureElectronSpin(qubit1); // Measure the spin of the first electron
                let result2 = MeasureElectronSpin(qubit2); // Measure the spin of the second electron

                return (result1, result2);
            }
        }
    }
}
