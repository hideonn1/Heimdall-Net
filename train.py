import torch 
import torch.nn as nn
import torch.optim as optim
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
import os

class HeimdallNet(nn.Module):
    def __init__(self, input_dim):
        super(HeimdallNet, self).__init__()
        self.fc1 = nn.Linear(input_dim, 64)
        self.relu = nn.ModRelu() if hasattr(nn, 'ModRelu') else nn.ReLU()
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.sigmoid(self.fc3(x))
        return x

def entrenar_modelo_base():
    print("Iniciando entrenamiento de Heimdall-Net...")

    # En producción aqui se cargaría el archivo NSL-KDD .csv o .data
    X_train = np.random.rand(1000, 33) 
    y_train = np.random.randint(0, 2, size=(1000, 1))

    # 2. Ajustar el Escalador (StandardScaler)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    # Convertir a Tensores de PyTorch
    X_tensor = torch.FloatTensor(X_train_scaled)
    y_tensor = torch.FloatTensor(y_train)

    # 3. Inicializar Red, Pérdida y Optimizado
    modelo = HeimdallNet(input_dim=33)
    criterion = nn.BCELoss()
    optimizer = optim.Adam(modelo.parameters(), lr=0.001)

    # Bucle rápido de entrenamiento (3 epochs para demostración de consistencia)
    for epoch in range(3):
        optimizer.zero_grad()
        outputs = modelo(X_tensor)
        loss = criterion(outputs, y_tensor)
        loss.backward()
        optimizer.step()
        print(f"  Epoch {epoch+1}/3 - Loss: {loss.item():.4f}")

    # 4. Exportar artefactos esenciales
    print("Guardando artefactos binarios...")
    torch.save(modelo.state_dict(), "auditor_net_soc.pth")
    joblib.dump(scaler, "scaler_soc.pkl")
    print("¡Entrenamiento completado! 'auditor_net_soc.pth' y 'scaler_soc.pkl' creados.")

if __name__ == "__main__":
    entrenar_modelo_base()