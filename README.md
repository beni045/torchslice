# torchslice

A script using torch.fx to 'slice' torch modules by setting intermediate inputs and outputs.
The sliced module can be used like a normal module, which can be convienient in many cases, like easily ONNX exporting a sub-graph of the orignal module.

Only torch is required to use, but version 1.8.0 or higher. 

