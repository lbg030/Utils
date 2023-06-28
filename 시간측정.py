import torch
import numpy as np


starter, ender = torch.cuda.Event(
    enable_timing=True), torch.cuda.Event(enable_timing=True)
repetitions = 300
timings = np.zeros((repetitions, 1))

for _ in range(10):
    _ = model(dummy_input)

# MEASURE PERFORMANCE
with torch.no_grad():
    for rep in range(repetitions):
        starter.record()
        _ = model(dummy_input)
        ender.record()
        # WAIT FOR GPU SYNC
        torch.cuda.synchronize()
        curr_time = starter.elapsed_time(ender)
        timings[rep] = curr_time

# https://velog.io/@hellojun12/Pytorch-Inference-time-%EC%B8%A1%EC%A0%95
