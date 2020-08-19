import face_recognition
import os

class faceRecog:
    def __init__(self):
        print("init")
    




    def auth(self,user):
        #retrive image register to that user
        user_image = face_recognition.load_image_file('C:/Users/ALEJANDROROMEROALDRE/Documents/maestria3ro/PROYECTOFINAL/software/python/imgs/'+str(user)+".jpg")
        user_face_encoding = face_recognition.face_encodings(user_image)[0]

        # Load temp image send by client

        image_temp = face_recognition.load_image_file('C:/Users/ALEJANDROROMEROALDRE/Documents/maestria3ro/PROYECTOFINAL/software/python/imgs/temp_'+user+".jpg")
        image_temp_encoding = face_recognition.face_encodings(image_temp)[0]

        # See how far apart the test image is from the known faces
        face_distances = face_recognition.face_distance([user_face_encoding], image_temp_encoding)
        
        if (face_distances[0] < 0.5):
            print(face_distances)
            os.remove('C:/Users/ALEJANDROROMEROALDRE/Documents/maestria3ro/PROYECTOFINAL/software/python/imgs/temp_'+user+".jpg")
            return True
        else:
            print(face_distances)
            os.remove('C:/Users/ALEJANDROROMEROALDRE/Documents/maestria3ro/PROYECTOFINAL/software/python/imgs/temp_'+user+".jpg")
            return False
        """ for i, face_distance in enumerate(face_distances):
            print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
            print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
            print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
            print() """