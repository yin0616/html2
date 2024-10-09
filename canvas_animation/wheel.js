/*
 *       _____ _____ _____                _       _
 *      |_   _/  __ \_   _|              (_)     | |
 *        | | | /  \/ | |  ___  ___   ___ _  __ _| |
 *        | | ||      | | / __|/ _ \ / __| |/ _` | |
 *       _| |_| \__/\ | |_\__ \ (_) | (__| | (_| | |
 *      |_____\_____/ |_(_)___/\___/ \___|_|\__,_|_|
 *                   ___
 *                  |  _|___ ___ ___
 *                  |  _|  _| -_| -_|  LICENSE
 *                  |_| |_| |___|___|
 *
 * IT NEWS  <>  PROGRAMMING  <>  HW & SW  <>  COMMUNITY
 *
 * This source code is a part of online courses at IT social
 * network WWW.ICT.SOCIAL
 *
 * Feel free to use it for whatever you want, modify it and share it but
 * don't forget to keep this link in your code.
 *
 * Visit http://www.ict.social/licenses for more information
 */

let canvas;
let context;
let angle = 0;
let image;

// Page loaded
window.onload = function () {
	canvas = document.getElementById("canvas");
	context = canvas.getContext("2d");
	image = document.getElementById("wheel");
	image.style.display = "none";
	setInterval(redraw, 20);
	redraw();
}

// Timer function
function redraw() {
	context.clearRect(0,0,500,500);
	context.save();
	context.translate(250, 250);
	context.rotate(angle);
	context.drawImage(image, -225, -225);
	context.restore();
	angle += (2 * Math.PI) / 360; // Rotates by 1 degree
}
