# Diseño y Arquitectura - Fitzone

## Arquitectura del Sistema

El sistema Fitzone seguirá un patrón de arquitectura **MVC (Modelo-Vista-Controlador)**:

```
┌──────────────┐     ┌──────────────────┐     ┌──────────────┐
│    Vista     │────▶│   Controlador    │────▶│    Modelo    │
│  (Interfaz)  │◀────│  (Lógica negocio)│◀────│   (Datos)    │
└──────────────┘     └──────────────────┘     └──────────────┘
```

## Módulos Principales

### Modelos de Datos

| Entidad | Descripción |
|---------|-------------|
| `Miembro` | Datos del socio del gimnasio |
| `Membresía` | Tipo y duración de la membresía |
| `Pago` | Registro de pagos realizados |
| `Rutina` | Plan de entrenamiento |
| `Equipo` | Equipamiento del gimnasio |
| `Asistencia` | Registro de visitas |

### Diagrama de Entidades (ER simplificado)

```
Miembro ──────── Membresía
   │                 │
   │                 └── Pago
   │
   ├──── Asistencia
   │
   └──── Rutina ──── Ejercicio

Equipo ──── Mantenimiento
```

## Tecnologías a Evaluar

| Capa | Opciones |
|------|----------|
| Frontend | HTML/CSS/JS, React, Vue.js |
| Backend | Python/Django, Node.js, Java/Spring |
| Base de Datos | PostgreSQL, MySQL, SQLite |

## Próximos Pasos

1. Definir el stack tecnológico definitivo
2. Diseñar el modelo de base de datos
3. Crear prototipos de la interfaz de usuario
4. Implementar los módulos principales
