# Filtro Python

En este repositorio encontraras un archivo que contiene un trabajo con el fin de realizar un sistema integral de registro y seguimiento para *Movistar*.

## Características

### Funcionalidades requeridas para el Módulo de Usuarios (Administrador)

***Registro y Gestión de Usuarios**:*

- Operaciones CRUD para crear, leer, actualizar y eliminar perfiles de usuarios.
- Captura de información detallada de cada usuario, incluyendo nombre, dirección, información de contacto, entre otros.
- Funcionalidad para asignar categorías de usuarios, como nuevos clientes, clientes regulares y clientes leales.

**Seguimiento del Historial de Usuarios:**

- Registro y almacenamiento de servicios utilizados por cada usuario.
- Seguimiento de las interacciones de los usuarios con la empresa, como consultas de servicio al cliente, reclamaciones y sugerencias.

**Personalización de Servicios:**

- Utilización de datos de usuario para ofrecer servicios y promociones personalizadas.
- Análisis de patrones de comportamiento de los usuarios para adaptar la oferta de servicios a las necesidades individuales.

**Gestión de la Fidelización de Clientes:**

- Identificación y seguimiento de clientes leales basados en la duración de su relación con la empresa.
- Integración con el módulo de bonificaciones para ofrecer recompensas especiales a los clientes más fieles.

### Funcionalidades Requeridas para Cada Módulo

**Módulo de Gestión de Servicios:**

- Operaciones CRUD para cada tipo de servicio ofrecido, como Internet de Fibra Óptica, planes pospago, prepago, etc.
- Capacidad para agregar, modificar y eliminar servicios según sea necesario.
- Registro de información detallada sobre cada servicio, incluyendo características, precios, entre otros.

**Módulo de Reportes:**

- Generación de informes sobre la cantidad de productos/servicios ofrecidos por la empresa.
- Análisis de datos para identificar los servicios más populares que se prestan por la empresa.
- Informes sobre usuarios que han adquirido cada servicio y con ello la cantidad de este mismo.

**Módulo de Bonificaciones para Clientes Leales:**

- Identificación automática de clientes que han permanecido con la compañía por más de 10 años.
- Cálculo y asignación de bonificaciones especiales para estos clientes, como descuentos, servicios adicionales gratuitos, entre otros (Solamente notificación para ser redireccionado al asesor de ventas).

## Estructura

![alt text](image-7.png)

Tenemos 3 archivos donde cada uno tienen funcionalidades distintas.

|Nombre del Archivo| Funcionalidad|
|--|--|
|```movistar.py```|Este archivo contiene todo el proyecto python.|
|```servicios.json```| Archivo json que contiene todo los datos de los servicios del usuario.|
|```usuario.json```| Archivo json que contiene todos los datos del usaurio.|
