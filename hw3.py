import cv2
import os
vid = cv2.VideoCapture(0)

def key_generation():
    #todo
    return None

def key_encryption():
    #todo
    return None

def key_decryption():
    #todo
    return None

def process_encrypted_frame(frame):
    b = frame[:, :, 0]
    g = frame[:, :, 1]
    r = frame[:, :, 2]
    # fill in the key_encryption here and pass down the values to the cv2.merge function
    encrypted_frames = cv2.merge((b^0xFF, g^0xFF, r^0xFF)) #pass down for display + decrypt
    return encrypted_frames

def process_decrypted_frame(frame):
    #todo
    b = frame[:, :, 0]
    g = frame[:, :, 1]
    r = frame[:, :, 2]
    # fill in the key_decryption here and pass down the values to the cv2.merge function
    decrypted_frames = cv2.merge((b^0xFF, g^0xFF, r^0xFF)) #pass down for display + decrypt
    return decrypted_frames #pass down for display

def main():
    
    cascade_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "haarcascade_frontalface_default.xml"
    )

    face_cascade = cv2.CascadeClassifier(cascade_path)

    try:
        while True:
            ret, frame = vid.read()
            if not ret:
                print("Failed to capture frame. Check webcam connection.")
                break
            #Key gen should go here

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))  # Detect faces
            
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 

            cv2.imshow("original", frame)
            
            if(len(faces) > 0):
                #shoow encrypted and decrypted frames if face is detected
                face_frame = frame[y:y+h, x:x+w] #crop out the face region
                encrypted_frame = process_encrypted_frame(face_frame); 
                combined_frame = frame.copy() #make a copy of the original
                combined_frame[y:y+h, x:x+w] = encrypted_frame #combine the matrix of the two
                cv2.imshow("encrypted_frames", combined_frame);

                decrypted_frame = process_decrypted_frame(encrypted_frame);
                combined_decrypted_frame = frame.copy()
                combined_decrypted_frame[y:y+h, x:x+w] = decrypted_frame
                cv2.imshow("decrypted_frame", combined_decrypted_frame); 
            else:
                #show regular frame if no face is detected
                cv2.imshow("encrypted_frames", frame);
                cv2.imshow("decrypted_frame", frame);

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print("Error occurred:", e)

    finally:
        vid.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()