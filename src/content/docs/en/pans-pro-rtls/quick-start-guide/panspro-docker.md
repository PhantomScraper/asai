---
title: "PANS PRO Docker"
lang: en
slug: "pans-pro-rtls/quick-start-guide/panspro-docker"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/quick-start-guide/panspro-docker/"
order: 90
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-docker">
<span id="panspro-docker"></span><h1>PANS PRO Docker</h1>
<p>This page provides:</p>
<blockquote>
<div><ul class="simple">
<li><p>The PANS PRO Docker package.</p></li>
<li><p>Information about system requirements.</p></li>
<li><p>Instructions on how to install PANS PRO Docker.</p></li>
</ul>
</div></blockquote>
<p>The installation is fast and easy and only needs to be done once.</p>
<div class="admonition-disclaimer admonition">
<p class="admonition-title">Disclaimer</p>
<p>The <a class="reference internal" href="#panspro-docker"><span class="std std-ref">PANS PRO Docker</span></a> installation is for professionals only. For demo purpose the <a class="reference internal" href="/docs/en/pans-pro-rtls/quick-start-guide/panspro-rpi#panspro-rpi"><span class="std std-ref">PANS PRO Raspberry Pi</span></a> is much better option.</p>
</div>
<p>Visit the official Docker to learn more about <a class="reference external" href="https://docs.docker.com/">Docker</a>.</p>
<p><strong>System requirements</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>System requirements follow <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/#system-requirements">Docker Desktop on Linux</a> or <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/#system-requirements">Docker Desktop on Windows</a>.</p></li>
<li><p>A desktop device: <strong>Requires 2 GB of free memory</strong>.</p></li>
<li><p>On windows, the installation of WSL consumes 2GB of RAM permanently. It is assigned to the Ubuntu WSL.</p></li>
<li><p><em>Recommended: A set (At least five devices) to verify.</em></p></li>
<li><p><em>Recommended: Batteries or Micro USB cables for powering the devices.</em></p></li>
<li><p><em>Recommended:</em> <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> <em>to configure devices.</em></p></li>
</ul>
</div></blockquote>
<p id="uidocker"><strong>Setup instructions</strong></p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Linux</label><div class="sd-tab-content docutils">
<p>The system is compatible with AMD64, ARM64, and ARM32 architectures.</p>
<ol class="arabic simple">
<li><p>Download PANS PRO Docker</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Please contact us for the download package at <a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Extract the PANS PRO Docker Archive</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Type in a terminal: <span class="red-text">$ unzip PANS-PRO-DOCKER-LINUX.zip -d /path/to/directory</span></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Install Docker on your operating system.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Run the <span class="red-text">leaps_docker_install.sh</span> script to install Docker on your operating system.</p></li>
</ul>
<p>For example, on Ubuntu (Linux):</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">leaps_docker_install</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</div></blockquote>
<ul class="simple">
<li><p>After the installation, and reboot your OS to ensure Docker is properly configured.</p></li>
<li><p>For detailed instructions, you can refer to the official <a class="reference external" href="https://docs.docker.com/get-docker/">Docker documentation</a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Update the correct configuration with IP Address.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Update <code class="docutils literal notranslate"><span class="pre">mqtt_host</span></code> in <code class="docutils literal notranslate"><span class="pre">leaps-server.conf</span></code> to point to the IP address of the gateway board. Get the address via shell.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>Run all LEAPS Docker containers.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Execute the <span class="red-text">leaps_docker_run_all.sh</span> script, which will pull and run the required Docker containers for <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>, <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a>, and Mosquitto (MQTT broker).</p></li>
</ul>
<p>For example, on Ubuntu (Linux):</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">leaps_docker_run_all</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</div></blockquote>
<ul class="simple">
<li><p>Execute the <span class="red-text">docker ps</span> command, make sure all containers start successfully and are ready for use.</p></li>
</ul>
<p>For example, on Ubuntu (Linux):</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">docker</span> <span class="n">ps</span>

