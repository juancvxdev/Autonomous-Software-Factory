package ec.dentista.agenda;

import java.time.LocalDateTime;

public class TurnoOcupadoException extends RuntimeException {

    public TurnoOcupadoException(String doctorId, LocalDateTime fechaHora) {
        super("El turno " + fechaHora + " del doctor " + doctorId + " ya no esta libre");
    }
}
