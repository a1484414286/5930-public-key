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
    #todo
    return frame #pass down for display + decrypt

def process_decrypted_frame(frame):
    #todo
    return frame #pass down for display

def main():
    try:
        while True:

            ret, frame = vid.read()

            if not ret:
                print("Failed to capture frame. Check webcam connection.")
                break

            cv2.imshow("frame", frame)
            cv2.imshow("frame", frame)
            cv2.imshow("frame2", frame)
            b = frame[:, :, 0] #2D arrays
            g = frame[:, :, 1]
            r = frame[:, :, 2]

            # encrypted_frame = process_encrypted_frame(frame);
            # cv2.imshow("encrypted_frame", encrypted_frame);
            
            # decrypted_frame = process_decrypted_frame(encrypted_frame);
            # cv2.imshow("decrypted_frame", decrypted_frame); 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print("Error occurred:", e)

    finally:
        vid.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()