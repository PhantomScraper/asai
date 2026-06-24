---
title: "LEAPS API"
lang: en
slug: "leaps-rtls/integration-guide/leaps-api"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/leaps-api/"
order: 67
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-api">
<span id="leapsapi"></span><h1>LEAPS API</h1>
<hr class="docutils">
<p>With <a class="reference external" href="https://www.leapslabs.com/">LEAPS</a> API, users have several options to interact and to control the <a class="reference external" href="https://www.leapslabs.com/">LEAPS</a> devices.</p>
<ul class="simple">
<li><p>The <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/tlv-api#leaps-tlv-api"><span class="std std-ref">TLV API</span></a> section provides guideline to <strong>binary</strong> TLV commands.</p></li>
<li><p>The <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/shell-api#leaps-shell-api"><span class="std std-ref">Shell API</span></a> section describes <strong>human-readable</strong> command-line interface commands.</p></li>
<li><p>The <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/mqtt-api#leaps-mqtt-api"><span class="std std-ref">MQTT API</span></a> section describes MQTT <strong>messages</strong>.</p></li>
</ul>
<p><a class="reference external" href="https://www.leapslabs.com/">LEAPS</a> device supports communication over multiple interfaces. Refer to <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/supported-interfaces#leaps-api-interfaces"><span class="std std-ref">list of supported interfaces</span></a> for details.</p>
<div class="toctree-wrapper compound">
</div>
<div class="section" id="leaps-com-tool">
<h2>LEAPS-COM tool</h2>
<p>To facilitate communication with LEAPS devices over multiple interfaces, a command-line tool
called <strong>leapscom</strong> is provided. This tool supports both network commissioning and diagnostic
operations. It streamlines the setup process by allowing automated command execution across
multiple devices, facilitates device discovery, and also automates firmware updates.
The <strong>leapscom</strong> supports Python 3.6 and above.</p>
<dl class="simple">
<dt><strong>List of features</strong></dt><dd><ul class="simple">
<li><p>Firmware updates can be performed concurrently on multiple devices.</p></li>
<li><p>Supports concurrent execution of commands over the Shell or TLV API.</p></li>
<li><p>Allows execution of predefined commands from a configuration file.</p></li>
<li><p>Enables automatic discovery of connected devices.</p></li>
<li><p>Supports uploading X.509 certificates and private key to devices with Ethernet or Wi-Fi interface for secure provisioning or authentication.</p></li>
<li><p>Supports multiple communication interfaces, including USB, BLE, and serial port.</p></li>
</ul>
</dd>
</dl>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/leaps-com/how-to-install">How to install ?</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/leaps-com/cmd-execution">Concurrent command execution</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/leaps-com/fw-update">Firmware update</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/leaps-com/cert-update">Certificate update</a></li>
</ul>
</div>
</div>
</div>


           </div>
