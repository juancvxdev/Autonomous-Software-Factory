package ec.dentista.agenda;

import org.junit.jupiter.api.Test;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

import static org.junit.jupiter.api.Assertions.*;

class AgendaDentalServiceTest {

    private static final LocalDateTime TURNO = LocalDateTime.of(2026, 7, 6, 9, 0);

    private final AgendaDentalService agenda = new AgendaDentalService();

    @Test
    void reservaTurnoLibre_ok() {
        CitaDental cita = agenda.reservar("doc-1", TURNO, "pac-1", "Ana Perez", "Limpieza");

        assertEquals("doc-1", cita.doctorId());
        assertEquals(TURNO, cita.fechaHora());
        assertEquals("pac-1", cita.pacienteId());
        assertFalse(agenda.estaDisponible("doc-1", TURNO));
        assertEquals(1, agenda.listar().size());
    }

    @Test
    void reservaTurnoOcupado_secuencial_rechaza() {
        agenda.reservar("doc-1", TURNO, "pac-1", "Ana Perez", "Limpieza");

        assertThrows(TurnoOcupadoException.class,
                () -> agenda.reservar("doc-1", TURNO, "pac-2", "Luis Mora", "Control"));
        assertEquals(1, agenda.listar().size());
    }

    @Test
    void reservaTurnoOcupado_concurrente_soloUnaProspera() throws Exception {
        AgendaDentalService agendaConcurrente = new AgendaDentalService();
        ExecutorService pool = Executors.newFixedThreadPool(2);
        CyclicBarrier inicio = new CyclicBarrier(2);
        CountDownLatch fin = new CountDownLatch(2);
        List<Future<Boolean>> resultados = new ArrayList<>();

        for (String paciente : List.of("pac-a", "pac-b")) {
            resultados.add(pool.submit(() -> {
                try {
                    inicio.await();
                    agendaConcurrente.reservar("doc-2", TURNO.plusHours(1), paciente, paciente, "Ortodoncia");
                    return true;
                } catch (TurnoOcupadoException ex) {
                    return false;
                } finally {
                    fin.countDown();
                }
            }));
        }

        fin.await();
        pool.shutdownNow();

        long exitos = 0;
        long rechazadas = 0;
        for (Future<Boolean> resultado : resultados) {
            if (resultado.get()) {
                exitos++;
            } else {
                rechazadas++;
            }
        }

        assertEquals(1, exitos);
        assertEquals(1, rechazadas);
        assertEquals(1, agendaConcurrente.listar().size());
        assertFalse(agendaConcurrente.estaDisponible("doc-2", TURNO.plusHours(1)));
    }

    @Test
    void reservaTurnoDistintoMismoDoctor_ok() {
        agenda.reservar("doc-1", TURNO, "pac-1", "Ana Perez", "Limpieza");
        agenda.reservar("doc-1", TURNO.plusHours(1), "pac-2", "Luis Mora", "Control");

        assertEquals(2, agenda.listar().size());
        assertFalse(agenda.estaDisponible("doc-1", TURNO));
        assertFalse(agenda.estaDisponible("doc-1", TURNO.plusHours(1)));
    }

    @Test
    void reservaMismaHoraDiferenteDoctor_ok() {
        agenda.reservar("doc-1", TURNO, "pac-1", "Ana Perez", "Limpieza");
        agenda.reservar("doc-2", TURNO, "pac-2", "Luis Mora", "Control");

        assertEquals(2, agenda.listar().size());
    }

    @Test
    void api_creaYListaCitas() {
        AgendaDentalController controller = new AgendaDentalController(new AgendaDentalService());
        AgendaDentalController.CrearCitaRequest request =
                new AgendaDentalController.CrearCitaRequest("doc-api", TURNO.plusDays(1), "pac-api", "Marta Ruiz", "Consulta");

        ResponseEntity<CitaDental> response = controller.crear(request);

        assertEquals(HttpStatus.CREATED, response.getStatusCode());
        assertNotNull(response.getBody());
        assertEquals("doc-api", response.getBody().doctorId());
        assertEquals(1, controller.listar().size());
    }

    @Test
    void api_turnoOcupado_devuelveConflict() {
        AgendaDentalController controller = new AgendaDentalController(new AgendaDentalService());
        AgendaDentalController.CrearCitaRequest request =
                new AgendaDentalController.CrearCitaRequest("doc-api", TURNO.plusDays(2), "pac-api", "Marta Ruiz", "Consulta");

        controller.crear(request);
        TurnoOcupadoException ex = assertThrows(TurnoOcupadoException.class,
                () -> controller.crear(new AgendaDentalController.CrearCitaRequest(
                        "doc-api", TURNO.plusDays(2), "pac-otro", "Pedro Diaz", "Control")));

        ResponseEntity<String> response = controller.manejarTurnoOcupado(ex);
        assertEquals(HttpStatus.CONFLICT, response.getStatusCode());
        assertTrue(response.getBody().contains("doc-api"));
    }
}
