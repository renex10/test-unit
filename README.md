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
