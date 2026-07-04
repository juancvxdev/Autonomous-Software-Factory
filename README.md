# Proyecto Final - Autonomous Software Factory

Autor: Juan José Córdova  
Asignatura: Ingeniería de Software - Maestría en Software  
Producto: sistema de reserva de citas dentales

Este repositorio integra el flujo completo del proyecto final:

Discovery Agent -> Agile Delivery Team -> Desarrollo con SDD -> Quality Agent

## Repositorios usados

- Discovery Agent: https://github.com/juancvxdev/discovery-agent
- Agile Delivery Team: https://github.com/juancvxdev/agile-delivery-team
- Quality Agent: https://github.com/juancvxdev/quality-agent
- Proyecto final: https://github.com/juancvxdev/Autonomous-Software-Factory

## Funcionalidad implementada

Se seleccionó la historia US-06 Anti doble-agendamiento del contexto `citasdentista`.

La funcionalidad evita que dos pacientes reserven el mismo turno del mismo doctor. El servicio usa una reserva atómica para que, incluso si dos solicitudes llegan casi al mismo tiempo, solo una cita quede registrada.

## Artefactos SDD

Los artefactos de Spec-Kit están en:

- `specs/us-06-anti-doble-agendamiento/spec.md`
- `specs/us-06-anti-doble-agendamiento/plan.md`
- `specs/us-06-anti-doble-agendamiento/tasks.md`

## Evidencia de calidad

- `quality-output/verification.json`
- `quality-output/report.html`
- `quality-output/semgrep.json`
- `quality-output/gate-output.txt`
- `quality-output/screenshots/gate-bloqueado.png`
- `quality-output/screenshots/gate-aprobado.png`
- `quality-output/before-fix/verification.json`
- `quality-output/before-fix/gate-output.txt`

Resultado final:

- Pruebas: 7/7
- Cobertura: 90.9%
- Seguridad: 0 críticas, 0 secretos
- Criterios: 8 criterios cumplen
- Gate: aprobado

## Informe final

El informe Word editable está en:

- `docs/Informe_Final_Autonomous_Software_Factory_Juan_Jose_Cordova.docx`

Incluye introducción, análisis de Discovery Agent, Agile Delivery Team, SDD, Quality Agent, capturas de consola del gate, conclusiones, recomendaciones y anexos con enlaces a repositorios.

## Evidencias por etapa

Los logs y evidencias usados para el informe están en:

- `evidence/discovery/`
- `evidence/agile/`
- `evidence/sdd/`
- `evidence/quality/`
