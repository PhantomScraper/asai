export const navLinks = [
  { name: 'Solutions', path: '/solutions' },
  { name: 'Products & Services', path: '/products-services' },
  { name: 'Projects', path: '/projects' },
  { name: 'Support', path: '/support' },
  { name: 'About', path: '/about' },
]

export const externalLinks = {
  docs: 'https://docs.leapslabs.com/',
  forum: 'https://forum.leapslabs.com/',
  store: 'https://store.leapslabs.com/',
  udkStart: 'https://docs.leapslabs.com/udk-start',
  qorvoUwb: 'https://www.qorvo.com/innovation/ultra-wideband/technology',
  comparison: 'https://docs.leapslabs.com/leaps-solutions/comparison/',
}

/** Datasheets: the UDK sheet lives on docs.leapslabs.com; the 2026 product range
 *  sheets are hosted locally until they are published on the docs site. */
export const datasheets = {
  lg1: '/datasheets/leaps-lg1-datasheet.pdf',
  lg2: '/datasheets/leaps-lg2-datasheet.pdf',
  lt1: '/datasheets/leaps-lt1-datasheet.pdf',
  lt2: '/datasheets/leaps-lt2-datasheet.pdf',
  lt3: '/datasheets/leaps-lt3-datasheet.pdf',
  lt4: '/datasheets/leaps-lt4-datasheet.pdf',
  rtls: '/datasheets/leaps-rtls-datasheet.pdf',
  udk: 'https://docs.leapslabs.com/_static/_pdfversion/udk-datasheet.pdf',
}

export const features = [
  {
    id: 'modular',
    title: 'Modular',
    description:
      'LEAPS RTLS is an advanced modular system that is versatile to meet your needs; it comprises of a highly sophisticated UWB Subsystem firmware, configurable in different modes and profiles.',
    icon: 'modular',
  },
  {
    id: 'secure',
    title: 'Secure',
    description:
      'LEAPS RTLS was designed from scratch with a strong focus on security and privacy.',
    icon: 'secure',
  },
  {
    id: 'versatile',
    title: 'Versatile',
    description:
      "LEAPS UWB Subsystem's versatility allows the functionality of a wide range of applications, from navigation and tracking in buildings with many rooms, open-space areas, fast movement, to long battery lifetime tracking applications.",
    icon: 'versatile',
  },
  {
    id: 'simple',
    title: 'Simple',
    description:
      'LEAPS RTLS is easy to set up and has a wide range of API options that allow easy integration into your products and services. Growing PANS RTLS and LEAPS RTLS community provides a valuable resource of information and help.',
    icon: 'simple',
  },
  {
    id: 'unique',
    title: 'Unique',
    description:
      'LEAPS RTLS is a unique Swiss Army knife for accurate positioning and data telemetry in real-time. A small, versatile module provides flexibility and a great return on investment.',
    icon: 'unique',
  },
  {
    id: 'proven',
    title: 'Proven',
    description:
      "LEAPS RTLS was built by the creators of Qorvo's DWM1001 and PANS RTLS which was achieved through a team of reliable and experienced experts trusted by Qorvo.",
    icon: 'proven',
  },
]

export const productDemos = [
  'Nearby Interaction Demo with an iPhone',
  'Locate Device Using Angle-of-Arrival Demo',
  'Infrastructure-less Proximity Demo',
  'Downlink TDoA RTLS Demo',
  'Uplink TDoA RTLS Demo',
  'TWR RTLS and Data Telemetry Demo',
]

export const productDescription =
  'The UDK (Ultra-Wideband Development Kit) is an all-in-one demonstration ready-to-use kit. The kit provides a wide range of evaluation demonstrations of the Ultra-Wideband technology ranging from Nearby Interaction demo with an iPhone, FiRa compatible proximity, infrastructure-less proximity, TDoA RTLS, TWR RTLS and data telemetry.'

export const kitContent = [
  'The kit consists of 6 hardware devices — one LC13 device with an integrated UWB AoA antenna and five LC14 devices with an integrated UWB non-AoA antenna.',
  'All devices can be configured in any mode of the demo including Anchor, Tag, Gateway, FiRa or Nearby Interaction.',
  'Qorvo QM33120W, an Ultra-Wideband FiRa compatible chipset, is integrated together with the popular Bluetooth-capable MCU nRF52840. With the external LNA/PA, the devices provide superior UWB range coverage.',
  "They are pre-programmed with LEAPS Ultra-Wideband Subsystem, an all-in-one advanced and versatile software stack that includes Qorvo's FiRa capable software library. Together with a set of tools, it forms a production-ready LEAPS RTLS.",
  'The kit includes two USB-C data cables for programming, data exchange and powering.',
  'A battery is not included.',
]

