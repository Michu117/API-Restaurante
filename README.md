# API Menuboard
Investigación e integración de un API público para aplicaciones de restaurantes.

# APIs Investigadas

## 1. OpenWeather - Weather API 
### Current Weather Data:
- Acceda a datos meteorológicos actuales de cualquier ubicación.
- Se recopilan y procesan datos meteorológicos de diferentes fuentes, como modelos meteorológicos globales y locales, satélites, radares y una amplia red de estaciones meteorológicas.
- Formatos JSON, XML y HTML.
- Incluido en suscripciones gratuitas y de pago.

[Documentación](https://openweathermap.org/current)

### Funcionalidades:
La API de OpenWeatherMap permite acceder a datos meteorológicos actuales de cualquier parte del mundo. Sus funcionalidades clave incluyen:

- **Consulta de datos meteorológicos actuales:** Proporciona información sobre temperatura, humedad, presión, velocidad del viento, nubosidad, visibilidad y fenómenos meteorológicos (lluvia, nieve, etc.).
- **Formatos de respuesta:** Soporta JSON (por defecto), XML y HTML.
- **Parámetros adicionales:** Permite definir unidades de medida (standard, metric, imperial) y soporte para múltiples idiomas.
- **API de geocodificación:** Convierte nombres de ciudades y códigos postales en coordenadas geográficas y viceversa.
- **Descarga masiva:** Permite obtener grandes volúmenes de datos sin necesidad de realizar llamadas a la API en tiempo real.

### Requisitos:
- Clave API (```appid```) obligatoria para autenticar las solicitudes.

Parámetros requeridos:
- ```lat``` y ```lon``` para coordenadas geográficas.
- ```q``` para nombre de ciudad (con código de país opcional).
- ```id``` para identificador de ciudad.
- ```zip``` para código postal (requiere código de país si no es EE.UU.).

### Limitaciones
- **Obsolescencia de ciertas funciones:** La geocodificación integrada y la búsqueda por nombre de ciudad han quedado obsoletas y no recibirán actualizaciones.
- **Visibilidad limitada:** Máximo de 10 km.
- **Restricción de llamadas:** Dependiendo del plan contratado, puede haber límites en la cantidad de solicitudes permitidas por minuto.
- 1000 llamadas API por día de forma gratuita y 0,0015 USD por llamada API por encima del límite diario.

## 2. TheMealDB
TheMealDB es una API RESTful que proporciona una base de datos abierta y colaborativa de recetas de todo el mundo.

[Documentación](https://www.themealdb.com/api.php)
### Funcionalidades:
- **Búsqueda de recetas por nombre:** Permite buscar recetas específicas utilizando el nombre del plato.
- **Listado de recetas por letra inicial:** Ofrece la posibilidad de listar todas las recetas que comienzan con una letra específica.
- **Obtener detalles completos de una receta por ID:** Proporciona información detallada de una receta específica mediante su identificador único.
- **Obtener una receta aleatoria:** Devuelve una receta seleccionada al azar.
- **Listar todas las categorías, áreas e ingredientes:** Facilita la obtención de listas completas de categorías de platos, áreas culinarias e ingredientes disponibles en la base de datos.
- **Filtrar recetas por ingrediente principal, categoría o área:** Permite filtrar recetas basándose en un ingrediente específico, una categoría de plato o una región culinaria.

### Requisitos:
- Clave API de prueba: Durante el desarrollo o para uso educativo, se puede utilizar la clave de prueba "1".

- Clave API de producción: Para aplicaciones que se lanzarán públicamente, es necesario convertirse en patrocinador para obtener una clave de producción. Los patrocinadores tienen acceso a funciones adicionales, como la capacidad de filtrar por múltiples ingredientes y agregar sus propias recetas e imágenes.

### Limitaciones
- **Acceso limitado para usuarios no patrocinadores:** Algunas funcionalidades avanzadas, como la selección de 10 recetas aleatorias, las últimas recetas añadidas y el filtrado por múltiples ingredientes, están disponibles únicamente para patrocinadores.

- **Sin límite de tasa conocido:** Actualmente, no se ha informado de un límite de solicitudes para la API, lo que facilita su uso en aplicaciones de desarrollo.

## 3. ExchangeRate-API
La ExchangeRate-API es una herramienta que proporciona datos de tipos de cambio de divisas a través de una API sencilla y rápida.

[Documentación](https://www.exchangerate-api.com/docs/overview)
### Funcionalidades:
- **Endpoint Estándar:** Permite obtener un objeto JSON con los tipos de cambio desde una moneda base a todas las demás monedas soportadas. 
- **Conversión de Pares:** Al enviar un par de códigos de moneda y una cantidad opcional, la API devuelve el tipo de cambio entre esas dos monedas y la conversión de la cantidad proporcionada. 
- **Datos Enriquecidos:** Ofrece información adicional como el nombre de la moneda, su símbolo, el país o región asociado y una URL de la bandera correspondiente. Esta funcionalidad está disponible para usuarios en los planes Business o Volume. 
- **Datos Históricos:** Permite acceder a tipos de cambio de fechas específicas en el pasado, con datos disponibles desde 1990 para algunos pares de monedas. Esta característica también está reservada para usuarios en los planes Business o Volume. 

### Requisitos:
- **Clave de API:** Para acceder a la mayoría de las funcionalidades, es necesario registrarse y obtener una clave de API. Sin embargo, existe un endpoint de acceso abierto que no requiere clave, aunque está sujeto a términos específicos y requiere atribución. 

### Limitaciones
- **Frecuencia de Actualización:** La frecuencia de actualización de los datos puede variar según el plan seleccionado. Los planes gratuitos pueden tener actualizaciones menos frecuentes en comparación con los planes de pago. 
- **Acceso a Funcionalidades Avanzadas:** Características como datos enriquecidos y datos históricos están disponibles únicamente para usuarios en los planes Business o Volume. 
- **Límites de Solicitudes:** Dependiendo del plan, existen límites en la cantidad de solicitudes que se pueden realizar a la API. Es importante revisar estos límites para asegurarse de que se ajusten a las necesidades de la aplicación.

# Propuesta de Integración:
## APIs Seleccionadas: TheMealDB y ExchangeRate
Incorporarmos TheMealDB y ExchangeRate-API en la aplicación de restaurante para mejorar la gestión del menú, y poder convertir la moneda para que cada cliente pueda saber el precio que tendría ese producto en su país. De esta forma permitiendo a los clientes explorar platos, ingredientes y recetas con detalles enriquecidos.
## Mejoras al sistema
### TheMealDB API:
TheMealDB es una API que proporciona acceso a una extensa base de datos de recetas, ingredientes e imágenes de platillos internacionales. Permite a los usuarios explorar platos de diferentes categorías y países, obtener detalles completos sobre cada platillo, incluyendo su nombre, ingredientes y métodos de preparación.
### ExchangeRate-API:
ExchangeRate-API ofrece acceso a tasas de cambio de divisas en tiempo real, permitiendo convertir cantidades entre diferentes monedas. Esta API es útil para restaurantes que reciben pagos internacionales o compran insumos de otros países, ya que permite realizar conversiones precisas de precios y costos en función de las tasas de cambio actuales.

# Implementación y Funcionamiento
