from qiskit import QuantumCircuit,Aer

def quantum_superposition():
    ckt = QuantumCircuit(1,1)
    ckt.h(0)
    ckt.measure(0,0) 
    qsim = Aer.get_backend('aer_simulator')
    result = qsim.run(ckt).result().get_counts()
    
    return result