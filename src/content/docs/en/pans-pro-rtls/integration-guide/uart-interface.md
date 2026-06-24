---
title: "UART Interface"
lang: en
slug: "pans-pro-rtls/integration-guide/uart-interface"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/uart-interface/"
order: 95
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="uart-interface">
<span id="pans-uart-interface"></span><h1>UART Interface</h1>
<p>Users can use an external host device to connect to the DWM module through UART interface at a baud rate 115200. The figure below shows the workflow of the DWM1001 UART interface. In the UART Generic mode communication, the host device is acting as the initiator, while the DWM module is the responder. DWM1001 UART provides two modes: the UART Generic mode and the UART Shell mode. The default mode of the DWM1001 UART is Generic mode. However, the two modes are transferable.</p>
<p>Generic mode to Shell mode: press “Enter” twice or input two bytes [0x0D, 0x0D] within one second.</p>
<p>If the module is in a “sleep” state in low-power mode as introduced in <em>low-power mode wake-up mechanism</em>, an extra byte will be needed before the double “Enter”. For example, pressing“Enter” three times will wake the module and transfer it to Shell mode. Shell mode to Generic mode: users need to input the “quit” command.</p>
<blockquote>
<div><div class="figure align-default" id="id1">
<a class="reference internal image-reference" href="../../../_images/image91.png"><img alt="../../../_images/image91.png" src="/docs-assets/_images/image91.png" style="width: 5.70833in; height: 2.29167in;"></a>
<p class="caption"><span class="caption-text">UART workflow</span></p>
</div>
</div></blockquote>
<hr class="docutils">
<div class="section" id="uart-tlv-mode">
<h2>UART TLV Mode</h2>
<p>UART TLV mode uses TLV format data. In this mode, the host device and the DWM module communicate using TLV Requests/responses. A full TLV Request communication flow includes the following steps:</p>
<ol class="arabic simple">
<li><p>The host device sends TLV Request;</p></li>
<li><p>DWM1001 responds with TLV data.</p></li>
</ol>
<p>On receiving any data, the UART starts a delay timer for the following data. If new data comes in within a delay period, specifically 25 clock cycles (25/32768 second ≈ 763 μs), the UART starts the delay timer and waits for new data. The delay timer will expire if no new data comes in within the delay period. The UART then sends the received data to the Generic API thread and waits for it to return the response data or error message.</p>
<p>The DWM1001 UART TLV mode thread transfers between three states in serial: “UART: Idle”, “UART: Receiving”, and “UART: Finished”. Each state will transfer to its next corresponding state on certain events.</p>
<ul class="simple">
<li><p>UART: Idle: is the state after initialization and after each successful TLV response. In this state, the UART only expects one byte as the start of the TLV Request or the double “Enter” command.</p>
<ul>
<li><p>Waiting for an event: receiving TLV Requests.</p></li>
<li><p>Action on an event:</p>
<ul>
<li><p>Start the delay timer.</p></li>
<li><p>Transfer to UART: Receiving.</p></li>
</ul>
</li>
</ul>
</li>
<li><p>UART: Receiving: is the state waiting for the end of the incoming request. On receiving any data in this state, the UART will refresh the delay timer. If the host device has finished sending bytes, the delay timer will expire.</p>
<ul>
<li><p>Waiting for an event: delay period timed out.</p></li>
<li><p>Action on an event - if received request is double “Enter”:</p>
<ul>
<li><p>Transfer to the UART Shell mode.</p></li>
</ul>
</li>
<li><p>Action on an event - if received request is not double “Enter”:</p>
<ul>
<li><p>Send received request to the Generic API thread.</p></li>
<li><p>Transfer to UART: Finished.</p></li>
</ul>
</li>
</ul>
</li>
<li><p>UART: Finished: is the state waiting for the Generic API thread to parse the incoming request and send the response data or error message back to the UART thread.</p>
<ul>
<li><p>Waiting for event: call_back() function called by the Generic API thread.</p></li>
<li><p>Action on an event:</p>
<ul>
<li><p>Send the response data or error message to the host device.</p></li>
<li><p>Transfer to UART: Idle.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="uart-tlv-mode-communication">
<h2>UART TLV mode communication</h2>
<p>The UART communication in TLV mode is illustrated in the figure below:</p>
<ol class="arabic">
<li><p>The host device sends a request in TLV format;</p></li>
<li><p>The DWM module responds with a message in TLV format.</p>
<div class="figure align-default" id="id2">
<a class="reference internal image-reference" href="../../../_images/image10.png"><img alt="../../../_images/image10.png" src="/docs-assets/_images/image10.png" style="width: 4.875in; height: 3.03194in;"></a>
<p class="caption"><span class="caption-text">UART TLV communication</span></p>
</div>
</li>
</ol>
</div>
<hr class="docutils">
<div class="section" id="uart-tlv-mode-communication-example">
<h2>UART TLV mode communication example</h2>
<p>The figure below illustrates an example of the host device sending the <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a> command to set pin 13 level HIGH ([0x28, 0x02, 0x0D, 0x01] in byte array and receiving the response from the DWM module using the UART API in TLV mode. The steps of the communication flow are:</p>
<ol class="arabic simple">
<li><p>The host device sends the <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a> command in TLV format: Type = 0x28, Length = 0x02, Value = 0x0D 0x01.</p></li>
<li><p>The DWM module responds in TLV format: Type = 0x40, Length = 0x01, value = 0x00,</p></li>
</ol>
<p>Where Type = 0x40 indicates this is a return message, Length = 0x01 indicates that there is one byte following as data, and value = 0x00 indicates the TLV Request is parsed correctly.</p>
<div class="figure align-default" id="id3">
<a class="reference internal image-reference" href="../../../_images/image11.png"><img alt="../../../_images/image11.png" src="/docs-assets/_images/image11.png" style="width: 3.90694in; height: 2.71806in;"></a>
<p class="caption"><span class="caption-text">UART TLV communication example</span></p>
</div>
</div>
<hr class="docutils">
<div class="section" id="uart-shell-mode-communication">
<h2>UART Shell mode communication</h2>
<p>UART Shell mode provides a prompt and uses Shell commands. The UART Shell mode intends to provide users with human-readable access to the APIs. Thus, all Shell commands are strings of letters followed by a character return, i.e. “Enter”. Users can input the string directly through the keyboard and press “Enter” to send the Shell commands. DWM1001 UART stays in the Shell mode after each Shell command except for the “quit” command.</p>
<p>As illustrated in the figure below, a full Shell command communication flow includes the following steps:</p>
<ol class="arabic simple">
<li><p>The host device sends the Shell command + “Enter” to the DWM1001.</p></li>
<li><p>If there’s any message to respond, the DWM1001 sends the message to the host device.</p></li>
<li><p>If there’s nothing to respond, the DWM1001 doesn’t send anything and keeps quiet.</p></li>
</ol>
<div class="figure align-default" id="id4">
<a class="reference internal image-reference" href="../../../_images/image12.png"><img alt="../../../_images/image12.png" src="/docs-assets/_images/image12.png" style="width: 3.88472in; height: 2.32222in;"></a>
<p class="caption"><span class="caption-text">UART Shell mode communication</span></p>
</div>
</div>
<hr class="docutils">
<div class="section" id="uart-shell-mode-communication-example">
<h2>UART Shell Mode communication example</h2>
<p>The figure below illustrates an example of a host device sending the “GPIO set” command using UART Shell to set pin 13 level HIGH (“gs 13” in a byte array, followed by “Enter” key, detailed in <em>gs</em>). The steps of the communication flow are:</p>
<ol class="arabic simple">
<li><p>The host device sends the “GPIO set” command in Shell mode: “gs 13” + “Enter”.</p></li>
<li><p>The DWM1001 responds to the host with the string “gpio13: 1”.</p></li>
</ol>
<div class="figure align-default" id="id5">
<a class="reference internal image-reference" href="../../../_images/image13.png"><img alt="../../../_images/image13.png" src="/docs-assets/_images/image13.png" style="width: 3.5625in; height: 2.34444in;"></a>
<p class="caption"><span class="caption-text">UART Shell mode communication example</span></p>
</div>
</div>
<hr class="docutils">
<div class="section" id="low-power-mode-wake-up-mechanism">
<h2>low-power mode wake-up mechanism</h2>
<p>As provided in the PANS library, the DWM module can work in a low-power mode. In the low-power mode, the module puts the API-related
threads into a “sleep” state when host devices do not communicate the API . In this case, the host device needs to
wake the module through external interfaces before the real communication can start.</p>
<p>For the UART interface, the host device needs to send a single byte first to wake up the module.</p>
<p>After the API transmission has finished, the host device needs to put the module back to “sleep” state to save power, as introduced in
<a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-sleep#dwm-sleep"><span class="std std-ref">dwm_sleep</span></a> and shell command <em>quit</em>.</p>
</div>
<hr class="docutils">
<div class="section" id="uart-wakeup">
<h2>UART wakeup</h2>
<p>If DWM sleeps (in low-power mode), the wakeup procedure has to be executed before SPI/UART starts accepting commands. At least one byte has to be sent on the UART interface to wake up from sleep (only in low-power mode).</p>
</div>
</div>


           </div>
