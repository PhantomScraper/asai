/** Product & solution visuals from docs.leapslabs.com and Pastel design prototype */

/** Photos keep their natural colors; PNG illustrations carry the old red brand
 *  accents and get re-toned blue via the global .recolor-blue filter. */
export const isPhoto = (src) => /\.jpe?g$/i.test(src)

/** Diagrams whose blue tone is baked into the file itself (selective recolor that
 *  preserves embedded device photos/logos) — must NOT get the CSS filter again. */
const preToned = new Set([
  '/images/portfolio/rtls-stack.png',
  '/images/docs/leaps-architect-solution.png',
  '/images/portfolio/uwb-comparison.png',
])

export const needsRecolor = (src) => !isPhoto(src) && !preToned.has(src)

export const productImages = {
  heroPortfolio: '/images/portfolio/solutions-isometric.png',
  solutionsIsometric: '/images/portfolio/solutions-isometric.png',
  rtlsUseCases: '/images/portfolio/rtls-use-cases.png',
  rtlsStack: '/images/portfolio/rtls-stack.png',
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
}

export const portfolioCards = [
  {
    id: 'solutions',
    image: productImages.solutionsIsometric,
    link: '/solutions',
    titleKey: 'home.portfolio.solutionsTitle',
    textKey: 'home.portfolio.solutionsText',
    ctaKey: 'home.portfolio.solutionsCta',
  },
  {
    id: 'technology',
    image: productImages.rtlsStack,
    link: '/solutions#technology',
    titleKey: 'home.portfolio.technologyTitle',
    textKey: 'home.portfolio.technologyText',
    ctaKey: 'home.portfolio.technologyCta',
  },
  {
    id: 'products',
    image: productImages.udkKit,
    link: '/our-products',
    titleKey: 'home.portfolio.productsTitle',
    textKey: 'home.portfolio.productsText',
    ctaKey: 'home.portfolio.productsCta',
  },
  {
    id: 'services',
    image: productImages.supportResources,
    link: '/our-services',
    titleKey: 'home.portfolio.servicesTitle',
    textKey: 'home.portfolio.servicesText',
    ctaKey: 'home.portfolio.servicesCta',
  },
]

export const solutionPillarImages = [
  productImages.rtlsIllustrations,
  productImages.solutionsIsometric,
  productImages.rtlsStack,
]

export const applicationImages = [
  productImages.applicationsWarehouses,
  productImages.applicationsHospitals,
  productImages.solutionsIsometric,
]
