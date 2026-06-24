---
title: "LEAPS VMWare"
lang: en
slug: "udk/udk-start/infrastructure-vmware"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/udk-start/infrastructure-vmware/"
order: 39
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-vmware">
<span id="id1"></span><h1>LEAPS VMWare</h1>
<blockquote>
<div><p>This page provides:</p>
<blockquote>
<div><ul class="simple">
<li><p>The LEAPS VMWare package.</p></li>
<li><p>Information about system requirements.</p></li>
<li><p>Instructions on how to install LEAPS VMWare.</p></li>
</ul>
</div></blockquote>
</div></blockquote>
<p>The installation is fast and easy and only needs to be done once.</p>
<p id="uivmware"><strong>System requirements</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>A desktop device.</p></li>
<li><p><em>Recommended: A set of UDK (At least five devices) to verify.</em></p></li>
<li><p><em>Recommended: Batteries or USB-C cables for powering the devices.</em></p></li>
<li><p><em>Recommended:</em> <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>to configure devices.</em></p></li>
</ul>
</div></blockquote>
<p><strong>Setup instructions</strong></p>
<ol class="arabic simple">
<li><p>Download and Install VMware Player or VMware Workstation.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Visit the following links to download the required software.</p>
<ul>
<li><p><a class="reference external" href="https://www.vmware.com/uk/products/workstation-player.html">VMware Workstation Player</a>.</p></li>
<li><p><a class="reference external" href="https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html">VMware Workstation Pro</a>.</p></li>
</ul>
</li>
<li><p>Choose the version compatible with your operating system and follow the installation instructions provided.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Download LEAPS VMWare.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS VMWare: <a class="reference external" href="https://drive.google.com/file/d/1By5GRLJCnKrMETvIk7INXXEKKhFTtli4/view?usp=drive_link">LEAPS-VMM-IMAGE-v1.1.0.zip</a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Extract the VMWare Archive.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Use a program like WinZip or 7-Zip to extract the downloaded LEAPS VMWare zip file.</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/extract_the_vmware_archive.png"><img alt="../../../_images/extract_the_vmware_archive.png" src="/docs-assets/_images/extract_the_vmware_archive.png" style="width: 463.0px; height: 262.0px;"></a>
</div>
<ol class="arabic simple" start="4">
<li><p>Import the Appliance.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Navigate to the extracted files and locate the .ova file.</p></li>
<li><p>Open the VMware application and go to <span class="red-text">File</span> » <span class="red-text">Import Appliance</span>.</p></li>
<li><p>Browse to the .ova file and click Open.</p></li>
<li><p>Type a name for the virtual machine, type or browse to the directory for the virtual machine files, and click Import.</p></li>
<li><p>Click the <span class="red-text">Import</span> button to start the import process. If the import fails, click Retry to try again, or click Cancel to cancel the import.</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/import_the_appliance.png"><img alt="../../../_images/import_the_appliance.png" src="/docs-assets/_images/import_the_appliance.png" style="width: 697.9px; height: 477.4px;"></a>
</div>
<ol class="arabic simple" start="5">
<li><p>Start the VMWare.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Once the import is completed, select the imported Virtual Machine and click the <span class="red-text">Start</span> button to launch it.</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/start_the_vmware.png"><img alt="../../../_images/start_the_vmware.png" src="/docs-assets/_images/start_the_vmware.png" style="width: 760.9px; height: 476.7px;"></a>
</div>
<ol class="arabic simple" start="6">
<li><p>Wait for the System to Boot.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Please be patient and allow a few minutes for the entire system to finish booting.</p></li>
<li><p>By default the account is <code class="docutils literal notranslate"><span class="pre">leaps</span></code> and password is <code class="docutils literal notranslate"><span class="pre">leaps</span></code>.</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/windows_vmware.png"><img alt="../../../_images/windows_vmware.png" src="/docs-assets/_images/windows_vmware.png" style="width: 600.5999999999999px; height: 487.2px;"></a>
</div>
<ol class="arabic simple" start="7">
<li><p>Use <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> to prepare network.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Configure demo: <a class="reference internal" href="/docs/en/udk/udk-start/twr-rtls-and-data-telemetry-demo#twr-rtls-and-data-telemetry-demo"><span class="std std-ref">TWR RTLS and Data Telemetry Demo</span></a> or <a class="reference internal" href="/docs/en/udk/udk-start/uplink-tdoa-rtls-demo#uplink-tdoa-rtls-demo"><span class="std std-ref">Uplink TDoA RTLS Demo</span></a>.</p></li>
<li><p>By default, the network ID will be <code class="docutils literal notranslate"><span class="pre">0x1234</span></code>.</p></li>
<li><p>For this example, it is necessary to connect the gateway board with ID <code class="docutils literal notranslate"><span class="pre">0x83A2</span></code>.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware_network_demo01.jpg"><img alt="../../../_images/vmware_network_demo01.jpg" src="/docs-assets/_images/vmware_network_demo01.jpg" style="width: 360.0px; height: 800.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>Connect the gateway board to your PC using a USB-C Data Cable.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Plug the USB-C Data Cable into the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a> on your PC. Ensure a stable connection.</p>
<img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/_images/leaps-connect-usb-port1.gif">
</li>
<li><p>In the running VMWare, navigate to the <span class="red-text">Virtual Machine</span> » <span class="red-text">Removable Devices.</span></p></li>
<li><p>Will hear two beeps as a confirmation if successfully connected in gateway mode as confirmation.</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/connect_the_gateway_board.png"><img alt="../../../_images/connect_the_gateway_board.png" src="/docs-assets/_images/connect_the_gateway_board.png" style="width: 718.1999999999999px; height: 488.59999999999997px;"></a>
</div>
<ol class="arabic simple" start="9">
<li><p>Check System Status.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Open a terminal or command prompt within the VMWare.</p></li>
<li><p>Use the <span class="red-text">mosquitto_sub</span> command to check the system status. This command will connect to the Mosquitto MQTT broker and display all messages received.</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>Check IP address.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>The IP address in step 6. In case not shown. Use the command <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">ifconfig</span></code> to check it.</p>
<ul>
<li><p>For this example is <code class="docutils literal notranslate"><span class="pre">192.168.26.151</span></code>.</p></li>
</ul>
</li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/windows_vmware_ip_address.png"><img alt="../../../_images/windows_vmware_ip_address.png" src="/docs-assets/_images/windows_vmware_ip_address.png" style="width: 600.5999999999999px; height: 487.2px;"></a>
</div>
<ul>
<li><p>Alternatively, can change the configuration as follows if the IP address cannot be checked.</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware-set-nat.png"><img alt="../../../_images/vmware-set-nat.png" src="/docs-assets/_images/vmware-set-nat.png" style="width: 525.6999999999999px; height: 510.29999999999995px;"></a>
</div>
<ul class="simple">
<li><p>Then, use the command <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">ifconfig</span></code> to check. For this example is <code class="docutils literal notranslate"><span class="pre">192.168.146.145</span></code>.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware-sudo-ipconfig.png"><img alt="../../../_images/vmware-sudo-ipconfig.png" src="/docs-assets/_images/vmware-sudo-ipconfig.png" style="width: 557.1999999999999px; height: 457.79999999999995px;"></a>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>Access <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Use your computer’s web browser.</p></li>
<li><p>Enter the IP address of the LEAPS VMware to access the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware_leaps_center_login.png"><img alt="../../../_images/vmware_leaps_center_login.png" src="/docs-assets/_images/vmware_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>Login <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Logging in with Username as <span class="red-text">admin</span> and Password as <span class="red-text">admin</span>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="12">
<li><p>The network on <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Check the network settings in <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> to match the network ID of the gateway board you have connected.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware_leaps_center_network.png"><img alt="../../../_images/vmware_leaps_center_network.png" src="/docs-assets/_images/vmware_leaps_center_network.png" style="width: 764.4000000000001px; height: 373.20000000000005px;"></a>
</div>
<ul class="simple">
<li><p>Please refer to the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> and <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> for more details on how to use the application to configure and visualize the nodes and network.</p></li>
</ul>
</div></blockquote>
<p>Now the system has been successfully set up and configured the system. Enjoy using it!</p>
</div>


           </div>
