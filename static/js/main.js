function changeText() { <!-- function changes the font of paragraph -->
    let paragraph = document.getElementById("special-two")
    paragraph.style.fontFamily = 'Georgia, serif';
}

function greeting() { <!-- function generates greeting -->
    let nameInput = document.getElementById("nameInput");
    alert("Hello," + nameInput.value + "!");
}

food = ["Ramen", "Rice and Stew", "Dumplings"];

foodList = document.getElementById("foodList");

let x = 0
while (x < food.length) {
    document.write("<p>" + food[x] + "</p>");
    x++;
}

function chooseCourses() { <!-- function creates checkboxes to be selected -->
    let checkboxes = document.querySelectorAll('input[name="courses"]');
    let selectedCourses = " ";
    for (let i = 0; i < checkboxes.length; i++) {
        let checkbox = checkboxes[i];
        if (checkbox.checked) {
            selectedCourses = selectedCourses + "," + checkbox.value;
        }
    }
    alert(selectedCourses);
}