export const kitIncludes = [
  'Free software configuration and visualization tools (software support for iOS, Android, Windows, MacOS and Linux platforms depending on the demo).',
  'An open online documentation and community forum.',
  'An open SDK based on Zephyr RTOS for starting development of custom applications.',
]

export const partNumber = 'QM33120WDK2 = UDK'

/** UDK (QM33120WDK2) authorized distributors — list and links confirmed by LEAPS
 *  in the agency review (no Richardson Electronics: currently not available). */
export const distributors = [
  {
    name: 'DigiKey',
    url: 'https://www.digikey.com/en/products/detail/qorvo/QM33120WDK2/26905169',
    logo: '/images/distributors/82b2eb4d48d54a16b8f7163841763bc6.png',
  },
  {
    name: 'Mouser',
    url: 'https://eu.mouser.com/ProductDetail/Qorvo/QM33120WDK2',
    logo: '/images/distributors/a40f58c14bf742908df1fd53a25aeb57.png',
  },
  {
    name: 'Avnet',
    url: 'https://www.avnet.com/americas/product/qorvo/qm33120wdk2/evolve-121598055/',
    logo: '/images/distributors/ed819279764b45768bd671a2cd68fe11.png',
  },
  {
    name: 'RFMW',
    url: 'https://www.rfmw.com/products/detail/qm33120wdk2-qorvo/859631/',
    logo: '/images/distributors/e67076c605bd4115ac42ca2baa91d17b.png',
  },
  {
    name: 'Symmetry Electronics',
    url: 'https://www.symmetryelectronics.com/products/qorvo/qm33120wdk2/',
    logo: '/images/distributors/5656c95bc2af415e8ca118aa4ac588c0.png',
  },
  {
    name: 'Qorvo',
    url: 'https://www.qorvo.com/products/p/QM33120WDK2',
    logo: '/images/distributors/e167dac274d54df2afcd9a245e915bbc.png',
  },
]

export const serviceCategories = [
  {
    id: 'adopt',
    title: 'Adopt',
    description:
      'Do you want to adopt LEAPS RTLS, PANS RTLS, or DWM1001 but need help to shorten the time needed to market them? Let us know about your project.',
    cta: 'Contact Us',
  },
  {
    id: 'customize',
    title: 'Customize',
    description:
      'Already know LEAPS RTLS, PANS RTLS or DWM1001 but need customization? Let us know about your needs.',
    cta: 'Contact Us',
  },
  {
    id: 'support',
    title: 'Support',
    description:
      'Do you need long term support for your products integrating LEAPS RTLS or DWM1001? Let us know how we can help you.',
    cta: 'Contact Us',
  },
]

export const customizationServices = [
  {
    title: 'Software',
    description:
      'Are you missing some features? Does LEAPS RTLS or PANS RTLS have limits which do not fit your needs? Or do you want a different system tailored for your application? Use our expertise in design and implementation of software for embedded and Android platforms.',
  },
  {
    title: 'Hardware',
    description:
      'Do you need hardware with more range, smaller footprints, and new features to integrate into your product fully? We provide services from consultation to prototyping and evaluation to production tests.',
  },
  {
    title: 'Certification',
    description:
      'Proper protocol and hardware design are the keys to a successful certification. Use our expertise to reduce costs and achieve a smooth FCC/ETSI/ARIB certification.',
  },
]

/** Application areas and solution topics sourced from docs.leapslabs.com */
export const solutionTopics = [
  {
    title: 'Comparison',
    description:
      'Brief information about LEAPS Ultra-Wideband solution in general before exploring the specifics of LEAPS RTLS and PANS PRO RTLS.',
    image: '/images/docs/comparison.png',
    docsUrl: 'https://docs.leapslabs.com/leaps-solutions/',
  },
  {
    title: 'Safety',
    description:
      'LEAPS RTLS empowers businesses to improve operational efficiency and enhance safety in warehouses, hospitals, factories, and other facilities.',
    image: '/images/docs/safety.png',
    docsUrl: 'https://docs.leapslabs.com/leaps-solutions/',
  },
  {
    title: 'Compliance',
    description:
      'Proper protocol and hardware design supported by LEAPS expertise helps achieve smooth certification for your UWB products.',
    image: '/images/docs/compliant.png',
    docsUrl: 'https://docs.leapslabs.com/leaps-solutions/',
  },
]

