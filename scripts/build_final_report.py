from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "Informe_Final_Autonomous_Software_Factory_Juan_Jose_Cordova.docx"
GATE_BLOCKED_IMG = ROOT / "quality-output" / "screenshots" / "gate-bloqueado.png"
GATE_APPROVED_IMG = ROOT / "quality-output" / "screenshots" / "gate-aprobado.png"


def set_cell_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def set_cell_text(cell, text, bold=False):
    cell.text = ""
    p = cell.paragraphs[0]
    r = p.add_run(text)
    r.bold = bold
    r.font.name = "Calibri"
    r.font.size = Pt(10)


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        set_cell_text(table.rows[0].cells[i], h, True)
        set_cell_shading(table.rows[0].cells[i], "E8EEF5")
    for row in rows:
        cells = table.add_row().cells
        for i, value in enumerate(row):
            set_cell_text(cells[i], str(value))
            cells[i].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    doc.add_paragraph()
    return table


def add_code_box(doc, title, text):
    p = doc.add_paragraph()
    p.style = "Heading 3"
    p.add_run(title)
    table = doc.add_table(rows=1, cols=1)
    table.style = "Table Grid"
    cell = table.rows[0].cells[0]
    set_cell_shading(cell, "F2F4F7")
    cell.text = ""
    p = cell.paragraphs[0]
    r = p.add_run(text.strip())
    r.font.name = "Consolas"
    r.font.size = Pt(9)
    doc.add_paragraph()


def add_bullets(doc, items):
    for item in items:
        doc.add_paragraph(item, style="List Bullet")


def configure_styles(doc):
    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(11)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.10

    for name, size, color in [
        ("Heading 1", 16, "2E74B5"),
        ("Heading 2", 13, "2E74B5"),
        ("Heading 3", 12, "1F4D78"),
    ]:
        style = styles[name]
        style.font.name = "Calibri"
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor.from_string(color)
        style.paragraph_format.space_before = Pt(10)
        style.paragraph_format.space_after = Pt(6)


