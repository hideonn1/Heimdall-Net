from app import inicializar_motor_ia, escanear_conexion
from parser_soc import parsear_log_fortinet
import warnings

# Silenciar alertas de versión del Scaler
warnings.filterwarnings("ignore", category=UserWarning)

# 1. Inicializar el entorno y cargar la IA
print("🚀 Cargando Sistemas del SOC Inteligente...")
modelo, scaler, device = inicializar_motor_ia()

# 2. Recibir el log crudo (Esto vendrá desde tu interfaz web en el futuro)
log_usuario = (
    'date=2026-05-22 time=23:18:12 type="traffic" action="accept" '
    'duration=5 sentbyte=1250 rcvdbyte=8500 msg="Regular HTTPS traffic"'
)

print(f"\n📥 Log recibido para auditoría:\n{log_usuario}\n")

# 3. Traducir el log con nuestro Parser
datos_vectorizados = parsear_log_fortinet(log_usuario)

# 4. Pasar los datos limpios a la Red Neuronal
probabilidad = escanear_conexion(datos_vectorizados, modelo, scaler, device)

# 5. Dictamen del Analista IA
print("="*50)
print(f"📊 RESULTADO DE EVALUACIÓN: {probabilidad * 100:.2f}% de Amenaza")
if probabilidad > 0.5:
    print("🚨 ALERTA: Tráfico identificado como Ataque/Intrusión.")
else:
    print("🔒 SEGURO: Tráfico normal verificado.")
print("="*50)