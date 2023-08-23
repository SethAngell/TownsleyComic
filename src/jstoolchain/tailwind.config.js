/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    "**/templates/*.html",
    "../accounts/templates/accounts/*.html",
    "../accounts/templates/registration/*.html",
    "../blog/templates/blog/*.html",
    "../profile/templates/profile/*.html",
  ],
  plugins: [require("@tailwindcss/typography")],
};