def main():
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    configure_styles(doc)

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("Proyecto Final: Autonomous Software Factory")
    run.bold = True
    run.font.size = Pt(18)
    run.font.color.rgb = RGBColor.from_string("1F4D78")

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle.add_run("Ingenier\u00eda de Software - Maestr\u00eda en Software").bold = True
    subtitle.add_run("\nJuan Jos\u00e9 C\u00f3rdova\nFecha de entrega: 5 de julio de 2026\nModalidad: individual")

    doc.add_paragraph()
    add_table(
        doc,
        ["Elemento", "Detalle"],
        [
            ["Producto trabajado", "Sistema de reserva de citas dentales"],
            ["Flujo integrado", "Discovery -> Delivery -> SDD -> Quality Gate"],
            ["Funcionalidad nueva", "US-06 Anti doble-agendamiento"],
            ["Stack", "Java 21, Spring Boot, Gradle, JaCoCo, Semgrep"],
            ["Resultado final", "Gate aprobado con 7/7 pruebas y cobertura 90.9%"],
        ],
    )

    doc.add_heading("Introducci\u00f3n", level=1)
    doc.add_paragraph(
        "Este informe integra los agentes trabajados durante la materia en un flujo completo de "
        "Autonomous Software Factory. El caso usado fue un sistema de reserva de citas dentales. "
        "La idea se descubri\u00f3 con el Discovery Agent, se organizo con el Agile Delivery Team, se "
        "implemento una funcionalidad mediante SDD y finalmente se valid\u00f3 con el Quality Agent."
    )

    doc.add_heading("An\u00e1lisis del Discovery Agent", level=1)
    doc.add_paragraph(
        "En la Unidad 1 utilic\u00e9 entrevistas de doctor, paciente y secretaria para descubrir el problema "
        "principal del producto. El hallazgo central fue que la agenda estaba dispersa entre WhatsApp, "
        "llamadas, papel y atenci\u00f3n presencial, sin una fuente \u00fanica de verdad."
    )
    add_bullets(
        doc,
        [
            "Personas identificadas: doctor, paciente y secretaria.",
            "Dolores principales: doble agendamiento, no-shows, falta de confirmaci\u00f3n y poca visibilidad de horarios.",
            "MVP definido: reserva aut\u00f3noma de citas dentales sobre horarios reales.",
            "M\u00e9trica principal: reducir la tasa de no-show y aumentar citas gestionadas dentro del sistema.",
        ],
    )

    doc.add_heading("An\u00e1lisis del Agile Delivery Team", level=1)
    doc.add_paragraph(
        "En la Unidad 2 use los resultados del Discovery Agent como insumo para organizar el MVP en epicas, "
        "historias INVEST y un plan de sprint. El trabajo separo el valor del producto en reserva aut\u00f3noma, "
        "confirmacion, fuente \u00fanica de recepcion y agenda del doctor."
    )
    add_table(
        doc,
        ["Epica", "Resultado"],
        [
            ["E-01", "Paciente reserva su cita viendo turnos reales"],
            ["E-02", "Paciente confirma, recuerda y libera su cita"],
            ["E-03", "Recepcion opera sobre una fuente \u00fanica, sin choques"],
            ["E-04", "Doctor consulta agenda en tiempo real con contexto"],
        ],
    )
    doc.add_paragraph(
        "Para el trabajo nuevo seleccione la historia US-06 Anti doble-agendamiento, porque representa un "
        "riesgo real de operaci\u00f3n y obliga a validar concurrencia, no solo el camino feliz."
    )

    doc.add_heading("An\u00e1lisis del desarrollo con SDD", level=1)
    doc.add_paragraph(
        "La funcionalidad US-06 se implement\u00f3 con Spec-Driven Development. Primero defin\u00ed los criterios en "
        "Spec-Kit y luego implement\u00e9 el servicio Spring Boot. Los artefactos quedaron versionados en "
        "`specs/us-06-anti-doble-agendamiento/`."
    )
    add_table(
        doc,
        ["Artefacto", "Prop\u00f3sito"],
        [
            ["spec.md", "Define FR-001 a FR-007, escenarios y edge cases"],
            ["plan.md", "Explica stack, dise\u00f1o t\u00e9cnico y validaci\u00f3n"],
            ["tasks.md", "Lista tareas de implementaci\u00f3n, pruebas y calidad"],
        ],
    )
    doc.add_paragraph(
        "El dise\u00f1o usa `ConcurrentHashMap.putIfAbsent` para que el turno dental se reserve de forma at\u00f3mica. "
        "As\u00ed, cuando dos pacientes intentan tomar el mismo horario, solo una reserva queda registrada."
    )

    doc.add_heading("An\u00e1lisis del Quality Agent", level=1)
    doc.add_paragraph(
        "La validaci\u00f3n se hizo con el Quality Agent de la Unidad 3, reutilizando su constituci\u00f3n, skill, "
        "subagentes, comandos, hook y conexi\u00f3n MCP. El agente valid\u00f3 los tres pilares del Definition of Done: "
        "pruebas, seguridad y criterios."
    )
    add_table(
        doc,
        ["Pilar", "Resultado final"],
        [
            ["Pruebas", "7/7 pruebas aprobadas, cobertura 90.9%"],
            ["Seguridad", "Semgrep sin hallazgos, 0 cr\u00edticas y 0 secretos"],
            ["Criterios", "FR-001 a FR-007 y edge case de concurrencia cubiertos"],
        ],
    )
    doc.add_paragraph("Como evidencia de validacion automatica se incluyeron las capturas de consola del gate bloqueado y del gate aprobado, generadas desde este proyecto final.")
    if GATE_BLOCKED_IMG.exists():
        p = doc.add_paragraph("Captura de consola - bloqueo del gate:")
        p.runs[0].bold = True
        doc.add_picture(str(GATE_BLOCKED_IMG), width=Inches(6.3))
    if GATE_APPROVED_IMG.exists():
        p = doc.add_paragraph("Captura de consola - resoluci\u00f3n aprobada:")
        p.runs[0].bold = True
        doc.add_picture(str(GATE_APPROVED_IMG), width=Inches(6.3))

    doc.add_heading("Conclusiones", level=1)
    add_bullets(
        doc,
        [
            "El flujo completo conecto descubrimiento, planificaci\u00f3n, desarrollo y validaci\u00f3n automatica.",
            "La historia US-06 demostr\u00f3 que la concurrencia debe probarse expl\u00edcitamente y no asumirse por cobertura.",
            "El Quality Gate cambio el cierre del trabajo: la funcionalidad solo se consider\u00f3 terminada cuando los tres pilares estuvieron en verde.",
        ],
    )

    doc.add_heading("Recomendaciones", level=1)
    add_bullets(
        doc,
        [
            "Mantener Spec-Kit como fuente de criterios antes de implementar nuevas historias.",
            "Ejecutar el Quality Agent antes de cada entrega para evitar omisiones de pruebas o seguridad.",
            "Agregar el gate a integraci\u00f3n continua cuando el producto avance a m\u00e1s funcionalidades.",
        ],
    )

    doc.add_heading("Anexos", level=1)
    add_table(
        doc,
        ["Repositorio", "Enlace"],
        [
            ["Discovery Agent", "https://github.com/juancvxdev/discovery-agent"],
            ["Agile Delivery Team", "https://github.com/juancvxdev/agile-delivery-team"],
            ["Quality Agent", "https://github.com/juancvxdev/quality-agent"],
            ["Proyecto final SDD + evidencia", "https://github.com/juancvxdev/Autonomous-Software-Factory"],
        ],
    )
    add_bullets(
        doc,
        [
            "Evidencia SDD: specs/us-06-anti-doble-agendamiento/spec.md, plan.md y tasks.md.",
            "Evidencia Quality Agent: quality-output/verification.json y quality-output/report.html.",
            "Evidencia del bloqueo: quality-output/before-fix/gate-output.txt.",
            "Evidencia de resoluci\u00f3n: quality-output/gate-output.txt.",
        ],
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
