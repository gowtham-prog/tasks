console.log("hi");
const home = document.querySelector("#home");
const app = document.querySelector("#AddApp");
const form = document.querySelector("form");
const file = document.querySelector(".home");
app.addEventListener("click", () => {
    form.style.display = "block";
    file.style.display = "none";
})
home.addEventListener("click", () => {
    file.style.display = "block";
    form.style.display = "none";
})
const subcat = {
    "entertainment": ["Social Media", "OTT"],
    "games": ["Adventure", "Action"],
    "ecommerce": ["Clothing", "Grocery"],
}

const category = document.querySelector(".app-category");
const subcategory = document.querySelector(".app-sub-category");

category.addEventListener("change", () => {
    console.log(subcat["entertainment"]);
    let change = `<option disabled selected>Sub Category</option>`;
    if (category.value == "Entertainment") {
        subcat["entertainment"].forEach(element => {
            change += `<option>${element}</option>`;
        });
    }
    if (category.value == "Games") {
        subcat["games"].forEach(element => {
            change += `<option>${element}</option>`;
        });
    }
    if (category.value == "E-commerce") {
        subcat["ecommerce"].forEach(element => {
            change += `<option>${element}</option>`;
        });
    }
    subcategory.innerHTML = change;
})

let points = 0;
const addpoints = document.querySelector("#add-points");
addpoints.addEventListener("click", () => {
    addpoints.innerHTML = points;
    points += 10;
})
const appname = document.querySelector(".app-name");
const application = document.querySelector("#form");


application.addEventListener("submit", (e) => {
    e.preventDefault();
    console.log("hello");
    const addfile = {
        "file": null,
        "name": appname.value,
        "points": points - 10,
        "complete": false,
        "user": null
    };
    const encodedCredentials = btoa("window.localStorage.getItem('username'):window.localStorage.getItem('password')");
    fetch("http://127.0.0.1:8000/api/saveapp", {
        method: "post",
        body: JSON.stringify(addfile),
        headers: {
            'Authorization': 'Basic' + encodedCredentials,
            "Content-type": "application/json",
        }
    }).then(response => response.json()).then(json => console.log(json));
    const field = document.querySelectorAll("form input");
    field.forEach((fil) => {
        fil.value = "";
    })
    points = 0;
    addpoints.innerHTML = "Add Points";
    category.innerHTML = `  <option disabled selected>App Category</option>
                            <option>Entertainment</option>
                            <option>Games</option>
                            <option>E-commerce</option>`;
    subcategory.innerHTML = `<option disabled selected>Sub Category</option>`;
})



