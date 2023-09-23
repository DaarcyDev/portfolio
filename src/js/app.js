const globTerminal = document.getElementById("draggable");
const globTerminal2 = document.getElementById("draggable2");
const globTerminal3 = document.getElementById("draggable3");
var data = 0
var konsole1 = ""
var konsole2 = ""
var konsole3 = ""
var konsole4 = ""
var konsole5 = ""
function setNextElementPosition(konsole) {
  if (konsole1 == "") {
    konsole1 = konsole
    console.log("konsole1 = ",konsole1.id)
    konsole1.style.left = "2%"
  }else if(konsole2 =="") {
    konsole2 = konsole
    konsole2.style.left = "23%";
    console.log(konsole.style.left)
    console.log("style left: ",konsole2.style.left)
    console.log("konsole2 = ",konsole2.id)
  }else if(konsole3 == ""){
    konsole3 = konsole
    konsole3.style.left = "44%";
    console.log("konsole3 = ",konsole3.id)      
  }else if(konsole3 ==""){
    konsole3 = konsole
    console.log("konsole3 = ",konsole3.id)
    konsole3.style.left = "65%"
  }
}


function initializeTerminal() {
  const closeAbout = document.getElementById("closeAbout");
  const minAbout = document.getElementById("minAbout");
  const maxAbout = document.getElementById("maxAbout");
  const restoreAbout = document.getElementById("restoreAbout");
  const closeProject = document.getElementById("closeProject");
  const minProject = document.getElementById("minProject");
  const maxProject = document.getElementById("maxProject");
  const restoreProject = document.getElementById("restoreProject");
  const closeSkills = document.getElementById("closeSkills");
  const minSkills = document.getElementById("minSkills");
  const maxSkills = document.getElementById("maxSkills");
  const restoreSkills = document.getElementById("restoreSkills");
  const about = document.getElementById("about");
  const projects = document.getElementById("projects");
  const skills = document.getElementById("skills");

  function displayTerminal(option, konsole, minButton, restoreButton, maxButton, closeButton) {

    option.addEventListener("click", function () {
      if (konsole.style.display === "none" || konsole.style.display === "") {
        konsole.style.display = "block";
        // konsole.log("hola")
        draggable(konsole, minButton, restoreButton, maxButton, closeButton)
      } else {
        konsole.style.display = "none";
      }
    });
    closeButton.addEventListener("click", function () {
      if (konsole.style.display === "none" || konsole.style.display === "") {
        konsole.style.display = "block";
      } else {
        konsole.style.display = "none";
      }

    });
    // konsole.log(maxButton)
    maxButton.addEventListener("click", function () {
      // konsole.log("hola")
      if (!konsole.classList.contains("maximize")) {
        konsole.classList.add("maximize");
        konsole.classList.remove("minimize")
        konsole.onmousedown = null;
      }

    });
    restoreButton.addEventListener("click", function () {
      if (!konsole.classList.contains("restore")) {
        konsole.classList.remove("maximize")
        konsole.classList.remove("minimize")
        draggable(konsole, minButton, restoreButton, maxButton, closeButton)
      }

    });
    minButton.addEventListener("click", function () {
      if (!konsole.classList.contains("minimize")) {
        konsole.classList.add("minimize");
        konsole.classList.remove("maximize")
        konsole.onmousedown = null;
        setNextElementPosition(konsole);

      }
    });


  }
  about.addEventListener("click", displayTerminal(about, globTerminal, minAbout, restoreAbout, maxAbout, closeAbout))
  projects.addEventListener("click", displayTerminal(projects, globTerminal2, minProject, restoreProject, maxProject, closeProject))
  skills.addEventListener("click", displayTerminal(skills, globTerminal3, minSkills, restoreSkills, maxSkills, closeSkills))
  // close.addEventListener("click", displayTerminal (null, null ) )


}

function draggable(terminal, minButton, restoreButton, maxButton, closeButton) {
  terminal.onmousedown = function (event) {
    let shiftX = event.clientX - terminal.getBoundingClientRect().left;
    let shiftY = event.clientY - terminal.getBoundingClientRect().top;

    terminal.style.position = 'absolute';
    terminal.style.zIndex = 100;
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
  function stopDraggable(minButton, restoreButton, maxButton, closeButton) {
    closeButton.addEventListener("mousedown", function (event) {
      event.stopPropagation();
    });
    maxButton.addEventListener("mousedown", function (event) {
      event.stopPropagation();
    });
    restoreButton.addEventListener("mousedown", function (event) {
      event.stopPropagation();
    });
    minButton.addEventListener("mousedown", function (event) {
      event.stopPropagation();
    });
  }
  stopDraggable(minButton, restoreButton, maxButton, closeButton)

}
initializeTerminal();
// draggable(globTerminal)
