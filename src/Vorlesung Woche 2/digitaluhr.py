import time
for h in range(24):
    for m in range(60):
        for s in range(60):
            time.sleep(0.002)
            print(str(h).zfill(2)+":"+str(m).zfill(2)+ \
                  ":"+ str(s).zfill(2))