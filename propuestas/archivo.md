PROYECTO
Desarrollador Woocommerce – Checkout y Envíos Personalizados

Descripción:
Estamos buscando un desarrollador WooCommerce con experiencia comprobable para personalizar el proceso de checkout y la gestión de envíos de nuestra tienda online. Aunque el checkout actual funciona, necesitamos una implementación técnica avanzada para optimizar el flujo y mejorar la experiencia del cliente, basándonos en mockups ya definidos. La tienda online es acaneli.pe.

Las personalizaciones clave incluyen:

1) Reorganización del checkout en secciones claras:
* Contacto
* Dirección
* Envío
* Resumen del pedido

2) Implementación de lógica condicional en la sección de Envío:
* Botones destacados para seleccionar entre 'Recojo en tienda' o 'Envío a domicilio'.
* Si se elige 'Recojo en tienda': Mostrar múltiples direcciones físicas de recojo, horarios de atención y aplicar envío gratuito.
* Si se elige 'Envío a domicilio': Ofrecer opciones como 'Envío Express' y 'Envío 2–4 días hábiles', incluir un selector de fecha de entrega y asegurar la actualización dinámica del total del pedido.

3) Un resumen del pedido que se actualice de forma dinámica en tiempo real según las opciones de envío seleccionadas por el cliente.

Es fundamental que el freelancer tenga experiencia previa en la personalización de procesos de checkout en WooCommerce y un profundo conocimiento de las reglas de envío y la integración de funcionalidades de fecha y franjas horarias de entrega. Este proyecto es puramente técnico; no se requiere trabajo de diseño gráfico ni estrategias de marketing.

Agradecemos que los interesados compartan ejemplos de trabajos similares y una breve explicación de su enfoque para la implementación de este proyecto.

Categoría: Programación y Tecnología
Subcategoría: Tiendas Online (e-commerce)
¿Cuál es el alcance del proyecto?: Cambio mediano
WooCommercePHPJavaScriptCSSWordPressHTMLProgramación y Tecnología


CONVERSACION:

NOSOTROS:
Hola, Estuve revisando el flujo actual en `acaneli.pe` y entiendo perfectamente lo que necesitan: transformar el checkout estándar de WooCommerce en una experiencia fluida y segmentada, tal como lo tienen en sus mockups.

Este es un trabajo 100% técnico y de lógica backend/frontend, que es donde tengo mi mayor experiencia. Para implementar los requerimientos puntuales que mencionas, mi enfoque sería el siguiente:
1. Estructura y UX
En lugar de usar plugins genéricos que cargan el sitio, modificaré los templates del checkout y usaré los "hooks" nativos de WooCommerce para separar visualmente las etapas (Contacto, Dirección, Envío, Resumen) sin romper la funcionalidad de actualización en tiempo real.
2. Lógica Condicional de Envíos
Esta es la parte crítica. Implementaré un script a medida para controlar la visualización dinámica:
- Si el cliente elige **"Recojo en tienda"**: Se ocultarán los campos de envío y se desplegarán las sedes con sus horarios mediante un selector limpio. Forzaremos el costo de envío a 0 de inmediato.
- Si elige **"Envío a domicilio"**: Se activarán las opciones de envío (Express vs Estándar) y, lo más importante, integraremos el selector de fecha (Datepicker) condicionado a los días hábiles que configuren.

3. Actualización Dinámica
Para asegurar que el total del pedido cambie al instante sin recargar la página, trabajaré sobre los fragmentos AJAX de WooCommerce. Esto garantiza que si el usuario cambia de "Express" a "Recojo", el total se recalcule en milisegundos, evitando errores en el pago.

Por qué trabajar conmigo?
Tengo experiencia avanzada manipulando el `checkout.js` y las clases de envío de WooCommerce. No me limito a instalar plugins; escribo el código necesario para que la funcionalidad sea exacta a lo que piden y el sitio no pierda velocidad.
Me gustaría ver los mockups para estimar con precisión el tiempo de desarrollo, pero calculo que es una implementación que podríamos tener operativa y testeada en pocos días.
Quedo atento para conversar.
Saludos,

