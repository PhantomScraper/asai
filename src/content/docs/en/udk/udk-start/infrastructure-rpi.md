---
title: "LEAPS Raspberry Pi"
lang: en
slug: "udk/udk-start/infrastructure-rpi"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/udk-start/infrastructure-rpi/"
order: 41
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-raspberry-pi">
<span id="leaps-raspberrypi"></span><h1>LEAPS Raspberry Pi</h1>
<p>This page provides:</p>
<blockquote>
<div><ul class="simple">
<li><p>The LEAPS Raspberry Pi package.</p></li>
<li><p>Information about system requirements.</p></li>
<li><p>Instructions on how to install LEAPS Raspberry Pi.</p></li>
</ul>
</div></blockquote>
<p>The installation is fast and easy and only needs to be done once.</p>
<p id="uiraspberrypi"><span class="red-text">Before starting: Remember to back up any important files from the SD card you want to keep, as all data will be permanently overwritten during formatting.</span></p>
<p><strong>System requirements</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>Raspberry Pi 3B or newer.</p></li>
<li><p><em>Recommended: A set of UDK (At least five devices) to verify.</em></p></li>
<li><p><em>Recommended: Batteries or USB-C cables for powering the devices.</em></p></li>
<li><p><em>Recommended:</em> <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>to configure devices.</em></p></li>
</ul>
</div></blockquote>
<p><strong>Setup instructions</strong></p>
<ol class="arabic simple">
<li><p>Download  LEAPS Raspberry Pi Image.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Docker: <a class="reference external" href="https://drive.google.com/file/d/1VmdslvrcuqN7vf6ppKKLfxMA2PENuYtT/view?usp=drive_link">LEAPS-RPI-IMAGE-v1.1.0.zip</a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Extract the LEAPS Raspberry Pi Archive.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Use a program like WinZip or 7-Zip to extract the downloaded LEAPS Raspberry Pi zip file.</p></li>
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
<li><p>Installing the  LEAPS Raspberry Pi Image.</p></li>
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
<li><p>Select ‘Use custom’ then select, the desired  LEAPS Raspberry Pi Image you want to install.</p></li>
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
<li><p>A new <span class="red-text">WRITE</span> button will appear with “once the  LEAPS Raspberry Pi Image and the SD card are selected.</p></li>
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
<li><p>Getting started with LEAPS.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Remove the SD card from your computer or laptop and insert it into the Raspberry Pi.</p></li>
<li><p>Make sure your Raspberry Pi is powered on.</p></li>
<li><p>The LEAPS system is installed and configured to boot with your Raspberry Pi.</p></li>
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
</ol>
<blockquote>
<div><div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/connect_leaps_udk_network.png"><img alt="../../../_images/connect_leaps_udk_network.png" src="/docs-assets/_images/connect_leaps_udk_network.png" style="width: 234.0px; height: 64.5px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
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
<li><p>Use <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> to prepare network.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Configure demo: <a class="reference internal" href="/docs/en/udk/udk-start/twr-rtls-and-data-telemetry-demo#twr-rtls-and-data-telemetry-demo"><span class="std std-ref">TWR RTLS and Data Telemetry Demo</span></a> or <a class="reference internal" href="/docs/en/udk/udk-start/uplink-tdoa-rtls-demo#uplink-tdoa-rtls-demo"><span class="std std-ref">Uplink TDoA RTLS Demo</span></a>.</p></li>
<li><p>By default, the network ID will be <code class="docutils literal notranslate"><span class="pre">0x1234</span></code>.</p></li>
<li><p>For this example, you need to connect the gateway board with ID <code class="docutils literal notranslate"><span class="pre">0x83A2</span></code>.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_network_demo01.jpg"><img alt="../../../_images/raspberry_pi_network_demo01.jpg" src="/docs-assets/_images/raspberry_pi_network_demo01.jpg" style="width: 360.0px; height: 800.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>Connection with Gateway Board.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Connect the gateway board to your Raspberry Pi using a USB-C Data Cable.</p></li>
<li><p>Plug the USB-C Data Cable into the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a> on your PC. Ensure a stable connection.</p></li>
<li><p>Will hear two beeps as a confirmation if successfully connected in gateway mode as confirmation.</p></li>
</ul>
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
</div></blockquote>
<ol class="arabic simple" start="14">
<li><p>Login <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Logging in with Username as <span class="red-text">admin</span> and Password as <span class="red-text">admin</span>.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_leaps_center_login.png"><img alt="../../../_images/raspberry_leaps_center_login.png" src="/docs-assets/_images/raspberry_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="15">
<li><p>Configure the network on <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Check the network settings in <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> to match the network ID of the gateway board you have connected.</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_leaps_center_udk.png"><img alt="../../../_images/raspberry_pi_leaps_center_udk.png" src="/docs-assets/_images/raspberry_pi_leaps_center_udk.png" style="width: 764.4000000000001px; height: 373.20000000000005px;"></a>
</div>
<ul class="simple">
<li><p>Please refer to the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> and <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> for more details on how to use the application to configure and visualize the nodes and network.</p></li>
</ul>
</div></blockquote>
<p>Now the system has been successfully set up and configured the system. Enjoy using it!</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><strong>How to reconfigure with any network</strong></p>
<ol class="arabic simple">
<li><p>Turn Off the LEAPS-AP Wi-Fi AP on Raspberry Pi</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>First, make sure to disable the Wi-Fi Access Point (AP) on your Raspberry Pi.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Connect Raspberry Pi to the Desired Network</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Connect your Raspberry Pi to the Ethernet or Wi-Fi network you want to use.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Check the IP Address</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Open a terminal on your Raspberry Pi and check the IP address with <code class="docutils literal notranslate"><span class="pre">ifconfig</span></code> command</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_check_ip.png"><img alt="../../../_images/raspberry_pi_check_ip.png" src="/docs-assets/_images/raspberry_pi_check_ip.png" style="width: 413.0px; height: 297.5px;"></a>
</div>
<ul class="simple">
<li><p>Note down the IP address; for example, it might be <code class="docutils literal notranslate"><span class="pre">192.168.0.104</span></code>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Update Corresponding IP Address</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Open the configuration file for the LEAPS gateway:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">nano</span> <span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="n">share</span><span class="o">/</span><span class="n">LEAPS</span><span class="o">-</span><span class="n">DOCKER</span><span class="o">-</span><span class="n">LINUX</span><span class="o">/</span><span class="n">leaps</span><span class="o">-</span><span class="n">gateway</span><span class="o">-</span><span class="n">hub</span><span class="o">/</span><span class="n">data</span><span class="o">/</span><span class="n">leaps</span><span class="o">-</span><span class="n">gateway</span><span class="o">.</span><span class="n">conf</span>
</pre></div>
</div>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_leaps_gateway.png"><img alt="../../../_images/raspberry_pi_leaps_gateway.png" src="/docs-assets/_images/raspberry_pi_leaps_gateway.png" style="width: 386.5px; height: 271.0px;"></a>
</div>
</li>
<li><p>Look for the line specifying the IP address and change it to <code class="docutils literal notranslate"><span class="pre">192.168.0.104</span></code>.</p></li>
<li><p>Next, open the configuration file for the LEAPS server:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">nano</span> <span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="n">share</span><span class="o">/</span><span class="n">LEAPS</span><span class="o">-</span><span class="n">DOCKER</span><span class="o">-</span><span class="n">LINUX</span><span class="o">/</span><span class="n">leaps</span><span class="o">-</span><span class="n">server</span><span class="o">-</span><span class="n">hub</span><span class="o">/</span><span class="n">data</span><span class="o">/</span><span class="n">leaps</span><span class="o">-</span><span class="n">server</span><span class="o">.</span><span class="n">conf</span>
</pre></div>
</div>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_leaps_server.png"><img alt="../../../_images/raspberry_pi_leaps_server.png" src="/docs-assets/_images/raspberry_pi_leaps_server.png" style="width: 387.5px; height: 268.5px;"></a>
</div>
</li>
<li><p>Again, update this file to reflect the new IP address <code class="docutils literal notranslate"><span class="pre">192.168.0.104</span></code>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>Restart LEAPS Server and LEAPS Gateway</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>After making the changes, restart both services:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">docker</span> <span class="n">restart</span> <span class="n">leaps_server</span>
</pre></div>
</div>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">docker</span> <span class="n">restart</span> <span class="n">leaps_gateway</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Confirm LEAPS Server and LEAPS Gateway are Working Properly</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Check the status of the running Docker containers:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps@raspberrypi:~ $ sudo docker ps
CONTAINER ID   IMAGE                          COMMAND                  CREATED      STATUS          PORTS                                                                                  NAMES
b5bc1d479a04   leapslabs/leaps_gateway:udk   "/app/leaps-gateway …"   6 days ago   Up 15 minutes                                                                                          leaps_gateway
68c33d70bc07   leapslabs/leaps_server:udk    "/app/leaps-server -…"   6 days ago   Up 15 minutes   0.0.0.0:7777-&gt;7777/tcp, 0.0.0.0:7777-&gt;7777/udp, :::7777-&gt;7777/tcp, :::7777-&gt;7777/udp   leaps_server
38092ca7b1b1   leapslabs/leaps_center:udk    "sh -c 'cd /app &amp;&amp;  …"   6 days ago   Up 15 minutes   80/tcp, 0.0.0.0:80-&gt;8080/tcp, [::]:80-&gt;8080/tcp                                        leaps_center
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Monitor MQTT Messages</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>To monitor MQTT messages, use:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>Open LEAPS Center and Update Host</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Launch the LEAPS Center application and update the host address to <code class="docutils literal notranslate"><span class="pre">192.168.0.104</span></code>.</p></li>
<li><p>Ensure to reload the networks to apply changes.</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_leaps_center_reconfig.png"><img alt="../../../_images/raspberry_pi_leaps_center_reconfig.png" src="/docs-assets/_images/raspberry_pi_leaps_center_reconfig.png" style="width: 764.8000000000001px; height: 372.40000000000003px;"></a>
</div>
<div class="line-block">
<div class="line"><br></div>
</div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><strong>How to Set a Password for Wi-Fi AP: LEAPS-AP</strong></p>
<blockquote>
<div><p>Set the access point security and password on Raspberry Pi OS Bookworm:</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">nmcli</span> <span class="n">con</span> <span class="n">modify</span> <span class="n">hotspot</span> <span class="n">wifi</span><span class="o">-</span><span class="n">sec</span><span class="o">.</span><span class="n">key</span><span class="o">-</span><span class="n">mgmt</span> <span class="n">wpa</span><span class="o">-</span><span class="n">psk</span>
<span class="n">sudo</span> <span class="n">nmcli</span> <span class="n">con</span> <span class="n">modify</span> <span class="n">hotspot</span> <span class="n">wifi</span><span class="o">-</span><span class="n">sec</span><span class="o">.</span><span class="n">psk</span> <span class="s2">"Leaps1234"</span>
</pre></div>
</div>
</div></blockquote>
<p>Setting up an access point on Raspberry Pi OS Bullseye and older:</p>
<blockquote>
<div><ol class="arabic simple">
<li><p>Edit Hostapd Configuration. Open the Hostapd configuration file with this command:</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">nano</span> <span class="o">/</span><span class="n">etc</span><span class="o">/</span><span class="n">hostapd</span><span class="o">/</span><span class="n">hostapd</span><span class="o">.</span><span class="n">conf</span>
</pre></div>
</div>
<ol class="arabic simple" start="2">
<li><p>Add the Following Parameters at the End of the File:</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">wpa</span><span class="o">=</span><span class="mi">2</span>
<span class="n">wpa_passphrase</span><span class="o">=</span><span class="n">Leaps1234</span>
<span class="n">wpa_key_mgmt</span><span class="o">=</span><span class="n">WPA</span><span class="o">-</span><span class="n">PSK</span>
<span class="n">wpa_pairwise</span><span class="o">=</span><span class="n">TKIP</span>
<span class="n">rsn_pairwise</span><span class="o">=</span><span class="n">CCMP</span>
</pre></div>
</div>
<ol class="arabic simple" start="3">
<li><p>Save and Exit</p></li>
</ol>
<blockquote>
<div><p>Press <cite>CTRL + O</cite> to save, then <cite>CTRL + X</cite> to exit the editor.</p>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Restart Your Raspberry Pi</p></li>
</ol>
<blockquote>
<div><p>To apply the changes, restart your Raspberry Pi.</p>
</div></blockquote>
</div></blockquote>
</div></blockquote>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><strong>Step-by-step instructions to expand the filesystem for LEAPS Raspberry Pi (For versions prior to v1.1.0)</strong></p>
<blockquote>
<div><ol class="arabic simple">
<li><p>Open raspi-config. From a terminal on your Raspberry Pi, run:</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">raspi</span><span class="o">-</span><span class="n">config</span>
</pre></div>
</div>
<ol class="arabic simple" start="2">
<li><p>Navigate to Expand Filesystem. Use the arrow keys and Enter:</p></li>
</ol>
<p><code class="docutils literal notranslate"><span class="pre">Advanced</span> <span class="pre">Options</span></code> -&gt; <code class="docutils literal notranslate"><span class="pre">Expand</span> <span class="pre">Filesystem</span></code></p>
<ol class="arabic simple" start="3">
<li><p>Confirm Expansion. Select <code class="docutils literal notranslate"><span class="pre">OK</span></code> when prompted.</p></li>
</ol>
<p>You’ll see a message saying the root filesystem will be expanded on the next reboot</p>
<ol class="arabic simple" start="4">
<li><p>Reboot. When prompted, choose <code class="docutils literal notranslate"><span class="pre">Yes</span></code> to reboot</p></li>
</ol>
<p>(or manually reboot later with <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">reboot</span></code>):</p>
<ol class="arabic simple" start="5">
<li><p>Verify (Optional). After reboot, confirm the disk is fully expanded:</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">df</span> <span class="o">-</span><span class="n">h</span> <span class="o">/</span>
</pre></div>
</div>
</div></blockquote>
</div>
</div>


           </div>
