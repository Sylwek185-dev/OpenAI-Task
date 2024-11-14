const footerYear = document.querySelector('.footer-year'); //date in footer

const showYearOnFooter = () => {
	const year = new Date().getFullYear();
	footerYear.innerHTML = year + ' Sylwester Rząd, All Rights Reserved';
};

showYearOnFooter();
