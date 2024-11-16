// Martín Nahuel Muñoz Codazzi 09/05/2024

package punto8;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

class AerolineaTest {
	Tripulante tripulante1, tripulante2, tripulante3, tripulante4, tripulante5, tripulante6, 
    tripulante7, tripulante8, tripulante9, tripulante10, tripulante11, tripulante12, 
    tripulante13, tripulante14, tripulante15, tripulante16, tripulante17, tripulante18, 
    tripulante19, tripulante20, tripulante21, tripulante22, tripulante23, tripulante24, 
    tripulante25, tripulante26, tripulante27, tripulante28, tripulante29, tripulante30;

	Avion avion1, avion2, avion3, avion4, avion5, avion6, avion7, avion8, 
	avion9, avion10;
	
	Vuelo vuelo1, vuelo2, vuelo3, vuelo4, vuelo5, vuelo6, vuelo7, vuelo8, vuelo9, vuelo10, vuelo11, vuelo12, vuelo13,
			vuelo14, vuelo15, vuelo16, vuelo17, vuelo18, vuelo19, vuelo20;
	
	Aerolinea aerolinea;

	@BeforeEach
	void setUp() throws Exception {
		tripulante1 = new Tripulante("Juan", Cargos.PILOTO, 23);
		tripulante2 = new Tripulante("María", Cargos.COPILOTO, 12);
		tripulante3 = new Tripulante("Pedro", Cargos.AEROMOZO, 18);
		tripulante4 = new Tripulante("Luisa", Cargos.INSPECTOR, 7);
		tripulante5 = new Tripulante("Carlos", Cargos.PILOTO, 15);
		tripulante6 = new Tripulante("Ana", Cargos.COPILOTO, 4);
		tripulante7 = new Tripulante("Miguel", Cargos.AEROMOZO, 21);
		tripulante8 = new Tripulante("Sofía", Cargos.INSPECTOR, 10);
		tripulante9 = new Tripulante("Diego", Cargos.PILOTO, 3);
		tripulante10 = new Tripulante("Lucía", Cargos.COPILOTO, 19);
		tripulante11 = new Tripulante("Martín", Cargos.AEROMOZO, 1);
		tripulante12 = new Tripulante("Elena", Cargos.INSPECTOR, 14);
		tripulante13 = new Tripulante("Pablo", Cargos.PILOTO, 25);
		tripulante14 = new Tripulante("Valentina", Cargos.COPILOTO, 2);
		tripulante15 = new Tripulante("Javier", Cargos.AEROMOZO, 16);
		tripulante16 = new Tripulante("Laura", Cargos.INSPECTOR, 8);
		tripulante17 = new Tripulante("Alejandro", Cargos.PILOTO, 22);
		tripulante18 = new Tripulante("Carmen", Cargos.COPILOTO, 11);
		tripulante19 = new Tripulante("Felipe", Cargos.AEROMOZO, 6);
		tripulante20 = new Tripulante("Isabella", Cargos.INSPECTOR, 17);
		tripulante21 = new Tripulante("Gonzalo", Cargos.PILOTO, 9);
		tripulante22 = new Tripulante("Adriana", Cargos.COPILOTO, 20);
		tripulante23 = new Tripulante("Ricardo", Cargos.AEROMOZO, 5);
		tripulante24 = new Tripulante("Paula", Cargos.INSPECTOR, 24);
		tripulante25 = new Tripulante("Sebastián", Cargos.PILOTO, 13);
		tripulante26 = new Tripulante("Valeria", Cargos.COPILOTO, 26);
		tripulante27 = new Tripulante("Fernando", Cargos.AEROMOZO, 0);
		tripulante28 = new Tripulante("Natalia", Cargos.INSPECTOR, 1);
		tripulante29 = new Tripulante("Roberto", Cargos.PILOTO, 8);
		tripulante30 = new Tripulante("Carolina", Cargos.COPILOTO, 19);
        avion1 = new Avion(Aviones.B737, 5);
        avion2 = new Avion(Aviones.B727, 180);
        avion3 = new Avion(Aviones.A380, 500);
        avion4 = new Avion(Aviones.A320, 200);
        avion5 = new Avion(Aviones.B747, 400);
        avion6 = new Avion(Aviones.B787, 300);
        avion7 = new Avion(Aviones.A350, 350);
        avion8 = new Avion(Aviones.B737, 160);
        avion9 = new Avion(Aviones.B727, 170);
        avion10 = new Avion(Aviones.A380, 550);        
        vuelo1 = new Vuelo(avion1, new Tripulante[]{tripulante1, tripulante2, tripulante3});
        vuelo2 = new Vuelo(avion2, new Tripulante[]{tripulante5, tripulante6, tripulante7, tripulante4});
        vuelo3 = new Vuelo(avion3, new Tripulante[]{tripulante9, tripulante10, tripulante11, tripulante4});
        vuelo4 = new Vuelo(avion4, new Tripulante[]{tripulante13, tripulante14, tripulante15});
        vuelo5 = new Vuelo(avion5, new Tripulante[]{tripulante1, tripulante18, tripulante19, tripulante20});
        vuelo6 = new Vuelo(avion6, new Tripulante[]{tripulante17, tripulante26, tripulante23, tripulante28});
        vuelo7 = new Vuelo(avion7, new Tripulante[]{tripulante21, tripulante22, tripulante27, tripulante8});
        vuelo8 = new Vuelo(avion1, new Tripulante[]{tripulante25, tripulante24, tripulante7, tripulante12});
        vuelo9 = new Vuelo(avion2, new Tripulante[]{tripulante1, tripulante3, tripulante7, tripulante4});
        vuelo10 = new Vuelo(avion3, new Tripulante[]{tripulante9, tripulante2, tripulante6});
        vuelo11 = new Vuelo(avion4, new Tripulante[]{tripulante1, tripulante5, tripulante7});
        vuelo12 = new Vuelo(avion5, new Tripulante[]{tripulante11, tripulante12, tripulante13, tripulante4});
        vuelo13 = new Vuelo(avion6, new Tripulante[]{tripulante14, tripulante3, tripulante16});
        vuelo14 = new Vuelo(avion7, new Tripulante[]{tripulante21, tripulante15, tripulante8, tripulante19});
        vuelo15 = new Vuelo(avion8, new Tripulante[]{tripulante1, tripulante18, tripulante13});
        vuelo16 = new Vuelo(avion9, new Tripulante[]{tripulante25, tripulante26, tripulante27});
        vuelo17 = new Vuelo(avion10, new Tripulante[]{tripulante1, tripulante5, tripulante3});
        vuelo18 = new Vuelo(avion1, new Tripulante[]{tripulante1, tripulante20, tripulante3, tripulante8});
        vuelo19 = new Vuelo(avion2, new Tripulante[]{tripulante13, tripulante14, tripulante15, tripulante8});
        vuelo20 = new Vuelo(avion3, new Tripulante[]{tripulante7, tripulante2, tripulante18, tripulante4});
        
		aerolinea = new Aerolinea(
			new Vuelo[] { vuelo1, vuelo2, vuelo3, vuelo4, vuelo5, vuelo6, vuelo7, vuelo8, vuelo9, vuelo10, vuelo11,
			vuelo12, vuelo13, vuelo14, vuelo15, vuelo16, vuelo17, vuelo18, vuelo19, vuelo20, });
     
	}