export const rtlsApplications = [
  {
    title: 'Warehouses',
    description:
      'Precise and accurate tracking of assets, people, and equipment in real-time to gain deeper insights and improve operational efficiency.',
  },
  {
    title: 'Hospitals',
    description:
      'Real-time location for patients, staff, and medical equipment with security and privacy built into the LEAPS RTLS design.',
  },
  {
    title: 'Factories',
    description:
      'Navigation, tracking, and data telemetry for automation and digitization — locating new values for your business processes.',
  },
]

export const uniquenessFeatures = [
  {
    title: 'Modular',
    description:
      'One module with one firmware, configurable in different modes and profiles. The module can run as Anchor, Tag, or Bridge. The profiles are fully scalable with high capacity and low power. All the magic is integrated on a tiny chip of 3x3 mm size.',
  },
  {
    title: 'Scalable',
    description:
      'A unique clustering mechanism allows anchors to form clusters automatically and reuse the air-time effectively. A large network can be deployed as easily as mounting and powering the device.',
  },
  {
    title: 'Telemetry',
    description:
      'Besides location, LEAPS RTLS provides a transport network for your IoT application. The data are transferred in real-time to and from the edge nodes, allowing deterministic timing for IoT applications.',
  },
  {
    title: 'Self-Monitoring',
    description:
      'Each node on the network collects statistics about itself. Infrastructure nodes monitor the communication of the surrounding nodes. The data provide an effective way to detect and signal issues.',
  },
  {
    title: 'Versatile',
    description:
      'Versatility makes it easy to balance the system requirements, costs, deployment time, and maintenance complexity. Applications range from simple distance proximity to high speed tracking or navigation of an unlimited amount of receivers.',
  },
  {
    title: 'Variant',
    description:
      'LEAPS RTLS supports various locating techniques, including Two-Way Ranging and Time Difference of Arrival. The raw measurements are available, thereby allowing position estimation to be optimized for specific applications.',
  },
  {
    title: 'Wireless',
    description:
      'Unique wireless routing backhaul simplifies the deployment and reduces the infrastructure costs. The data between the nodes and the server are sent wirelessly via Ultra-wideband between infrastructure nodes.',
  },
  {
    title: 'Updatable',
    description:
      'Network nodes can be updated automatically and wirelessly via Ultra-wideband. Deploy the firmware to the Initiator and get the whole network updated automatically.',
  },
  {
    title: 'Secure',
    description:
      'State-of-the-art security keeps firmware consistent, authorizes nodes on the network, protects against a wide range of attacks and guarantees secure data exchange for the whole data chain. Navigation with complete privacy is possible.',
  },
  {
    title: 'Precision',
    description:
      'Flexible profiles allow the selection of mode with optimal balance between location precision, node capacity and power consumption. The high amount and high rate of measurements allow the best precision and location robustness.',
  },
  {
    title: 'Timing',
    description:
      'Both time-slotted TDMA and probabilistic media access methods are supported. TDMA is suitable where reliability and high capacity are needed.',
  },
  {
    title: 'API',
    description:
      'Easy-to-use APIs are available for Bluetooth, MQTT, UART, SPI, and on module Shell. Detailed design allows for keeping the latency as low as possible.',
  },
  {
    title: 'Low-Power',
    description:
      'The unique network protocol provides effective two way communication with nodes mostly in sleep mode. An integrated motion sensor helps to reduce consumption further by activating a low update rate when node stays still.',
  },
  {
    title: 'Coexistence',
    description:
      'Multiple separated LEAPS RTLS networks can coexist in the overlapped area. The overlapping networks will coexist synchronously in a way that does not negatively affect the performance.',
  },
]

export const aboutContent = {
  intro:
    "LEAPS is a company based in the Czech Republic that focuses on building and marketing Real-Time Location and Real-Time Telemetry systems based on Ultra-wideband. The company was founded in 2016 and is known for designing and developing Qorvo's (Decawave's) DWM1001, DWM3001 modules and PANS RTLS. LEAPS supplies technology and design services to Fortune 500 companies around the world.",
  docsIntro:
    'LEAPS is a company based in Prague (the Czech Republic, EU) that focuses on building and marketing Real-Time Location and Real-Time Telemetry systems based on Ultra-wideband. With more than 10 years of experience in system development using Ultra-Wideband, LEAPS has one of the most innovative teams in converting the Ultra-wideband chip into a useful solution.',
  teamNote:
    'Our team consists of all senior embedded engineers who work with great passion from Prague, Ho Chi Minh City in Vietnam, and Pelotas in Brazil.',
  rtlsNote:
    'LEAPS RTLS is a collection of advanced software that provides location services for a wide range of use cases. It offers the most advanced fully-embedded UWB Sub-System on the market that covers features ranging from proximity, navigation and tracking to real-time data telemetry and routing backhaul.',
  valueNote:
    'LEAPS provides a new dimension that helps businesses locate new values, improve process efficiency, increase safety, improve reliability, navigate indoors, process automatization …',
}