CLIENTE:
“Gracias. Me gusta tu enfoque. Para asegurar compatibilidad y que no se rompa con updates:
¿Lo harás como plugin propio (y si hay overrides, solo mínimos en child theme, sin tocar core)?
¿Trabajarás en staging primero y luego pasas a producción?
¿Cómo evitarás estados inconsistentes del total cuando el cliente cambia Recojo/Envío/Express (debounce, una sola llamada AJAX, refresh order review controlado)?
Actualmente usamos culqi ¿Ya has probado checkout dinámico con esa pasarela?”
Comparación rápida con la propuesta anterior que me mostraste (la del “cambio de decisión”)
La anterior estaba muy enfocada en comportamiento real del usuario y edge cases (eso es oro).
Esta es más “técnica directa” y está bien, pero le falta mencionar cómo manejará los cambios y consistencia (A/C que ya vimos).

NOSOTROS:
Hola

Gracias por la confianza. Me gusta que apuntes a algo prolijo y estable, es exactamente como trabajo. Te cuento cómo lo encaro y qué cosas tener en cuenta:
1. Actualizaciones y estabilidad
Para evitar problemas a futuro, no voy a tocar archivos base ni de WooCommerce ni del tema.
Toda la lógica (fechas, reglas de envío, etc.) va a ir en un plugin propio, hecho a medida.
Así, podés actualizar WooCommerce o cambiar el tema más adelante sin que esto se rompa.
2. Entorno de pruebas (staging)
Vamos a trabajar sí o sí sobre un entorno de pruebas.
Primero se clona la web y ahí hago todo el desarrollo. Probamos bien el flujo completo (recojo, envío y pagos) y recién cuando esté todo OK, se pasa a la web real.
La idea es no afectar nunca las ventas.
3. Control de montos (recojo vs envío)
Esto lo manejo con dos controles:
A nivel visual, cuando el cliente cambia una opción, el botón de pago se bloquea un momento hasta que el total se actualiza bien.
Antes de cobrar, el sistema vuelve a validar todo. Si es recojo, el envío tiene que ser 0. Si algo no coincide, se corrige antes de procesar el pago.
4. Pagos con Culqi
He trabajado bastante con Culqi. Me voy a asegurar de que siempre reciba el monto final correcto, incluso cuando hay cambios de envío o descuentos, reiniciando la pasarela cuando haga falta.
Posibles riesgos
Como pasa en muchos sitios con WooCommerce, pueden surgir algunos puntos a revisar:
Conflictos con plugins que ya estén tocando el carrito, el checkout o los precios.
Temas muy personalizados que modifiquen el comportamiento normal de WooCommerce.
Plugins de caché u optimización que interfieran con la actualización de totales.
Por eso el staging es clave: todo esto se detecta y se corrige antes de salir a producción.
Aprovecho para preguntarte:
¿Usan hoy algún plugin que modifique el checkout, envíos o precios?
¿El tema tiene personalizaciones importantes?
Tiempos y valor
El trabajo llevaría entre 4 y 5 días hábiles, incluyendo pruebas y ajustes.
El valor total del desarrollo es de USD 300.
Cuando quieras, arrancamos armando el entorno de pruebas.
Quedo atento.
Saludos

CLIENTE:
Actualmente no usamos un plugin dedicado que reemplace o modifique completamente el checkout de WooCommerce (por ejemplo, one-page checkout externo o checkout en pasos cerrado).
El checkout es el clásico de WooCommerce, funcionando sobre el theme Porto.

Plugins actuales
- WooCommerce (checkout estándar).
- Theme Porto (con personalizaciones visuales).
- Plugins del ecosistema Crocoblock / Jet (JetEngine, JetFormBuilder),
pero no están interviniendo directamente el checkout de WooCommerce.

Envíos y precios
- Los métodos de envío y costos están configurados desde WooCommerce → Envíos.
- No usamos plugins avanzados de shipping (table rates, delivery slots, checkout delivery date, etc.).
- No hay plugins de dynamic pricing ni reglas de precios complejas fuera de WooCommerce.

Justamente por eso buscamos una implementación limpia mediante plugin propio + hooks de WooCommerce, que permita:
- Bloques progresivos (no wizard cerrado)
- Lógica condicional de envíos
- Actualización dinámica del total vía AJAX
- Evitar conflictos con plugins existentes y futuras actualizaciones

UX esperada (bloques progresivos)

A nivel de experiencia, no buscamos un wizard rígido, sino un checkout por bloques progresivos, tal como está definido en los mockups:
- El checkout se divide visualmente en: Contacto → Dirección → Envío → Resumen.
- El cliente completa Contacto y Dirección y, una vez validados:
    *esos bloques colapsan
    *se muestran solo como resumen, sin campos editables visibles.
