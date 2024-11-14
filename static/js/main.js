const footerYear = document.querySelector('.footer-year'); //date in footer

const showYearOnFooter = () => {
	const year = new Date().getFullYear();
	footerYear.innerHTML = year + ' Sylwester Rząd, All Rights Reserved';
};

showYearOnFooter();

document
	.getElementById('contact-form')
	.addEventListener('submit', function (event) {
		event.preventDefault(); // Zatrzymanie domyślnego wysłania formularza

		// Przypisanie adresu e-mail z pola do ukrytego pola "_replyto"
		const email = document.getElementById('email').value;
		document.getElementById('replyto').value = email;

		const name = document.getElementById('name').value;
		const message = document.getElementById('message').value;

		// Utworzenie obiektu FormData
		const formData = new FormData();
		formData.append('name', name);
		formData.append('email', email);
		formData.append('message', message);

		// Wysłanie danych formularza do FormSubmit
		fetch('https://formsubmit.co/sylwek185@op.pl', {
			method: 'POST',
			mode: 'no-cors',
			body: formData,
		})
			.then(() => {
				alert('Wiadomość została wysłana pomyślnie!');
				document.getElementById('contact-form').reset();
			})
			.catch((error) => {
				console.error('Błąd:', error);
				alert('Wystąpił błąd. Spróbuj ponownie później.');
			});
	});