export const aboutValues = [
  {
    title: 'Innovation',
    description:
      'LEAPS has one of the most innovative teams in converting the Ultra-wideband chip into a useful solution. The proof is that the best-in-class semiconductor company Qorvo has chosen LEAPS as a system provider among their 3000+ clients and partners.',
  },
  {
    title: 'Experience',
    description:
      'LEAPS team has more than 10 years of acquired experience in developing the Real-Time Location System using different technologies (2.4 GHz ToF, 2.4 GHz phase-measurement, sensor fusion, and Ultra-wideband). Since 2014, the team has been focusing fully on Ultra-wideband technology.',
  },
]

export const team = [
  {
    name: 'Tran Duy Khanh',
    displayName: 'TRAN Duy Khanh',
    role: 'CEO',
    photo: '/images/team/tran-duy-khanh.jpg',
    linkedin: 'https://cz.linkedin.com/in/khanh-tran-duy-14bb3038',
  },
  {
    name: 'Jiří KUBIAS',
    displayName: 'Jiří KUBIAS',
    role: 'CTO',
    photo: '/images/team/jiri-kubias.jpg',
    linkedin: 'https://cz.linkedin.com/in/jiri-kubias-640a8750',
  },
]

export const verifiedFacts = [
  { label: 'Founded', value: '2016' },
  { label: 'Headquarters', value: 'Prague, Czech Republic' },
  { label: 'Known for', value: 'DWM1001, DWM3001, PANS RTLS' },
  { label: 'Experience', value: '10+ years in UWB RTLS' },
]

export const contact = {
  company: 'LEAPS s.r.o.',
  addressLines: ['Hodoninska 1', '141 00', 'Prague 4', 'Czech Republic, EU'],
  phone: '+420 222 966 953',
  email: 'info@leapslabs.com',
  vat: 'CZ04768655',
  web: 'https://www.leapslabs.com',
}

/** LinkedIn only, per LEAPS feedback in the agency review */
export const socialLinks = [
  { name: 'LinkedIn', url: 'https://www.linkedin.com/company/leapslabs', icon: 'linkedin' },
]

export const supportResources = [
  {
    title: 'Documentation',
    description:
      'Comprehensive descriptions for every component of the UDK DEMO KIT, LEAPS RTLS, and PANS PRO RTLS.',
    link: 'https://docs.leapslabs.com/',
    linkText: 'Read Documentation',
  },
  {
    title: 'Quick Start Guide',
    description: 'Follow the UDK quick start guide to begin practical evaluation of Ultra-Wideband and RTLS technology.',
    link: 'https://docs.leapslabs.com/udk-start',
    linkText: 'UDK Quick Start',
  },
  {
    title: 'Community Forum',
    description:
      'Engage in discussions, raise inquiries, and connect with the global LEAPS community of customers and users.',
    link: 'https://forum.leapslabs.com/',
    linkText: 'Visit Forum',
  },
]

export const docSections = [
  { title: 'LEAPS Solutions', url: 'https://docs.leapslabs.com/leaps-solutions/' },
  { title: 'UDK Demo Kit', url: 'https://docs.leapslabs.com/udk/' },
  { title: 'LEAPS RTLS', url: 'https://docs.leapslabs.com/leaps-rtls/' },
  { title: 'PANS PRO RTLS', url: 'https://docs.leapslabs.com/pans-pro-rtls/' },
  { title: 'Hardware', url: 'https://docs.leapslabs.com/hardware/' },
  { title: 'FAQ', url: 'https://docs.leapslabs.com/faq/' },
  { title: 'Support', url: 'https://docs.leapslabs.com/support/' },
]

/* ------------------------------------------------------------------ */
/* 2026 hardware range (UWB channels 5 & 9, FCC/CE/ARIB Japan)         */
/* Language-neutral spec values from the official device datasheets;   */
/* names and descriptions live in the i18n locale files under          */
/* productsServices.anchors.items / productsServices.tags.items.       */
/* ------------------------------------------------------------------ */

