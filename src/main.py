from source import *
from tqdm import tqdm
import time
from tqdm import tqdm

printWellcome()

P0,P1,P2,iterations,option,pauses = callInput()
plt.ion()  
fig, ax = plt.subplots()

progress_bar = tqdm(total=iterations, desc="Loading", unit=" iteration")
startTime=time.time()
for i in range(iterations + 1):
    update(i,P0,P1,P2,iterations,option,pauses)
    progress_bar.update(1)
progress_bar.close()
print("Selesai!")
print(f'Waktu total : {(time.time()-startTime)*1000} ms')
plt.ioff()  
plt.show()
