

const brandDropdown = document.getElementById("brand");
const modelDropdown = document.getElementById("model");

brandDropdown.addEventListener("change", function () {

    const selectedBrand = this.value;

    modelDropdown.innerHTML =
        '<option value="">Loading...</option>';

    fetch(`/get_models/${selectedBrand}`)

        .then(response => response.json())

        .then(models => {

            modelDropdown.innerHTML =
                '<option value="">-- Select Model --</option>';

            models.forEach(function(model){

                const option = document.createElement("option");

                option.value = model;
                option.textContent = model;

                modelDropdown.appendChild(option);

            });

        });

});





const form = document.getElementById("predictionForm");

form.addEventListener("submit", async function(event){

    event.preventDefault();

    const status = document.querySelector(".status");

status.textContent = "Predicting...";

document.getElementById("price").textContent = "₹ -----";

    const formData = new FormData(form);

    const response = await fetch("/predict",{

        method:"POST",

        body:formData

    });

    const data = await response.json();

    document.getElementById("price").innerHTML =
        "₹ " + data.predicted_price;

    status.textContent = "Prediction Complete ✓";

    document.getElementById("carDetails").innerHTML = `

<div class="summary">

    <p><strong>Brand</strong><br>${data.brand}</p>

    <p><strong>Model</strong><br>${data.model}</p>

    <p><strong>Year</strong><br>${data.year}</p>

    <p><strong>Fuel</strong><br>${data.fuel}</p>

    <p><strong>Transmission</strong><br>${data.transmission}</p>

    <p><strong>Body Type</strong><br>${data.body}</p>

    <p><strong>City</strong><br>${data.city}</p>

    <p><strong>Owner</strong><br>${data.owner}</p>

    <p><strong>KM Driven</strong><br>${data.km}</p>

</div>

`;

});