export const anchorSpecs = [
  {
    id: 'lg1',
    partNumber: 'LR-LG1A1',
    image: '/images/hardware/lg1.png',
    datasheet: datasheets.lg1,
    specs: {
      power: '7–32 VDC / USB 5 V',
      backhaul: 'WiFi 2.4 GHz b/g/n',
      bluetooth: 'BLE 5.2',
      accuracy: '< 0.5 m (TWR & TDoA)',
      temp: '-40 °C … +85 °C',
      size: '85 × 57 × 17 mm · 50 g',
      ip: 'IP30',
      mounting: '1/4″ camera mount',
    },
  },
  {
    id: 'lg2',
    partNumber: 'LR-LG2A1',
    image: '/images/hardware/lg2.png',
    datasheet: datasheets.lg2,
    specs: {
      power: 'PoE 802.3af / 7–32 VDC / USB 5 V',
      backhaul: 'Daisy-chained PoE Ethernet + WiFi 2.4 GHz',
      bluetooth: 'BLE 5.2',
      accuracy: '< 0.5 m (TWR & TDoA)',
      temp: '-40 °C … +85 °C',
      size: '127 × 98 × 41 mm · 135 g',
      ip: 'IP30',
      mounting: '1/4″ camera mount / 4-screw bracket',
    },
  },
  {
    id: 'lgx',
    partNumber: 'LR-LGxA1',
    image: '/images/hardware/lg2.png',
    datasheet: null,
    specs: {
      power: 'PoE / external source',
      backhaul: 'Daisy-chained PoE Ethernet + WiFi, embedded Linux',
      bluetooth: 'BLE',
      accuracy: '< 0.5 m (TWR & TDoA)',
      temp: '-40 °C … +85 °C',
      size: '—',
      ip: '—',
      mounting: '—',
    },
  },
]

export const tagSpecs = [
  {
    id: 'lt1',
    partNumber: 'LR-LT1A1',
    image: '/images/hardware/lt1.png',
    datasheet: datasheets.lt1,
    specs: {
      battery: 'Coin-cell CR2477, 1000 mAh',
      batteryLife: 'UL-TDoA 12 mo – 5 y · TWR 3 mo – 3 y',
      accuracy: '< 0.5 m (TWR & TDoA)',
      temp: '-30 °C … +85 °C',
      size: '68 × 50 × 18 mm · 38 g',
      ip: 'IP66',
      mounting: '2 screws',
    },
  },
  {
    id: 'lt2',
    partNumber: 'LR-LT2A1',
    image: '/images/hardware/lt2.png',
    datasheet: datasheets.lt2,
    specs: {
      battery: 'Rechargeable LiPo 3.7 V, 600 mAh (USB)',
      batteryLife: 'UL-TDoA 9 mo – 3 y · TWR 2 mo – 2 y',
      accuracy: '< 0.5 m (TWR & TDoA)',
      temp: '-20 °C … +45 °C (with battery)',
      size: '68 × 50 × 18 mm · 38 g',
      ip: 'IP66',
      mounting: '2 screws',
    },
  },
  {
    id: 'lt3',
    partNumber: 'LR-LT3A1',
    image: '/images/hardware/lt3.png',
    datasheet: datasheets.lt3,
    specs: {
      battery: 'Rechargeable LiPo 3.7 V, 1000 mAh (USB)',
      batteryLife: 'UL-TDoA 12 mo – 5 y · TWR 3 mo – 3 y',
      accuracy: '< 0.5 m (TWR & TDoA)',
      temp: '-20 °C … +45 °C (with battery)',
      size: '75 × 95 × 15 mm · 72 g',
      ip: '—',
      mounting: 'Lanyard / clip-on / card holder',
    },
  },
  {
    id: 'lt4',
    partNumber: 'LR-LT4A1',
    image: '/images/hardware/lt4.png',
    datasheet: datasheets.lt4,
    specs: {
      battery: 'Rechargeable LiPo 3.7 V, 600 mAh (USB)',
      batteryLife: 'UL-TDoA 1 – 5 y · TWR 3 mo – 3 y',
      accuracy: '< 0.5 m (TWR & TDoA)',
      temp: '-20 °C … +45 °C (with battery)',
      size: '43 × 48 × 22 mm · 38 g',
      ip: 'IP66',
      mounting: 'Universal NATO strap',
    },
  },
]

/** Milestones from leapslabs.com/about (dates are language-neutral) */
export const milestoneDates = [
  '04/2016', '01/2017', '01/2018', '03/2019', '10/2019',
  '02/2020', '01/2021', '12/2022', '10/2023',
]

/** Case-study logos/links (text lives in i18n successStories) */
export const successStoryMeta = [
  { id: 'qorvo', link: 'https://www.qorvo.com' },
  { id: 'toyota', link: null },
  { id: 'amazon', link: null },
  { id: 'nous', link: 'https://nousdigital.com/en/our-products/nous-sonic/' },
  { id: 'umano', link: 'https://www.umanomedical.com' },
]
