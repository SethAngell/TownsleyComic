/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    "**/templates/*.html",
    "**/templates/**/*.html",
    "../accounts/templates/accounts/*.html",
    "../accounts/templates/registration/*.html",
    "../blog/templates/blog/*.html",
    "../profile/templates/profile/*.html",
    "../content/templates/content/*.html"
  ],
  plugins: [require("@tailwindcss/typography")],
};
