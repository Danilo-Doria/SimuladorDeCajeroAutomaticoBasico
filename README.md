<div align="center">

# 🏧 Simulador de Cajero Automático Básico

**Simulador Interactivo de Operaciones Bancarias en Consola desarrollado con Python**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

</div>

---

## 📖 Descripción

**SimuladorDeCajeroAutomaticoBasico** es una aplicación de terminal desarrollada en **Python 3** que emula las operaciones financieras fundamentales de un cajero automático bancario (ATM).

El programa permite configurar sesiones con múltiples operaciones consecutivas, control de saldo en tiempo real, validación de montos positivos y manejo preventivo de fondos insuficientes y errores de formato.

---

## 🚀 Características Principales

- **Sesiones Multioperación:** Permite al usuario definir el número exacto de transacciones que desea ejecutar en su sesión.
- **Consulta de Saldo en Tiempo Real:** Visualización instantánea del saldo disponible.
- **Retiro de Dinero con Protección de Sobregiro:** Validación estricta que impide retiros superiores al saldo actual ("Fondos insuficientes") y bloquea montos negativos.
- **Depósito de Fondos:** Incremento seguro del saldo con validación de valores positivos.
- **Manejo Robusto de Excepciones:** Empleo de bloques `try / except ValueError` para evitar caídas del programa ante ingresos alfanuméricos en campos numéricos.
- **Estructura Moderna de Control:** Uso de sentencia `match - case` de Python para el enrutamiento limpio de las opciones de menú.

---

## 📂 Estructura del Proyecto

```text
SimuladorDeCajeroAutomaticoBasico/
├── LICENSE                 # Licencia MIT
├── main.py                 # Lógica completa del cajero y ciclo de transacciones
└── README.md               # Documentación del proyecto
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.10+** (requiere soporte para la sentencia `match - case`)

---

## ⚙️ Puesta en Marcha

### 1. Clonar el repositorio
```bash
git clone https://github.com/Danilo-Doria/SimuladorDeCajeroAutomaticoBasico.git
cd SimuladorDeCajeroAutomaticoBasico
```

### 2. Ejecutar la aplicación
```bash
python3 main.py
```

### 3. Flujo de Uso
1. Indica la cantidad de operaciones que deseas efectuar durante la sesión.
2. Selecciona la opción deseada:
   - `1` → Consultar saldo
   - `2` → Retirar Dinero
   - `3` → Depositar Dinero
3. Ingresa los montos correspondientes y observa el balance actualizado tras cada movimiento.

---

## 👨💻 Author

- GitHub: **[Danilo-Doria](https://github.com/Danilo-Doria)**
- LinkedIn: **[Danilo Doria Diaz](https://www.linkedin.com/in/danilo-doria-diaz)**
- Mail: **danilodoria519@gmail.com**

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
