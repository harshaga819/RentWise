    function toggleForm() {
        const form = document.getElementById('rentForm');
        const homepage = document.getElementById('homepage');
        
        homepage.style.display = 'none'; 
        form.style.display = 'block';  
        window.scrollTo(0, 0);
    }

    function setRandomValue(selectId, inputId) {
        const selectedRange = document.getElementById(selectId).value;
        if (selectedRange) {
            const [min, max] = selectedRange.split('-').map(Number);
            const randomValue = Math.floor(Math.random() * (max - min + 1)) + min;
            document.getElementById(inputId).value = randomValue;
        } else {
            document.getElementById(inputId).value = '';
        }
    }

    document.getElementById("rentFormAction").addEventListener("submit", function (event) {
        event.preventDefault();

        document.getElementById("loading").style.display = "block";
        document.getElementById("predictionResult").style.display = "none";

        const formData = new FormData(this);

        fetch("/predict", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("loading").style.display = "none";

            if (data.prediction_range) {
                document.getElementById("predictionResult").style.display = "block";
                document.getElementById("predictedRentRange").textContent = data.prediction_range;
            } else {
                console.error("Prediction error:", data);
                alert("Error predicting rent. Please try again.");
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById("loading").style.display = "none";
            alert("Something went wrong. Please try again later.");
        });
    });
