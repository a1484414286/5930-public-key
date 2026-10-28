import cv2
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
    try:
        while True:
            ret, frame = vid.read()
            if not ret:
                print("Failed to capture frame. Check webcam connection.")
                break
            #Key gen should go here
            cv2.imshow("original", frame)
            encrypted_frame = process_encrypted_frame(frame=frame);
            cv2.imshow("encrypted_frames", encrypted_frame);
            
            decrypted_frame = process_decrypted_frame(encrypted_frame);
            cv2.imshow("decrypted_frame", decrypted_frame); 

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print("Error occurred:", e)

    finally:
        vid.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()