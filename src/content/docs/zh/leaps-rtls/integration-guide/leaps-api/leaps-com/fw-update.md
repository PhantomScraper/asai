---
title: "Firmware update"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-api/leaps-com/fw-update"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-api/leaps-com/fw-update/"
order: 119
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="firmware-update">
<h1>Firmware update</h1>
<p><strong>Leapscom</strong> supports firmware updates over USB, BLE, or serial port interfaces.
You can update one or multiple devices simultaneously. Both the Main Firmware and
the Extended Loader can be updated—either together or separately, depending on your needs.</p>
<p>See section <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-com/cmd-execution#discovering-leaps-devices"><span class="std std-ref">Discovering devices</span></a> on how to list all available devices for update
on the given interface.</p>
<p>Firmware updates can only be performed using interfaces that support the TLV API.
Leapscom does not support running firmware updates and command execution simultaneously.
Therefore, the options –main and –eldr cannot be used together with –cfg, –tlv, or –shell.</p>
<p><strong>Options</strong></p>
<dl class="std option">
<dt class="sig sig-object std" id="cmdoption-main">
<span class="sig-name descname"><span class="pre">--main</span></span><span class="sig-prename descclassname"> <span class="pre">BIN_FILE</span></span></dt>
<dd><p>Path to the binary file representing Main Firmware.</p>
</dd></dl>

<dl class="std option">
<dt class="sig sig-object std" id="cmdoption-eldr">
<span class="sig-name descname"><span class="pre">--eldr</span></span><span class="sig-prename descclassname"> <span class="pre">BIN_FILE</span></span></dt>
<dd><p>Path to the binary file representing Extended-Loader. Not all devices support the Extended Loader.</p>
</dd></dl>

<p><strong>Usage</strong></p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
USB</label><div class="sd-tab-content docutils">
<p>Connect USB data cable to the <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB port</span></a>.
Execute following command to update Firmware and Extended-Loader on the available devices that are connected on the USB interface.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--usb<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
<p>In order to update only certain devices you need to specify serial number.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--usb<span class="w"> </span>630D46F2D51482FC<span class="w"> </span>7E1C5859C2ECF343<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
BLE</label><div class="sd-tab-content docutils">
<p>Before update, make sure that BLE is enabled on the devices (see section <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-com/cmd-execution#discovering-leaps-devices"><span class="std std-ref">Discovering devices</span></a> for more details).
Execute following command to update Firmware and Extended-Loader of all the devices that are advertising on the BLE interface.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--ble<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
<p>In order to update only certain devices you need to specify the BLE address.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--ble<span class="w"> </span>FE:40:B4:BC:D3:42<span class="w"> </span>E0:05:86:49:A9:40<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
Serial port</label><div class="sd-tab-content docutils">
<p>Connect USB data cable to the <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">Serial port</span></a>.
Execute following command to update Firmware and Extended-Loader over the serial ports.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--dev<span class="w"> </span>/dev/ttyACM0<span class="w"> </span>/dev/ttyACM1<span class="w"> </span>/dev/ttyACM2<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
</div>
</div>
<p>Firmware update can take up to several minutes depending on the amount of devices
being updated and depending on the chosen interface.</p>
</div>


           </div>
