package ec.dentista.agenda;

import java.time.LocalDateTime;

public record CitaDental(
        String doctorId,
        LocalDateTime fechaHora,
        String pacienteId,
        String pacienteNombre,
        String motivo
) {
}
