# LEAPS Website

Modern Vue 3 website for [LEAPS Labs](https://www.leapslabs.com/) — accurate positioning and data telemetry using Ultra-Wideband technology.

Built based on the [Pastel design review](https://usepastel.com/link/oed0y9l3#/) with updated, modern UI and full content from the current website.

## Tech Stack

- **Vue 3** + **Vite**
- **Vue Router** for multi-page navigation
- CSS custom properties for design system

## Pages

| Route | Description |
|-------|-------------|
| `/` | Home — hero, features, help cards |
| `/our-products` | UDK Development Kit, demos, distributors |
| `/our-projects` | Case studies and applications |
| `/our-services` | Adopt, customize, support services |
| `/solutions` | UWB technology and LEAPS uniqueness |
| `/support` | Documentation, FAQ, community |
| `/about` | Company info, team, contact form |

## Getting Started

```bash
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173)

## Build

```bash
npm run build
npm run preview
```

## Design Notes

- Brand colors: LEAPS red (`#b83232`), clean light backgrounds
- Typography: Instrument Sans (headings) + DM Sans (body)
- Responsive with mobile hamburger menu
- Pastel feedback incorporated: distributor logos on products, redesigned projects section, active nav highlighting
