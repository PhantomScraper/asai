---
title: "Concurrent command execution"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/leaps-com/cmd-execution"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/leaps-com/cmd-execution/"
order: 118
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="concurrent-command-execution">
<h1>Concurrent command execution</h1>
<p><strong>Leapscom</strong> is designed to run either TLV (Type-Length-Value) commands or shell commands over a selected
interface on target devices. This is useful for managing and testing LEAPS subsystem devices concurrently.</p>
<div class="section" id="tlv-commands">
<span id="tlv-option"></span><h2>TLV commands</h2>
<dl class="std option">
<dt class="sig sig-object std" id="cmdoption-tlv">
<span class="sig-name descname"><span class="pre">--tlv</span></span><span class="sig-prename descclassname"> <span class="pre">TLV_COMMAND</span> <span class="pre">[TLV_COMMAND</span> <span class="pre">...]</span></span></dt>
<dd><p>List of TLV commands as hexadecimal string. See <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-list#api-commmand-list"><span class="std std-ref">list of supported TLV commands</span></a>.</p>
</dd></dl>

<p>For example, to execute a following sequence of commands for all devices that are connected on the USB interface:</p>
<ul class="simple">
<li><p>Configure as TAGs (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-tag-set#leaps-cfg-tag-set"><span class="std std-ref">leaps_cfg_tag_set</span></a>)</p></li>
<li><p>Apply the configuration by resetting the devices (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a>)</p></li>
<li><p>Blink all LEDs (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-blink-leds#leaps-blink-leds"><span class="std std-ref">leaps_blink_leds</span></a>)</p></li>
</ul>
<p>Use following:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--usb<span class="w"> </span>--tlv<span class="w"> </span><span class="m">0503720402</span><span class="w"> </span><span class="m">1400</span><span class="w"> </span><span class="m">2000</span>
</pre></div>
</div>
</div></blockquote>
</div>
<div class="section" id="shell-commands">
<span id="shell-option"></span><h2>Shell commands</h2>
<dl class="std option">
<dt class="sig sig-object std" id="cmdoption-shell">
<span class="sig-name descname"><span class="pre">--shell</span></span><span class="sig-prename descclassname"> <span class="pre">SHELL_COMMAND</span> <span class="pre">[SHELL_COMMAND</span> <span class="pre">...]</span></span></dt>
<dd><p>List of shell commands. See <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/shell-api#leaps-shell-api"><span class="std std-ref">list of supported Shell commands</span></a>.</p>
</dd></dl>

<p>For example, to execute a following sequence of commands for all devices that are connected
on serial port as serial device <code class="docutils literal notranslate"><span class="pre">/dev/ttyACM0</span></code> and <code class="docutils literal notranslate"><span class="pre">/dev/ttyACM1</span></code>:</p>
<blockquote>
<div><ul class="simple">
<li><p>Set network ID to <code class="docutils literal notranslate"><span class="pre">1234</span></code> (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#nis"><span class="std std-ref">nis</span></a>)</p></li>
<li><p>Configure as TAGs with BLE enabled, UWB mode: active and LEDs enabled. (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#tcs"><span class="std std-ref">tcs</span></a>)</p></li>
<li><p>Apply the configuration by resetting the devices (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#reset"><span class="std std-ref">リセット</span></a>)</p></li>
</ul>
</div></blockquote>
<p>use following:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--dev<span class="w"> </span>/dev/ttyACM0<span class="w"> </span>/dev/ttyACM1<span class="w"> </span>--shell<span class="w"> </span><span class="s1">'nis 1234'</span><span class="w"> </span><span class="s1">'tcs ble 1 uwb 2 leds 1'</span><span class="w"> </span>reset<span class="w"> </span>--verbose
</pre></div>
</div>
</div></blockquote>
<p>Use verbose output if you want to see the details and the response to the shell command.</p>
</div>
<div class="section" id="retries-on-failure">
<span id="command-attempts"></span><h2>Retries on Failure</h2>
<p>If a command fails (e.g., due to a timeout or no response), Leapscom can automatically retry the
command a specified number of times to increases reliability when working with unstable connections or devices under test.</p>
<dl class="std option">
<dt class="sig sig-object std" id="cmdoption-a">
<span id="cmdoption-attempts"></span><span class="sig-name descname"><span class="pre">-a</span></span><span class="sig-prename descclassname"></span><span class="sig-prename descclassname"><span class="pre">,</span> </span><span class="sig-name descname"><span class="pre">--attempts</span></span><span class="sig-prename descclassname"> <span class="pre">NUMBER</span></span></dt>
<dd><p>Maximum number of attempts in case of a failed command.</p>
</dd></dl>

</div>
<div class="section" id="custom-timeout-support">
<span id="command-timeout"></span><h2>Custom Timeout Support</h2>
<p>Users can specify a timeout duration for each command.
If the command does not complete or return a response within the timeout window, it will be considered failed, triggering a retry if configured.</p>
<dl class="std option">
<dt class="sig sig-object std" id="cmdoption-t">
<span id="cmdoption-timeout"></span><span class="sig-name descname"><span class="pre">-t</span></span><span class="sig-prename descclassname"></span><span class="sig-prename descclassname"><span class="pre">,</span> </span><span class="sig-name descname"><span class="pre">--timeout</span></span><span class="sig-prename descclassname"> <span class="pre">SECONDS</span></span></dt>
<dd><p>Timeout in seconds, e.g.: 0.5.</p>
</dd></dl>

</div>
<div class="section" id="supported-interfaces">
<h2>Supported Interfaces</h2>
<p>Leapscom is designed to operate concurrently, enabling efficient command execution on multiple devices at the same time.
Commands are sent over a user-specified interface (e.g., USB, BLE, serial ports).</p>
<dl class="std option">
<dt class="sig sig-object std" id="cmdoption-u">
<span id="cmdoption-usb"></span><span class="sig-name descname"><span class="pre">-u</span></span><span class="sig-prename descclassname"></span><span class="sig-prename descclassname"><span class="pre">,</span> </span><span class="sig-name descname"><span class="pre">--usb</span></span><span class="sig-prename descclassname"> <span class="pre">[SERIAL_NUMBER</span> <span class="pre">...]</span></span></dt>
<dd><p>List of USB serial numbers. If no serial number is given, all available LEAPS devices are used.</p>
</dd></dl>

<dl class="std option">
<dt class="sig sig-object std" id="cmdoption-b">
<span id="cmdoption-ble"></span><span class="sig-name descname"><span class="pre">-b</span></span><span class="sig-prename descclassname"></span><span class="sig-prename descclassname"><span class="pre">,</span> </span><span class="sig-name descname"><span class="pre">--ble</span></span><span class="sig-prename descclassname"> <span class="pre">[MAC_ADDRESS</span> <span class="pre">...]</span></span></dt>
<dd><p>List of BLE MAC addresses. If no address is given, all scanned LEAPS devices are used.</p>
</dd></dl>

<dl class="std option">
<dt class="sig sig-object std" id="cmdoption-d">
<span id="cmdoption-dev"></span><span class="sig-name descname"><span class="pre">-d</span></span><span class="sig-prename descclassname"></span><span class="sig-prename descclassname"><span class="pre">,</span> </span><span class="sig-name descname"><span class="pre">--dev</span></span><span class="sig-prename descclassname"> <span class="pre">[SERIAL_DEVICE</span> <span class="pre">...]</span></span></dt>
<dd><p>List of serial devices. It can be tty device on Linux and MAC or COM port on Windows.</p>
</dd></dl>

<p>Commands can be executed in two ways:</p>
<ul class="simple">
<li><dl class="simple">
<dt>Broadcast to all connected devices</dt><dd><p>The command is sent to every device currently connected to the system or network.
This is useful when the same action needs to be performed universally (e.g., syncing time, applying a global configuration).</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt>Targeted to specific devices</dt><dd><p>The command is sent only to explicitly specified devices. This allows for granular control,
enabling you to apply actions to a subset of devices based on criteria like device ID, group, or type.</p>
</dd>
</dl>
</li>
</ul>
</div>
<div class="section" id="discovering-devices">
<span id="discovering-leaps-devices"></span><h2>Discovering devices</h2>
<p>You can list all available LEAPS devices connected to your PC on the USB or serial port or
scan for all available devices that are advertising on the BLE interface using the command:</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
USB</label><div class="sd-tab-content docutils">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--lsusb
<span class="go">Leaps USB devices with ID 1915:e8e3:</span>
<span class="go">1.[630D46F2D51482FC] address 74 on bus 1, Label: "ID0A97"</span>
<span class="go">2.[7E1C5859C2ECF343] address 73 on bus 1, Label: "ID5606"</span>
<span class="go">3.[EACD147C04DD6BA8] address 75 on bus 1, Label: "IDD220"</span>
<span class="go">4.[2FB14F372E0341A6] address 72 on bus 1, Label: "ID4C15"</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
BLE</label><div class="sd-tab-content docutils">
<p>Make sure that BLE is enabled on the device (see <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-get#leaps-cfg-get"><span class="std std-ref">leaps_cfg_get</span></a>).</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--lsble
<span class="go">Scanning for BLE devices, please wait...</span>
<span class="go">1.[FE:40:B4:BC:D3:42] - AdvertisementData(local_name='LEAPSDECAECC259555606', service_data={'680c21d9-c946-4c1f-9c11-baa1c21329e7': b'4\x12\x06V\x02A\xff\x00\x00'}, rssi=-56)</span>
<span class="go">2.[E0:05:86:49:A9:40] - AdvertisementData(local_name='LEAPSDECA14D5F2450A97', service_data={'680c21d9-c946-4c1f-9c11-baa1c21329e7': b'\x00\x00\x97\n\x01[\xff\x00\x00'}, rssi=-61)</span>
<span class="go">3.[EF:7E:7A:E3:38:B6] - AdvertisementData(local_name='LEAPSDECA032E37404C15', service_data={'680c21d9-c946-4c1f-9c11-baa1c21329e7': b'4\x12\x15L\x02\xc9\xff\x00\x00'}, rssi=-62)</span>
<span class="go">4.[D3:B6:82:62:5F:06] - AdvertisementData(local_name='LEAPSDECADD047C15D220', service_data={'680c21d9-c946-4c1f-9c11-baa1c21329e7': b'4\x12 \xd2\x02U\xff\x00\x00'}, rssi=-64)</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
Serial port</label><div class="sd-tab-content docutils">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--lsdev
<span class="go">Leaps serial ports:</span>
<span class="go">1. ttyACM6 - DAPLink CMSIS-DAP - mbed Serial Port, Label: "ID93A6"</span>
<span class="go">2. ttyACM5 - DAPLink CMSIS-DAP - mbed Serial Port, Label: "IDC485"</span>
<span class="go">3. ttyACM4 - DAPLink CMSIS-DAP - mbed Serial Port, Label: "ID1391"</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="section" id="configuration-file">
<h2>Configuration file</h2>
<p>To run list of commands from configuration file:</p>
<dl class="std option">
<dt class="sig sig-object std" id="cmdoption-c">
<span id="cmdoption-cfg"></span><span class="sig-name descname"><span class="pre">-c</span></span><span class="sig-prename descclassname"></span><span class="sig-prename descclassname"><span class="pre">,</span> </span><span class="sig-name descname"><span class="pre">--cfg</span></span><span class="sig-prename descclassname"> <span class="pre">YAML_FILE</span></span></dt>
<dd><p>YAML configuration file that contains definition of the command sequence.</p>
</dd></dl>

<p>Example configuration file: <cite>configure-tags.yaml</cite>:</p>
<div class="highlight-yaml notranslate"><div class="highlight"><pre><span></span><span class="c1"># configure device as TAG, set node ID to 0xABCD and reset</span>
<span class="nt">tlv</span><span class="p">:</span>
<span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">cmd</span><span class="p">:</span><span class="w"> </span><span class="s">'0503720402'</span><span class="w"> </span><span class="c1"># TLV command - 'cfg_tag_set'</span>
<span class="w">    </span><span class="nt">timeout</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">2.5</span>
<span class="w">    </span><span class="l l-Scalar l-Scalar-Plain">attempts 3</span>
<span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">cmd</span><span class="p">:</span><span class="w"> </span><span class="s">'2e02cdab'</span><span class="w"> </span><span class="c1"># TLV command - 'panid_set`</span>
<span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">cmd</span><span class="p">:</span><span class="w"> </span><span class="s">'14</span><span class="nv"> </span><span class="s">00'</span><span class="w"> </span><span class="c1"># TLV command - 'reset'</span>
</pre></div>
</div>
<ul class="simple">
<li><p><strong>tlv.cmd</strong>: See section <a class="reference internal" href="#tlv-option"><span class="std std-ref">TLV commands</span></a>.</p></li>
<li><p><strong>tlv.cmd.timeout</strong>: See section <a class="reference internal" href="#command-timeout"><span class="std std-ref">Custom Timeout Support</span></a>.</p></li>
<li><p><strong>tlv.cmd.attempts</strong>: See section <a class="reference internal" href="#command-attempts"><span class="std std-ref">Retries on Failure</span></a>.</p></li>
</ul>
<p>To execute commands defined in the configuration file use for example:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--usb<span class="w"> </span>--cfg<span class="w"> </span>configure-tags.yaml
</pre></div>
</div>
</div></blockquote>
<p>Possible configuration file using shell commands:</p>
<div class="highlight-yaml notranslate"><div class="highlight"><pre><span></span><span class="c1"># See information about the device, then configure as TAG and reset</span>
<span class="nt">shell</span><span class="p">:</span>
<span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">cmd</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">si</span><span class="w"> </span><span class="c1"># SHELL command 'si'</span>
<span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">cmd</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">ut</span><span class="w"> </span><span class="c1"># SHELL command 'ut'</span>
<span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">cmd</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">acs leds 1 ble 1</span><span class="w"> </span><span class="c1"># SHELL command 'tcs' set LEDs ON and BLE ON</span>
<span class="w">    </span><span class="nt">timeout</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">3.0</span><span class="w"> </span><span class="c1"># delay 2 seconds after the command</span>
<span class="w">    </span><span class="l l-Scalar l-Scalar-Plain">attempts 5</span>
<span class="w">  </span><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">cmd</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">reset</span><span class="w"> </span><span class="c1"># SHELL command 'reset'</span>
<span class="w">    </span><span class="nt">timeout</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">5.0</span>
</pre></div>
</div>
<ul class="simple">
<li><p><strong>shell.cmd</strong>: See section <a class="reference internal" href="#shell-option"><span class="std std-ref">Shell commands</span></a>.</p></li>
<li><p><strong>shell.cmd.timeout</strong>: See section <a class="reference internal" href="#command-timeout"><span class="std std-ref">Custom Timeout Support</span></a>.</p></li>
<li><p><strong>shell.cmd.attempts</strong>: See section <a class="reference internal" href="#command-attempts"><span class="std std-ref">Retries on Failure</span></a>.</p></li>
</ul>
<p>To execute commands defined in the configuration file and see the verbose output:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--usb<span class="w"> </span>--cfg<span class="w"> </span>configure-tags.yaml<span class="w"> </span>-v
</pre></div>
</div>
</div></blockquote>
<p>Verbose output need to be enabled to display output to the shell commands.</p>
</div>
</div>


           </div>