<span class="n">CONTAINER</span> <span class="n">ID</span>   <span class="n">IMAGE</span>                       <span class="n">COMMAND</span>                  <span class="n">CREATED</span>          <span class="n">STATUS</span>          <span class="n">PORTS</span>                                              <span class="n">NAMES</span>
<span class="mi">6</span><span class="n">f2ae0c87d65</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_mosquitto</span><span class="p">:</span><span class="n">latest</span>   <span class="s2">"/docker-entrypoint.…"</span>   <span class="mi">9</span> <span class="n">seconds</span> <span class="n">ago</span>    <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">1883</span><span class="o">-&gt;</span><span class="mi">1883</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">15675</span><span class="o">-&gt;</span><span class="mi">15675</span><span class="o">/</span><span class="n">tcp</span>   <span class="n">leaps_mosquitto</span>
<span class="mi">3</span><span class="n">d84cad7a913</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_server</span><span class="p">:</span><span class="n">latest</span>      <span class="s2">"/app/leaps-server -…"</span>   <span class="mi">10</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">udp</span>     <span class="n">leaps_server</span>
<span class="mi">633</span><span class="n">c97e96f6e</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_center</span><span class="p">:</span><span class="n">latest</span>      <span class="s2">"sh -c 'cd /app &amp;&amp;  …"</span>   <span class="mi">10</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">10</span> <span class="n">seconds</span>   <span class="mi">80</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">80</span><span class="o">-&gt;</span><span class="mi">8080</span><span class="o">/</span><span class="n">tcp</span>                       <span class="n">leaps_center</span>
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Prepare the network as in <a class="reference internal" href="/docs/en/pans-pro-rtls/quick-start-guide/panspro-rtls-setup#pans-pro-demo"><span class="std std-ref">PANS PRO Demo</span></a> and connect the gateway board.</p></li>
<li><p>Mosquitto and check messages (optional)</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Use mosquitto_sub on your system.</p></li>
<li><p>To check for messages, use the following command in your terminal (This command will connect to the Mosquitto MQTT broker and display all messages received).</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>Access the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> via IP address.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Use your computer’s web browser.</p></li>
<li><p>Enter the IP address or <span class="red-text">localhost</span> to access the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps_center_login.png"><img alt="../../../_images/leaps_center_login.png" src="/docs-assets/_images/leaps_center_login.png" style="width: 667.4499999999999px; height: 315.0px;"></a>
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
<li><p>Use <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> to prepare network.</p></li>
<li><p>Configure the network on the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Check the network settings in <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> to match the network ID of the gateway board you have connected.</p></li>
<li><p>Check the correct host configured as the PC’s IP address.</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/leaps_center_pans.png"><img alt="../../../_images/leaps_center_pans.png" class="align-center" src="/docs-assets/_images/leaps_center_pans.png" style="width: 764.4000000000001px; height: 360.40000000000003px;"></a>
</div></blockquote>
</li>
<li><p>Please refer to the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> and <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> for more details on how to use the application to configure and visualize the nodes and network.</p></li>
</ul>
</div></blockquote>
<p>Now the system has been successfully set up and configured the system. Enjoy using it!</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Windows</label><div class="sd-tab-content docutils">
<ol class="arabic simple">
<li><p>Download PANS PRO Docker.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Please contact us for the download package at <a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Extract the PANS PRO Docker Archive.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Use a program like WinZip or 7-Zip to extract the downloaded PANS PRO Docker zip file.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Install Docker Desktop on Windows.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Follow the instructions provided in the Docker documentation for <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/">Docker Windows Installation</a>.</p></li>
<li><p>Once the installation is complete, restart your Windows system to ensure all changes take effect.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Update the correct configuration with IP Address using PowerShell.</p></li>
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
<span class="mi">6</span><span class="n">f2ae0c87d65</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_mosquitto</span><span class="p">:</span><span class="n">latest</span>   <span class="s2">"/docker-entrypoint.…"</span>   <span class="mi">9</span> <span class="n">seconds</span> <span class="n">ago</span>    <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">1883</span><span class="o">-&gt;</span><span class="mi">1883</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">15675</span><span class="o">-&gt;</span><span class="mi">15675</span><span class="o">/</span><span class="n">tcp</span>   <span class="n">leaps_mosquitto</span>
<span class="mi">3</span><span class="n">d84cad7a913</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_server</span><span class="p">:</span><span class="n">latest</span>      <span class="s2">"/app/leaps-server -…"</span>   <span class="mi">11</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">11</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">udp</span>    <span class="n">leaps_server</span>
<span class="mi">633</span><span class="n">c97e96f6e</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_center</span><span class="p">:</span><span class="n">latest</span>      <span class="s2">"sh -c 'cd /app &amp;&amp;  …"</span>   <span class="mi">12</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">12</span> <span class="n">seconds</span>   <span class="mi">80</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">80</span><span class="o">-&gt;</span><span class="mi">8080</span><span class="o">/</span><span class="n">tcp</span>                       <span class="n">leaps_center</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Prepare the network as in <a class="reference internal" href="/docs/en/pans-pro-rtls/quick-start-guide/panspro-rtls-setup#pans-pro-demo"><span class="std std-ref">PANS PRO Demo</span></a> and connect the gateway board.</p></li>
<li><p>Access the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> via IP address.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Use your computer’s web browser.</p></li>
<li><p>Enter the IP address or <span class="red-text">localhost</span> to access the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_login.png"><img alt="../../../_images/docker_leaps_center_login.png" src="/docs-assets/_images/docker_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>Login the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Logging in with Username as <span class="red-text">admin</span> and Password as <span class="red-text">admin</span>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p>Use <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> to prepare network.</p></li>
<li><p>Configure the network on the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Check the network settings in <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> to match the network ID of the gateway board you have connected.</p></li>
<li><p>Check the correct host configured as the PC’s IP address.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps_center_pans.png"><img alt="../../../_images/leaps_center_pans.png" src="/docs-assets/_images/leaps_center_pans.png" style="width: 764.4000000000001px; height: 360.40000000000003px;"></a>
</div>
<ul class="simple">
<li><p>Please refer to the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> and <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> for more details on how to use the application to configure and visualize the nodes and network.</p></li>
</ul>
</div></blockquote>
<p>Now the system has been successfully set up and configured the system. Enjoy using it!</p>
</div>
</div>
</div>


           </div>
