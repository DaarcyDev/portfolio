const globTerminal = document.getElementById("draggable");
const globTerminal2 = document.getElementById("draggable2");
const globTerminal3 = document.getElementById("draggable3");
const globTerminal4 = document.getElementById("draggable4");
const globTerminal5 = document.getElementById("draggable5");
const globTerminal6 = document.getElementById("draggable6");
var konsole1 = ""
var konsole2 = ""
var konsole3 = ""
var konsole4 = ""
var konsole5 = ""
const backgroundURLs = [
  "/static/images/wall-01.webp",
  "/static/images/wall-02.webp",
  "/static/images/wall-03.webp",
  "/static/images/wall-04.webp",
  "/static/images/wall-05.webp",
  "/static/images/wall-06.webp",
  "/static/images/wall-07.webp",
  "/static/images/wall-08.webp",
];

function changeBackground() {
  const randomURL = backgroundURLs[Math.floor(Math.random() * backgroundURLs.length)];

  document.querySelector('.background').style.backgroundImage = `url(${randomURL})`;
}



function projects() {
  const websiteButtons = document.querySelectorAll('.websiteImage');
  const websiteSections = document.querySelectorAll('.website');

  websiteButtons.forEach((button) => {
    button.addEventListener('click', (event) => {
      const selectedCategory = button.getAttribute('data-category');
      websiteSections.forEach((section) => {
        section.style.display = 'none';
      });

      const selectedSection = document.querySelector('.website[data-category="' + selectedCategory + '"]');
      if (selectedSection) {
        selectedSection.style.display = 'flex';
        selectedSection.scrollIntoView({ behavior: "smooth", block: "end" });
      }
    });
  });
}

function ranger() {
  const categories = document.querySelectorAll('.category');
  const projects = document.querySelectorAll('.project');
  const projectContent = document.querySelectorAll('.project-content');
  categories.forEach((category) => {
    category.addEventListener('click', (event) => {
      categories.forEach((cat) => {
        cat.classList.remove("select");
      });
      category.classList.add("select");      
      const selectedCategory = category.getAttribute('data-category');
      
      projects.forEach((project) => {
        
        if (project.getAttribute('data-category') != selectedCategory) {
          project.style.display = 'none';
        }
      });
      projectContent.forEach((content) => {
        if (content.getAttribute('data-category') === selectedCategory) {
          content.style.display = 'none';
        }
      });
  
      projects.forEach((project) => {
        
        if (project.getAttribute('data-category') === selectedCategory) {
          project.style.display = 'block';
        }
      });
      projectContent.forEach((content) => {
        
        if (content.getAttribute('data-category') === selectedCategory) {
          content.style.display = 'block';
        }
      });
      
      const firstProject = document.querySelector('.project[data-category="' + selectedCategory + '"]');

      if (firstProject) {
        firstProject.click();
      }
    });
  });

  projects.forEach((project) => {
    project.addEventListener('click', (event) => {
      projects.forEach((proj) => {
        proj.classList.remove("select");
      });
      project.classList.add("select");
      const projectCategory = project.getAttribute('data-project-content');
      projectContent.forEach((content) => {
        content.style.display = 'none';
      });
      const selectedCategory = project.getAttribute('data-category');
      projectContent.forEach((content) => {
        if (content.getAttribute('data-project-content') === projectCategory && content.getAttribute('data-category') === selectedCategory) {
          content.style.display = 'block';
        }
      });
    });
  });
}

