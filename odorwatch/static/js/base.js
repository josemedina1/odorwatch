window.addEventListener('beforeunload', function (event) {
    // Reemplaza la URL actual sin reenvío de datos
    window.location.replace(window.location.href);
});


document.getElementById("runScriptBtn").onclick = function () {
    console.log("iniciandoo")
};


  // Función para mostrar/ocultar sublistas específicas
  function toggleSublista(id) {
    const sublista = document.getElementById(id);
    if (sublista.style.display === "none" || sublista.style.display === "") {
      sublista.style.display = "block"; // Muestra la sublista
    } else {
      sublista.style.display = "none"; // Oculta la sublista
    }
  }