	@Test
	void testGetVuelos() {
		assertEquals(20,aerolinea.getVuelos().length);
	}

	@Disabled
	@Test
	void testSetVuelos() {
		fail("Not yet implemented");
	}

	@Test
	void testAerolinea() {
		assertNotNull(aerolinea);
	}

	@Test
	void testVuelosEn() {
		assertEquals(3, aerolinea.vuelosEn(tripulante1, Aviones.B737));
		assertEquals(1, aerolinea.vuelosEn(tripulante1, Aviones.B747));
		assertEquals(1, aerolinea.vuelosEn(tripulante5, Aviones.A380));
		assertEquals(0, aerolinea.vuelosEn(tripulante15, Aviones.B787));
	}

	@Test
	void testAntiguedadPromedio() {
		assertEquals(10, aerolinea.antiguedadPromedio(Aviones.A350));
		assertEquals(17,aerolinea.antiguedadPromedio(Aviones.A320));
		assertEquals(11,aerolinea.antiguedadPromedio(Aviones.A380));
		assertEquals(13,aerolinea.antiguedadPromedio(Aviones.B727));
	}

	@Test
	void testVuelosSobrecargados() {
		assertEquals(3,aerolinea.vuelosSobrecargados().size());
	}

	@Test
	void testMasInspeccionado() {
		assertEquals(Aviones.B737,aerolinea.masInspeccionado());
	}

	@Test
	void testAvionesPilotadosPor() {		
		assertEquals(5, aerolinea.avionesPilotadosPor(tripulante1.getNombre()).size());
		assertEquals(0, aerolinea.avionesPilotadosPor(tripulante2.getNombre()).size());
	}

	@Test
	void testEmpleadoDelMes() {
		assertEquals(tripulante1,aerolinea.empleadoDelMes());
	}

}
