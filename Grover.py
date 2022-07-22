import cirq

q0, q1 = cirq.LineQubit.range(2)
# q0 = cirq.GridQubit(0, 0)
# q1 = cirq.GridQubit(0, 1)

grover = cirq.Circuit()
grover.append([cirq.H(q0), cirq.H(q1)])

# Oracle for |00⟩ :
grover.append([cirq.X(q0), cirq.X(q1)])
grover.append(cirq.CX(q0,q1))
grover.append([cirq.X(q0), cirq.X(q1)])

grover.append([cirq.H(q0), cirq.H(q1)])

# reflection circuit :
grover.append([cirq.Z(q0), cirq.Z(q1)])
grover.append(cirq.CX(q0,q1))

grover.append([cirq.H(q0), cirq.H(q1)])
grover.append([cirq.measure(q0), cirq.measure(q1)])

print(grover)

simulator = cirq.Simulator()
result = simulator.simulate(grover)
# result = simulator.run(circuit, repetitions=40) # NISQ computers
print(result)