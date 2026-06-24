---
title: "Hardware Interfaces"
lang: en
slug: "udk/udk-start/device-hw-interfaces"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/udk-start/device-hw-interfaces/"
order: 35
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="hardware-interfaces">
<span id="hardware-interface"></span><h1>Hardware Interfaces</h1>
<p>Before proceeding with the demos, it is essential to get familiar with the hardware interface, particularly focusing on the <span class="red-text">buttons A, B, and C</span>, the <span class="red-text">2 USB-C ports</span>, the <span class="red-text">front RGB LEDs</span> and the <span class="green-text">two side GREEN LEDs</span>. Understanding these elements will significantly help you in setting up each demonstration effectively.</p>
<hr class="docutils">
<blockquote id="uihwinterfaces">
<div><a class="reference internal image-reference" href="../../../_images/for-buttons.png"><img alt="../../../_images/for-buttons.png" class="align-right" src="/docs-assets/_images/for-buttons.png" style="width: 260.0px; height: 226.3px;"></a>
</div></blockquote>
<p><strong>Buttons, LEDs and user interaction</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>Button A: Power ON/OFF button (long-press).</p>
<ul>
<li><p><span class="green-text">GREEN LED</span>: Power status</p></li>
</ul>
</li>
<li><p>Button B: Switch between Qorvo NI / UCI and LEAPS UWBS modes (long-press).</p>
<ul>
<li><p><span class="green-text">GREEN LED</span>: UWB status</p></li>
</ul>
</li>
<li><p>Button C: N/A (for future use).</p>
<ul>
<li><p>RGB LEDs: indicates device mode during the power on.</p>
<ul>
<li><p><span class="red-text">RED</span> is LEAPS UWBS</p></li>
<li><p><span class="blue-text">BLUE</span> is Qorvo NI</p></li>
<li><p><span class="green-text">GREEN</span> is Qorvo UCI</p></li>
</ul>
</li>
</ul>
</li>
<li><p>A buzzer: used for alarm.</p></li>
<li><p>A haptic motor: used for alarm.</p></li>
</ul>
</div></blockquote>
<hr class="docutils">
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/for-usb-type-c.png"><img alt="../../../_images/for-usb-type-c.png" class="align-right" src="/docs-assets/_images/for-usb-type-c.png" style="width: 275.44px; height: 259.16px;"></a>
</div></blockquote>
<p><strong>Data interfaces</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>USB-C Data Port 1: USB command line and binary API.</p></li>
<li><p>USB-C Data Port 2: DAPLink + USB/UART command line and binary API.</p></li>
<li><p>Integrated UWB antenna.</p></li>
<li><p>Integrated Bluetooth antenna.</p></li>
</ul>
</div></blockquote>
<hr class="docutils">
<p><strong>Development interfaces</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>Integrated DAPLink with SWD Debugger and USB/UART converter: used for programming, debugging purposes and for device configuration.</p></li>
<li><p>6-pin Tag Connect compatible connector for external J-Link debugger.</p></li>
<li><p>PCB jumper pads: SWD_RST, SWD_DIO, SWD_CLK, DBG_TXD, DBG_RXD.</p></li>
<li><p>GPIOs: J11 (P0.21, P0.24, DW_GP0, DW_GP1, DW_GP2, DW_GP3, DW_GP4, DW_GP5, DW_GP6), J12 (P0.11, P0.12, P0.13, P0.14, P0.29, P0.31, P1.14, P1.07).</p></li>
<li><p>NFC antenna pads: P0.09/NFC1, P0.10/NFC2.</p></li>
<li><p>3.7V battery connector.</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/lc14_b2-top-view.png"><img alt="../../../_images/lc14_b2-top-view.png" class="align-center" src="/docs-assets/_images/lc14_b2-top-view.png" style="width: 452.5px; height: 561.5px;"></a>
</div></blockquote>
<hr class="docutils">
<p><strong>Port Pin Mapping</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 51%">
<col style="width: 24%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Alternative Function</p></th>
<th class="head"><p><a class="reference internal" href="/docs/en/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a></p></th>
<th class="head"><p><a class="reference internal" href="/docs/en/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UART TX</p></td>
<td><p>P1.13</p></td>
<td><p>P1.13</p></td>
</tr>
<tr class="row-odd"><td><p>UART RX</p></td>
<td><p>P1.15</p></td>
<td><p>P1.15</p></td>
</tr>
<tr class="row-even"><td><p>UWB SPI CS</p></td>
<td><p>P0.20</p></td>
<td><p>P0.20</p></td>
</tr>
<tr class="row-odd"><td><p>UWB SPI CLK</p></td>
<td><p>P0.16</p></td>
<td><p>P0.16</p></td>
</tr>
<tr class="row-even"><td><p>UWB SPI SDO</p></td>
<td><p>P0.17</p></td>
<td><p>P0.17</p></td>
</tr>
<tr class="row-odd"><td><p>UWB SPI SDI</p></td>
<td><p>P0.23</p></td>
<td><p>P0.23</p></td>
</tr>
<tr class="row-even"><td><p>UWB IRQ</p></td>
<td><p>P0.25</p></td>
<td><p>P0.25</p></td>
</tr>
<tr class="row-odd"><td><p>UWB RESET</p></td>
<td><p>P0.15</p></td>
<td><p>P0.15</p></td>
</tr>
<tr class="row-even"><td><p>LED RED</p></td>
<td><p>P0.27</p></td>
<td><p>P0.27</p></td>
</tr>
<tr class="row-odd"><td><p>LED BLUE</p></td>
<td><p>P0.4</p></td>
<td><p>P0.4</p></td>
</tr>
<tr class="row-even"><td><p>LED GREEN</p></td>
<td><p>P0.5</p></td>
<td><p>P0.5</p></td>
</tr>
<tr class="row-odd"><td><p>LED EXTERNAL 0</p></td>
<td><p>P1.12</p></td>
<td><p>P1.12</p></td>
</tr>
<tr class="row-even"><td><p>LED EXTERNAL 1</p></td>
<td><p>P0.30</p></td>
<td><p>P0.30</p></td>
</tr>
<tr class="row-odd"><td><p>BUTTON MAIN</p></td>
<td><p>P0.26</p></td>
<td><p>P0.26</p></td>
</tr>
<tr class="row-even"><td><p>BUTTON EXTERNAL 0</p></td>
<td><p>P1.11</p></td>
<td><p>P1.11</p></td>
</tr>
<tr class="row-odd"><td><p>BUTTON EXTERNAL 1</p></td>
<td><p>P0.28</p></td>
<td><p>P0.28</p></td>
</tr>
<tr class="row-even"><td><p>ACC I2C SDA</p></td>
<td><p>P0.22</p></td>
<td><p>P0.22</p></td>
</tr>
<tr class="row-odd"><td><p>ACC I2C SCL</p></td>
<td><p>P0.19</p></td>
<td><p>P0.19</p></td>
</tr>
<tr class="row-even"><td><p>ACC IRQ</p></td>
<td><p>P1.1</p></td>
<td><p>P1.1</p></td>
</tr>
<tr class="row-odd"><td><p>BUZZER</p></td>
<td><p>P0.2</p></td>
<td><p>P0.2</p></td>
</tr>
<tr class="row-even"><td><p>MOTOR</p></td>
<td><p>P1.10</p></td>
<td><p>P1.10</p></td>
</tr>
<tr class="row-odd"><td><p>BATTERY ADC PIN</p></td>
<td><p>P0.3</p></td>
<td><p>P0.3</p></td>
</tr>
<tr class="row-even"><td><p>DCDC3V3 CONTROL PIN</p></td>
<td><p>N/A</p></td>
<td><p>N/A</p></td>
</tr>
<tr class="row-odd"><td><p>CHARGER STATUS PIN</p></td>
<td><p>N/A</p></td>
<td><p>N/A</p></td>
</tr>
<tr class="row-even"><td><p>USB DETECTOR PIN</p></td>
<td><p>P1.9</p></td>
<td><p>N/A</p></td>
</tr>
<tr class="row-odd"><td><p>API SPI CS</p></td>
<td><p>P0.29</p></td>
<td><p>P0.12</p></td>
</tr>
<tr class="row-even"><td><p>API SPI CLK</p></td>
<td><p>P0.12</p></td>
<td><p>P0.11</p></td>
</tr>
<tr class="row-odd"><td><p>API SPI SDO</p></td>
<td><p>P0.11</p></td>
<td><p>P0.14</p></td>
</tr>
<tr class="row-even"><td><p>API SPI SDI</p></td>
<td><p>P0.14</p></td>
<td><p>P0.31</p></td>
</tr>
<tr class="row-odd"><td><p>API IRQ</p></td>
<td><p>P0.31</p></td>
<td><p>P0.29</p></td>
</tr>
</tbody>
</table>
</div>


           </div>
