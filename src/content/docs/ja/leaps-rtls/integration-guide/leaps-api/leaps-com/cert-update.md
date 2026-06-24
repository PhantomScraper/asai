---
title: "Certificate update"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/leaps-com/cert-update"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/leaps-com/cert-update/"
order: 120
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="certificate-update">
<h1>Certificate update</h1>
<p><strong>Leapscom</strong> supports update of the X.509 certificates and the private key over USB, BLE or serial port interface.
Refer to <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cert-update-start#leaps-cert-update-start"><span class="std std-ref">leaps_cert_update_start</span></a> for more details on the update over <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/tlv-api#leaps-tlv-api"><span class="std std-ref">TLV API</span></a>.
Only devices with Ethernet or Wi-Fi interface make use of the certificates when TLS is enabled.</p>
<p>You can update one or multiple devices simultaneously and you can update only certain certificate if needed.</p>
<p>Certificate updates can only be performed using interfaces that support the TLV API.
Leapscom does not support running certificate updates together with custom command execution or firmware update simultaneously.
Therefore, the options --ca, --cert and --key cannot be used together with --main, --eldr, --cfg, --tlv, or --shell.</p>
<p><strong>Options</strong></p>
<dl class="std option">
<dt class="sig sig-object std" id="cmdoption-ca">
<span class="sig-name descname"><span class="pre">--ca</span></span><span class="sig-prename descclassname"> <span class="pre">DER_FILE</span></span></dt>
<dd><p>Path to the CA certificate file in DER (.der) format.</p>
</dd></dl>

<dl class="std option">
<dt class="sig sig-object std" id="cmdoption-cert">
<span class="sig-name descname"><span class="pre">--cert</span></span><span class="sig-prename descclassname"> <span class="pre">DER_FILE</span></span></dt>
<dd><p>Path to the client certificate file in DER (.der) format.</p>
</dd></dl>

<dl class="std option">
<dt class="sig sig-object std" id="cmdoption-key">
<span class="sig-name descname"><span class="pre">--key</span></span><span class="sig-prename descclassname"> <span class="pre">DER_FILE</span></span></dt>
<dd><p>Path to the client private key file in DER (.der) format.</p>
</dd></dl>

<p><strong>Usage</strong></p>
<p>See section <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/leaps-com/cmd-execution#discovering-leaps-devices"><span class="std std-ref">Discovering devices</span></a> on how to list all available devices for update
on the given interface.
Execute following command to update update CA-certificate, Client certificate and Private key.</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
USB</label><div class="sd-tab-content docutils">
<p>Connect USB data cable to the <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB port</span></a>.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--usb<span class="w"> </span>--ca<span class="w"> </span>ca-cert.der<span class="w"> </span>--cert<span class="w"> </span>client-cert.der.der<span class="w"> </span>--key<span class="w"> </span>client-priv-key.der
</pre></div>
</div>
<p>In order to update only certain devices you need to specify serial number.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--usb<span class="w"> </span>630D46F2D51482FC<span class="w"> </span>7E1C5859C2ECF343<span class="w"> </span>--ca<span class="w"> </span>ca-cert.der<span class="w"> </span>--cert<span class="w"> </span>client-cert.der.der<span class="w"> </span>--key<span class="w"> </span>client-priv-key.der
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
BLE</label><div class="sd-tab-content docutils">
<p>Before update, make sure that BLE is enabled on the devices (see section <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/leaps-com/cmd-execution#discovering-leaps-devices"><span class="std std-ref">Discovering devices</span></a> for more details).</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--ble<span class="w"> </span>--ca<span class="w"> </span>ca-cert.der<span class="w"> </span>--cert<span class="w"> </span>client-cert.der.der<span class="w"> </span>--key<span class="w"> </span>client-priv-key.der
</pre></div>
</div>
<p>In order to update only certain devices you need to specify the BLE address.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--ble<span class="w"> </span>FE:40:B4:BC:D3:42<span class="w"> </span>E0:05:86:49:A9:40<span class="w"> </span>--ca<span class="w"> </span>ca-cert.der<span class="w"> </span>--cert<span class="w"> </span>client-cert.der.der<span class="w"> </span>--key<span class="w"> </span>client-priv-key.der
</pre></div>
</div>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
Serial port</label><div class="sd-tab-content docutils">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--dev<span class="w"> </span>/dev/ttyACM0<span class="w"> </span>/dev/ttyACM1<span class="w"> </span>/dev/ttyACM2<span class="w"> </span>--ca<span class="w"> </span>ca-cert.der<span class="w"> </span>--cert<span class="w"> </span>client-cert.der.der<span class="w"> </span>--key<span class="w"> </span>client-priv-key.der
</pre></div>
</div>
</div>
</div>
</div>


           </div>
