const terminal = document.getElementById("draggable");

function initializeTerminal(terminal) {
  const close = document.getElementById("close");
  const min = document.getElementById("min");
  const max = document.getElementById("max");
  const restore = document.getElementById("restore");
  const about = document.getElementById("about");

  about.addEventListener("click", function () {
    if (terminal.style.display === "none" || terminal.style.display === "") {
      terminal.style.display = "block";
    } else {
      terminal.style.display = "none";
    }
  });

  close.addEventListener("click", function () {
    if (terminal.style.display === "none" || terminal.style.display === "") {
      terminal.style.display = "block";
    } else {
      terminal.style.display = "none";
    }
  });
  max.addEventListener("click", function () {
    if (!terminal.classList.contains("maximize")){
      terminal.classList.add("maximize");
      terminal.classList.remove("minimize")
      terminal.onmousedown = null;
    }
  });
  restore.addEventListener("click", function () {
    if (!terminal.classList.contains("restore")){
      terminal.classList.remove("maximize")
      terminal.classList.remove("minimize")
      draggable()
    }
  });
  min.addEventListener("click", function () {
    if (!terminal.classList.contains("minimize")){
      terminal.classList.add("minimize");
      terminal.classList.remove("maximize")
      terminal.onmousedown = null;
    }
  });
}

function draggable() {
  terminal.onmousedown = function (event) {
    let shiftX = event.clientX - terminal.getBoundingClientRect().left;
    let shiftY = event.clientY - terminal.getBoundingClientRect().top;
    
    terminal.style.position = 'absolute';
    terminal.style.zIndex = 1000;
    document.body.append(terminal);

    moveAt(event.pageX, event.pageY);

    // mueve el elemento a las coordenadas (pageX, pageY)
    // tomando en cuenta la posición inicial
    
    function moveAt(pageX, pageY) {
      terminal.style.left = pageX - shiftX + 'px';
      terminal.style.top = pageY - shiftY + 'px';
    }
    

    function onMouseMove(event) {
      moveAt(event.pageX, event.pageY);
    }
    
    // mueve el elemento con mousemove
    document.addEventListener('mousemove', onMouseMove);

    // suelta el elemento, elimina el manejador innecesario
    terminal.onmouseup = function () {
      document.removeEventListener('mousemove', onMouseMove);
      terminal.onmouseup = null;
    };
  };

  terminal.ondragstart = function () {
    return false;
  };
  const closeButton = document.getElementById("close");
  const maximize = document.getElementById("max");
  const restore = document.getElementById("restore");
  const minimize = document.getElementById("min");
  closeButton.addEventListener("mousedown", function (event) {
    event.stopPropagation();
  });
  maximize.addEventListener("mousedown", function (event) {
    event.stopPropagation();
  });
  restore.addEventListener("mousedown", function (event) {
    event.stopPropagation();
  });
  minimize.addEventListener("mousedown", function (event) {
    event.stopPropagation();
  });
  
}

// Llama primero initializeTerminal y luego draggable
initializeTerminal(terminal);
draggable();
