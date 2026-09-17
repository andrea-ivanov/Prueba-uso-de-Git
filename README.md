# Guía Básica de GitHub

Esta guía cubre los conceptos esenciales para empezar a trabajar con Git y GitHub: repositorios, ramas, commits, pull requests y sincronización de cambios.

## 👥 Integrantes

| Nombre | GitHub |
|---|---|
| Nombre Apellido 1 | <a href="https://github.com/Alejandrorr572" target="_blank" rel="noopener noreferrer"><span style="background:#1E90FF;color:#fff;padding:6px 10px;border-radius:5px;display:inline-block;text-decoration:none;">Alejandrorr572</span></a> |
| Alejandro El Harchi Argüelles | <a href="https://github.com/Harchi18" target="_blank" rel="noopener noreferrer"><span style="background:#28A745;color:#fff;padding:6px 10px;border-radius:5px;display:inline-block;text-decoration:none;">Harchi18 </span></a> |
| Nombre Apellido 3 | <a href="https://github.com/nicooprezz" target="_blank" rel="noopener noreferrer"><span style="background:#FF6347;color:#fff;padding:6px 10px;border-radius:5px;display:inline-block;text-decoration:none;">nicooprezz </span></a> |
| Andrea Ivanov | <a href="https://github.com/andrea-ivanov" target="_blank" rel="noopener noreferrer"><span style="background:#5F9EA0;color:#fff;padding:6px 10px;border-radius:5px;display:inline-block;text-decoration:none;">andrea-ivanov</span></a> |
| Profesor | <a href="https://github.com/EnriqueJRodriguez" target="_blank" rel="noopener noreferrer"><span style="background:#000000;color:#fff;padding:6px 10px;border-radius:5px;display:inline-block;text-decoration:none;">EnriqueJRodriguez</span></a> |


## 📌 Conceptos básicos

Para descargar una copia local de un repositorio existente:
diowhaduiwhauidhwauidhwuiahduiwahuidwa

```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio
```

## 🌿 Trabajar con ramas

### Crear una nueva rama

```bash
git branch nombre-rama
```

### Cambiar a una rama

```bash
git checkout nombre-rama
```

### Crear y cambiar a la vez

```bash
git checkout -b nombre-rama
```

### Ver todas las ramas

```bash
git branch
```

### Buenas prácticas de nombres de ramas

- `feature/nueva-funcionalidad`
- `fix/corregir-bug`
- `docs/actualizar-readme`

## 💾 Hacer commits

### 1. Revisar el estado de los archivos

```bash
git status
```

### 2. Añadir archivos al área de preparación (staging)

```bash
git add archivo.txt       # un archivo específico
git add .                 # todos los archivos modificados
```

### 3. Crear el commit

```bash
git commit -m "Mensaje claro y descriptivo del cambio"
```

### 4. Ver el historial de commits

```bash
git log
```

## 📤 Subir cambios a GitHub (push)

```bash
git push origin nombre-rama
```

Si es la primera vez que subes esa rama:

```bash
git push -u origin nombre-rama
```

## 📥 Traer cambios del repositorio remoto

### `git fetch`

Descarga los cambios del remoto **sin fusionarlos** con tu rama local. Te permite ver qué ha cambiado antes de decidir integrarlo.

```bash
git fetch origin
```

### `git pull`

Es un `fetch` + `merge` en un solo paso: descarga los cambios y los combina automáticamente con tu rama actual.

```bash
git pull origin main
```

> 💡 **Tip:** usa `git fetch` cuando quieras revisar los cambios antes de aplicarlos, y `git pull` cuando quieras actualizarte directamente.

## 🔀 Pull Requests (PR)

Un **Pull Request** es una solicitud para fusionar los cambios de tu rama con otra rama (normalmente `main` o `develop`), permitiendo revisión antes de integrarlos.

### Pasos típicos

1. Crea una rama y haz tus cambios (commits).
2. Sube la rama a GitHub:
   ```bash
   git push -u origin nombre-rama
   ```
3. Ve al repositorio en GitHub y haz clic en **"Compare & pull request"**.
4. Describe los cambios realizados y su propósito.
5. Solicita revisión a tus compañeros de equipo.
6. Una vez aprobado, haz clic en **"Merge pull request"**.
7. Elimina la rama si ya no es necesaria:
   ```bash
   git branch -d nombre-rama          # local
   git push origin --delete nombre-rama  # remota
   ```

## 🔄 Flujo de trabajo resumido

```bash
# 1. Actualiza tu rama principal
git checkout main
git pull origin main

# 2. Crea una nueva rama para tu tarea
git checkout -b feature/mi-tarea

# 3. Haz cambios y commits
git add .
git commit -m "Descripción del cambio"

# 4. Sube tu rama
git push -u origin feature/mi-tarea

# 5. Abre un Pull Request en GitHub

# 6. Tras la aprobación, fusiona y limpia
git checkout main
git pull origin main
git branch -d feature/mi-tarea
```

## 📚 Recursos adicionales

- [Documentación oficial de Git](https://git-scm.com/doc)
- [Guías de GitHub](https://docs.github.com/es)
