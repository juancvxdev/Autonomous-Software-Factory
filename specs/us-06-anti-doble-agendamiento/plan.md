# Implementation Plan: US-06 Anti doble-agendamiento

## Contexto

La funcionalidad seleccionada viene del Agile Delivery Team para el MVP de citas dentales. Se eligio US-06 porque protege uno de los dolores mas importantes de recepcion: evitar que dos pacientes queden en el mismo turno del mismo doctor.

## Stack

- Java 21
- Spring Boot 3.3
- Gradle
- JUnit 5
- JaCoCo

## Diseno tecnico

El turno se identifica por `doctorId` y `fechaHora`. Para evitar doble reserva se usa una operacion atomica con `ConcurrentHashMap.putIfAbsent`. Esto permite que dos solicitudes concurrentes compitan por el mismo turno y que solo una insercion gane.

## Componentes

- `CitaDental`: entidad inmutable de cita.
- `TurnoDental`: clave logica unica por doctor y horario.
- `TurnoOcupadoException`: error de negocio para conflicto de agenda.
- `AgendaDentalService`: servicio de reserva y consulta.
- `AgendaDentalController`: API REST para crear y listar citas.

## Validacion

La validacion se realiza con pruebas unitarias y de controlador:

- reserva de turno libre.
- rechazo secuencial.
- rechazo concurrente.
- turnos distintos para el mismo doctor.
- misma hora para doctores diferentes.
- creacion/listado por API.
- conflicto REST cuando el turno esta ocupado.

## Riesgos

- La concurrencia no puede probarse solo por cobertura; debe tener una prueba explicita.
- El criterio de aceptación de Spec-Kit debe quedar trazado a pruebas, no solo al codigo.
