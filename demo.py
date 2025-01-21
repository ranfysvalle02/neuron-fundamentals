class McCullochPittsNeuron:  
    def __init__(self, weights, threshold):  
        self.weights = weights  
        self.threshold = threshold  
  
    def activate(self, inputs):  
        total_input = sum(w * i for w, i in zip(self.weights, inputs))  
        return 1 if total_input >= self.threshold else 0  
  
# AND Gate Simulation  
and_neuron = McCullochPittsNeuron(weights=[1, 1], threshold=2)  
and_test_cases = [  
    ([0, 0], 0),  
    ([0, 1], 0),  
    ([1, 0], 0),  
    ([1, 1], 1),  
]  
print("AND Gate Simulation:")  
for inputs, expected in and_test_cases:  
    result = and_neuron.activate(inputs)  
    print(f"Inputs: {inputs}, Expected: {expected}, Actual: {result}")  
  
# OR Gate Simulation  
or_neuron = McCullochPittsNeuron(weights=[1, 1], threshold=1)  
or_test_cases = [  
    ([0, 0], 0),  
    ([0, 1], 1),  
    ([1, 0], 1),  
    ([1, 1], 1),  
]  
print("\nOR Gate Simulation:")  
for inputs, expected in or_test_cases:  
    result = or_neuron.activate(inputs)  
    print(f"Inputs: {inputs}, Expected: {expected}, Actual: {result}")  
  
# NOT Gate Simulation  
not_neuron = McCullochPittsNeuron(weights=[-1], threshold=0)  
not_test_cases = [  
    ([0], 1),  
    ([1], 0),  
]  
print("\nNOT Gate Simulation:")  
for inputs, expected in not_test_cases:  
    result = not_neuron.activate(inputs)  
    print(f"Input: {inputs[0]}, Expected: {expected}, Actual: {result}")  
  
# Attempting XOR Gate with Single Neuron (Fails)  
xor_neuron = McCullochPittsNeuron(weights=[1, -1], threshold=0)  
xor_test_cases = [  
    ([0, 0], 0),  
    ([0, 1], 1),  
    ([1, 0], 1),  
    ([1, 1], 0),  
]  
print("\nAttempting XOR Gate Simulation with Single Neuron (Fails):")  
for inputs, expected in xor_test_cases:  
    result = xor_neuron.activate(inputs)  
    print(f"Inputs: {inputs}, Expected: {expected}, Actual: {result}")  
  
# XOR Gate Simulation Using Multiple Neurons  
# First Layer Neurons  
or_neuron = McCullochPittsNeuron(weights=[1, 1], threshold=1)  
nand_neuron = McCullochPittsNeuron(weights=[-2, -2], threshold=-3)  
  
# Second Layer Neuron  
and_neuron = McCullochPittsNeuron(weights=[1, 1], threshold=2)  
  
print("\nXOR Gate Simulation Using Multiple Neurons:")  
for inputs, expected in xor_test_cases:  
    output_or = or_neuron.activate(inputs)  
    output_nand = nand_neuron.activate(inputs)  
    new_inputs = [output_or, output_nand]  
    result = and_neuron.activate(new_inputs)  
    print(f"Inputs: {inputs}, Expected: {expected}, Actual: {result}")  

"""
AND Gate Simulation:
Inputs: [0, 0], Expected: 0, Actual: 0
Inputs: [0, 1], Expected: 0, Actual: 0
Inputs: [1, 0], Expected: 0, Actual: 0
Inputs: [1, 1], Expected: 1, Actual: 1

OR Gate Simulation:
Inputs: [0, 0], Expected: 0, Actual: 0
Inputs: [0, 1], Expected: 1, Actual: 1
Inputs: [1, 0], Expected: 1, Actual: 1
Inputs: [1, 1], Expected: 1, Actual: 1

NOT Gate Simulation:
Input: 0, Expected: 1, Actual: 1
Input: 1, Expected: 0, Actual: 0

Attempting XOR Gate Simulation with Single Neuron (Fails):
Inputs: [0, 0], Expected: 0, Actual: 1
Inputs: [0, 1], Expected: 1, Actual: 0
Inputs: [1, 0], Expected: 1, Actual: 1
Inputs: [1, 1], Expected: 0, Actual: 1

XOR Gate Simulation Using Multiple Neurons:
Inputs: [0, 0], Expected: 0, Actual: 0
Inputs: [0, 1], Expected: 1, Actual: 1
Inputs: [1, 0], Expected: 1, Actual: 1
Inputs: [1, 1], Expected: 0, Actual: 0
"""
