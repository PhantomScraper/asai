---
title: "PANS PRO API"
lang: en
slug: "pans-pro-rtls/integration-guide/pans-pro-api"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/pans-pro-api/"
order: 93
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-api">
<span id="id1"></span><h1>PANS PRO API</h1>
<p>This guide specifies the public application interface of the DWM module based on Decawave’s DW1000 IC.
The API essentially is a set of functions providing a means to communicate with the MCU to drive the module through
the library on application level without having to deal with the details of accessing the DW1000 IC part and
other peripherals directly through its SPI/I2C interface register set.The DW1000 IC part, which has the UWB
physical layer defined in IEEE 802.15.4-2011 standard, acts as the UWB radio module controlled by the
module’s MCU. The module presents multiple interfaces for users to interact with the
system. These include the UART and SPI hardware interfaces and the BLE
interface, usable via a smartphone application.</p>
<p><strong>API and its guide</strong></p>
<p>Set of API functions may be accessed through various communication interfaces providing flexibility to developers in
using the module and integrating it into their systems. The API accesses mainly come in two types:</p>
<blockquote>
<div><ol class="arabic simple">
<li><p>External access API: via UART, SPI and BLE.</p></li>
<li><p>Integrated access API: via onboard user app (C code).</p></li>
</ol>
</div></blockquote>
<p>Among the above API interfaces:</p>
<blockquote>
<div><ol class="arabic simple">
<li><p>The UART (Generic), the SPI and the onboard APIs are introduced in the section <em>API</em> <em>commands</em>.</p></li>
<li><p>The UART (Shell) APIs are introduced in the section <em>Shell commands</em>.</p></li>
<li><p>The BLE APIs are introduced in the section <em>TLV type list</em>.</p></li>
</ol>
</div></blockquote>
<p>Following pages specify the PANS API functions themselves, providing descriptions of each API functions in detail in terms of its parameters, functionality and utility.</p>
<p>Users can use the API to configure each individual module.</p>
<hr class="docutils">
<p>Following subsections will show each kind of supported API</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/tlv-api">TLV API</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api">Shell API</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/mqtt-api">MQTT API</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/supported-intefaces">Supported Interfaces</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-limitation">API Limitations</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-operation">API Operation</a></li>
</ul>
</div>
</div>


           </div>
