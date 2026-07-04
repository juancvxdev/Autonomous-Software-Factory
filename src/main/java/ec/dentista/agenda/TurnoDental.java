package ec.dentista.agenda;

import java.time.LocalDateTime;

public record TurnoDental(String doctorId, LocalDateTime fechaHora) {

    public static TurnoDental de(String doctorId, LocalDateTime fechaHora) {
        return new TurnoDental(doctorId, fechaHora);
    }
}
