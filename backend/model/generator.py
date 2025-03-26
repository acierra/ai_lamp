import torch
import torch.nn as nn

class Generator3D(nn.Module):
    def __init__(self):
        super(Generator3D, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(100, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 32 * 32 * 32),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.fc(x)
        return x.view(-1, 32, 32, 32)  # Куб размером 32x32x32
