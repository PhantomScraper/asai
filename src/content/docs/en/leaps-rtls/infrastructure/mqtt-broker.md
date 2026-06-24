---
title: "MQTT Broker"
lang: en
slug: "leaps-rtls/infrastructure/mqtt-broker"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/infrastructure/mqtt-broker/"
order: 72
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-broker">
<span id="id1"></span><h1>MQTT Broker</h1>
<p>An MQTT broker is a server that receives all client messages and then routes the messages to the appropriate destination clients. An MQTT client is any device (from a microcontroller up to a fully-fledged server) that runs an MQTT library and connects to an MQTT broker over a network.</p>
<p>An open-source MQTT broker, LEAPS Mosquitto is a copy of docker image <a class="reference external" href="https://hub.docker.com/_/eclipse-mosquitto">eclipse-mosquitto:1.5.11</a> with integrated custom <code class="docutils literal notranslate"><span class="pre">mosquitto.conf</span></code> file located in <code class="docutils literal notranslate"><span class="pre">/mosquitto/config/mosquitto.conf</span></code>.
For additional information, please see <a class="reference external" href="https://hub.docker.com/_/eclipse-mosquitto">eclipse-mosquitto</a></p>
<hr class="docutils">
<div class="section" id="installation">
<h2>Installation</h2>
<div class="section" id="system-requirements">
<h3>System requirements</h3>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Docker’s system requirements vary based on the operating system.</p>
<ul class="simple">
<li><p>For Linux, you need a 64-bit architecture, compatible kernel version, and specific kernel features.</p></li>
<li><p>On Windows, use Docker Desktop on Windows 10 with virtualization enabled</p></li>
<li><p>On macOS, use Docker Desktop with macOS 10.13 or newer. In terms of hardware, a minimum of 2GB RAM is recommended, along with sufficient CPU and disk space.</p></li>
</ul>
<p>Refer to <a class="reference external" href="https://docs.docker.com/">Docker</a> official documentation for up-to-date details.</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="instructions">
<h3>Instructions</h3>
<ol class="arabic simple">
<li><p>Install Docker on your PC</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
On Linux</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/linux-install/">Install Docker Desktop on Linux</a></p>
<p>Additionally, you can refer to the following commands to install:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">curl -fsSL https://get.docker.com -o get-docker.sh</span>
<span class="go">sudo sh ./get-docker.sh</span>
<span class="go">sudo usermod -aG docker $USER</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
On Windows</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/">Install Docker Desktop on Windows</a></p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
On macOS</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/mac-install/">Install Docker Desktop on macOS</a></p>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Open a command prompt or terminal window on your PC, then install the LEAPS Mosquitto Docker packages, run:</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 1883:1883/tcp -p 15675:15675 --name some_name leapslabs/leaps_mosquitto:latest mosquitto ---cfg /mosquitto/config/mosquitto.conf</span>
</pre></div>
</div>
<p>where <code class="docutils literal notranslate"><span class="pre">some_name</span></code> is the name you want to assign to your container and <code class="docutils literal notranslate"><span class="pre">tag</span></code> is the tag specifying the <code class="docutils literal notranslate"><span class="pre">leaps-mosquitto</span></code> version you want.</p>
<ul class="simple">
<li><p>Recommended run options</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--user</span> <span class="pre">$(id</span> <span class="pre">-u):$(id</span> <span class="pre">-g)</span></code> Run the instance under a specific user and group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">--restart</span> <span class="pre">unless-stopped</span></code> Restart the instance automatically in case the server crashes.</p></li>
</ul>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>The LEAPS Mosquitto installation process will begin.</p></li>
</ol>
<blockquote>
<div><p>For example, on Ubuntu (Linux):</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 1883:1883/tcp -p 15675:15675 --name leaps_mosquitto leapslabs/leaps_mosquitto:latest mosquitto ---cfg /mosquitto/config/mosquitto.conf</span>

<span class="go">Unable to find image 'leapslabs/leaps_mosquitto:latest' locally</span>
<span class="go">latest: Pulling from leapslabs/leaps_mosquitto</span>
<span class="go">f7dab3ab2d6e: Already exists</span>
<span class="go">2a0a6c9fa787: Already exists</span>
<span class="go">a211eff771d6: Already exists</span>
<span class="go">d362e2a9c11b: Already exists</span>
<span class="go">Digest: sha256:a97752d6e2d81e2701c7cd5f807eb4256322983f8aa3135da8235b647e6a9b4e</span>
<span class="go">Status: Downloaded newer image for leapslabs/leaps_mosquitto:latest</span>
<span class="go">1f526e755ad9a356c439003b93c200802628ae9bc046827e7327d0334804b565</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Verify that the installation is successful, run:</p></li>
</ol>
<blockquote>
<div><p>For example, on Ubuntu (Linux):</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker ps</span>

<span class="go">CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS                          PORTS     NAMES</span>
<span class="go">b1145b72db35   leapslabs/leaps_mosquitto:latest  "sh -c 'cd /app &amp;&amp;  …"   37 seconds ago   11 seconds ago                            leaps_mosquitto</span>
</pre></div>
</div>
</div></blockquote>
<p>So, you have successfully installed and started LEAPS Mosquitto on your PC.</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="getting-started">
<h2>Getting started</h2>
<div class="section" id="leaps-mosquitto-docker">
<h3>LEAPS Mosquitto Docker</h3>
<ul class="simple">
<li><p>Start LEAPS Mosquitto, run: <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">start</span> <span class="pre">leaps_mosquitto</span></code></p></li>
<li><p>Stop LEAPS Mosquitto, run: <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">stop</span> <span class="pre">leaps_mosquitto</span></code></p></li>
<li><p>Restart LEAPS Mosquitto, run: <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_mosquitto</span></code></p></li>
<li><p>Remove LEAPS Mosquitto, run <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">rm</span> <span class="pre">--force</span> <span class="pre">leaps_mosquitto</span></code></p></li>
</ul>
</div>
</div>
<hr class="docutils">
<div class="section" id="customized-options">
<h2>Customized options</h2>
<blockquote>
<div><p><strong>Mandatory options</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>port 1883 - default listener port</p></li>
<li><p>listener 1884 enabling listener at 1884</p></li>
<li><p>listener 15675 enabling listener at 15675</p></li>
</ul>
</div></blockquote>
<p><strong>Recommended options</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>user mosquitto - Drop root priviledges</p></li>
<li><p>max_inflight_messages 200 - increase infighting QoS messages per client as few QoS1 could be sent at once.</p></li>
<li><p>max_queued_messages 1000 - increase the maximum number of QoS 1 and 2 messages to hold in a queue per client above those currently in-flight.</p></li>
<li><p>allow_zero_length_clientid true - allow client ID to be zero lenghth</p></li>
<li><p>persistent_client_expiration 14d - Auto protection from poorly designed clients</p></li>
</ul>
</div></blockquote>
</div></blockquote>
</div>
<div class="section" id="troubleshooting">
<h2>Troubleshooting</h2>
<ul class="simple">
<li><p>Use the following command <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_mosquitto</span></code> to restart LEAPS Mosquitto.</p></li>
<li><p>Check the logs when the LEAPS Mosquitto is running, open the docker desktop, and select the leaps_mosquitto container.</p></li>
</ul>
</div>
</div>


           </div>
