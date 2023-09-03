// Ruta del archivo JSON relativa al directorio de tu proyecto
const jsonFilePath = "datos.json";

// Función para cargar y mostrar los datos desde el JSON
function cargarDatos() {
    fetch(jsonFilePath)
        .then(response => {
            if (!response.ok) {
                throw new Error("No se pudo cargar el archivo JSON");
            }
            return response.json();
        })
        .then(data => {
            // Supongamos que el JSON tiene tres propiedades: dato1, dato2 y dato3
            const dataContainer = document.getElementById("data");
            dataContainer.innerHTML = `
                <p>Dato 1: ${data.dato1}</p>
                <p>Dato 2: ${data.dato2}</p>
                <p>Dato 3: ${data.dato3}</p>
            `;
        })
        .catch(error => {
            console.error("Error al cargar el JSON:", error);
        });
}

// Llamar a la función para cargar los datos cuando se carga la página
cargarDatos();
