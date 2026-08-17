/** Product & solution visuals from docs.leapslabs.com and the agency design round.
 *  All artwork is used in its original LEAPS brand-red coloring — no CSS re-toning. */

export const productImages = {
  heroPortfolio: '/images/portfolio/solutions-isometric.png',
  solutionsIsometric: '/images/portfolio/solutions-isometric.png',
  rtlsUseCases: '/images/portfolio/rtls-use-cases.png',
  /* The old rtls-stack.png carried a baked-in blue tone from the Qorvo redesign —
   * the original red architecture diagram from docs.leapslabs.com replaces it. */
  rtlsStack: '/images/docs/leaps-architect-solution.png',
  uwbComparison: '/images/portfolio/uwb-comparison.png',
  supportResources: '/images/portfolio/support-resources.png',
  udkKit: '/images/products/udk-kit.jpg',
  udkBanner: '/images/docs/udk-all-in-one.png',
  rtlsIllustrations: '/images/docs/illustrations.png',
  rtlsArchitecture: '/images/docs/leaps-architect-solution.png',
  aboutMark: '/images/about/leaps-mark.png',
  aboutInnovation: '/images/about/innovation.png',
  aboutExperience: '/images/about/experience.png',
  applicationsWarehouses: '/images/portfolio/applications-warehouses.png',
  applicationsHospitals: '/images/portfolio/applications-hospitals.png',
  /* Network structure diagram provided by LEAPS during the agency review (Pastel #47) */
  networkStructure: '/images/design/42t31f9qvoLScZiu.png',
  /* Qorvo UWB vs other wireless technologies chart (Pastel #51) */
  uwbTechComparison: '/images/design/N62rVnSJhvXsaVkP.png',
}

/** Product photos extracted from the official datasheets */
export const hardwareImages = {
  lg1: '/images/hardware/lg1.png',
  lg2: '/images/hardware/lg2.png',
  lt1: '/images/hardware/lt1.png',
  lt2: '/images/hardware/lt2.png',
  lt3: '/images/hardware/lt3.png',
  lt4: '/images/hardware/lt4.png',
}

export const solutionPillarImages = [
  productImages.rtlsIllustrations,
  productImages.solutionsIsometric,
  productImages.rtlsStack,
]

/** Application-example visuals from the LEAPS company presentation (slides 8–10),
 *  in the same order as solutions.appExamples in the locale files. The slugs
 *  anchor the detail blocks on the Projects page (/projects#uc-<slug>). */
export const appExampleImages = [
  '/images/applications/agv-navigation.jpg',
  '/images/applications/assets-people-tracking.jpg',
  '/images/applications/elderly-monitoring.jpg',
]

export const appExampleSlugs = ['agv-navigation', 'assets-people-tracking', 'elderly-monitoring']
