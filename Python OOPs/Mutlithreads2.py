from threading import Thread
from time import sleep, time
from multiprocessing import Process

def download(file_name):
    print("downloading", file_name)
    sleep(2)
    print("downloaded", file_name)

files = ["file1", "file2", "file3", "file4", "file5"]

start_time = time()
for file in files:
    download(file)
end_time = time()
print(f"Without threads Time taken {end_time - start_time:.2f}")

threads = []

for file in files:
    t = Thread(target=download, args=(file,))
    threads.append(t)

start_time = time()

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time()

print(f"With threads Time taken {end_time - start_time:.2f}")

processes = []

for file in files:
    p = Process(target=download, args=(file,))
    processes.append(p)

start_time = time()

for p in processes:
    p.start()

for p in processes:
    p.join()

end_time = time()

print(f"With processes Time taken {end_time - start_time:.2f}")