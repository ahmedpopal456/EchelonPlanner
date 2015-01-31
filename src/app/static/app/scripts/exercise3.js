var pvalid = false;
var evalid = false;
var english = cookieCheck();

//{% load staticfiles %}

function cookieCheck() {
	var cookies = document.cookie.split(";"), i = 0, cookie = null;
	for (i = 0; i < cookies.length; i++) {
		cookie = cookies[i];
		if (cookie[0] === "en") {
			return cookie[1];
		}
	}
	return true;
}

function readFlag() {
	if (document.getElementById("flag").src === "\"{% static 'app/images/french-flag.gif' %}\"") {
		document.cookie = "en=false";
	}
	if (document.getElementById("flag").src === "\"{% static 'app/images/flag-uk.gif' %}\"") {
		document.cookie = "en=true";
	}
	english = !english;
	translate();
}

function translate() { // NO ACCENTS

	if (!english) {
		document.body.innerHTML = document.body.innerHTML.replace(
				"Registration", "Inscription");
		document.body.innerHTML = document.body.innerHTML
				.replace("Please submit your log-in information or <a href=\"register\">register here</a>",
						"Veuillez soumettre vos coordonées d'utilisateur ou vous <a href=\"register\">inscrire ici</a>"); 
		document.body.innerHTML = document.body.innerHTML
		.replace("Please fill out the form",
				"Veuillez remplire le formulaire");
		document.body.innerHTML = document.body.innerHTML.replace(
				"Login Details", "D. connexion");
		document.body.innerHTML = document.body.innerHTML.replace("Username",
				"Nom d'utilisateur");
		document.body.innerHTML = document.body.innerHTML.replace("Password",
				"Mot de passe");
		document.body.innerHTML = document.body.innerHTML.replace(
				"Retype Password", "Mot de passe (bis)");
		document.body.innerHTML = document.body.innerHTML.replace("User Data",
				"D. utilis.");
		document.body.innerHTML = document.body.innerHTML.replace("First Name",
				"Prénom");
		document.body.innerHTML = document.body.innerHTML.replace(
				"Middle Name", "2e Prénom");
		document.body.innerHTML = document.body.innerHTML.replace("Last Name",
				"Nom de famille");
		document.body.innerHTML = document.body.innerHTML.replace("Email",
				"Courriel");
		document.getElementById("subbut").value = "Soumettre";
		document.getElementById("flag").src = '../static/app/images/flag-uk.gif';
		document.getElementById("flag").alt = "English";
	}
	if (english) {
		document.body.innerHTML = document.body.innerHTML.replace(
				"Inscription", "Registration");
		document.body.innerHTML = document.body.innerHTML
				.replace("Veuillez soumettre vos coordonées d'utilisateur ou vous <a href=\"register\">inscrire ici</a>",
						"Please submit your log-in information or <a href=\"register\">register here</a>");
		document.body.innerHTML = document.body.innerHTML
		.replace("Veuillez remplire le formulaire",
				"Please fill out the form");
		document.body.innerHTML = document.body.innerHTML.replace(
				"D. connexion", "Login Details");
		document.body.innerHTML = document.body.innerHTML.replace(
				"Nom d'utilisateur", "Username");
		document.body.innerHTML = document.body.innerHTML.replace(
				"Mot de passe", "Password");
		document.body.innerHTML = document.body.innerHTML.replace(
				"Mot de passe (bis)", "Retype Password");
		document.body.innerHTML = document.body.innerHTML.replace("D. utilis.",
				"User Data");
		document.body.innerHTML = document.body.innerHTML.replace("Prénom",
				"First Name");
		document.body.innerHTML = document.body.innerHTML.replace("2e Prénom",
				"Middle Name");
		document.body.innerHTML = document.body.innerHTML.replace(
				"Nom de famille", "Last Name");
		document.body.innerHTML = document.body.innerHTML.replace("Courriel",
				"Email");
		document.getElementById("subbut").value = "Submit";
		document.getElementById("flag").src = '../static/app/images/french-flag.gif';
		document.getElementById("flag").alt = "Francais";
	}
}

function passcheck() {
	var pass = document.getElementById("pass").value, repass = document
			.getElementById("repass").value;
	if (pass.match(/\S/) && repass.match(/\S/)) {
		if (pass.localeCompare(repass) !== 0) {
			document.getElementById("pwarning").src = "../static/app/images/exclamation_red.png";
			pvalid = false;
		} else {
			document.getElementById("pwarning").src = "../static/app/images//tick.png";
			pvalid = true;
		}
		document.getElementById("pwarning").style.visibility = "visible";
	} else {
		document.getElementById("pwarning").style.visibility = "false";
		pvalid = false;
	}
}

function emailcheck() {
	var email = document.getElementById("email").value;
	if (email.search(/[a-z]{1}[0-9a-z]{1,}[@]{1}[a-z]{2}[.]{1}[a-z]{2,3}/) === -1) {
		document.getElementById("ewarning").src = "../static/app/images/exclamation_red.png";
		evalid = false;
	} else {
		document.getElementById("ewarning").src = "../static/app/images/tick.png";
		evalid = true;
	}
	document.getElementById("ewarning").style.visibility = "visible";
}

function allCheck() {
	var user = document.getElementById("user").value, fname = document
			.getElementById("fname").value, lname = document
			.getElementById("lname").value, isvalid = pvalid
			&& evalid
			&& (user.search(/\S{1, }/) * fname.search(/\S{1, }/)
					* lname.search(/\S{1, }/) !== 0);
	return isvalid;
}

function submitCheck() {
	if (!allCheck) {
		document.getElementbyId("end").innerHTML = "The form contains errors";
		return false;
	}
	document.getElementbyId("end").innerHTML = "";
	return true;
}