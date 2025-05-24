import torch

print(torch.__version__)          # Should show 2.x.x (latest)
print(torch.cuda.is_available())  # Should return True
print(torch.version.cuda)         # Should show 11.8