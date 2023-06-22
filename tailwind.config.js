/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      'terrain': "url('/static/media/terrain.png')",},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}