/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        bg: "var(--bg)",
        ink: "var(--ink)",
        accent: "var(--accent)",
        paper: "#FFFBF2",
        coal: "#14110C",
      },
      fontFamily: {
        display: ["'Bricolage Grotesque'", "sans-serif"],
        body: ["'Plus Jakarta Sans'", "sans-serif"],
      },
    },
  },
  plugins: [],
};
