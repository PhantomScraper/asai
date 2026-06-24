---
title: "PANS PRO Raspberry Pi"
lang: en
slug: "pans-pro-rtls/quick-start-guide/panspro-rpi"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/quick-start-guide/panspro-rpi/"
order: 91
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-raspberry-pi">
<span id="panspro-rpi"></span><h1>PANS PRO Raspberry Pi</h1>
<p>This page provides:</p>
<blockquote>
<div><ul class="simple">
<li><p>The PANS PRO Raspberry Pi package.</p></li>
<li><p>Information about system requirements.</p></li>
<li><p>Instructions on how to install PANS PRO Raspberry Pi.</p></li>
</ul>
</div></blockquote>
<p>The installation is fast and easy and only needs to be done once.</p>
<p id="uiraspberrypi"><span class="red-text">Before starting: Remember to back up any important files from the SD card you want to keep, as all data will be permanently overwritten during formatting.</span></p>
<p><strong>System requirements</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>Raspberry Pi 3B or newer.</p></li>
<li><p><em>Recommended: A set (At least five devices) to verify.</em></p></li>
<li><p><em>Recommended: Batteries or Micro USB cables for powering the devices.</em></p></li>
<li><p><em>Recommended:</em> <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> <em>to configure devices.</em></p></li>
</ul>
</div></blockquote>
<p><strong>Setup instructions</strong></p>
<ol class="arabic simple">
<li><p>Download PANS PRO Raspberry Pi Image.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Please contact us for the download package at <a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Extract the PANS PRO Raspberry Pi Archive.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Use a program like WinZip or 7-Zip to extract the downloaded PANS PRO Raspberry Pi zip file.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Launching the Raspberry Pi Imager.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Your operating system may try to block the installer.</p></li>
<li><p><em>On Windows: If you see a warning message, click</em> <span class="red-text">More info</span> <em>and</em> <span class="red-text">Run anyway</span>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Installing the PANS PRO Raspberry Pi Image.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Insert your SD card into the computer or laptop’s SD card slot.</p></li>
<li><p>Open the Raspberry Pi Imager.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_imager.png"><img alt="../../../_images/raspberry_pi_imager.png" src="/docs-assets/_images/raspberry_pi_imager.png" style="width: 541.6px; height: 363.20000000000005px;"></a>
</div>
<ul class="simple">
<li><p>Select ‘Use custom’ then select, the desired PANS PRO Raspberry Pi Image you want to install.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_image_use_custom.png"><img alt="../../../_images/raspberry_pi_image_use_custom.png" src="/docs-assets/_images/raspberry_pi_image_use_custom.png" style="width: 604.8000000000001px; height: 361.6px;"></a>
</div>
<ul class="simple">
<li><p>Choose the correct SD card to install the image on. The drives may be displayed differently on different platforms.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/choose_the_correct_sd_card.png"><img alt="../../../_images/choose_the_correct_sd_card.png" src="/docs-assets/_images/choose_the_correct_sd_card.png" style="width: 604.8000000000001px; height: 359.20000000000005px;"></a>
</div>
<ul class="simple">
<li><p>Take extra care to select the correct drive based on its memory capacity.</p></li>
<li><p>A new <span class="red-text">WRITE</span> button will appear with “once the PANS PRO Raspberry Pi Image and the SD card are selected.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_image_write.png"><img alt="../../../_images/raspberry_pi_image_write.png" src="/docs-assets/_images/raspberry_pi_image_write.png" style="width: 607.2px; height: 360.8px;"></a>
</div>
<ul class="simple">
<li><p>Click the <span class="red-text">WRITE</span> button.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>Writing and finishing up.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Wait for the Raspberry Pi Imager to complete the writing process.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_image_writing.png"><img alt="../../../_images/raspberry_pi_image_writing.png" src="/docs-assets/_images/raspberry_pi_image_writing.png" style="width: 605.6px; height: 362.40000000000003px;"></a>
</div>
<ul class="simple">
<li><p>Once you receive a confirmation message, you can safely eject your SD card.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_image_confirm.png"><img alt="../../../_images/raspberry_pi_image_confirm.png" src="/docs-assets/_images/raspberry_pi_image_confirm.png" style="width: 604.8000000000001px; height: 362.40000000000003px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Getting started with PANS PRO.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Remove the SD card from your computer or laptop and insert it into the Raspberry Pi.</p></li>
<li><p>Make sure your Raspberry Pi is powered on.</p></li>
<li><p>The PANS PRO system is installed and configured to boot with your Raspberry Pi.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Wait for the System to Boot.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Please be patient and allow a few minutes for the entire system to finish booting</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>Connect to the <code class="docutils literal notranslate"><span class="pre">LEAPS-AP</span></code> network broadcasted by the Raspberry Pi with the password <code class="docutils literal notranslate"><span class="pre">Leaps1234</span></code>.</p></li>
<li><p>SSH into the Raspberry Pi (optional).</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>On a PC (or even another Raspberry Pi), open a PowerShell or Terminal window, then enter the following command to connect to the Raspberry Pi via SSH.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">ssh</span> <span class="n">leaps</span><span class="o">@</span><span class="mf">192.168.200.1</span>
</pre></div>
</div>
</li>
<li><p>By default the account is <code class="docutils literal notranslate"><span class="pre">leaps</span></code> and password is <code class="docutils literal notranslate"><span class="pre">leaps</span></code>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>Use <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> to prepare network and determine the <code class="docutils literal notranslate"><span class="pre">network</span> <span class="pre">ID</span></code>.</p></li>
<li><p>Configure and connection with Gateway board.</p></li>
</ol>
<blockquote>
<div><p>11.1. Open the configuration file.</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">sudo nano /usr/share/LEAPS-DOCKER-LINUX/leaps-server-hub/data/leaps-server.conf</span>
</pre></div>
</div>
</div></blockquote>
<p>11.2. Update the LEAPS Server configuration.</p>
<blockquote>
<div><ul class="simple">
<li><p>Change the MQTT API variant to either “pans”:</p></li>
</ul>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">mqtt_api = pans</span>
</pre></div>
</div>
</div></blockquote>
<p>11.3. Restart the LEAPS Server.</p>
<blockquote>
<div><ul class="simple">
<li><p>After saving your changes, restart the services:</p></li>
</ul>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">sudo docker restart leaps_server</span>
</pre></div>
</div>
</div></blockquote>
<p>11.4. Confirm LEAPS Server status.</p>
<blockquote>
<div><ul class="simple">
<li><p>Check the status of the running Docker containers:</p></li>
</ul>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">leaps@raspberrypi:~ $ </span>sudo<span class="w"> </span>docker<span class="w"> </span>ps
<span class="go">CONTAINER ID        IMAGE                           COMMAND                  CREATED        STATUS              PORTS                                                  NAMES</span>
<span class="go">68c33d70bc07        leapslabs/leaps_server:udk    "/app/leaps-server -..." 6 days ago     Up 15 minutes       0.0.0.0:7777-&gt;7777/tcp, 0.0.0.0:7777-&gt;7777/udp, :::7777-&gt;7777/tcp, :::7777-&gt;7777/udp   leaps_server</span>
<span class="go">38092ca7b1b1        leapslabs/leaps_center:udk     "sh -c 'cd /app &amp;&amp; ..." 6 days ago     Up 15 minutes       80/tcp, 0.0.0.0:80-&gt;8080/tcp, [::]:80-&gt;8080/tcp                    leaps_center</span>
</pre></div>
</div>
</div></blockquote>
<p>11.5. Connect Raspberry PI Ethernet directly to the gateway board or to a separate switch with the gateway boards.</p>
<blockquote>
<div><ul class="simple">
<li><p>IP address: 192.168.200.1</p></li>
<li><p>Network mask: 255.255.255.0</p></li>
</ul>
<p>Note: it can be connected to your common switch/router, but IP addresses might conflict. Ethernet configuration of the Raspberry PI is static as follows</p>
</div></blockquote>
<p>11.6. Check the network ID on the gateway boards matches UWB Network. Refer further to the <code class="docutils literal notranslate"><span class="pre">Gateway</span> <span class="pre">Configuration</span></code> in <code class="docutils literal notranslate"><span class="pre">Quick</span> <span class="pre">Start</span> <span class="pre">with</span> <span class="pre">Web</span></code>.</p>
</div></blockquote>
<ol class="arabic simple" start="12">
<li><p>Check system status (optional).</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Use the <span class="red-text">mosquitto_sub</span> command to check the system status. This command will connect to the Mosquitto MQTT broker and display all messages received.</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="13">
<li><p>Access <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>In a web browser, access the address <span class="red-text">192.168.200.1/24</span>. (This can be opened directly on Raspberry Pi or, on a PC that is connected to the <code class="docutils literal notranslate"><span class="pre">LEAPS-AP</span></code> network broadcasted by the Raspberry Pi with the password <code class="docutils literal notranslate"><span class="pre">Leaps1234</span></code> - Step 9)</p></li>
<li><p>If you are on a LAN network, use another computer’s web browser to access the Raspberry Pi’s IP address.</p></li>
<li><p>Configure the network settings in <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> to match the network ID of the gateway board you have connected.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps_center_login.png"><img alt="../../../_images/leaps_center_login.png" src="/docs-assets/_images/leaps_center_login.png" style="width: 762.8000000000001px; height: 360.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="14">
<li><p>Login <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Logging in with Username as <span class="red-text">admin</span> and Password as <span class="red-text">admin</span>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="15">
<li><p>Configure the network on <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Check the network settings in <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> to match the network ID of the gateway board you have connected.</p></li>
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
