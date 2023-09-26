const globTerminal = document.getElementById("draggable");
const globTerminal2 = document.getElementById("draggable2");
const globTerminal3 = document.getElementById("draggable3");
const globTerminal4 = document.getElementById("draggable4");
const globTerminal5 = document.getElementById("draggable5");
var konsole1 = ""
var konsole2 = ""
var konsole3 = ""
var konsole4 = ""
var konsole5 = ""

function position() {
  const scrollPosition = window.scrollX;
  const sections = document.querySelectorAll('.slide');
  sections.forEach((section, index) => {
    const sectionStart = section.offsetLeft;
    const sectionEnd = sectionStart + section.offsetWidth;

    if (scrollPosition >= sectionStart && scrollPosition < sectionEnd) {
      currentPosition = index + 1
    }
  })
  return (currentPosition)
}
function changeIcons() {
  const firstPosition = document.getElementById("firstPosition");
  const secondPosition = document.getElementById("secondPosition");
  const thirdPosition = document.getElementById("thirdPosition");
  const fourthPosition = document.getElementById("fourthPosition");
  const fifthPosition = document.getElementById("fifthPosition");

  function changeIcon(currentPosition, position, number) {
    if (currentPosition == number) {
      position.classList.add('current');
      position.classList.add('fa-ghost');
      position.classList.remove('fa-circle');
    } else {
      position.classList.add('fa-circle');
      position.classList.remove('fa-ghost');
      position.classList.remove('current');
    }
  }
  number = position()

  if (position() == 1) {
    changeIcon(number, firstPosition, 1)
  } else {
    changeIcon(number, firstPosition, 1)
  }
  if (position() == 2) {
    changeIcon(number, secondPosition, 2)
  } else {
    changeIcon(number, secondPosition, 2)
  }
  if (position() == 3) {
    changeIcon(number, thirdPosition, 3)
  } else {
    changeIcon(number, thirdPosition, 3)
  }
  if (position() == 4) {
    changeIcon(number, fourthPosition, 4)
  } else {
    changeIcon(number, fourthPosition, 4)
  }
  if (position() == 5) {
    changeIcon(number, fifthPosition, 5)
  } else {
    changeIcon(number, fifthPosition, 5)
  }

}


function setNextElementPosition(konsole, restoreButton, maxButton) {
  maxButton.addEventListener("click", function () {
    if (konsole1 === konsole) {
      konsole1 = ""
    }
    if (konsole2 === konsole) {
      konsole2 = ""
    }
    if (konsole3 === konsole) {
      konsole3 = ""
    }
    if (konsole4 === konsole) {
      konsole4 = ""
    }
    if (konsole5 === konsole) {
      konsole5 = ""
    }
  });
  restoreButton.addEventListener("click", function () {
    if (konsole1 === konsole) {
      konsole1 = ""
    }
    if (konsole2 === konsole) {
      konsole2 = ""
    }
    if (konsole3 === konsole) {
      konsole3 = ""
    }
    if (konsole4 === konsole) {
      konsole4 = ""
    }
    if (konsole5 === konsole) {
      konsole5 = ""
    }
  });

  if (konsole1 == "") {
    konsole1 = konsole
    console.log("konsole1 = ", konsole1.id)
    konsole1.style.left = "0%"
  } else if (konsole2 == "") {

    konsole2 = konsole
    konsole2.style.left = "18%";
    console.log("konsole2 = ", konsole2.id)

  } else if (konsole3 == "") {
    konsole3 = konsole
    konsole3.style.left = "36%";
    console.log("konsole3 = ", konsole3.id)

  } else if (konsole4 == "") {
    konsole4 = konsole
    console.log("konsole4 = ", konsole4.id)
    konsole4.style.left = "54%"

  } else if (konsole5 == "") {
    konsole4 = konsole
    console.log("konsole4 = ", konsole4.id)
    konsole4.style.left = "72%"

  } else {
    console.log("error")
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
  const closeBlog = document.getElementById("closeBlog");
  const minBlog = document.getElementById("minBlog");
  const maxBlog = document.getElementById("maxBlog");
  const restoreBlog = document.getElementById("restoreBlog");
  const closeContact = document.getElementById("closeContact");
  const minContact = document.getElementById("minContact");
  const maxContact = document.getElementById("maxContact");
  const restoreContact = document.getElementById("restoreContact");
  const about = document.getElementById("about");
  const projects = document.getElementById("projects");
  const skills = document.getElementById("skills");
  const blog = document.getElementById("blog");
  const contact = document.getElementById("contact");


  function displayTerminal(option, konsole, minButton, restoreButton, maxButton, closeButton) {

    option.addEventListener("click", function () {
      if (konsole.style.display === "none" || konsole.style.display === "") {
        konsole.style.display = "block";
        konsole.classList.remove("maximize")
        konsole.classList.remove("minimize")
        // konsole.log("hola")
        draggable(konsole, minButton, restoreButton, maxButton, closeButton)
      } else {
        konsole.style.display = "none";
      }
    });
    option.addEventListener("click", function () {
      if (position() == 1) {
        konsole.style.left = "5%";
      }
      if (position() == 2) {
        konsole.style.left = "25%";
      }
      if (position() == 3) {
        konsole.style.left = "45%";
      }
      if (position() == 4) {
        konsole.style.left = "65%";
      }
      if (position() == 5) {
        konsole.style.left = "85%";
      }
    })

    closeButton.addEventListener("click", function () {
      if (konsole.style.display === "none" || konsole.style.display === "") {
        konsole.style.display = "block";
        konsole.classList.remove("maximize")
        konsole.classList.remove("minimize")
      } else {
        konsole.style.display = "none";
      }

    });
    maxButton.addEventListener("click", function () {
      if (!konsole.classList.contains("maximize")) {
        konsole.classList.add("maximize");
        konsole.classList.remove("minimize")
        console.log("prueba")
        konsole.onmousedown = null;
        if (position() == 1) {
          konsole.style.left = ".3%";
          console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
        if (position() == 2) {
          konsole.style.left = "20.3%";
          console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
        if (position() == 3) {
          konsole.style.left = "40.3%";
          console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
        if (position() == 4) {
          konsole.style.left = "60.3%";
          console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
        if (position() == 5) {
          konsole.style.left = "80.3%";
          console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
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
        setNextElementPosition(konsole, restoreButton, maxButton);
        if (position() == 1) {
          konsole.style.left = ".3%";
          console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
        if (position() == 2) {
          konsole.style.left = "20.3%";
          console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
        if (position() == 3) {
          konsole.style.left = "40.3%";
          console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
        if (position() == 4) {
          konsole.style.left = "60.3%";
          console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
        if (position() == 5) {
          konsole.style.left = "80.3%";
          console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
      }
    });


  }
  about.addEventListener("click", displayTerminal(about, globTerminal, minAbout, restoreAbout, maxAbout, closeAbout))
  projects.addEventListener("click", displayTerminal(projects, globTerminal2, minProject, restoreProject, maxProject, closeProject))
  skills.addEventListener("click", displayTerminal(skills, globTerminal3, minSkills, restoreSkills, maxSkills, closeSkills))
  blog.addEventListener("click", displayTerminal(blog, globTerminal4, minBlog, restoreBlog, maxBlog, closeBlog))
  contact.addEventListener("click", displayTerminal(contact, globTerminal5, minContact, restoreContact, maxContact, closeContact))

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
window.addEventListener('scroll', changeIcons);
changeIcons();