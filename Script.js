window.onload = () => {
	let button = document.querySelector("#btn");

	// Function for calculating BMI
	button.addEventListener("click", calculateBMI);
};

function calculateBMI() {

	/* Getting input from user into height variable.
	Input is string so typecasting is necessary. */
	let height = parseInt(document
			.querySelector("#height").value);

	/* Getting input from user into weight variable. 
	Input is string so typecasting is necessary.*/
	let weight = parseInt(document
			.querySelector("#weight").value);

	let result = document.querySelector("#result");

	// Checking the user providing a proper
	// value or not
	if (height === "" || isNaN(height)) 
		result.innerHTML = "Provide a valid Height!";

	else if (weight === "" || isNaN(weight)) 
		result.innerHTML = "Provide a valid Weight!";

	// If both input is valid, calculate the bmi
	else {

		// Fixing upto 2 decimal places
		let bmi = (weight / ((height * height) 
							/ 10000)).toFixed(2);

		// Dividing as per the bmi conditions
		if (bmi < 18.6) result.innerHTML=
        `<img src="https://www.planetayurveda.com/pa-wp-images/underweight.jpg" style="width:50px; height:100px;"> UNDERWEIGHT😒: <span>${bmi}</span>`;

		else if (bmi >= 18.6 && bmi < 24.9) 
			result.innerHTML = 
            `<img src="https://images.ctfassets.net/eexbcii1ci83/4bn8wMZJuSZvOTvH6PblGL/6f8f30d63658c6ed08da138656ffc03a/Height_To_Weight_Chart-_Weight_According_to_Height_in_Kg_for_Men_and_Women.jpg" style="width:50px; height:100px;"> NORMAL😍: <span>${bmi}</span>`;

		else result.innerHTML =`<img src="https://as2.ftcdn.net/v2/jpg/01/63/88/15/1000_F_163881568_DBeWEmh3nNJRtmKniOBO3iPD3ulpJZlM.jpg"133620 style="width:50px; height:100px;"> OVERWEIGHT😮: <span>${bmi}</span>`;
			 
	}
}