- El usuario puede volver a editar cualquier bloque si lo necesita.
- El flujo es progresivo y guiado, pero no bloquea la navegación ni fuerza pasos artificiales.

NOSOTROS:
Tracy, como estás? Buenas tardes, estuvimos revisando tus consultas. Con esto ya terminamos de entender, en primera instancia, tu requerimiento a desarrollar.

Hace 2 días 
A continuación le comentamos las tareas que planificamos realizar, para que las repase, y en caso de tener alguna duda, poder ayudarle a solventarlas.

---

1) Compatibilidad con updates (sin tocar core)

* No se toca el core de WooCommerce ni del theme Porto.
* La implementación va como plugin propio usando hooks/filtros nativos.
* Si llegara a ser estrictamente necesario un override (por ejemplo, por alguna limitación de markup del theme), sería mínimo y documentado en un child theme. La idea es evitar overrides y trabajar con hooks + DOM reordering.

---

2) Checkout por bloques progresivos

La UX que describe (bloques que colapsan y quedan como resumen, pero editables) la implementaremos como “bloques progresivos”:

* Secciones: Contacto / Dirección / Envío / Resumen
* Al completar y validar un bloque:

  * colapsa y queda en modo “resumen”
  * el siguiente bloque se expande
* Siempre se puede volver a editar cualquier bloque (sin romper el estado del checkout).
* Esto se hace reordenando los campos nativos del checkout, no reemplazando WooCommerce.

---

3) Lógica condicional de Envío

Acá la clave es que no sea solo visual: tiene que quedar consistente en WooCommerce (sesión + método de envío real).

* Recojo en tienda

  * UI: selector de sede + horarios visibles.
  * Backend: se fuerza método equivalente a “pickup” y costo 0.
  * Se guardan sede/horario como meta del pedido (para fulfillment).
* Envío a domicilio

  * UI: Express vs 2–4 días + selector de fecha (y franja si lo piden).
  * Backend: se setea el método de envío real de WooCommerce.
  * La fecha elegida también queda como meta del pedido.
  * Reglas: días hábiles, cut-off horario, feriados (información de negocio necesaria).

---

4) Consistencia del total en cambios rápidos (punto relevante)

Este punto es necesario para evitar el escenario “cambia el envío pero el total del pedido quedó desactualizado”. Para ello encaramos un control de estado + un update_checkout bien gobernado en frontend y backend.

Esto cubre edge cases típicos:

* el usuario cambia Dirección y, antes de que Woo recalcule, quiere pagar
* alterna Recojo ⇄ Delivery rápido
* vuelve a editar un bloque anterior y el shipping debe recalcularse sí o sí

---

5) Culqi (checkout dinámico + monto correcto)

Revisamos el método de pago Culqi. Culqi debe cobrar el total final que WooCommerce confirma.

* Lo probamos directamente con su plugin actual en staging.
* Si el flujo de Culqi “cachea” el monto en frontend, se reinicializa / actualiza cuando Woo termina.
* Y a nivel servidor, el monto que se envía a Culqi siempre debe salir del Order Total final (post-recalc) para que no haya desfases por cambios de envío.

---

6) Trabajo en ambiente Staging en primera instancia

* Clonamos el sitio a staging (misma config de plugins/theme).
* Desarrollo + pruebas completas del flujo: Contacto → Dirección → Envío → Pago (Culqi).
* Revisión por etapa con usted como cliente (casos de uso y revisión de lo desarrollado).
* Deploy a producción con backup y checklist de smoke test.

Hace 2 días 
Para avanzar, si está de acuerdo con los descripto, vamos a necesitar en primera instancia:

1. Mockups (aunque sea PDF/capturas).

2. Información referida al negocio:
- Ejemplo: Lista de sedes de recojo + horarios (y si hay reglas tipo “solo ciertos días”).
- Este punto lo iremos refinando estudiando la lógica implementada actualmente, pero tener en cuenta que es posible solicitar información de negocio.

3. Credenciales:
-Acceso al hosting para poder realizar ambientes de prueba.
-Credenciales de BD
-Posibles credenciales varias (como ser Tokens de acceso)

4. Información complementaria varia.

