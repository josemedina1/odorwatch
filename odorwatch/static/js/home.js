  // Función para mostrar/ocultar la sublista
function toggleSublista() {
    const sublista = document.getElementById("sublista");
    if (sublista.style.display === "none" || sublista.style.display === "") {
      sublista.style.display = "block"; // Muestra la sublista
    } else {
      sublista.style.display = "none"; // Oculta la sublista
    }
}