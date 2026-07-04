# Proyecto Final - Autonomous Software Factory

Autor: Juan Jose Cordova  
Asignatura: Ingenieria de Software - Maestria en Software  
Producto: sistema de reserva de citas dentales  

Este repositorio integra el flujo completo del proyecto final:

Discovery Agent -> Agile Delivery Team -> Desarrollo con SDD -> Quality Agent

## Repositorios usados

- Discovery Agent: https://github.com/juancvxdev/discovery-agent
- Agile Delivery Team: https://github.com/juancvxdev/agile-delivery-team
- Quality Agent: https://github.com/juancvxdev/quality-agent
- Proyecto final: https://github.com/juancvxdev/Autonomous-Software-Factory

## Funcionalidad implementada

Se selecciono la historia US-06 Anti doble-agendamiento del contexto `citasdentista`.

La funcionalidad evita que dos pacientes reserven el mismo turno del mismo doctor. El servicio usa una reserva atomica para que, incluso si dos solicitudes llegan casi al mismo tiempo, solo una cita quede registrada.

## Artefactos SDD

Los artefactos de Spec-Kit estan en:

- `specs/us-06-anti-doble-agendamiento/spec.md`
- `specs/us-06-anti-doble-agendamiento/plan.md`
- `specs/us-06-anti-doble-agendamiento/tasks.md`

## Evidencia de calidad

- `quality-output/verification.json`
- `quality-output/report.html`
- `quality-output/semgrep.json`
- `quality-output/gate-output.txt`
- `quality-output/before-fix/verification.json`
- `quality-output/before-fix/gate-output.txt`

Resultado final:

- Pruebas: 7/7
- Cobertura: 90.9%
- Seguridad: 0 criticas, 0 secretos
- Criterios: 8 criterios cumplen
- Gate: aprobado

## Informe final

El informe Word editable esta en:

- `docs/Informe_Final_Autonomous_Software_Factory_Juan_Jose_Cordova.docx`

Incluye introduccion, analisis de Discovery Agent, Agile Delivery Team, SDD, Quality Agent, conclusiones, recomendaciones y anexos con enlaces a repositorios.

## Evidencias y prompts

Los prompts y logs usados para el informe estan en:

- `evidence/discovery/`
- `evidence/agile/`
- `evidence/sdd/`
- `evidence/quality/`
