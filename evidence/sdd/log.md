# Log / evidencia - Desarrollo con SDD

Artefactos Spec-Kit versionados:

- `specs/us-06-anti-doble-agendamiento/spec.md`
- `specs/us-06-anti-doble-agendamiento/plan.md`
- `specs/us-06-anti-doble-agendamiento/tasks.md`

Funcionalidad implementada:

- `AgendaDentalService` usa `ConcurrentHashMap.putIfAbsent` para que solo una reserva gane el turno.
- `AgendaDentalController` expone creacion y consulta de citas dentales.
- `AgendaDentalServiceTest` valida reserva libre, rechazo secuencial, rechazo concurrente, turnos distintos, doctores distintos y conflicto REST.

Resultado de pruebas:

- Pruebas ejecutadas: 7
- Fallos: 0
- Errores: 0
- Cobertura JaCoCo: 90.9%
