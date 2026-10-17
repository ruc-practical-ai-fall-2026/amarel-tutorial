"""train.py

Basic Python training script for exploring Amarel.
"""

import time

import torch
from torch import nn

# Require an NVIDIA GPU
assert torch.cuda.is_available(), "CUDA is unavailable"
device = torch.device("cuda")

print("PyTorch:", torch.__version__, flush=True)
print("GPU:", torch.cuda.get_device_name(0), flush=True)

# Generate synthetic classification data
torch.manual_seed(42)

x = torch.randn(10000, 100, device=device)
y = (x[:, :10].sum(dim=1) > 0).long()

# Define a simple MLP
model = nn.Sequential(
    nn.Linear(100, 256),
    nn.ReLU(),
    nn.Linear(256, 256),
    nn.ReLU(),
    nn.Linear(256, 2),
).to(device)

optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

# Train the model
torch.cuda.synchronize()
start = time.perf_counter()

for epoch in range(100):
    optimizer.zero_grad()

    output = model(x)
    loss = loss_fn(output, y)

    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f"Epoch {epoch:3d} | Loss: {loss.item():.4f}", flush=True)

torch.cuda.synchronize()
elapsed = time.perf_counter() - start

print(f"Training time: {elapsed:.2f} seconds")
print(f"Peak GPU memory: {torch.cuda.max_memory_allocated() / 1e9:.3f} GB")

# Save the trained model
torch.save(model.state_dict(), "model.pt")
print("Training complete!")
