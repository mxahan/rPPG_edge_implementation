import numpy as np

import tflite_runtime.interpreter as tflite 

import time

data= np.load('test_data.npz.npy')

data = data.reshape(-1, 100, 100, 40)

data = np.array(data, dtype=np.float32)

interpreter  =  tflite.Interpreter(model_path =  'masud_lit_f16.tflite')

start_time=time.time()
interpreter.allocate_tensors()


input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

# format input_data
# interpreter set tensor
# we can provide intermediate data too by selecing the index

interpreter.set_tensor(input_index, data)

# getting out the output, 
# allocate tensor, fill values before invoke
interpreter.invoke()
# have everything in # get_tensor_details()
# all intermediate results are there.
# get_tensor to get some tensor from the desired index
# mostly we want output_index
predictions = interpreter.get_tensor(output_index)


np.save('something', predictions)

print("--- %s seconds ---" % (time.time() - start_time))
