# ATM Machine Simulation

Este proyecto simula las operaciones básicas de un cajero automático (ATM) que permite realizar depósitos y retiros de dinero, con soporte para billetes de $10,000 y $20,000. El sistema verifica y maneja diversos escenarios, como validaciones de montos y límites de billetes, además de mostrar el saldo actual en el cajero.

## Requisitos del Sistema

- **Python versión**: 3.8 o superior
- **Sistemas Operativos compatibles**: Windows, macOS, Linux

> **Nota**: Asegúrate de tener la versión de Python correcta instalada y configurada en tu sistema. Puedes verificar tu versión de Python con el comando:
  ```bash
  python --version


git clone https://github.com/tuusuario/atm-machine.git
cd atm-machine

python -m venv venv
source venv/bin/activate  # En macOS/Linux
.\venv\Scripts\activate   # En Windows

pip install -r requirements.txt



atm-machine/
│
├── models/
│   └── atm_machine.py     # Lógica principal del cajero automático (ATM)
│
├── tests/
│   └── test_atm_machine.py # Pruebas unitarias para verificar la funcionalidad del ATM
│
├── atm.py                 # Script principal para ejecutar la simulación del ATM
│
└── README.md              # Documentación del proyecto



python atm.py


python -m unittest discover -s tests -v






Cobertura de Código con Coverage

Este proyecto utiliza coverage.py para medir la cobertura de las pruebas y generar un reporte en HTML.
Instrucciones para la Cobertura de Código

    Instala la Herramienta coverage.py

    Si coverage.py no está instalado, instálalo con el siguiente comando:

    bash

pip install coverage

Ejecuta las Pruebas con Coverage

Usa coverage para ejecutar las pruebas y recolectar los datos de cobertura:

bash

coverage run -m unittest discover -s tests

Esto generará un archivo oculto llamado .coverage en el directorio principal, que contiene los datos de cobertura.

Genera el Reporte en HTML

Para crear el reporte de cobertura en formato HTML:

bash

coverage html