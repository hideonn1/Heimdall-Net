# Heimdall-Net 🛡️
*Neural Intrusion Detection Engine for Network Infrastructure.*

Heimdall-Net es un sistema inteligente de detección de intrusiones (IDS) diseñado para monitorear el tráfico de red en tiempo real. Utiliza una red neuronal profunda entrenada para identificar patrones anómalos, combinando la precisión de PyTorch con la capacidad de captura de paquetes de Scapy.

## Características
- **Inferencia en tiempo real:** Análisis de tráfico basado en modelos de deep learning.
- **Detección de anomalías:** Identificación de comportamientos sospechosos (DoS, escaneos de red).
- **API Integrada:** Endpoint listo para dashboards con FastAPI.
- **Diseñado para Auditores:** Basado en estándares de ciberseguridad.

## 🛠️ Instalación
1. Clona el repositorio:
   `git clone https://github.com/hideonn1/Heimdall-Net.git`
2. Instala las dependencias:
   `pip install -r requirements.txt`

## Cómo funciona


1. **Captura:** El módulo `live_scanner.py` intercepta los paquetes de red.
2. **Parsing:** `parser_soc.py` normaliza los datos.
3. **Inferencia:** El motor cargado en `app.py` evalúa el riesgo y genera un veredicto.

## ⚠️ Nota sobre los modelos
Debido a su tamaño, los archivos de pesos (`.pth`) y el escalador (`.pkl`) no están incluidos en este repositorio. Esta versión del software no es la última.