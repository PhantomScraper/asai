---
title: "Generic"
lang: en
slug: "faq/generic"
section: "faq"
sourceUrl: "https://docs.leapslabs.com/faq/generic/"
order: 29
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="generic">
<span id="faq-generic"></span><h1>Generic</h1>
<hr class="docutils">
<div class="line-block">
<div class="line">The following FAQ (Frequently Asked Questions) cover common questions related to Ultra-Wideband, <a class="reference internal" href="/docs/en/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a> or <a class="reference internal" href="/docs/en/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a>.</div>
</div>
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>I am new to the Real-Time Location System. Do you have a list of basic terminology?<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>Anchor</strong> - <strong>AN (Anchor Node)</strong> - Infrastructure node with fixed location - reference node capable of measuring location data, data offload and routing.</p>
<ul>
<li><p class="sd-card-text">An Anchor can have Gateway function enabled - it functions as a gateway between UWB Sub-system and other interfaces, such as Ethernet and WiFi. The UWB Sub-system is connected to the host via SPI or USB interfaces.</p></li>
</ul>
</li>
<li><p class="sd-card-text"><strong>Location Engine (LE)</strong> - An algorithm for position estimation using measured values. There are two major groups used</p></li>
</ul>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text"><strong>Trilateration</strong> - Location engine which uses distances between nodes to estimate the position, especially when TWR is used.</p></li>
<li><p class="sd-card-text"><strong>Multilateration</strong> - Location engine which uses time differences between nodes to estimate the position, especially when TDoA is used.</p></li>
</ul>
</div></blockquote>
<ul class="simple">
<li><p class="sd-card-text"><strong>Navigation</strong> - A mode of positioning when the location data are collected and used on the side of the mobile object. In navigation mode of LEAPS RTLS and PANS PRO RTLS, the location is calculated on the module, and the data are available via on-module API. This approach provides very low latency of location data on the mobile device, reduces infrastructure costs, and significantly simplifies deployment. Typical applications are e.g. navigation of drones, robots, tools, vehicles and portable devices.</p></li>
<li><p class="sd-card-text"><strong>Node</strong> - A network device capable of communicating with other devices (Anchor, Tag, …).</p></li>
<li><p class="sd-card-text"><strong>Tag</strong> - <strong>TN (Tag Node)</strong> - Mobile node with moving location - It uses Anchors to measure, locate its position and depending on the mode it can exchange data at a specified update rate.</p></li>
<li><p class="sd-card-text"><strong>Time Difference of Arrival (TDoA)</strong> - It is a measurement technique where the difference in time is measured between nodes at known fixed locations. The result of the measurement is time difference. The nodes at a known fixed location typically need to be synchronized. TDoA is a hyperbolic location position method that has two major sub-categories</p></li>
</ul>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text"><strong>Uplink TDoA (UL-TDoA)</strong> - is a <strong>tracking</strong> mode of the TDoA, where a Tag usually sends at a random time a short message called Blink. The Anchors receive the Blink and use their synchronized time to estimate the Tag’s location using hyperbolic positioning method. This positioning method requires at least 4 measurements and is usually more sensitive to the shape of Anchors deployment. As the Tags need to send only a short blink, this method requires lowest power consumption. A UL-TDoA Tag also has lower requirement for the hardware design and the battery. Network scalability and Tag low power consumption is easier to achieve using this method due to its random access to be media in comparison to a TWR system, where a more complex time scheduling and collision avoidance scheme is required.</p></li>
<li><p class="sd-card-text"><strong>Downlink TDoA (DL-TDoA)</strong> - is a <strong>navigation</strong> mode of the TDoA, where a Tag would only listen to the network messages from Anchors containing time and usually Anchor positions. Based on these data, the Tag can calculate its position. It is an analogy to the GNSS (Global Navigation Satellite System) for an indoor use. As the Tags only listen and do not transmit, there is no limit for the number of Tags. This mode allows a complete privacy of the Tags as they do not transmit.</p></li>
</ul>
</div></blockquote>
<ul class="simple">
<li><p class="sd-card-text"><strong>Tracking</strong> - A mode of positioning when the location and telemetry data are collected on a centralized server. The data are available via LEAPS Server API. This mode is suitable for monitoring and processing data of a large number of devices in a single place, typically on a server. Typical applications are e.g. asset tracking, zone violation detection, athlete’s performance monitoring and personnel tracking.</p></li>
<li><p class="sd-card-text"><strong>Two-way Ranging (TWR)</strong> - Is a group of measurement techniques where the range between two nodes is estimated by exchanging messages both way. The result of the measurement is distance. Time synchronization of the nodes is not required for the Tag position calculation.</p></li>
<li><p class="sd-card-text"><strong>Ultra-Wideband (UWB)</strong> - is a radio technology that can use a very low energy level for short-range, high-bandwidth communications over a large portion of the radio spectrum. In comparison to other technology like Bluetooth, WIFI or GPS, UWB is very immune to multipath fading. Hence, this makes it suitable for accurate positioning, especially indoors.</p></li>
</ul>
</div>
</details><hr class="docutils">
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>What are the differences between DWM1001, PANS RTLS, PANS PRO RTLS and LEAPS RTLS?<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>DWM1001</strong> is a hardware module based on Decawave/Qorvo’s DW1000 Ultra Wideband (UWB) transceiver IC, which is an IEEE 802.15.4-2011 UWB implementation. It integrates UWB and Bluetooth® antennas, all RF circuitry, Nordic Semiconductor nRF52832 and a motion sensor. The module was initially designed by LEAPS and marketed under Decawave brand.</p></li>
<li><p class="sd-card-text"><strong>PANS RTLS</strong> is a complete Real-Time Location System and network stack based on TWR measurement technique. The UWB Sub-system is configurable into Anchor, Tag or Gateway modes. The software stack has been developed by LEAPS and is marketed under the Decawave/Qorvo brand.</p></li>
<li><p class="sd-card-text"><strong>PANS PRO RTLS</strong> is based on PANS RTLS stack. It is maintained and provided to the market by LEAPS. Many software improvements and bugfixes have been implemented in PANS PRO RTLS in order to provide a production level ready stack. A range of certified products has been introduced to the market with this software stack. The stack is provided free of charge to the market in binary code in the same way as the PANS RTLS stack.</p></li>
<li><p class="sd-card-text"><strong>LEAPS RTLS</strong> is an advanced Real-Time Location System that can cover a wide range of navigation and tracking use cases. Its core is an embedded UWB Sub-system that can be configured in different modes and profiles. The stack can operate in Anchor, Tags or Gateway modes. The networking profiles are fully scalable with high capacity and low power. Its versatility makes it easy to balance the system requirements, costs, deployment time and maintenance complexity. Applications range from simple distance proximity, to high speed tracking or navigation of unlimited amount of receivers. Supported measurement techniques that include TWR (Two-Way Ranging), UL-TDoA (tracking using Uplink Time Difference of Arrival) and DL-TDoA (navigation using Downlink Time Difference of Arrival). The LEAPS stack is integrated in LEAPS’s as well as thirdparty’s products.</p></li>
</ul>
</div>
</details><hr class="docutils">
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>How LEAPS has participated in the creation of DWM1001 modules and PANS RTLS network stack?<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>DWM1001 module</strong> was initially designed by LEAPS, who worked on the design, module bring-up, validation and bringing the design into production under Decawave/Qorvo’s brand.</p></li>
<li><p class="sd-card-text"><strong>LEAPS</strong> has designed and developed the <strong>software stack of PANS RTLS</strong>, including an extensive set of embedded tests used for module calibration and functional tests in production.</p></li>
</ul>
</div>
</details><hr class="docutils">
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>What are the differences in architecture between LEAPS RTLS and PANS PRO RTLS?<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<p class="sd-card-text">Comparison of system architecture of LEAPS RTLS (top) and PANS PRO RTLS (bottom):</p>
<p class="sd-card-text"><strong>LEAPS RTLS System Architecture</strong></p>
<img alt="../../_images/leaps-architect-solution.png" class="align-center" src="/docs-assets/_images/leaps-architect-solution.png">
<p class="sd-card-text"><strong>PANS PRO RTLS System Architecture</strong></p>
<img alt="../../_images/pans_pro-sub-system.png" class="align-center" src="/docs-assets/_images/pans_pro-sub-system.png">
</div>
</details><hr class="docutils">
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>How to achieve the longest possible range between 2 devices?<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<p class="sd-card-text">This has some relation to the <a class="reference external" href="https://www.omnicalculator.com/physics/fresnel-zone">Fresnel zones</a>. Long time ago we have done some measurements in about 1.2m - 1.5m height the signal gets lost at some distance and then comes back after 5-10 m for a while. Then we realize the Fresnel zones and increased the height to 2m and since then we don’t observe this issues anymore.</p>
<p class="sd-card-text">For most radio signals you should take care only about 1st Fresnel zone, but for UWB it seems that also other zones are important.</p>
<p class="sd-card-text">Practical example:</p>
<p class="sd-card-text">Distance between antennas = 100m</p>
<ul class="simple">
<li><p class="sd-card-text">Frequency = 6.5GHz</p></li>
<li><p class="sd-card-text">1st zone radius = 1.07m</p></li>
<li><p class="sd-card-text">2st zone radius = 1.52m</p></li>
<li><p class="sd-card-text">3st zone radius = 1.86m</p></li>
</ul>
<p class="sd-card-text">Distance between antennas = 200m</p>
<ul class="simple">
<li><p class="sd-card-text">Frequency = 6.5GHz</p></li>
<li><p class="sd-card-text">1st zone radius = 1.52m</p></li>
<li><p class="sd-card-text">2st zone radius = 2.15m</p></li>
<li><p class="sd-card-text">3st zone radius = 2.63m</p></li>
</ul>
<p class="sd-card-text">Online calculator is here <a class="reference external" href="https://www.omnicalculator.com/physics/fresnel-zone">Fresnel Zone Calculator</a></p>
</div>
</details></div>


           </div>
