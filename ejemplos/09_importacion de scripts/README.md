# Importacion de scripts paso a paso

Esta carpeta muestra una idea simple:

1. Un archivo principal.
2. Un script de `frontend`.
3. Un script de `backend`.
4. Una importacion entre archivos creados por ti.

## Idea del ejemplo

Aqui simulamos una aplicacion pequena:

- El `frontend` muestra mensajes en pantalla.
- El `backend` prepara los datos o la respuesta.
- El archivo principal importa ambos y los conecta.

## Orden recomendado

1. Lee `backend/servicio_saludo.py`
2. Lee `frontend/pantalla.py`
3. Lee `app_principal.py`
4. Ejecuta `app_principal.py`

## Como ejecutarlo

Desde la carpeta `Python-Class` ejecuta:

```bash
py "ejemplos/09_importacion de scripts/app_principal.py"
```

O tambien:

```bash
python "ejemplos/09_importacion de scripts/app_principal.py"
```

## Que debes observar

1. `app_principal.py` importa funciones de otros archivos.
2. El backend crea el mensaje.
3. El frontend lo muestra.
4. El archivo principal coordina todo.

## Antes de subir cambios

1. Lee los comentarios.
2. Ejecuta el archivo principal.
3. Haz un cambio pequeno, por ejemplo el texto del saludo.
4. Ejecuta otra vez para ver el resultado.