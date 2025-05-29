
# Sesión 1: Introducción a Git

## Objetivo
- Comprender qué es Git
- Entender cómo funciona
- Usar comandos básicos

---

## ¿Qué es Git?
Git es un sistema de control de versiones distribuido, gratuito y de código abierto.

### ¿Para qué sirve?
- Guardar cambios
- Volver a versiones anteriores
- Trabajar en equipo
- Rastrear historial

---

## Git vs GitHub
- **Git**: herramienta local para control de versiones
- **GitHub**: plataforma en la nube para alojar repositorios Git

---

## ¿Cómo funciona Git?
Git guarda *snapshots* de los archivos, no diferencias.

### Tres áreas principales:
1. **Working Directory**: donde editas tus archivos.
2. **Staging Area**: zona temporal donde seleccionas los cambios.
3. **Repository**: historial de versiones confirmado.

```
[Working Directory] --> git add --> [Staging Area] --> git commit --> [Repository]
```

---

## Configuración inicial
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

---

## Comandos principales
```bash
git init                      # Inicializa un repositorio
git status                   # Muestra el estado
git add archivo.txt          # Añade un archivo al staging
git add .                    # Añade todos los cambios
git commit -m "mensaje"      # Guarda los cambios en el repositorio
git log                      # Muestra el historial de commits
```

---

## Trabajo con ramas
```bash
git branch nombre_rama       # Crear nueva rama
git checkout nombre_rama     # Cambiar a la rama
git merge nombre_rama        # Fusionar con la rama actual
```

---

## Otros comandos útiles
```bash
git diff                     # Ver diferencias
git remote add origin URL    # Conectar con repositorio remoto
git push -u origin main      # Subir cambios a GitHub
git pull origin {rama}
```

---

## Buenas prácticas
- Commits claros y frecuentes
- Revisar antes de usar `git add .`
- Usar ramas para nuevas funcionalidades


