package ec.dentista.agenda;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDateTime;
import java.util.List;

@RestController
@RequestMapping("/api/citas")
public class AgendaDentalController {

    private final AgendaDentalService agenda;

    public AgendaDentalController(AgendaDentalService agenda) {
        this.agenda = agenda;
    }

    @PostMapping
    public ResponseEntity<CitaDental> crear(@RequestBody CrearCitaRequest request) {
        CitaDental cita = agenda.reservar(
                request.doctorId(),
                request.fechaHora(),
                request.pacienteId(),
                request.pacienteNombre(),
                request.motivo()
        );
        return ResponseEntity.status(HttpStatus.CREATED).body(cita);
    }

    @GetMapping
    public List<CitaDental> listar() {
        return agenda.listar();
    }

    @ExceptionHandler(TurnoOcupadoException.class)
    public ResponseEntity<String> manejarTurnoOcupado(TurnoOcupadoException ex) {
        return ResponseEntity.status(HttpStatus.CONFLICT).body(ex.getMessage());
    }

    public record CrearCitaRequest(
            String doctorId,
            LocalDateTime fechaHora,
            String pacienteId,
            String pacienteNombre,
            String motivo
    ) {
    }
}
