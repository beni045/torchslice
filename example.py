# --------- EXAMPLE ---------------

# Define a torch.nn.Module with intermediate values
# wrapped with set_input(), set_output()

import torch
from torchslice import set_input, set_output, slice_module


class MyModule(torch.nn.Module):
    def __init__(self, N, M):
        super(MyModule, self).__init__()
        self.linear0 = torch.nn.Linear(M, M)
        self.linear1 = torch.nn.Linear(M, M)
        self.linear2 = torch.nn.Linear(M, M)
        self.linear3 = torch.nn.Linear(M, M)
        self.linear4 = torch.nn.Linear(M, M)
        self.linear5 = torch.nn.Linear(M, M)

    def forward(self, tensorA, tensorB, tensorC):
        out1 = self.linear0(tensorA)
        out2 = self.linear1(tensorB)
        out3 = self.linear2(tensorC)

        out4 = self.linear3(tensorA)
        out5 = self.linear4(tensorB)
        out6 = self.linear5(tensorC)

        out1 = set_input(out1)  # intermediate value set as input
        out2 = set_input(out2)  # intermediate value set as input
        out3 = set_input(out3)  # intermediate value set as input

        sum1 = out1 + out2 + out3
        sum1 = set_output(sum1) # intermediate value set as output
        sum2 = out4 + out5 + out6 
        sum2 = set_output(sum2) # intermediate vallue set as output

        return sum1, sum2, sum1 / sum2


# Initalize module
mod = MyModule(20,20)
# Initialize inputs to module
tensorA, tensorB, tensorC =  torch.rand(20,20), torch.rand(20,20), torch.rand(20,20)

# Pass module, inputs to slice_module.
# If inputs are not passed, the model will still be sliced
# but the returned inputs, outputs will be None
sliced_mod, inputs, outputs = slice_module(mod,(tensorA,tensorB,tensorC))

# Intermediate IO dicts
print('Inputs: ', inputs.keys()) 
print('Outputs: ', outputs.keys())

# Show new graph
sliced_mod.graph.print_tabular()    # This print requires to install tabulate module - conda install tabulate
                                    # Can also print(sliced_mod.graph) without tabulate module
