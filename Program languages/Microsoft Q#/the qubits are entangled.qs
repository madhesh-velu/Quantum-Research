// Create two qubits
qubit q1, q2;

// Generate an entangled state
operation CreateEntangledState() : Unit {
    CNOT(q1, q2);
}

// Measure the qubits in the Z basis
operation MeasureQubits() : (Bool, Bool) {
    let q1Result = Measure(q1, PauliZ);
    let q2Result = Measure(q2, PauliZ);
    return (q1Result, q2Result);
}

// Check if the qubits are entangled
operation IsEntangled() : Bool {
    // Generate an entangled state
    CreateEntangledState();

    // Measure the qubits in the Z basis
    let (q1Result, q2Result) = MeasureQubits();

    // If the results are opposite, then the qubits are entangled
    return q1Result != q2Result;
}

// Example usage:
let isEntangled = IsEntangled();

if (isEntangled) {
    Console.WriteLine("The qubits are entangled!");
} else {
    Console.WriteLine("The qubits are not entangled.");
}
