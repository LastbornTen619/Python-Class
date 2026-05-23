# Python-Class

Guia para estudiantes para usar este repositorio con Git y GitHub.

## Que vas a hacer aqui

En este repositorio vas a:

1. Ver ejemplos de clase.
2. Subir tus ejercicios.
3. Aprender a usar Git desde la terminal.

## Regla principal

Trabaja siempre en tu propia rama y dentro de tu propia carpeta.

## Estructura recomendada del repositorio

```text
Python-Class/
	ejemplos/
		01-funciones/
		02-condicionales/
		03-bucles/
		08_Interfaces/
	ejercicios/
		nombre-apellido/
			01-funciones/
			02-condicionales/
			03-bucles/
```

Ejemplo:

```text
ejercicios/
	juan-perez/
		01-funciones/
			ejercicio_1.py
		02-condicionales/
			ejercicio_2.py
```

## Configuracion inicial en la computadora del estudiante

Estos comandos se ejecutan una sola vez por equipo.

### 1. Configurar nombre y correo

```bash
git config --global user.name "Nombre Apellido"
git config --global user.email "correo@ejemplo.com"
```

### 2. Activar el administrador de credenciales

```bash
git config --global credential.helper manager
```

### 3. Iniciar sesion con GitHub una sola vez

```bash
git credential-manager github login
```

Esto abre el navegador para autorizar Git. Cuando termina, Git recuerda la cuenta y normalmente ya no pide autenticacion en cada `push`.

## Primer uso del repositorio

### 1. Clonar el repositorio

```bash
git clone https://github.com/LastbornTen619/Python-Class.git
```

### 2. Entrar a la carpeta

```bash
cd Python-Class
```

### 3. Descargar cambios recientes

```bash
git pull origin main
```

## Crear tu rama personal

Crea tu rama con un nombre claro.

Formato recomendado:

```text
nombre-apellido
```

Ejemplo:

```bash
git switch -c juan-perez
```

La primera vez que la suba a GitHub:

```bash
git push -u origin juan-perez
```

Despues de eso, ya puede usar solo:

```bash
git push
```

## Flujo diario del estudiante

### 1. Entrar al repo

```bash
cd Python-Class
```

### 2. Ir a su rama

```bash
git switch juan-perez
```

### 3. Revisar el material actualizado

```bash
git pull origin main
```

### 4. Crear o editar su ejercicio dentro de su carpeta

Ejemplo de ruta:

```text
ejercicios/juan-perez/01-funciones/
```

### 5. Revisar cambios

```bash
git status
```

### 6. Agregar cambios

```bash
git add .
```

### 7. Hacer commit

```bash
git commit -m "Entrega ejercicio de funciones"
```

### 8. Subir cambios

```bash
git push
```

## Comandos basicos que deben aprender

```bash
git status
git add .
git commit -m "mensaje"
git push
git pull origin main
git branch
git switch nombre-rama
git switch -c nueva-rama
git log --oneline
```

## Reglas para mantener orden

1. No trabajar directamente en `main`.
2. Usa solo tu carpeta y tu rama.
3. Los ejemplos estan en `ejemplos/`.
4. Tus ejercicios van en `ejercicios/nombre-apellido/`.
5. Los commits deben tener mensajes claros.

## Si Git vuelve a pedir autenticacion

Ejecuta otra vez:

```bash
git credential-manager github login
```

## Si aparece error de carpeta no confiable en red

En equipos que usan carpetas compartidas o unidades de red puede aparecer un error de seguridad. En ese caso se agrega la carpeta como segura:

```bash
git config --global --add safe.directory '%(prefix)///100.120.167.121/General/Python-Class'
```

## Resumen rapido

```bash
git config --global user.name "Nombre Apellido"
git config --global user.email "correo@ejemplo.com"
git config --global credential.helper manager
git credential-manager github login
git clone https://github.com/LastbornTen619/Python-Class.git
cd Python-Class
git switch -c nombre-apellido
git push -u origin nombre-apellido
```