# Comandos basicos de GitHub con Git

Este archivo contiene los comandos mas usados para trabajar con un repositorio de GitHub desde la terminal.

## Clonar un repositorio

```bash
git clone https://github.com/usuario/repositorio.git
```

## Entrar a la carpeta del proyecto

```bash
cd nombre-del-repositorio
```

## Ver el estado del repositorio

```bash
git status
```

## Agregar cambios

Agregar un archivo:

```bash
git add archivo.txt
```

Agregar todos los archivos modificados:

```bash
git add .
```

## Guardar cambios

```bash
git commit -m "Mensaje del cambio"
```

## Subir cambios a GitHub

Si tu rama principal es `main`:

```bash
git push origin main
```

Si tu rama principal es `master`:

```bash
git push origin master
```

## Descargar cambios desde GitHub

```bash
git pull origin main
```

## Ver ramas

```bash
git branch
```

## Crear una rama nueva

```bash
git switch -c nueva-rama
```

## Cambiar de rama

```bash
git switch nombre-rama
```

## Ver historial de commits

```bash
git log --oneline
```

## Conectar un repositorio local con GitHub

```bash
git remote add origin https://github.com/usuario/repositorio.git
```

## Flujo basico

```bash
git status
git add .
git commit -m "Mi cambio"
git push origin main
```

## Nota

Git es la herramienta que usas en la terminal.
GitHub es la plataforma donde alojas el repositorio en linea.