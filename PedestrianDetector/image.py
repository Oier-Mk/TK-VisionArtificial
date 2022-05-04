from counter import getNDetections
import traceback

def detectImage(path, model):
    #https://docs.ultralytics.com/tutorials/pytorch-hub/
    print("Conteo comenzado")

    try:
        # Inference
        results = model(path)
        results.save()
        
        print(results.xyxy[0])
        print(results.print())
        print("\033[1mN of objects -> " + str(getNDetections(results)) + '\033[0m')
  
    except Exception:
        #print(f"La imagen {path.split(os.path.sep)[-1]} no tiene matriculas reconocobles")
        print(traceback.format_exc())

    print("Conteo completado")