function position() {
  let currentPosition = 0;
  const scrollLeft = window.scrollLeft || window.pageXOffset;
  const scrollTop = window.scrollTop || window.pageYOffset;
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
  const closeArch = document.getElementById("closeArch");
  const minArch = document.getElementById("minArch");
  const maxArch = document.getElementById("maxArch");
  const restoreArch = document.getElementById("restoreArch");
  const about = document.getElementById("about");
  const projects = document.getElementById("projects");
  const skills = document.getElementById("skills");
  const blog = document.getElementById("blog");
  const contact = document.getElementById("contact");
  const arch = document.getElementById("Arch");

  const time = 1500;
  
  
  function displayTerminal(option, konsole, minButton, restoreButton, maxButton, closeButton) {

    function projects(){
      const datascienceButton = document.getElementById("datascienceButton");
      const websiteButton = document.getElementById("websiteButton");
      const website = document.getElementById("websites")
      const websiteInfo = document.getElementById("websiteInfo")
      const datascience = document.getElementById("datascience")
      const programmingLanguages = document.getElementById("programmingLanguages")
      const userInterface = document.getElementById("userInterface")
      const developmentTools = document.getElementById("developmentTools")
      const databases = document.getElementById("databases")
      const dataProcessing = document.getElementById("dataProcessing")
      const operatingSystems = document.getElementById("operatingSystems")
      const programmingLanguagesButton = document.getElementById("programmingLanguagesButton")
      const userInterfaceButton = document.getElementById("userInterfaceButton")
      const developmentToolsButton = document.getElementById("developmentToolsButton")
      const databasesButton = document.getElementById("databasesButton")
      const dataProcessingButton = document.getElementById("dataProcessingButton")
      const operatingSystemsButton = document.getElementById("operatingSystemsButton")
      
      programmingLanguagesButton.addEventListener("click",function(){
        programmingLanguages.classList.add("tools")
        programmingLanguages.scrollIntoView({ behavior: "smooth", block: "end" });
        userInterface.classList.remove("tools")
        developmentTools.classList.remove("tools")
        databases.classList.remove("tools")
        dataProcessing.classList.remove("tools")
        operatingSystems.classList.remove("tools")
      })
      userInterfaceButton.addEventListener("click",function(){
        programmingLanguages.classList.remove("tools")
        userInterface.classList.add("tools")
        userInterface.scrollIntoView({ behavior: "smooth", block: "end" });
        developmentTools.classList.remove("tools")
        databases.classList.remove("tools")
        dataProcessing.classList.remove("tools")
        operatingSystems.classList.remove("tools")
      })
      developmentToolsButton.addEventListener("click",function(){
        programmingLanguages.classList.remove("tools")
        userInterface.classList.remove("tools")
        developmentTools.classList.add("tools")
        developmentTools.scrollIntoView({ behavior: "smooth", block: "end" });
        databases.classList.remove("tools")
        dataProcessing.classList.remove("tools")
        operatingSystems.classList.remove("tools")
      })
      databasesButton.addEventListener("click",function(){
        programmingLanguages.classList.remove("tools")
        userInterface.classList.remove("tools")
        developmentTools.classList.remove("tools")
        databases.classList.add("tools")
        databases.scrollIntoView({ behavior: "smooth", block: "end" });
        dataProcessing.classList.remove("tools")
        operatingSystems.classList.remove("tools")
      })
      dataProcessingButton.addEventListener("click",function(){
        programmingLanguages.classList.remove("tools")
        userInterface.classList.remove("tools")
        developmentTools.classList.remove("tools")
        databases.classList.remove("tools")
        dataProcessing.classList.add("tools")
        dataProcessing.scrollIntoView({ behavior: "smooth", block: "end" });
        operatingSystems.classList.remove("tools")
      })
      operatingSystemsButton.addEventListener("click",function(){
        programmingLanguages.classList.remove("tools")
        userInterface.classList.remove("tools")
        developmentTools.classList.remove("tools")
        databases.classList.remove("tools")
        dataProcessing.classList.remove("tools")
        operatingSystems.classList.add("tools")
        operatingSystems.scrollIntoView({ behavior: "smooth", block: "end" });
      })
      
      websiteButton.addEventListener("click", function () {
        website.style.display ="flex"
        websiteInfo.style.display="block"
        website.scrollIntoView({ behavior: "smooth", block: "end" });
        datascience.style.display ="none"
      })
      datascienceButton.addEventListener("click", function () {
        datascience.style.display ="flex"
        datascience.scrollIntoView({ behavior: "smooth", block: "end" });
        website.style.display ="none"
        websiteInfo.style.display="none"
      })
      restoreButton.addEventListener("click", function () {
        datascience.style.display ="none"
        website.style.display ="none"
        websiteInfo.style.display="none"
      })
      closeButton.addEventListener("click", function () {
        datascience.style.display ="none"
        website.style.display ="none"
        websiteInfo.style.display="none"
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
        const categories = document.querySelectorAll('.category');
        const firstcategory = categories[0];

        if (firstcategory) {
          firstcategory.click(); // Simular un clic en el primer proyecto
        }
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
  arch.addEventListener("click", displayTerminal(arch, globTerminal6, minArch, restoreArch, maxArch, closeArch))

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
    
    screenDiv.appendChild(terminal); 

    terminal.style.position = 'absolute';
    terminal.style.zIndex = 100;
    
    moveAt(event.pageX, event.pageY);


    function moveAt(pageX, pageY) {
      const minX = screenDiv.offsetLeft;
      const maxX = minX + screenDiv.offsetWidth - terminal.offsetWidth;
      const minY = screenDiv.offsetTop;
      const maxY = minY + screenDiv.offsetHeight - terminal.offsetHeight;
      
      let adjustedX = pageX - shiftX;
      let adjustedY = pageY - shiftY;
      
      adjustedX = Math.max(minX, Math.min(maxX, adjustedX));
      adjustedY = Math.max(minY, Math.min(maxY, adjustedY));

      terminal.style.left = adjustedX + 'px';
      terminal.style.top = adjustedY + 'px';
    }

    function onMouseMove(event) {
      moveAt(event.pageX, event.pageY);
    }
    
    document.addEventListener('mousemove', onMouseMove);
    
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
ranger()
projects()
document.querySelector('#Arch').addEventListener('click', changeBackground);
