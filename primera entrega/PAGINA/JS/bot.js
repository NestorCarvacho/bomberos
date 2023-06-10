document.addEventListener("DOMContentLoaded", function() {
    // Definir respuestas del bot con opciones de botones
    const botResponses = {
        "inicio": {
            message: "¡Hola! Bienvenido a nuestra página de bomberos. ¿Qué deseas ver?",
            options: ["Sobre Nosotros", "Nuestros Funcionarios", "Nuestra Historia", "Contáctanos", "Realiza tu Aporte"]
        },
        "Sobre Nosotros": "Aquí encontrarás información sobre nuestra institución y su misión.",
        "Nuestros Funcionarios": "Conoce a nuestros valientes bomberos y su labor en la comunidad.",
        "Nuestra Historia": "Descubre la historia y los logros de nuestro cuartel de bomberos.",
        "Contáctanos": "Si necesitas comunicarte con nosotros, aquí encontrarás nuestros datos de contacto.",
        "Realiza tu Aporte": "¡Tu opinión es importante! Envíanos tu aporte o comentario.",
    };

    // Obtener elementos del DOM
    var chatInput = document.getElementById("chat-input");
    var optionsContainer = document.getElementById("options-container");
    var chatLog = document.getElementById("chat-log");

    // Mostrar mensaje de bienvenida y opciones
    displayMessage(botResponses["inicio"].message, "bot");
    displayOptions(botResponses["inicio"].options);

    // Manejar el evento de clic en los botones de opción
    optionsContainer.addEventListener("click", function(event) {
        var userInput = event.target.textContent;
        var response = getBotResponse(userInput);
        displayMessage(userInput, "user");
        displayMessage(response, "bot");
    });

    // Obtener respuesta del bot
    function getBotResponse(userInput) {
        return botResponses[userInput] || "Lo siento, no entiendo tu selección.";
    }

    // Mostrar mensaje en el chat
    function displayMessage(message, sender) {
        var messageContainer = document.createElement("div");
        messageContainer.className = "message " + sender;
        messageContainer.innerHTML = message;
        chatLog.appendChild(messageContainer);
        chatLog.scrollTop = chatLog.scrollHeight;
    }

    // Mostrar opciones en el chat
    function displayOptions(options) {
        optionsContainer.innerHTML = "";
        options.forEach(function(option) {
            var optionButton = document.createElement("button");
            optionButton.className = "option-btn";
            optionButton.textContent = option;
            optionsContainer.appendChild(optionButton);
        });
    }
});
document.getElementById('chat-icon').addEventListener('click', function() {
    var chatContainer = document.getElementById('chat-container');
    chatContainer.style.display = chatContainer.style.display === 'none' ? 'block' : 'none';
  });
  