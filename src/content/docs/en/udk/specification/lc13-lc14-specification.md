---
title: "LC13 and LC14 Specifications"
lang: en
slug: "udk/specification/lc13-lc14-specification"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/specification/lc13-lc14-specification/"
order: 54
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="lc13-and-lc14-specifications">
<h1>LC13 and LC14 Specifications</h1>
<hr class="docutils">
<div class="section" id="overview">
<h2>Overview</h2>
<p>This section provides technical details of the LC13 and LC14 devices. The LC13/LC14 devices can be used to create an Anchor Node (AN), Anchor Initiator Node (ANI), Tag Node (TN) and Gateway for a Real-Time Location System (RTLS). It is also compatible with FiRa Nearby Interaction and Two-Way Ranging Angle-of-Arrival (TWR-AoA) demo. Furthermore, this open platform can be used for developing UWB or Bluetooth applications.</p>
</div>
<hr class="docutils">
<div class="section" id="key-features">
<h2>Key Features</h2>
<ul class="simple">
<li><p>Based on Murata 2AB SIP (MCU nRF52840 with Bluetooth, UWB QM33120W IC, LIS2DW accelerometer, crystals and internal power regulators).</p></li>
<li><p>Qorvo QM33120W - Ultra Wideband (UWB):</p>
<ul>
<li><p>Based on the IEEE802.15.4z standard and implements enhanced security features.</p></li>
<li><p>Supports both channel 5 (6.5 GHz) and channel 9 (8 GHz) with UWB RF compliance compatible with FCC, Japan’s ARIB, ETSI and +10dB ETSI of the CE.</p></li>
<li><p>Integrates Low Noise Amplifier (LNA) and Power Amplifier (PA) to increase the UWB range (up to 150m).</p></li>
<li><p>With integrated non-AoA (LC14) and AoA antennas (LC13).</p></li>
<li><p>FiRa™ PHY and MAC compatible. Interoperable with the Apple U1 chip and Android FiRa compatible smart devices.</p></li>
<li><p>Backward compatibility with DW1000 IEEE802.15.4a UWB IC on channel 5.</p></li>
</ul>
</li>
<li><p>Supports Two-Way Ranging (TWR), Time Difference of Arrival (TDoA) and Phase Difference of Arrival (PDoA).</p></li>
<li><p>Nordic Semiconductor nRF52840 - Bluetooth® Low-Energy (BLE) 5.3 RF Technology with an integrated antenna.</p></li>
<li><p>Supports NFC tag antenna connector.</p></li>
<li><p>2 USB C ports integrate a DAPLink programmer with Virtual COM and a USB device interface for data communication.</p></li>
<li><p>Alternatively, J-Link can be used via an onboard 6-pin Tag Connect compatible connector.</p></li>
<li><p>It contains RGB LEDs, 2x <span class="green-text">GREEN</span> LEDs, a front button, two side buttons, a USB connector for a nRF52 USB device, a buzzer, a haptic motor and extra GPIOs for connection with external sensors or IOs.</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Please kindly refer to the <a class="reference external" href="https://www.murata.com/en-global/products/connectivitymodule/ultra-wide-band/qorvo">Murata 2AB module</a> and <a class="reference external" href="https://www.qorvo.com/products/wireless-connectivity/ultra-wideband">Qorvo DW3000 IC</a> pages for additional details.</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="software-compatibility">
<h2>Software Compatibility</h2>
<p>It is compatible with LEAPS UWBS, Qorvo FiRa compatible UWBS (Nearby Interaction, TWR AoA), PANS PRO UWBS and third-party stack (open platform). The default firmware is LEAPS UWBS with Qorvo FiRa compatible demos supplied from the production.</p>
</div>
<hr class="docutils">
<div class="section" id="electrical-parameters">
<h2>Electrical Parameters</h2>
<table class="colwidths-given custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 65%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Parameter</p></th>
<th class="head"><p>Value</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Battery power supply</p></td>
<td><p>+3.7V (Battery not included in the kit. Fenix RCR123A is recommended)</p></td>
</tr>
<tr class="row-odd"><td><p>USB C (power and data)</p></td>
<td><p>5V @ 500mA max</p></td>
</tr>
<tr class="row-even"><td><p>Operating temperature (without battery)</p></td>
<td><p>-40°C - +85°C</p></td>
</tr>
<tr class="row-odd"><td><p>Operating temperature (with battery)</p></td>
<td><p>-20°C - +45°C</p></td>
</tr>
<tr class="row-even"><td><p>UWB supported channels</p></td>
<td><div class="line-block">
<div class="line">Channel 5 (6240–6739.2 MHz, CF=6489.6 MHz)</div>
<div class="line">Channel 9 (7738–8237.2 MHz, CF=7987.2 MHz, FiRa compatible)</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>UWB transmit powers</p></td>
<td><div class="line-block">
<div class="line">FCC/ARIB/ETSI: -41.3 dBm/MHz max</div>
<div class="line">ETSI (+10 dB): -31.3 dBm/MHz max</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>Target Accuracy</p></td>
<td><div class="line-block">
<div class="line">Ranging accuracy: +/- 9 [cm]</div>
<div class="line">PDoA accuracy: +/- 5 [deg]</div>
<div class="line">AoA accuracy: +/- 2.5 [deg]</div>
</div>
</td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul class="simple">
<li><p>To achieve the lowest power consumption, please cut the SWD_DIO jumper. The sleep current would be around 24uA @ 3.7V. When not cut, the sleep current would be around 270uA @ 3.7V.</p></li>
<li><p>To be able to use the external Jlink, please cut the SWD_DIO jumper.</p></li>
<li><p>The other jumpers can stay untouched.</p></li>
</ul>
</div>
</div>
<hr class="docutils">
<div class="section" id="mechanical-parameters">
<h2>Mechanical Parameters</h2>
<table class="colwidths-given custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 65%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Parameter</p></th>
<th class="head"><p>Value</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Size</p></td>
<td><p>W=72 x H=120 x D=30 mm</p></td>
</tr>
<tr class="row-odd"><td><p>Weight</p></td>
<td><div class="line-block">
<div class="line">Without battery: 82g</div>
<div class="line">With battery: 101g</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>Color</p></td>
<td><p>LC13 - Gray, LC14 - White</p></td>
</tr>
<tr class="row-odd"><td><p>Mounting</p></td>
<td><p>Compatible with 1/4”-20 screw camera mount</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="device-overview">
<h2>Device Overview</h2>
<p>The following pictures give an overview of the main components of the LC13 and LC14 devices.</p>
<p><strong>Front/Back view of the LC14 device</strong></p>
<p><a class="reference internal" href="../../../_images/for-buttons.png"><img alt="pic3" src="/docs-assets/_images/for-buttons.png" style="width: 47%;"></a>   <a class="reference internal" href="../../../_images/for-usb-type-c.png"><img alt="pic4" src="/docs-assets/_images/for-usb-type-c.png" style="width: 44%;"></a></p>
<hr class="docutils">
<p><strong>Front/Back view of the LC13 device</strong></p>
<a class="reference internal image-reference" href="../../../_images/lc13_device.png"><img alt="../../../_images/lc13_device.png" class="align-center" src="/docs-assets/_images/lc13_device.png" style="width: 477.90000000000003px; height: 389.7px;"></a>
<hr class="docutils">
<p><strong>Top view of the board</strong></p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/lc14_b2-top-view.png"><img alt="pic1" src="/docs-assets/_images/lc14_b2-top-view.png" style="width: 100%;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/lc13_b2-top-view.png"><img alt="pic2" src="/docs-assets/_images/lc13_b2-top-view.png" style="width: 93%;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="safety-instructions">
<h2>Safety Instructions</h2>
<ul class="simple">
<li><p>Do not expose the device to water or moisture whilst in operation.</p></li>
<li><p>Do not expose the device to heat from any source.</p></li>
<li><p>Take care whilst handling to avoid mechanical or electrical damage to the product.</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="warnings">
<h2>Warnings</h2>
<ul class="simple">
<li><p>This device should only be connected to an external power supply rated at 5V/0.5A DC or a 3.7V battery.</p></li>
<li><p>Replacement of a battery with an incorrect type can defeat a safeguard (for example, in the case of some lithium battery types).</p></li>
<li><p>Disposal of a battery into fire or a hot oven, or mechanically crushing or cutting of a battery, which can result in an explosion.</p></li>
<li><p>Leaving a battery in an extremely high temperature surrounding environment can result in an explosion or the leakage of flammable liquid or gas.</p></li>
<li><p>A battery subjected to extremely low air pressure may result in an explosion or the leakage of flammable liquid or gas.</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="important-notice">
<h2>Important Notice</h2>
<ul class="simple">
<li><p>The hardware and software of the kit are intended for demonstration purposes only. To obtain an industrial-grade system, please kindly contact us to discuss the specific needs and requirements.</p></li>
<li><p>For more detailed information on Qorvo software tools, such as Qorvo’s FiRa compatible stack, Qorvo Nearby Interaction and UWB Ranging &amp; AoA Demo Application, please refer to the appropriate documentation or resources that are available at <a class="reference external" href="https://www.qorvo.com">Qorvo’s website</a>.</p></li>
</ul>
<hr class="docutils">
</div>
</div>


           </div>
