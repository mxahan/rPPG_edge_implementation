import cv2
import numpy as np

def video_reader(def_video = 'jn_test.mp4'):
    data = []
    im_size = (100,100)
    
    cap = cv2.VideoCapture(def_video)
    

    
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret==False:
            break
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        gray  = gray[:,:,1]

        
       
        gray = cv2.resize(gray, im_size)
        
        # pdb.set_trace()
       
        data.append(gray)
        
        #cv2.imshow('frame', gray)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    
    fps = cap.get(cv2.CAP_PROP_FPS)
        
    cap.release()
    cv2.destroyAllWindows()
    data =  np.array(data)
    
    return fps, data
