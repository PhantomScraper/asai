---
title: "LEAPS RTLS Features"
lang: en
slug: "udk/specification/leaps-rtls-features"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/specification/leaps-rtls-features/"
order: 52
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-rtls-features">
<h1>LEAPS RTLS Features</h1>
<p>In addition to the specific features of the UDK kit, this section provides an overview of the LEAPS RTLS system from a broader perspective.</p>
<hr class="docutils">
<div class="section" id="key-features">
<h2>Key Features</h2>
<p>The LEAPS RTLS system provides an advanced and comprehensive solution for real-time accurate positioning and data telemetry using Ultra-Wideband wireless technology. The core of the solution is the highly sophisticated embedded software stack called LEAPS UWBS (Ultra-Wideband Sub-system) that offers many advanced features, including:</p>
<ul class="simple">
<li><p>A great versatility in a small footprint makes LEAPS a unique Swiss Army knife for accurate positioning and data telemetry in real-time. The UWB Sub-system is based on one firmware and is configurable in different modes and networking profiles.</p></li>
<li><p>Highly embedded, effective, optimized stack focusing on versatility, high performance, low memory, and low power consumption.</p></li>
<li><p>Proven system scalability deployed in various large-scale plants and buildings with an operational range of 50,000+ m2.</p></li>
<li><p>A modular structure facilitates adding new features and support for new hardware, which currently supports over 15 distinct board types and variants.</p></li>
<li><p>Currently, it is available on various hardware platforms, including Murata 2AB, DWM3001C, DWM1001C, and Ambiq Micro MCU.</p></li>
<li><p>An extensive API allows users to easily configure and customize the system according to their specific needs, providing a highly adaptable and versatile solution for real-time location tracking. The application can use binary Type-Length-Value (TLV) frame format via various interfaces like UART, USB, SPI, BLE or human readable shell command line over UART, USB and BLE interfaces.</p></li>
<li><p>The LEAPS RTLS system also provides an extensive range of free software tools that allow easy configuration and management of the system.</p></li>
<li><p>A continuous development of the LEAPS RTLS will provide more features to cover a wider range of applications in the future. This allows the users and product builders to learn one concept and deploy in many applications.</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="performance">
<h2>Performance</h2>
<ul class="simple">
<li><p>The networking stack is designed in the way that it always aims to reuse the air-time using an effective mechanism for both Anchors and Tags. This allows a virtually unlimited amount of nodes to be deployed in a spread area. All of this happens automatically using effective mechanisms of Anchors Auto-Clustering and Tags Roaming.</p></li>
<li><p>Depending on the measurement mode of the Tags, the maximum density can be 320 Hz for the TWR, 600 Hz for the UL-TDoA or an unlimited amount of Tags when DL-TDoA is used. The maximum density is achieved under specific conditions, when all the Tags are in range with each other, then there can be e.g. 3200 Tags with an update rate 0.1Hz, 320 Tags @ 1Hz or 32 Tags @ 10 Hz. The Tags would function with zero or minimum interference with each other.</p></li>
<li><p>Maximum tag location rate: Depending on network profile and measurement mode. Typically, 10 Hz for TWR, DL-TDoA and UL-TDoA. DL-TDoA can provide up to 50 Hz update rate per Tag.</p></li>
<li><p>X-Y location accuracy: Better than 50 cm, typically 10 cm.</p></li>
<li><p>Point-to-point range: Up to 50 m in Line-of-Sight conditions (CH5/CH9), up-to 150 m when PA is used.</p></li>
<li><p>Infrastructure deployment grid size: Typically, 20 x 20m and can work up to 40 x 40m.</p></li>
<li><p>Superior power management provides a long battery lifetime for TWR and TDoA modes.</p></li>
<li><p>Adaptive location rate using motion sensor activity enables a longer battery lifetime and a higher total amount of Tags.</p></li>
</ul>
</div>
</div>


           </div>
