# Feature Specification: Anti doble-agendamiento de citas dentales

**Feature Branch**: `us-06-anti-doble-agendamiento`  
**Created**: 2026-07-04  
**Status**: Implemented  
**Input**: Historia US-06 del Agile Delivery Team: "Como secretaria, quiero que el sistema impida agendar dos pacientes en el mismo turno de un doctor, para eliminar el doble agendamiento y los horarios mal anotados."

## User Scenarios & Testing

### User Story 1 - Bloquear turnos ocupados (Priority: P1)

Como secretaria de la consulta dental, quiero que un turno ocupado no pueda reservarse de nuevo, para evitar choques entre pacientes.

**Acceptance Scenarios**:

1. **Given** un turno libre de un doctor, **When** se registra una reserva, **Then** la cita queda creada y el turno deja de aparecer disponible.
2. **Given** un turno ya ocupado, **When** otro paciente intenta reservarlo, **Then** el sistema rechaza la operacion e indica que el turno no esta libre.

### User Story 2 - Controlar reservas simultaneas (Priority: P1)

Como sistema, debo resolver reservas simultaneas sobre el mismo turno, para que solo una cita quede registrada.

**Acceptance Scenarios**:

1. **Given** dos reservas casi simultaneas sobre el mismo doctor y horario, **When** se procesan, **Then** solo una queda confirmada y la otra se rechaza.
2. **Given** una reserva rechazada por concurrencia, **When** se consulta la disponibilidad, **Then** el turno ya no aparece como libre.

## Edge Cases

- Dos pacientes intentan reservar el mismo turno al mismo tiempo.
- Un paciente intenta reservar un turno que fue tomado segundos antes.
- Un doctor tiene dos turnos distintos el mismo dia; reservar uno no debe bloquear el otro.
- Dos doctores pueden tener citas en la misma hora sin conflicto entre ellos.

## Requirements

### Functional Requirements

- **FR-001**: El sistema MUST permitir reservar un turno libre para un doctor, fecha, hora y paciente.
- **FR-002**: El sistema MUST rechazar una segunda reserva secuencial sobre el mismo doctor, fecha y hora.
- **FR-003**: El sistema MUST garantizar que ante dos reservas concurrentes sobre el mismo turno solo una quede registrada.
- **FR-004**: El sistema MUST mantener disponible un turno distinto del mismo doctor aunque otro turno ya este ocupado.
- **FR-005**: El sistema MUST permitir que dos doctores diferentes tengan citas en la misma hora sin generar conflicto.
- **FR-006**: El sistema MUST exponer por API REST la creacion y consulta de citas dentales.
- **FR-007**: El sistema MUST responder con conflicto cuando un turno ya no esta libre.

### Key Entities

- **CitaDental**: doctor, fecha y hora, paciente, motivo.
- **TurnoDental**: combinacion unica de doctor, fecha y hora.

## Success Criteria

### Measurable Outcomes

- **SC-001**: Todas las pruebas automatizadas pasan.
- **SC-002**: La cobertura de lineas del modulo es igual o mayor a 80%.
- **SC-003**: Semgrep no reporta vulnerabilidades criticas ni secretos expuestos.
- **SC-004**: Cada FR y el edge case de concurrencia tienen una prueba asociada.
