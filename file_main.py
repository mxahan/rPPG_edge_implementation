import numpy as np

import tflite_runtime.interpreter as tflite 

import time

from vid_read import  video_reader

#%% Prepocessing dataset


for _ in range(1):
    start_time =  time.time()
    fp, datt = video_reader('output.mov')
    print("video_cv time --- %s seconds ---" % (time.time() - start_time))
    print(fp)
    print(datt.shape)

print('\n')



datt = np.array(datt, dtype =np.float32)

datt =datt[0:640]
#datt = datt.astype(np.float16)
#datt=datt.astype(np.float32)




for _ in range(3):
    # datt = np.float32(np.random.rand(16*40, 100, 100))
    start_time = time.time()
    
    datt = datt[:,:,:,np.newaxis]
    
    frame_cons = 40 # how many frame to consider at a time
    im_size = (100,100)
    
    trainX =[]
    
    for i in range(np.int(datt.shape[0]/40)):
        
        img = np.reshape(datt[i*frame_cons:(i+1)*frame_cons,:,:,0], [frame_cons, *im_size])
        img = np.moveaxis(img, 0,-1)
        trainX.append(img)
    
    
    trainX = np.array(trainX, dtype = np.float32)
    trainX = (trainX-trainX.min())
    
    data = trainX/ trainX.max()
    
    print("Prepocessing time -- %s seconds -- " % (time.time() - start_time)+ " size of "+str(i+1) )

print('\n')

np.save('test_data.npz',data)


#%% load data from the origin



for _ in range(3):
    start_time = time.time()
    data= np.load('test_data.npz.npy')
    data = data.reshape(-1, 100, 100, 40)
    data = np.array(data, dtype=np.float32)
    print("Data_load (prepocessed) time --- %s seconds ---" % (time.time() - start_time))


print('\n')

#%% alternatively synthetic data
"""
data = np.float32(np.random.rand(16,100,100,40))
"""

#%% Model inference
#data=data.astype(np.float16)
#data=data.astype(np.float32)
batch_size, _, _, _ = data.shape
print(data.shape)

for _ in range(3):
    start_time = time.time()
    interpreter  =  tflite.Interpreter(model_path =  'emon_lite_p.tflite')
    print("Model_load time --- %s seconds ---" % (time.time() - start_time))



print('\n')


start_time=time.time()




input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

interpreter.resize_tensor_input(input_index, [batch_size,100,100,40])
interpreter.allocate_tensors()


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

print("warmup time --- %s seconds ---" % (time.time() - start_time))

print('\n')

#%% Looped version : Aveage inference time

start_time1 =  time.time()
for i in range(5):
    # data = np.float16(np.random.rand(16,100,100,40))
    data = data.astype(np.float32)


    batch_size, _, _, _ = data.shape
    interpreter  =  tflite.Interpreter(model_path =  'emon_lite_p.tflite')
    start_time=time.time()
    input_index = interpreter.get_input_details()[0]["index"]
    output_index = interpreter.get_output_details()[0]["index"]
    interpreter.resize_tensor_input(input_index, [batch_size,100,100,40])
    interpreter.allocate_tensors()
    interpreter.set_tensor(input_index, data)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_index)
    np.save('something', predictions)
    
    print("Inference time --- %s seconds ---" % (time.time() - start_time))
    


print('\n')

print("Total time -- %s seconds -- " % (time.time() - start_time1)+ "batch size of "+str(i+1) )
