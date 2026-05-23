from scapy.all import sniff, IP, TCP
from app import inicializar_motor_ia, escanear_conexion
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

# Cargamos el cerebro de la IA
modelo, scaler, device = inicializar_motor_ia()

def capturar_trafico_y_analizar(paquetes):
    """Procesa los paquetes capturados y los pasa a la IA."""
    # Aquí simplificamos: contamos paquetes y bytes para alimentar las 33 columnas
    num_paquetes = len(paquetes)
    total_bytes = sum([len(p) for p in paquetes if p.haslayer(IP)])
    
    # Creamos un vector de 33 elementos (basado en el promedio de tu red)
    vector_red = [0.0] * 33
    vector_red[0] = 10.0          # Duración simulada de la captura
    vector_red[1] = float(total_bytes)
    vector_red[14] = float(num_paquetes)

    # Análisis de la IA
    probabilidad = escanear_conexion(vector_red, modelo, scaler, device)
    
    print(f"\nANALIZANDO TU RED EN VIVO...")
    print(f"Paquetes capturados: {num_paquetes} | Probabilidad de Anomalía: {probabilidad * 100:.2f}%")
    if probabilidad > 0.5:
        print("¡ALERTA! Tu red muestra patrones sospechosos.")
    else:
        print("Todo parece normal en tu conexión.")

print("Iniciando escucha en tu interfaz de red (10 segundos)...")
# sniff captura tráfico real. count=50 captura los primeros 50 paquetes.
paquetes = sniff(count=50, timeout=10)
capturar_trafico_y_analizar(paquetes)