Podemos avanzar en generar una propuesta en Workana con estimación y precio incluido. No obstante si posee alguna consulta más, estamos a disposición para ayudarlo.

Muchas gracias.

ATT. Smiley Code - Agencia FreeLancer experta en Programación y Tecnología

CLIENTE:
Hola, gracias por el detalle.
Para que puedan analizar correctamente el alcance y definir tiempos y presupuesto, les estaré compartiendo los mockups completos en PDF con todo el flujo del checkout, reglas de envío y escenarios considerados.
La idea es que, a partir de esos mockups, puedan:
Revisar el alcance completo
Definir el plan de trabajo en días / etapas
Enviarnos la propuesta formal en Workana con el presupuesto
Una vez tengamos la propuesta en Workana y esté todo alineado, recién coordinamos el envío de credenciales, accesos y ambiente de staging, para mantener el proceso ordenado y seguro para ambas partes.
En breve les comparto los mockups en PDF.
Quedo atenta a cualquier duda durante la revisión.
Gracias y seguimos en contacto.
Saludos,
Tracy

INSTRUCCION PARA LA IA: LEER EL MOCKUP

NOSOTROS:
En el mockup se ve como punto clave la geolocalización para el recojo en tienda (mostrar la opción solo cuando la dirección esté dentro de la zona correspondiente), y esa lógica ya está contemplada dentro de esta propuesta técnica.
Desarrollo limpio y mantenible
Desarrollo de un plugin a medida donde quedará centralizada toda la lógica del checkout (envíos, validaciones, selectores).
No se modifica el core de WooCommerce ni archivos base del tema Porto.
Uso exclusivo de hooks y filtros nativos para reorganizar campos y construir el flujo por bloques progresivos (Contacto → Dirección → Envío → Resumen).
Lógica personalizada y proximidad (punto crítico)
Recojo en tienda condicional: la opción de recojo (y sus sedes) se mostrará únicamente cuando la dirección ingresada pertenezca a la zona de cobertura de esa tienda, tal como indica el mockup.
Envío a domicilio: validación de zonas y selector de fechas con reglas de días hábiles.
Actualización vía AJAX: el total del carrito se recalcula correctamente al cambiar dirección, zona o método de envío.
Experiencia de usuario fiel al diseño
Checkout dividido en bloques con cabeceras grises y botones “Editar” funcionales para volver a pasos anteriores sin recargar la página.
Visualización clara de sedes con sus horarios (por ejemplo, Lun–Vie 9:30–18:30), respetando lo definido en el mockup.
Integración de pagos
Flujo validado con Culqi, asegurando que el monto procesado coincida siempre con el total final calculado según las reglas de envío.
Plan de Trabajo (4 semanas estimado)
Divido el proyecto en etapas semanales para que puedan revisar avances de forma clara:
Semana 1: Staging y lógica de proximidad
Clonación del sitio a entorno de staging.
Creación del plugin base.
Desarrollo del motor de reglas: script que analiza dirección/distrito y determina si corresponde habilitar el recojo en tienda.
Carga de sedes y horarios desde el backend.
Semana 2: UX y bloques progresivos
Reestructuración visual del checkout para alinearlo con el mockup.
Manejo de estados: bloque activo (editable) vs bloque resumido (con botón “Editar”).
Desarrollo del comportamiento JavaScript para expandir y colapsar secciones.
Semana 3: Integración completa y reglas de negocio
Integración del calendario de fechas para envíos a domicilio.
Pruebas intensivas de AJAX (cambios rápidos de dirección, zona y método de envío).
Validación del flujo completo con Culqi en entorno de pruebas.
Semana 4: Testing y salida a producción
Smoke test completo en desktop y mobile.
Revisión final en staging junto con ustedes.
Deploy a producción en horario seguro.
Presupuesto y tiempos
Inversión total: USD 450
Duración estimada: 4 semanas
El valor incluye desarrollo, pruebas en staging, despliegue a producción y un mes de garantía sobre el código entregado.
Siguientes pasos
Para comenzar, una vez aprobada la propuesta en Workana, necesitaría:
Accesos al hosting (cPanel/FTP) y WP-Admin.
Tabla de reglas de zonas: distritos asociados a cada tienda.
Horarios exactos de cada sede.
Quedo atento para avanzar cuando lo indiques.
Saludos,
Smiley Code – Agencia experta en programación y tecnología