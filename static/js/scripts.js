/*!
* Start Bootstrap - Personal v1.0.1 (https://startbootstrap.com/template-overviews/personal)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-personal/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

document.addEventListener('DOMContentLoaded', function () {
    console.log("JavaScript call")
    document.addEventListener('DOMContentLoaded', function () {
        const form = document.getElementById('contactForm');
        const submitButton = document.getElementById('submitButton');

        form.addEventListener('input', function () {
            if (form.checkValidity()) {
                submitButton.classList.remove('disabled');
            } else {
                submitButton.classList.add('disabled');
            }
        });
    });
});