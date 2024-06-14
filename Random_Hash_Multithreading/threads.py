from threading import Thread
import time

def car(speed, pilot):
    route = 0
    while route < 100:
        route += speed
        time.sleep(0.3)
        print(f'Pilot-{pilot}  KM: {route}\n')
        
        
t_car1 = Thread(target=car, args=[5, 'Senna'])
t_car2 = Thread(target=car, args=[10, 'Vetel'])

t_car1.start()
t_car2.start()