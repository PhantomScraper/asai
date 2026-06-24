---
title: "SPI Interface"
lang: en
slug: "pans-pro-rtls/integration-guide/spi-interface"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/spi-interface/"
order: 96
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="spi-interface">
<span id="pans-spi-interface"></span><h1>SPI Interface</h1>
<p>DWM1001 SPI interface uses TLV format data. Users can use an external
host device in SPI master mode to connect to the DWM module SPI
interface, which operates in slave mode. The maximum SPI clock
frequency is 8 MHz. (This is maximum supported by the MCU) In the
DWM1001 SPI schemes, the host device communicates with the DWM1001
through TLV Requests. A full TLV Request communication flow includes
the following steps:</p>
<ol class="arabic simple">
<li><p>The host device sends TLV Request;</p></li>
<li><p>The DWM1001 prepares response;</p></li>
<li><p>The host device reads the SIZE (length of each response) and NUM (number of transfers);</p></li>
<li><p>The host device reads data response;</p></li>
</ol>
<p>Because SPI uses full duplex communication, when the host device (as
the SPI master) writes x bytes, it sends x bytes to the DWM
module (as the slave) and receives x bytes dummy at the same time.
Similar to reading, the host device sends x bytes of dummy and
receives x bytes of data as a response. In the DWM1001 SPI scheme,
the dummy bytes are octets of value 0xFF.</p>
<blockquote>
<div><div class="figure align-default" id="id1">
<a class="reference internal image-reference" href="../../../_images/image41.png"><img alt="../../../_images/image41.png" src="/docs-assets/_images/image41.png" style="width: 5.66667in; height: 2.84444in;"></a>
<p class="caption"><span class="caption-text">SPI workflow</span></p>
</div>
</div></blockquote>
<p>As shown in the figure above, the DWM1001 SPI thread transfers between four states in serial.</p>
<p>Each state will transfer to its next corresponding state on certain events.</p>
<ul>
<li><p>SPI: Idle: the state after initialization and after each successful data transmission/response. Any received data is assumed to be a TLV Request in this state. Thus, on receiving any data, the SPI thread in the firmware passes the received data to the Generic API. The Generic API parses the TLV Requests and prepares the return data.</p>
<blockquote>
<div><ul class="simple">
<li><p>Waiting for an event: receiving TLV Requests.</p></li>
<li><p>Action on an event – if Type == 0xFF:</p></li>
</ul>
</div></blockquote>
</li>
</ul>
<ul>
<li><p>SPI: Wait for call_back: the DWM1001 SPI waits for the Generic API to parse the TLV Request and prepare the response. Any data from the host side will be ignored and returned with 0x00 in this state.</p>
<blockquote>
<div><ul>
<li><p>Waiting for an event: call_back() function is called by the Generic API.</p></li>
<li><p>Action on an event:</p>
<blockquote>
<div><ul class="simple">
<li><p>Toggle Data-Ready GPIO pin HIGH – detailed in <em>SPI Scheme: TLV communication using Data-Ready GPIO pin</em>.</p></li>
<li><p>Transfer to “SPI: Wait for READ SIZE/NUM”.</p></li>
</ul>
</div></blockquote>
</li>
</ul>
</div></blockquote>
</li>
<li><p>SPI: Wait for Read SIZE/NUM: the DWM1001 SPI has prepared the SIZE byte as a response, and there will be NUM of transfers. SIZE and NUM are a total of 2-byte non-zero data, namely SIZE/NUM. They indicated the total number (i.e. SIZE*NUM bytes) of data or error messages to be responded. The DWM1001 SPI, as a slave, is waiting for the host device to read the SIZE/NUM bytes.</p>
<blockquote>
<div><ul>
<li><p>Waiting for an event: the host device reads two bytes.</p></li>
<li><p>Action on an event:</p>
<blockquote>
<div><ul class="simple">
<li><p>Respond with the SIZE/NUM bytes.</p></li>
<li><p>Transfer to “SPI: Wait for READ DATA/ERR”.</p></li>
</ul>
</div></blockquote>
</li>
</ul>
</div></blockquote>
</li>
</ul>
<ul>
<li><p>SPI: Wait for Read DATA/ERR: The DWM1001 SPI has prepared SIZE bytes of data or error messages for each of the NUM transfers as a response to the TLV Request and is waiting for the host device to read it.</p>
<blockquote>
<div><ul class="simple">
<li><p>Waiting for an event: the host device does NUM transfers. Each transfer should be SIZE bytes. Otherwise, data maybe lost.</p></li>
<li><p>Action on an event:</p>
<ul>
<li><p>Respond with DATA/ERR.</p></li>
<li><p>Toggle Data-Ready GPIO pin LOW – detailed in <em>SPI Scheme: TLV communication using Data-Ready GPIO pin</em>. Transfer to “SPI: Idle”.</p></li>
</ul>
</li>
</ul>
</div></blockquote>
</li>
</ul>
<p>In DWM1001, starting from “SPI: Idle”, traversing all four states listed above and returning to “SPI:
Idle” indicates a full TLV Request communication flow. The user should have received the response data or error message by the end of the communication flow.</p>
<p>A few different usages and examples are illustrated in the following subsections.</p>
<hr class="docutils">
<div class="section" id="spi-tlv-communication-using-polling">
<h2>SPI TLV communication using polling</h2>
<p>The figure below shows the normal communication flow of a host device writing/reading information to/from the DWM module:</p>
<ol class="arabic simple">
<li><p>The host device sends the request in TLV format.</p></li>
<li><p>The host device reads the SIZE/NUM bytes, indicating the number of transfers to be done and the number of bytes ready to be read in each transfer.</p></li>
</ol>
<ol class="arabic simple" start="3">
<li><p>The host device reads SIZE bytes data response in TLV format.</p></li>
</ol>
<div class="figure align-default" id="id2">
<a class="reference internal image-reference" href="../../../_images/image51.png"><img alt="../../../_images/image51.png" src="/docs-assets/_images/image51.png" style="width: 5.70833in; height: 3.29167in;"></a>
<p class="caption"><span class="caption-text">SPI TLV communication using polling</span></p>
</div>
<div class="line-block">
<div class="line">The figure below illustrates an example of host device writing the <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a> TLV Request to set pin 13 level HIGH ([0x28, 0x02, 0x0D, 0x01] in byte array and reading the response from the DWM module.</div>
<div class="line">The communication flow of the transmission and response includes:</div>
</div>
<blockquote>
<div><ol class="arabic simple">
<li><p>The host device writes the <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a> command to set pin 13 level HIGH in TLV format, 4 bytes in total: Type = 0x28, length = 0x02, value = 0x0D 0x01.</p></li>
</ol>
</div></blockquote>
</div>
<hr class="docutils">
<div class="section" id="spi-tlv-communication-using-data-ready-gpio-pin">
<h2>SPI TLV communication using Data-Ready GPIO pin</h2>
<p>Users can set up the interrupt Data-Ready GPIO pin (GPIO P0.26) from the DWM1001 to indicate when data is ready, instead of the master polling multiple times to check the response status. When the Data-Ready function is set up, the Data-Ready GPIO pin will be set to LOW level when there’s no data to be read; when the response SIZE/NUM and data are ready to be read, the Data-Ready GPIO pin will be set to HIGH level during states “SPI: Wait for Read SIZE/NUM” and “SPI: Wait for Read DATA/ERR”. Thus, the users can use the Data-Ready GPIO pin as an interrupt or a status pin.</p>
<p>To set up Data-Ready GPIO pin for the SPI scheme, users need to use dwm_int_cfg TLV Request through SPI Scheme: normal TLV communication introduced in <em>SPI TLV communication using polling</em>.</p>
<p>The communication flow of this scheme is illustrated in the figure below.</p>
<ol class="arabic">
<li><p>Set up the SPI interrupt.</p></li>
<li><p>The host device writes the request in TLV format.</p></li>
<li><p>The host device waits until the Data-Ready GPIO pin on DWM1001 to go HIGH.</p></li>
<li><p>The host device reads the SIZE/NUM bytes.</p></li>
<li><p>The host device reads the SIZE bytes data response in TLV format in each transfer for NUM times.</p>
<div class="figure align-default" id="id3">
<a class="reference internal image-reference" href="../../../_images/image71.png"><img alt="../../../_images/image71.png" src="/docs-assets/_images/image71.png" style="width: 5.70833in; height: 4.34444in;"></a>
<p class="caption"><span class="caption-text">SPI TLV communication using Data-Ready GPIO pin</span></p>
</div>
</li>
</ol>
<p>As can be seen from the steps, this scheme uses the Data-Ready GPIO pin on the DWM1001 to indicate the host device when the response data is ready. This makes the host device less busy in reading SIZE byte.</p>
</div>
<hr class="docutils">
<div class="section" id="spi-partial-transmission">
<h2>SPI partial transmission</h2>
<p>When reading data from the DWM module, if the host device doesn’t read all bytes of data in one transmission, the reading operation will still be considered done. The rest of the response will be abandoned. For example, in the “SPI: Wait for Read DATA/ERR” state, the DWM module has prepared SIZE bytes of response data and expects the host device to read all SIZE bytes of the response. However, if the host device only reads part of the data, the DWM module will drop the rest and transfer to the next state: “SPI: IDLE”.</p>
</div>
<hr class="docutils">
<div class="section" id="spi-error-recovery-mechanism">
<h2>SPI error recovery mechanism</h2>
<p>The DWM1001 SPI has a special type value 0xFF, called type_nop. A TLV data message with type_nop means no operation. In the “SPI: IDLE” state, when the DWM1001 SPI receives a message and finds the type byte is 0xFF, it will not perform any operation, including sending the TLV data message to the Generic API thread.</p>
<p>The type_nop is designed for error recovery. If the host device is not sure what state the DWM1001 SPI is in, it can make use of the SPI response and the non-partial transmission mechanism and reset the DWM1001 SPI to “SPI: IDLE” state by sending three 0xFF dummy bytes, each in a single transmission. After the three transmissions, the response data from the DWM1001 SPI will become all dummy bytes of value 0xFF, indicating that the DWM1001 SPI is in the “SPI: IDLE” state.</p>
</div>
<hr class="docutils">
<div class="section" id="low-power-mode-wake-up-mechanism">
<h2>Low-power mode wake-up mechanism</h2>
<p>As provided in the PANS library, the DWM module can work in a low-power mode. In the low-power mode, the module puts the API-related
threads into a “sleep” state when host devices do not communicate the API . In this case, the host device needs to
wake the module through external interfaces before the real communication can start.</p>
<p>For the SPI interface, putting the chip select pin to low level wake ups up the module, i.e. no extra transmission is needed.</p>
<p>After the API transmission has finished, the host device needs to put the module back to “sleep” state to save power, as introduced in
<a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-sleep#dwm-sleep"><span class="std std-ref">dwm_sleep</span></a> and shell command <em>quit</em>.</p>
</div>
<hr class="docutils">
<div class="section" id="spi-wakeup">
<h2>SPI wakeup</h2>
<p>If DWM sleeps (in low-power mode), the wakeup procedure has to be executed before SPI starts accepting commands. At least a 35 microseconds wide pulse has to be generated on the CS pin of the SPI to  wake up from sleep (only in low-power mode).</p>
</div>
</div>


           </div>
