# Tasks: US-06 Anti doble-agendamiento

## Spec-Kit

- [x] Definir `spec.md` con FR, acceptance scenarios y edge cases.
- [x] Definir `plan.md` con stack, diseno y validacion.
- [x] Definir `tasks.md` con trabajo verificable.

## Implementacion

- [x] Crear modelo `CitaDental`.
- [x] Crear clave `TurnoDental`.
- [x] Crear excepcion `TurnoOcupadoException`.
- [x] Implementar `AgendaDentalService` con reserva atomica.
- [x] Implementar `AgendaDentalController` con endpoints REST.

## Pruebas

- [x] Probar reserva de turno libre.
- [x] Probar rechazo secuencial de turno ocupado.
- [x] Probar rechazo concurrente.
- [x] Probar turno distinto del mismo doctor.
- [x] Probar misma hora con doctores diferentes.
- [x] Probar creacion y listado por API.
- [x] Probar respuesta de conflicto.

## Calidad

- [x] Ejecutar pruebas con Gradle y JaCoCo.
- [x] Ejecutar escaneo de seguridad con Semgrep.
- [x] Consolidar `quality-output/verification.json`.
- [x] Ejecutar gate de Definition of Done.
- [x] Generar `quality-output/report.html`.
