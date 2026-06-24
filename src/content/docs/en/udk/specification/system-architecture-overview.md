---
title: "LEAPS RTLS"
lang: en
slug: "udk/specification/system-architecture-overview"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/specification/system-architecture-overview/"
order: 53
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-rtls">
<h1>LEAPS RTLS</h1>
<p>This section provides a more detailed understanding of the LEAPS RTLS system and outlines its specific components,
which are further elaborated in the following subsections.</p>
<hr class="docutils">
<div class="section" id="leaps-rtls-architecture">
<h2>LEAPS RTLS Architecture</h2>
<p>The following image provides an overview of the main concepts of the LEAPS RTLS system. Further, detailed information about each component will be provided in subsequent sections.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The firmware for the UDK contains the LEAPS UWB Sub-System as well as Qorvo FiRa UWB Sub-System.</p>
</div>
<div class="figure align-default" id="id1">
<img alt="The LEAPS RTLS Sub-system" class="with-shadow float-center" src="/docs-assets/_images/leaps-architect-solution-for-udk.png">
<p class="caption"><span class="caption-text">LEAPS RTLS Architecture.</span></p>
</div>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leaps-uwbs.png"><img alt="../../../_images/leaps-uwbs.png" class="align-right" src="/docs-assets/_images/leaps-uwbs.png" style="width: 91.80000000000001px; height: 75.8px;"></a>
</div>
<div class="section" id="leaps-uwbs">
<h2>LEAPS UWBS</h2>
<p>LEAPS UWBS is a fully-embedded UWB Sub-System that covers a wide range of use cases. One UWB Sub-System is configurable in different modes and profiles. The UWBS can run as an Anchor or Tag. Gateway represents a gateway between the UWB network and the upper layer. The networking profiles are fully scalable with high capacity and low power.</p>
<ul class="simple">
<li><p>Versatility makes it easy to balance the system requirements, costs, deployment time and maintenance complexity. Applications range from simple distance proximity to high-speed tracking or navigation of unlimited receivers.</p></li>
<li><p>It integrates a sophisticated UWBMAC that allows adaptive clustering of the infrastructure devices, air-time reuse, slot allocation, etc. A scalable, proven collision detection, collision avoidance, and collision resolution allow the system to function robustly in complex environments.</p></li>
<li><p>Supported measurement techniques include TWR, DL-TDoA and UL-TDoA. Integrated location engines allow the device to operate independently in the navigation mode using DL-TDoA or TWR.</p></li>
<li><p>Superior power management provides a long battery lifetime for TWR and TDoA modes.</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsapi.png"><img alt="../../../_images/leapsapi.png" class="align-right" src="/docs-assets/_images/leapsapi.png" style="width: 87.3px; height: 144.6px;"></a>
</div>
<div class="section" id="leaps-api">
<h2>LEAPS API</h2>
<ul class="simple">
<li><p>The LEAPS RTLS software stack provides APIs that allow easy configuration of the device to suit custom applications. It provides user with flexibility to tailor the system to their specific needs.</p></li>
<li><p>The API utilizes binary Type-Length-Value (TLV) frame format for external devices via UART, USB, SPI and BLE interfaces. When data centralization is used, the communication via MQTT using JSON is available for the high-level applications.</p></li>
<li><p>The API command line interface is supported via the UART, USB and BLE interfaces with more user-friendly and readable format.</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsmanager.png"><img alt="../../../_images/leapsmanager.png" class="align-right" src="/docs-assets/_images/leapsmanager.png" style="width: 101.7px; height: 119.1px;"></a>
</div>
<div class="section" id="leaps-manager">
<h2>LEAPS Manager</h2>
<p>LEAPS Manager is a mobile application that provides device discovery, device configuration, network configuration, network management and location visualization.</p>
<ul class="simple">
<li><p>The Demo Wizard allows an easy and fast way to configure the kit with the predefined demo setups.</p></li>
<li><p>The Grid in 2D and 3D provides real-time position updates and visualization of the devices in the network.</p></li>
<li><p>The communication with the devices is done via the BLE with support for up to 6 concurrent connections to maintain connection reliability.</p></li>
<li><p>When data centralization is used, communication with the LEAPS Server via MQTT is available, allowing management and visualization of the devices for the whole network.</p></li>
<li><p>Other useful features include device management, firmware update over BLE, Anchors auto-positioning, logging and debug console.</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsgateway.png"><img alt="../../../_images/leapsgateway.png" class="align-right" src="/docs-assets/_images/leapsgateway.png" style="width: 90.3px; height: 63.599999999999994px;"></a>
</div>
<div class="section" id="leaps-gateway">
<h2>LEAPS Gateway</h2>
<p>LEAPS Gateway serves as a gateway between the UWB subsystem and the TCP/IP networks.</p>
<ul class="simple">
<li><p>The LEAPS Gateway communicates on one side with the LEAPS UWBS via the generic LEAPS API over SPI or USB, and on the other side with the LEAPS Server via the TCP/IP.</p></li>
<li><p>Depending on the LEAPS UWB network profile, it provides a medium for transferring uplink and downlink location and telemetry data of the Anchors and Tags to and from the Leaps Server.</p></li>
<li><p>The interconnection with the UWBS is done via the SPI on a dedicated LEAPS Gateway embedded device. When the interconnection with the LEAPS UWBS is done via the USB, like in the case of the UDK devices, LEAPS Gateway runs on a Linux platform as a daemon service.</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsserver.png"><img alt="../../../_images/leapsserver.png" class="align-right" src="/docs-assets/_images/leapsserver.png" style="width: 77.1px; height: 63.599999999999994px;"></a>
</div>
<div class="section" id="leaps-server">
<h2>LEAPS Server</h2>
<p>LEAPS Server is a central data hub for the UWB network. It interconnects all the LEAPS Gateway devices with the world via a MQTT Broker.</p>
<ul class="simple">
<li><p>Functions as an uplink data concentrator, downlink data router, data processor, location engine, device management, device access control and ensures quality of service.</p></li>
<li><p>Communicates with the world via a connectors. Currently, the supported connector is MQTT, which includes support for AWS.</p></li>
<li><p>The LEAPS Server runs as a daemon service on the Linux platform.</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapscenter.png"><img alt="../../../_images/leapscenter.png" class="align-right" src="/docs-assets/_images/leapscenter.png" style="width: 85.5px; height: 121.0px;"></a>
</div>
<div class="section" id="leaps-center">
<h2>LEAPS Center</h2>
<p><a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> is a web application that provides device management, network management and visualization of location and telemetry data for the whole network.</p>
<ul class="simple">
<li><p>The Grid in 2D and 3D provides real-time position updates and visualization of the devices in the network.</p></li>
<li><p>Other useful features include User Management, Zone Management, Zone History, Floorplan Management, Position History and Position Heatmap.</p></li>
<li><p>The <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> communicates with the LEAPS Server via the MQTT. It runs as a service on Linux or Windows platforms.</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsbroker.png"><img alt="../../../_images/leapsbroker.png" class="align-right" src="/docs-assets/_images/leapsbroker.png" style="width: 93.3px; height: 51.9px;"></a>
</div>
<div class="section" id="mqtt-broker">
<h2>MQTT Broker</h2>
<p>An MQTT broker is a server that receives all messages from the clients and then routes the messages to the appropriate destination clients. An MQTT client is any device (from a microcontroller up to a fully-fledged server) running an MQTT library and connecting to an MQTT broker over a network.</p>
<hr class="docutils">
</div>
</div>


           </div>
