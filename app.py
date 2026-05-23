import torch
import torch.nn as nn
import numpy as np
import pickle
import os

# 1. DEFINIR LA ARQUITECTURA (Debe ser idéntica a la del entrenamiento)
class AuditorNet(nn.Module):
    def __init__(self, input_size):
        super(AuditorNet, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )
    def forward(self, x):
        return self.network(x)

def inicializar_motor_ia():
    """Carga el modelo y el escalador en memoria asegurando portabilidad."""
    ruta_modelo = 'auditor_net_soc.pth'
    ruta_scaler = 'scaler_soc.pkl'
    
    if not os.path.exists(ruta_modelo) or not os.path.exists(ruta_scaler):
        raise FileNotFoundError("🚨 Faltan los archivos 'auditor_net_soc.pth' o 'scaler_soc.pkl' en el directorio.")

    # Cargar el escalador de datos
    with open(ruta_scaler, 'rb') as f:
        scaler = pickle.load(f)
        
    # Detectar entorno: Usa CUDA si está disponible, si no, levanta en CPU sin romper el script
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Instanciar la red con las 33 características de entrada
    model = AuditorNet(input_size=33).to(device)
    
    # Cargar los pesos entrenados (map_location asegura que abra en CPU si no hay GPU dedicada)
    model.load_state_dict(torch.load(ruta_modelo, map_location=device))
    model.eval() # Modo evaluación crítico para congelar capas de entrenamiento
    
    return model, scaler, device

def escanear_conexion(datos_crudos, model, scaler, device):
    """Ejecuta la inferencia matemática sobre una lista de 33 parámetros."""
    # Convertir a matriz, escalar y pasar a tensor
    array_datos = np.array(datos_crudos).reshape(1, -1)
    datos_escalados = scaler.transform(array_datos)
    tensor_datos = torch.tensor(datos_escalados, dtype=torch.float32).to(device)
    
    with torch.no_grad():
        probabilidad = model(tensor_datos).item()
    
    return probabilidad

# =====================================================================
# EJEMPLO DE USO INMEDIATO
# =====================================================================
if __name__ == "__main__":
    print("Levantando el motor de auditoría inteligente...")
    try:
        model, scaler, device = inicializar_motor_ia()
        print(f"Motor operativo corriendo en: {device.type.upper()}")
        
        # Simulación de un log de red sospechoso (33 métricas numéricas)
        log_prueba = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 300, 15, 
            1.0, 1.0, 0.0, 0.0, 0.05, 0.07, 0.0, 255, 15, 0.06, 0.07, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0
        ]
        
        score = escanear_conexion(log_prueba, model, scaler, device)
        
        print(f"\n[RESULTADO] Alerta de Amenaza: {score * 100:.2f}%")
        if score > 0.5:
            print("DIAGNÓSTICO SOC: MALICIOUS TRAFFIC (Activar contención)")
        else:
            print("DIAGNÓSTICO SOC: CLEAN CONNECTION")
            
    except Exception as e:
        print(f"Error al iniciar la inferencia: {e}")