# Guía de Contribución - Fitzone

¡Gracias por tu interés en contribuir al proyecto Fitzone! Este documento explica cómo puedes participar en el desarrollo.

## 📋 Proceso de Contribución

1. **Crea un fork** del repositorio.
2. **Crea una rama** con un nombre descriptivo para tu cambio:
   ```bash
   git checkout -b feature/nombre-de-la-funcionalidad
   ```
3. **Realiza tus cambios** siguiendo las convenciones del proyecto.
4. **Confirma tus cambios** con un mensaje claro y descriptivo:
   ```bash
   git commit -m "feat: descripción breve del cambio"
   ```
5. **Sube tus cambios** a tu fork:
   ```bash
   git push origin feature/nombre-de-la-funcionalidad
   ```
6. **Abre un Pull Request** describiendo los cambios realizados.

## 📝 Convenciones de Commits

Utilizamos el estándar [Conventional Commits](https://www.conventionalcommits.org/es/):

| Tipo | Descripción |
|------|-------------|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de errores |
| `docs` | Cambios en documentación |
| `style` | Cambios de formato (sin afectar lógica) |
| `refactor` | Refactorización de código |
| `test` | Añadir o modificar pruebas |
| `chore` | Tareas de mantenimiento |

## 🐛 Reportar Errores

Para reportar un error, abre un **Issue** en GitHub con la siguiente información:

- Descripción clara del problema
- Pasos para reproducirlo
- Comportamiento esperado vs. comportamiento actual
- Capturas de pantalla (si aplica)

## 💡 Proponer Mejoras

Para proponer una nueva funcionalidad, abre un **Issue** con la etiqueta `enhancement` y describe:

- El problema que resuelve
- La solución propuesta
- Alternativas consideradas

## 📁 Estructura del Código

Sigue la estructura de carpetas definida en el README:

- `src/models/` — Modelos de datos
- `src/controllers/` — Lógica de negocio
- `src/views/` — Interfaz de usuario
- `src/utils/` — Utilidades compartidas
- `tests/` — Pruebas unitarias e integración
- `docs/` — Documentación técnica

## ✅ Checklist antes de un Pull Request

- [ ] El código sigue las convenciones del proyecto
- [ ] Se han añadido pruebas para los nuevos cambios
- [ ] La documentación ha sido actualizada si es necesario
- [ ] El CHANGELOG.md refleja los cambios realizados
- [ ] Todos los tests existentes pasan correctamente
