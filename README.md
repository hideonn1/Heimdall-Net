# Heimdall-Net 🛡️

Neural Intrusion Detection Engine for Network Infrastructure.

Heimdall-Net es un sistema inteligente de detección de intrusiones (IDS) basado en redes neuronales profundas (PyTorch). El sistema está diseñado para auditar registros de tráfico y logs de seguridad en busca de patrones anómalos.

## Características

* Inferencia de Red Inteligente: Motor entrenado en arquitecturas de red profunda para clasificación de anomalías.
* Pipeline Automatizado: Auto-generación de artefactos binarios (.pth y .pkl) mediante scripts de entrenamiento.
* Microservicio Nativo: Backend asíncrono expuesto mediante una API REST en FastAPI.
* Arquitectura Dockerizada: Entorno completamente aislado para asegurar portabilidad.

## Despliegue Rápido (Con Docker) 🐋

La forma más rápida de poner en marcha Heimdall-Net es utilizando Docker.

1. Clonar el repositorio:
git clone [https://github.com/hideonn1/Heimdall-Net.git](https://github.com/hideonn1/Heimdall-Net.git)
cd Heimdall-Net
2. Construir la imagen de Docker:
docker build -t heimdall-net .
3. Correr el contenedor:
docker run -d -p 8000:8000 --name guardian-soc heimdall-net
4. Acceder a la API interactiva:
Abre tu navegador e ingresa a: http://localhost:8000/docs

## 💻 Instalación y Uso Local (Sin Docker)

1. Instalar Dependencias:
pip install -r requirements.txt
2. Generar el Modelo:
python train.py
3. Ejecutar los Módulos:

* Para la API: python -m uvicorn api.py:app --reload
* Para el escáner: python live_scanner.py

## Arquitectura del Pipeline

El flujo de datos se divide en tres capas críticas:
[ Capa de Entrada ] --> [ Capa de Procesamiento ] --> [ Capa de Inferencia ]
Tráfico Crudo (Scapy) --> Parser & Normalización --> Red Neuronal (PyTorch)

## Licencia

Este proyecto es de código abierto para fines académicos.