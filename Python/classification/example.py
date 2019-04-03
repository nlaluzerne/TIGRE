import numpy as np
from inference import infer

example_image = np.random.rand(400, 400, 3)

print(infer([example_image]))
