package ec.dentista.agenda;

import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.Comparator;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;

@Service
public class AgendaDentalService {

    private final ConcurrentMap<TurnoDental, CitaDental> citas = new ConcurrentHashMap<>();

    public CitaDental reservar(
            String doctorId,
            LocalDateTime fechaHora,
            String pacienteId,
            String pacienteNombre,
            String motivo
    ) {
        TurnoDental turno = TurnoDental.de(doctorId, fechaHora);
        CitaDental nueva = new CitaDental(doctorId, fechaHora, pacienteId, pacienteNombre, motivo);
        CitaDental existente = citas.putIfAbsent(turno, nueva);
        if (existente != null) {
            throw new TurnoOcupadoException(doctorId, fechaHora);
        }
        return nueva;
    }

    public boolean estaDisponible(String doctorId, LocalDateTime fechaHora) {
        return !citas.containsKey(TurnoDental.de(doctorId, fechaHora));
    }

    public List<CitaDental> listar() {
        return citas.values().stream()
                .sorted(Comparator.comparing(CitaDental::doctorId).thenComparing(CitaDental::fechaHora))
                .toList();
    }
}
