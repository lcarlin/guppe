"""
mod_system_info.py

Módulo de coleta de informações de sistema.
Compatível com Linux, Windows e macOS.

Dependências:
- psutil
- py-cpuinfo
"""

import platform
import psutil
import cpuinfo
import logging

__all__ = ['get_system_info']

logger = logging.getLogger(__name__)

def get_system_info():
    """
    Coleta e retorna informações detalhadas de hardware e sistema operacional.

    Returns:
        dict: Dicionário contendo informações de CPU, memória e sistema.
    """
    info = {}

    try:
        cpu = cpuinfo.get_cpu_info()
        info['cpu_brand'] = cpu.get('brand_raw', 'N/A')
        info['cpu_arch'] = cpu.get('arch', 'N/A')
        info['cpu_bits'] = cpu.get('bits', 'N/A')
        info['cpu_freq'] = cpu.get('hz_actual_friendly', 'N/A')

        info['cpu_cores_physical'] = psutil.cpu_count(logical=False)
        info['cpu_cores_logical'] = psutil.cpu_count(logical=True)

        mem = psutil.virtual_memory()
        info['ram_total_gb'] = round(mem.total / (1024 ** 3), 2)
        info['ram_available_gb'] = round(mem.available / (1024 ** 3), 2)

        info['system'] = platform.system()
        info['platform'] = platform.platform()
        info['processor'] = platform.processor()
        info['machine'] = platform.machine()

    except Exception as e:
        logger.error(f"Erro ao coletar informações do sistema: {e}")
        info['error'] = str(e)

    return info

# Para testes diretos do módulo
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sys_info = get_system_info()
    for key, value in sys_info.items():
        print(f"{key}: {value}")
