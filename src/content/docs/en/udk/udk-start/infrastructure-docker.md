---
title: "LEAPS Docker"
lang: en
slug: "udk/udk-start/infrastructure-docker"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/udk-start/infrastructure-docker/"
order: 40
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-docker">
<span id="id1"></span><h1>LEAPS Docker</h1>
<p>This page provides:</p>
<blockquote>
<div><ul class="simple">
<li><p>The LEAPS Docker package.</p></li>
<li><p>Information about system requirements.</p></li>
<li><p>Instructions on how to install LEAPS Docker.</p></li>
</ul>
</div></blockquote>
<p>The installation is fast and easy and only needs to be done once.</p>
<p>Visit the official Docker to learn more about <a class="reference external" href="https://docs.docker.com/">Docker</a>.</p>
<p><strong>System requirements</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>System requirements follow <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/#system-requirements">Docker Desktop on Linux</a> or <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/#system-requirements">Docker Desktop on Windows</a>.</p></li>
<li><p>A desktop device: <strong>Requires 2 GB of free memory</strong>.</p></li>
<li><p>On windows, the installation of WSL consumes 2GB of RAM permanently. It is assigned to the Ubuntu WSL.</p></li>
<li><p><em>Recommended: A set of UDK (At least five devices) to verify.</em></p></li>
<li><p><em>Recommended: Batteries or USB-C cables for powering the devices.</em></p></li>
<li><p><em>Recommended:</em> <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>to configure devices.</em></p></li>
</ul>
</div></blockquote>
<p id="uidocker"><strong>Setup instructions</strong></p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Linux</label><div class="sd-tab-content docutils">
<p>The system is compatible with AMD64, ARM64, and ARM32 architectures.</p>
<ol class="arabic simple">
<li><p>Download LEAPS Docker</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Docker <a class="reference download internal" download="" href="../../../_downloads/ae97200ed08d464a52759cdc643e7c12/LEAPS-DOCKER-LINUX-v1.1.0.zip"><code class="xref download docutils literal notranslate"><span class="pre">LEAPS-DOCKER-LINUX-v1.1.0.zip</span></code></a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Extract the LEAPS Docker Archive</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Type in a terminal: <span class="red-text">$ unzip LEAPS-DOCKER-LINUX-v1.1.0.zip -d /path/to/directory</span></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Install Docker on the operating system.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Run the <span class="red-text">leaps_docker_install.sh</span> script to install Docker on the operating system. For example, on Ubuntu (Linux):</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">leaps_docker_install</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</li>
<li><p>After the installation, and reboot the OS to ensure Docker is properly configured.</p></li>
<li><p>For detailed instructions, you can refer to the official <a class="reference external" href="https://docs.docker.com/get-docker/">Docker documentation</a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Update the correct configuration with IP Address.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Use the <span class="red-text">update_configuration_ip.sh</span> script to update the system’s configuration with the PC’s IP address. For example, on Ubuntu (Linux):</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">update_configuration_ip</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>Run all LEAPS Docker containers.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Execute the <span class="red-text">leaps_docker_run_all.sh</span> script, which will pull and run the required Docker containers for <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>, <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a>, <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a>, and Mosquitto (MQTT broker). For example, on Ubuntu (Linux):</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">leaps_docker_run_all</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</li>
<li><p>Execute the <span class="red-text">docker ps</span> command, make sure all containers start successfully and are ready for use. For example, on Ubuntu (Linux):</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">docker</span> <span class="n">ps</span>

<span class="n">CONTAINER</span> <span class="n">ID</span>   <span class="n">IMAGE</span>                       <span class="n">COMMAND</span>                  <span class="n">CREATED</span>          <span class="n">STATUS</span>          <span class="n">PORTS</span>                                              <span class="n">NAMES</span>
<span class="mi">6</span><span class="n">f2ae0c87d65</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_mosquitto</span><span class="p">:</span><span class="n">udk</span>   <span class="s2">"/docker-entrypoint.…"</span>   <span class="mi">9</span> <span class="n">seconds</span> <span class="n">ago</span>    <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">1883</span><span class="o">-&gt;</span><span class="mi">1883</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">15675</span><span class="o">-&gt;</span><span class="mi">15675</span><span class="o">/</span><span class="n">tcp</span>   <span class="n">leaps_mosquitto</span>
<span class="mi">3</span><span class="n">d84cad7a913</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_server</span><span class="p">:</span><span class="n">udk</span>      <span class="s2">"/app/leaps-server -…"</span>   <span class="mi">10</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">udp</span>     <span class="n">leaps_server</span>
<span class="mi">633</span><span class="n">c97e96f6e</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_center</span><span class="p">:</span><span class="n">udk</span>      <span class="s2">"sh -c 'cd /app &amp;&amp;  …"</span>   <span class="mi">10</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">10</span> <span class="n">seconds</span>   <span class="mi">80</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">80</span><span class="o">-&gt;</span><span class="mi">8080</span><span class="o">/</span><span class="n">tcp</span>                       <span class="n">leaps_center</span>
</pre></div>
</div>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">docker</span> <span class="n">ps</span>

