/** @type {import('tailwindcss').Config} */
module.exports = {
  prefix: 'tw-',

  content: ['./public/**/*.html', './src/**/*.{js,jsx,ts,tsx,vue}'],
  darkMode: 'media', // or 'media' or 'class'
  theme: {
    extend: {
      maxWidth: {
        'screen-xxl': '1600px',
      },
    },
  },
  variants: {},

}
