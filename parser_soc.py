import re

def parsear_log_fortinet(linea_log):
    """
    Toma una línea de log cruda de Fortinet y extrae las características
    necesarias para las 33 columnas del modelo de IA.
    """
    # 1. Inicializar las 33 columnas en 0.0 (parámetros por defecto)
    # Posiciones clave: 
    # [0]=duration, [1]=src_bytes, [2]=dst_bytes, [14]=count, [15]=srv_count...
    vector_ia = [0.0] * 33
    
    # 2. Expresiones Regulares para capturar los valores del Syslog
    # Buscamos patrones como: duration=12, sentbyte=4500, rcvdbyte=8900
    patron_duration = re.search(r'duration=(\d+)', linea_log)
    patron_src_bytes = re.search(r'sentbyte=(\d+)', linea_log)
    patron_dst_bytes = re.search(r'rcvdbyte=(\d+)', linea_log)
    
    # Simulación de métricas de ráfaga/conteo si el log indica escaneo o conexiones repetidas
    patron_msg = re.search(r'msg="([^"]+)"', linea_log)
    
    # 3. Asignar los valores extraídos a sus posiciones exactas en el vector
    if patron_duration:
        vector_ia[0] = float(patron_duration.group(1))
        
    if patron_src_bytes:
        vector_ia[1] = float(patron_src_bytes.group(1))
        
    if patron_dst_bytes:
        vector_ia[2] = float(patron_dst_bytes.group(1))
        
    # Lógica de Auditoría: Si el log dice "pingsweep" o "port_scan", simulamos comportamiento anómalo
    if patron_msg and ("scan" in patron_msg.group(1).lower() or "flood" in patron_msg.group(1).lower()):
        vector_ia[14] = 300.0  # Elevamos el 'count' (conexiones simultáneas)
        bitter_error = 1.0
        vector_ia[16] = bitter_error  # 'serror_rate' al 100%
        vector_ia[17] = bitter_error  # 'srv_serror_rate' al 100%
        
    return vector_ia

# =====================================================================
# PRUEBA DEL TRADUCTOR
# =====================================================================
if __name__ == "__main__":
    # Log simulado de un ataque real registrado por un FortiGate
    log_crudo_fortinet = (
        'date=2026-05-22 time=23:15:00 devname=FG-SOC device_id=FGT80E '
        'logid="0419016384" type="traffic" subtype="anomaly" level="alert" '
        'srcip=192.168.1.50 dstip=10.0.0.1 action="clear" msg="TCP SYN Flood/Port Scan detected" '
        'duration=0 sentbyte=0 rcvdbyte=0'
    )
    
    print("📝 Procesando log crudo de Fortinet...")
    vector_listo = parsear_log_fortinet(log_crudo_fortinet)
    
    print(f"\n✅ Vector de 33 características generado:")
    print(vector_listo)
    print(f"Métricas clave extraídas -> Duration: {vector_listo[0]} | Src_Bytes: {vector_listo[1]} | Count: {vector_listo[14]}")