<span class="n">CONTAINER</span> <span class="n">ID</span>   <span class="n">IMAGE</span>                     <span class="n">COMMAND</span>                  <span class="n">CREATED</span>              <span class="n">STATUS</span>                          <span class="n">PORTS</span>     <span class="n">NAMES</span>
<span class="mi">6</span><span class="n">bb3bf42cb63</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_gateway</span><span class="p">:</span><span class="n">udk</span>   <span class="s2">"/app/leaps-gateway …"</span>   <span class="n">About</span> <span class="n">a</span> <span class="n">minute</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="n">About</span> <span class="n">a</span> <span class="n">minute</span>                         <span class="n">leaps_gateway</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Connect the gateway board to the PC use a USB-C Data Cable.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Plug the USB-C Data Cable into the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a> on the PC. Ensure a stable connection.</p></li>
</ul>
<img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/_images/leaps-connect-usb-port1.gif">
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Mosquitto and check messages (optional)</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Use mosquitto_sub on the system. To check for messages, use the following command in the terminal.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</li>
<li><p>This command will connect to the Mosquitto MQTT broker and display all messages received.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>Access the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> via IP address.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Use the computer’s web browser.</p></li>
<li><p>Enter the IP address or <span class="red-text">localhost</span> to access the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_login.png"><img alt="../../../_images/docker_leaps_center_login.png" src="/docs-assets/_images/docker_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p>Login the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Logging in with Username as <span class="red-text">admin</span> and Password as <span class="red-text">admin</span>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>Use <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> to prepare network.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Configure demo: <a class="reference internal" href="/docs/en/udk/udk-start/twr-rtls-and-data-telemetry-demo#twr-rtls-and-data-telemetry-demo"><span class="std std-ref">TWR RTLS and Data Telemetry Demo</span></a> or <a class="reference internal" href="/docs/en/udk/udk-start/uplink-tdoa-rtls-demo#uplink-tdoa-rtls-demo"><span class="std std-ref">Uplink TDoA RTLS Demo</span></a>.</p></li>
<li><p>By default, the network ID will be <code class="docutils literal notranslate"><span class="pre">0x1234</span></code>.</p></li>
<li><p>For this example, it is necessary to connect the gateway board with ID <code class="docutils literal notranslate"><span class="pre">0x83A2</span></code>.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_network_demo01.jpg"><img alt="../../../_images/docker_network_demo01.jpg" src="/docs-assets/_images/docker_network_demo01.jpg" style="width: 360.0px; height: 800.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>Configure the network on the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Check the network settings in <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> to match the network ID of the gateway board you have connected.</p></li>
<li><p>Check the correct host configured as the PC’s IP address.</p></li>
<li><p>For this example, the network ID is <code class="docutils literal notranslate"><span class="pre">0x1234</span></code> and host is <code class="docutils literal notranslate"><span class="pre">192.168.1.12</span></code>.</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_config_network.png"><img alt="../../../_images/docker_leaps_center_config_network.png" src="/docs-assets/_images/docker_leaps_center_config_network.png" style="width: 626.4000000000001px; height: 409.6px;"></a>
</div>
</li>
<li><p>Please refer to the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> and <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> for more details on how to use the application to configure and visualize the nodes and network.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_network.png"><img alt="../../../_images/docker_leaps_center_network.png" src="/docs-assets/_images/docker_leaps_center_network.png" style="width: 764.4000000000001px; height: 373.20000000000005px;"></a>
</div>
</div></blockquote>
<p>Now the system has been successfully set up and configured the system. Enjoy using it!</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Windows</label><div class="sd-tab-content docutils">
<ol class="arabic simple">
<li><p>Download LEAPS Docker.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Docker <a class="reference download internal" download="" href="../../../_downloads/0bfac2c46fb0b9265d7f58941736f12a/LEAPS-DOCKER-WINDOWS-v1.1.0.zip"><code class="xref download docutils literal notranslate"><span class="pre">LEAPS-DOCKER-WINDOWS-v1.1.0.zip</span></code></a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Extract the LEAPS Docker Archive.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Use a program like WinZip or 7-Zip to extract the downloaded LEAPS Docker zip file.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Install Docker Desktop on Windows.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Follow the instructions provided in the Docker documentation for <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/">Docker Windows Installation</a>.</p></li>
<li><p>Once the installation is complete, restart the Windows system to ensure all changes take effect.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Update the correct configuration with IP Address using PowerShell.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Use the <span class="red-text">update_configuration_ip.bat</span> script to update the system’s configuration with the PC’s IP address.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">./</span><span class="n">update_configuration_ip</span><span class="o">.</span><span class="n">bat</span>
</pre></div>
</div>
</li>
<li><p>For this example, the leaps-server configuration is updated with the current IP address: <code class="docutils literal notranslate"><span class="pre">192.168.1.12</span></code>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>Run all LEAPS Docker containers using PowerShell.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Execute the <span class="red-text">leaps_docker_run_all.bat</span> script, which will pull and run the required Docker containers for <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>, LEAPS Server, and Mosquitto (MQTT broker).</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">./</span><span class="n">leaps_docker_run_all</span><span class="o">.</span><span class="n">bat</span>
</pre></div>
</div>
</li>
<li><p>Make sure all containers start successfully and are ready for use.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">CONTAINER</span> <span class="n">ID</span>   <span class="n">IMAGE</span>                       <span class="n">COMMAND</span>                  <span class="n">CREATED</span>          <span class="n">STATUS</span>          <span class="n">PORTS</span>                                              <span class="n">NAMES</span>
<span class="mi">6</span><span class="n">f2ae0c87d65</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_mosquitto</span><span class="p">:</span><span class="n">udk</span>   <span class="s2">"/docker-entrypoint.…"</span>   <span class="mi">9</span> <span class="n">seconds</span> <span class="n">ago</span>    <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">1883</span><span class="o">-&gt;</span><span class="mi">1883</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">15675</span><span class="o">-&gt;</span><span class="mi">15675</span><span class="o">/</span><span class="n">tcp</span>   <span class="n">leaps_mosquitto</span>
<span class="mi">3</span><span class="n">d84cad7a913</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_server</span><span class="p">:</span><span class="n">udk</span>      <span class="s2">"/app/leaps-server -…"</span>   <span class="mi">11</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">11</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">udp</span>    <span class="n">leaps_server</span>
<span class="mi">633</span><span class="n">c97e96f6e</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_center</span><span class="p">:</span><span class="n">udk</span>      <span class="s2">"sh -c 'cd /app &amp;&amp;  …"</span>   <span class="mi">12</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">12</span> <span class="n">seconds</span>   <span class="mi">80</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">80</span><span class="o">-&gt;</span><span class="mi">8080</span><span class="o">/</span><span class="n">tcp</span>                       <span class="n">leaps_center</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Connect the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a> use <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Raspberry</span> <span class="pre">Pi</span></code>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Make sure there is a connection to Windows.</p></li>
<li><p>Refer to <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a> setup on <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Raspberry</span> <span class="pre">Pi</span></code> and, update the IP address accordingly. For example, <code class="docutils literal notranslate"><span class="pre">leaps-server-host</span></code> will be updated to <code class="docutils literal notranslate"><span class="pre">192.168.1.12</span></code>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Mosquitto and check messages (optional)</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Use mosquitto_sub on the system. To check for messages, use the following command in the terminal.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</li>
<li><p>This command will connect to the Mosquitto MQTT broker and display all messages received.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>Access the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> via IP address.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Use the computer’s web browser.</p></li>
<li><p>Enter the IP address or <span class="red-text">localhost</span> to access the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_login.png"><img alt="../../../_images/docker_leaps_center_login.png" src="/docs-assets/_images/docker_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p>Login the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Logging in with Username as <span class="red-text">admin</span> and Password as <span class="red-text">admin</span>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>Use <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> to prepare network.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Configure demo: <a class="reference internal" href="/docs/en/udk/udk-start/twr-rtls-and-data-telemetry-demo#twr-rtls-and-data-telemetry-demo"><span class="std std-ref">TWR RTLS and Data Telemetry Demo</span></a> or <a class="reference internal" href="/docs/en/udk/udk-start/uplink-tdoa-rtls-demo#uplink-tdoa-rtls-demo"><span class="std std-ref">Uplink TDoA RTLS Demo</span></a>.</p></li>
<li><p>By default, the network ID will be <code class="docutils literal notranslate"><span class="pre">0x1234</span></code>.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_network_demo01.jpg"><img alt="../../../_images/docker_network_demo01.jpg" src="/docs-assets/_images/docker_network_demo01.jpg" style="width: 360.0px; height: 800.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>Configure the network on the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Check the network settings in <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> to match the network ID of the gateway board you have connected.</p></li>
<li><p>Check the correct host configured as the PC’s IP address.</p></li>
<li><p>For this example, the network ID is <code class="docutils literal notranslate"><span class="pre">0x1234</span></code> and host is <code class="docutils literal notranslate"><span class="pre">192.168.1.12</span></code>.</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_config_network.png"><img alt="../../../_images/docker_leaps_center_config_network.png" src="/docs-assets/_images/docker_leaps_center_config_network.png" style="width: 626.4000000000001px; height: 409.6px;"></a>
</div>
<ul class="simple">
<li><p>Please refer to the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> and <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> for more details on how to use the application to configure and visualize the nodes and network.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_network.png"><img alt="../../../_images/docker_leaps_center_network.png" src="/docs-assets/_images/docker_leaps_center_network.png" style="width: 764.4000000000001px; height: 373.20000000000005px;"></a>
</div>
</li>
</ul>
</div></blockquote>
<p>Now the system has been successfully set up and configured the system. Enjoy using it!</p>
</div>
</div>
</div>


           </div>
