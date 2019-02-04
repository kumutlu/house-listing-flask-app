const startApp = () => {
  fetch('http://127.0.0.1:5000/houses')
    .then(response => response.json())
    .then(houses => renderCards(houses))
    .catch(err => console.error(err))
}

// Render house cards
const renderCards = (houses) => {
  for (let i = 0; i < houses.length; i++) {
    const container = document.getElementById('list-container')
    const house = houses[i]

    const newHouse = document.createElement('div')
    newHouse.className = 'house-card'

    const pictureContainer = document.createElement('div')
    pictureContainer.className = 'house-picture-container'
    const img = document.createElement('IMG')
    img.src = house.picture
    pictureContainer.appendChild(img)

    const h2 = document.createElement('h2')
    h2.innerText = house.name

    const list = document.createElement('ul')

    for (let j = 0; j < 3; j++) {
      const newLI = document.createElement('li')

      if (j === 0) {
        newLI.innerHTML = `Price: ${house.price}`
      } else if (j === 1) {
        newLI.innerHTML = `Location: ${house.location}`
      } else {
        newLI.innerHTML = `Size: ${house.size}`
      }
      list.appendChild(newLI)
    }

    const description = document.createElement('div')
    description.className = 'house-description'
    const h3 = document.createElement('h3')
    h3.innerHTML = 'Description'
    description.appendChild(h3)
    const par = document.createElement('p')
    par.innerHTML = house.description
    description.appendChild(par)



    newHouse.appendChild(pictureContainer)
    newHouse.appendChild(h2)
    newHouse.appendChild(list)
    newHouse.appendChild(description)

    container.appendChild(newHouse)

  }
}

startApp()

function myFunction() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

myFunction()

function check(form)
{
 
 if(form.userid.value == "koguz" && form.pswrd.value == "1234")
  {
    window.open('index.html', "_self")
    
  }
 else
 {
   alert("Username or Password is incorrect!")
  }
}