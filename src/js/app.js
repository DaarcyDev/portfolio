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
  let currentPosition = 0;
  const scrollLeft = window.scrollLeft || window.pageXOffset; // Scroll horizontal
  const scrollTop = window.scrollTop || window.pageYOffset;    // Scroll vertical
  const sections = document.querySelectorAll('.slide');

  sections.forEach((section, index) => {
    const sectionStartX = section.offsetLeft;
    const sectionEndX = sectionStartX + section.offsetWidth;
    const sectionStartY = section.offsetTop;
    const sectionEndY = sectionStartY + section.offsetHeight;

    if (
      scrollLeft >= sectionStartX &&
      scrollLeft < sectionEndX &&
      scrollTop >= sectionStartY &&
      scrollTop < sectionEndY
    ) {
      currentPosition = index + 1;
      // // console.log(currentPosition);
    }
  });

  return currentPosition;
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

  const time = 1500;
  
  
  function displayTerminal(option, konsole, minButton, restoreButton, maxButton, closeButton) {

    function projects(){
      const datascienceButton = document.getElementById("datascienceButton");
      const websiteButton = document.getElementById("websiteButton");
      const website = document.getElementById("websites")
      const datascience = document.getElementById("datascience")
      const website1 = document.getElementById("website1")
      const website1Info = document.getElementById("website1Info")
      const website2 = document.getElementById("website2")
      const website2Info = document.getElementById("website2Info")
      const website3 = document.getElementById("website3")
      const website3Info = document.getElementById("website3Info")
      website1.addEventListener("click",function(){
        website1Info.style.display="flex"
        website1Info.scrollIntoView({ behavior: "smooth", block: "end", inline: "center", container: konsole });
        website2Info.style.display="none"
        website3Info.style.display="none"
      })
      website2.addEventListener("click",function(){
        website1Info.style.display="none"
        website2Info.style.display="flex"
        website2Info.scrollIntoView({ behavior: "smooth", block: "end", inline: "center", container: konsole });
        website3Info.style.display="none"
      })
      website3.addEventListener("click",function(){
        website1Info.style.display="none"
        website2Info.style.display="none"
        website3Info.style.display="flex"
        website3Info.scrollIntoView({ behavior: "smooth", block: "end", inline: "center", container: konsole });
      })
      websiteButton.addEventListener("click", function () {
        website.style.display ="flex"
        website.scrollIntoView({ behavior: "smooth", block: "end", inline: "center", container: konsole });
        datascience.style.display ="none"
        
      })
      datascienceButton.addEventListener("click", function () {
        datascience.style.display ="flex"
        datascience.scrollIntoView({ behavior: "smooth", block: "end", inline: "center", container: konsole });
        website.style.display ="none"
        website1Info.style.display="none"
        website2Info.style.display="none"
        website3Info.style.display="none"
      })
      restoreButton.addEventListener("click", function () {
        datascience.style.display ="none"
        website.style.display ="none"
        website1Info.style.display="none"
        website2Info.style.display="none"
        website3Info.style.display="none"
      })
      closeButton.addEventListener("click", function () {
        datascience.style.display ="none"
        website.style.display ="none"
        website1Info.style.display="none"
        website2Info.style.display="none"
        website3Info.style.display="none"
      })
    }
    option.addEventListener("click", function () {
      
      if (konsole.style.display === "none" || konsole.style.display === "") {
        
        var screenDiv = document.querySelector('.display');
        if (position() == 1) {
          screenDiv = document.querySelector('.first');
        }
        if (position() == 2) {
          screenDiv = document.querySelector('.second');
        }
        if (position() == 3) {
          screenDiv = document.querySelector('.third');
        }
        if (position() == 4) {
          screenDiv = document.querySelector('.fourth');
        }
        if (position() == 5) {
          screenDiv = document.querySelector('.fifth');
        }
        const elements = konsole.querySelectorAll(".comand");
        const texts = konsole.querySelectorAll(".text");
        texts.forEach(function(text) {
          text.classList.add("animationText");
            setTimeout(function() {
            text.classList.remove("animationText");
          }, time);
        });
        elements.forEach(function(element) {
          element.classList.add("animationComand");
            setTimeout(function() {
            element.classList.remove("animationComand");
          }, time);
        });
        screenDiv.appendChild(konsole);
        konsole.style.display = "block";
        konsole.classList.remove("maximize")
        konsole.classList.remove("minimize")

        konsole.onmousedown = null;
        setTimeout(function () {
          draggable(konsole, minButton, restoreButton, maxButton, closeButton)  
        }, 1000);
        
      } else {
        konsole.style.display = "none";
      }
    });
    option.addEventListener("click", function () {
      if (position() == 1) {
        if (window.innerWidth <= 900) {
          konsole.style.left = "10%";
          konsole.style.top = "5%";
        }else{
          konsole.style.left = "5%";
        }
        
        // konsole.style.top = "17rem";
      }
      if (position() == 2) {
        if (window.innerWidth <= 900) {
          konsole.style.left = "10%";
          konsole.style.top = "25%";
        }else{
          konsole.style.left = "25%";
        }
        
        // konsole.style.top = "17rem";
      }
      if (position() == 3) {
        if (window.innerWidth <= 900) {
          konsole.style.left = "10%";
          konsole.style.top = "45%";
        }else{
          konsole.style.left = "45%";
        }
        
        // konsole.style.top = "17rem";
      }
      if (position() == 4) {
        if (window.innerWidth <= 900) {
          konsole.style.left = "10%";
          konsole.style.top = "65%";
        }else{
          konsole.style.left = "65%";
        }
        
        // konsole.style.top = "17rem";
      }
      if (position() == 5) {
        if (window.innerWidth <= 900) {
          konsole.style.left = "10%";
          konsole.style.top = "85%";
        }else{
          konsole.style.left = "85%";
        }
        
        // konsole.style.top = "17rem";
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
        // console.log("prueba")
        konsole.onmousedown = null;
        if (position() == 1) {
          if (window.innerWidth <= 900) {
            konsole.style.left = "1.5%";
            konsole.style.top = "3.5%";
          }else{
            konsole.style.top = "8%";
            konsole.style.top = "8%";
            konsole.style.left = ".3%";
          }
          
          // console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
        if (position() == 2) {
          if (window.innerWidth <= 900) {
            konsole.style.left = "1.5%";
            konsole.style.top = "23.5%";
          }else{
            konsole.style.top = "8%";
            konsole.style.left = "20.3%";
          }
          
          // console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
        if (position() == 3) {
          if (window.innerWidth <= 900) {
            konsole.style.left = "1.5%";
            konsole.style.top = "43.5%";
          }else{
            konsole.style.top = "8%";
            konsole.style.left = "40.3%";
          }
          
          // console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
        if (position() == 4) {
          if (window.innerWidth <= 900) {
          konsole.style.left = "1.5%";
          konsole.style.top = "63.5%";
          }else{
            konsole.style.top = "8%";
            konsole.style.left = "60.3%";
          }
          
          // console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
        }
        if (position() == 5) {
          if (window.innerWidth <= 900) {
          konsole.style.left = "1.5%";
          konsole.style.top = "83.5%";
          }else{
            konsole.style.top = "8%";
            konsole.style.left = "80.3%";
          }
          
          // console.log(`max position: ${konsole.id} position ${konsole.style.left}`)
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
      }
    });
    projects()


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
    var screenDiv = document.querySelector('.display');
    if (position() == 1) {
      screenDiv = document.querySelector('.first');
    }
    if (position() == 2) {
      screenDiv = document.querySelector('.second');
    }
    if (position() == 3) {
      screenDiv = document.querySelector('.third');
    }
    if (position() == 4) {
      screenDiv = document.querySelector('.fourth');
    }
    if (position() == 5) {
      screenDiv = document.querySelector('.fifth');
    }
    
    screenDiv.appendChild(terminal); // Mover la terminal al div .screen

    terminal.style.position = 'absolute';
    terminal.style.zIndex = 100;
    
    moveAt(event.pageX, event.pageY);

    // mueve el elemento a las coordenadas (pageX, pageY)
    // tomando en cuenta la posición inicial

    function moveAt(pageX, pageY) {
      // Obtén las coordenadas límite para mantener la terminal dentro del div .screen
      const minX = screenDiv.offsetLeft;
      const maxX = minX + screenDiv.offsetWidth - terminal.offsetWidth;
      const minY = screenDiv.offsetTop;
      const maxY = minY + screenDiv.offsetHeight - terminal.offsetHeight;
      
      // Ajusta las coordenadas para que no salga del div .screen
      let adjustedX = pageX - shiftX;
      let adjustedY = pageY - shiftY;
      
      // Limita las coordenadas a los valores máximos y mínimos
      adjustedX = Math.max(minX, Math.min(maxX, adjustedX));
      adjustedY = Math.max(minY, Math.min(maxY, adjustedY));

      terminal.style.left = adjustedX + 'px';
      terminal.style.top = adjustedY + 'px';
      // terminal.style.transform = `translate(${adjustedX}px, ${adjustedY}px)`; 
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
// projects()3