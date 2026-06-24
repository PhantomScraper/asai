---
title: "LEAPS Center"
lang: en
slug: "pans-pro-rtls/infrastructure/leaps-center"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/infrastructure/leaps-center/"
order: 98
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-center">
<span id="pans-pro-center"></span><h1>LEAPS Center</h1>
<p><a class="reference internal" href="#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a> is a web application that provides device management, network management, and visualization of location and telemetry data for the whole network.</p>
<div class="section" id="key-features">
<h2>Key Features</h2>
<ul class="simple">
<li><p>The Grid in 2D and 3D provides real-time position updates and visualization of the devices in the network.</p></li>
<li><p>Other useful features include User Management, Zone Management, Zone History, Floorplan Management, Position History and Position Heatmap.</p></li>
<li><p>The <a class="reference internal" href="#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a> interconnects with the <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/leaps-server#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a> via the <a class="reference external" href="https://mosquitto.org/">MQTT Broker</a>. It runs as a service on Linux and Windows platforms.</p></li>
</ul>
</div>
<div class="section" id="installation">
<h2>Installation</h2>
<div class="section" id="system-requirements">
<h3>System Requirements</h3>
<p>Docker’s system requirements vary based on the operating system.</p>
<ul class="simple">
<li><p>For Linux, you need a 64-bit architecture, compatible kernel version, and specific kernel features.</p></li>
<li><p>On Windows, use Docker Desktop on Windows 10 with virtualization enabled</p></li>
<li><p>On macOS, use Docker Desktop with macOS 10.13 or newer. In terms of hardware, a minimum of 2GB RAM is recommended, along with sufficient CPU and disk space.</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Refer to <a class="reference external" href="https://docs.docker.com/">Docker</a> official documentation for up-to-date details.</p>
</div>
</div>
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
<li><p>Prepare the configuration package.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Create the leaps_center directory containing the <a class="reference internal" href="#pans-configuration-files"><span class="std std-ref">Configuration files</span></a></p>
<ul>
<li><p>leaps-center-web.conf</p></li>
<li><p>application.properties</p></li>
<li><p>leaps-center-history.properties</p></li>
<li><p>leaps-center-web.properties</p></li>
</ul>
</li>
<li><p>Or you can download the LEAPS Center configuration package (<a class="reference external" href="https://drive.google.com/file/d/1T-TECozBs9O87w4sCUHM1bXtLkd6jvHM/view?usp=drive_link">LEAPS_CENTER_DOCKER.zip</a>).</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Open a command prompt or terminal window on your PC.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Navigate to the directory where you extracted from the LEAPS Center configuration package.</p></li>
</ul>
<p>For example, on Ubuntu (Linux):</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd LEAPS_CENTER_DOCKER/</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Install the LEAPS Center Docker packages, run:</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 80:8080/tcp --name some_name -v /path/to/data/data/:/app/data/ -e LEAPS_CENTER_HOME=/app/data/ leapslabs/leaps_center:tag sh -c "cd /app &amp;&amp;  java -jar leaps-center-web.jar"</span>
</pre></div>
</div>
<p>where <code class="docutils literal notranslate"><span class="pre">some_name</span></code> is the name you want to assign to your container and <code class="docutils literal notranslate"><span class="pre">tag</span></code> is the tag specifying the <code class="docutils literal notranslate"><span class="pre">leaps-center-web</span></code> version you want.</p>
<p>The leaps_center image must operate with an externally mounted folder that contains configuration files and space for application logs and configuration/node history databases.</p>
<p>The option <code class="docutils literal notranslate"><span class="pre">-v</span> <span class="pre">/path/to/data/:/app/data/</span></code> mount the folder located in <code class="docutils literal notranslate"><span class="pre">/path/to/data/</span></code> to internal <code class="docutils literal notranslate"><span class="pre">/app/data</span></code> folder. The data folder must contain the files described below.</p>
<ul class="simple">
<li><p>Recommended run options</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--user</span> <span class="pre">$(id</span> <span class="pre">-u):$(id</span> <span class="pre">-g)</span></code> Run the instance under a specific user and group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">--restart</span> <span class="pre">unless-stopped</span></code> Restart the instance automatically in case the server crashes.</p></li>
</ul>
</li>
<li><p>Optional run options</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--security-opt</span> <span class="pre">seccomp=unconfined</span></code> This option is needed on a  32bit Raspberry Pi image (Raspbian), as it contains an obsolete seccomp library with a bug that negatively affects the Docker image (it won’t be able to connect to the MQTT server). This option allows us to override this issue.</p></li>
</ul>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>The LEAPS Center installation process will begin.</p></li>
</ol>
<blockquote>
<div><p>For example, on Ubuntu (Linux):</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 80:8080/tcp --name leaps_center -v $PWD/leaps_center/:/app/data/ -e LEAPS_CENTER_HOME=/app/data/ leapslabs/leaps_center:latest sh -c "cd /app &amp;&amp;  java -jar leaps-center-web.jar"</span>

<span class="go">Unable to find image 'leapslabs/leaps_center:latest' locally</span>
<span class="go">latest: Pulling from leapslabs/leaps_center</span>
<span class="go">a458657ccc71: Pull complete</span>
<span class="go">Digest: sha256:a19b127656d41d8607f043c2c83924e5b9a5cbd4dc23cfbed070be3b9cfc6b9a</span>
<span class="go">Status: Downloaded newer image for leapslabs/leaps_center:latest</span>
<span class="go">320d3768289874e063619f75faca7a24dd75a08884df8cd8fb2cc9b54c6f0a46</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Verify that the installation is successful, run:</p></li>
</ol>
<blockquote>
<div><p>For example, on Ubuntu (Linux):</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker ps</span>

<span class="go">CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS                          PORTS     NAMES</span>
<span class="go">b1145b72db35   leapslabs/leaps_center:latest   "sh -c 'cd /app &amp;&amp;  …"   37 seconds ago   11 seconds ago                            leaps_center</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Open a web browser and enter the following <a class="reference external" href="http://localhost:80">http://localhost:80</a>; The LEAPS Center application will load in a web browser.</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/lc_login.png"><img alt="../../../_images/lc_login.png" class="align-center" src="/docs-assets/_images/lc_login.png" style="width: 716.4px; height: 520.2px;"></a>
</div></blockquote>
<p>So, you have successfully installed and started LEAPS Center on your PC.</p>
</div>
</div>
<div class="section" id="configuration-files">
<span id="pans-configuration-files"></span><h2>Configuration files</h2>
<ul>
<li><p>leaps-center-web.conf</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">JAVA_OPTS="-Xms256m -Xmx512m -Xss256k"</span>
</pre></div>
</div>
</li>
<li><p>application.properties</p></li>
<li><p>leaps-center-history.properties</p></li>
<li><p>leaps-center-web.properties</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
application.properties</label><div class="sd-tab-content docutils">
<p>This configuration file controls application logging.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">spring.main.banner-mode=OFF</span>

<span class="go">logging.level.root=OFF</span>
<span class="go">logging.level.global.leaps.center.mqtt=OFF</span>
<span class="go">logging.level.global.leaps.center.init=OFF</span>
<span class="go">logging.level.global.leaps.center.service=OFF</span>
<span class="go">logging.level.global.leaps.center.history.filter=OFF</span>
<span class="go">logging.level.global.leaps.center.history.service=OFF</span>
<span class="go">logging.level.global.leaps.center.history=OFF</span>
<span class="go">logging.level.global.leaps.center.web.component=OFF</span>
<span class="go">logging.level.global.leaps.center.web.rest=OFF</span>
<span class="go">logging.level.global.leaps.center.web.sse=OFF</span>
<span class="go">logging.level.global.leaps.center.web=OFF</span>
<span class="go">logging.level.global.leaps.center=OFF</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
leaps-center-history.properties</label><div class="sd-tab-content docutils">
<p>This configuration file controls the node position history logging.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">#</span>
<span class="gp">#       </span>LEAPS<span class="w"> </span>-<span class="w"> </span>Low<span class="w"> </span>Energy<span class="w"> </span>Accurate<span class="w"> </span>Positioning<span class="w"> </span>System<span class="w"> </span>-<span class="w"> </span>LEAPS<span class="w"> </span>Center.
<span class="gp">#</span>
<span class="gp">#       </span>Copyright<span class="w"> </span><span class="o">(</span>c<span class="o">)</span><span class="w"> </span><span class="m">2016</span>-2021,<span class="w"> </span>LEAPS.
<span class="gp">#</span>
<span class="gp">#       </span>Licensed<span class="w"> </span>under<span class="w"> </span>the<span class="w"> </span>Apache<span class="w"> </span>License,<span class="w"> </span>Version<span class="w"> </span><span class="m">2</span>.0<span class="w"> </span><span class="o">(</span>the<span class="w"> </span><span class="s2">"License"</span><span class="o">)</span><span class="p">;</span>
<span class="gp">#       </span>You<span class="w"> </span>may<span class="w"> </span>not<span class="w"> </span>use<span class="w"> </span>this<span class="w"> </span>file<span class="w"> </span>except<span class="w"> </span><span class="k">in</span><span class="w"> </span>compliance<span class="w"> </span>with<span class="w"> </span>the<span class="w"> </span>License.
<span class="gp">#       </span>You<span class="w"> </span>may<span class="w"> </span>obtain<span class="w"> </span>a<span class="w"> </span>copy<span class="w"> </span>of<span class="w"> </span>the<span class="w"> </span>License<span class="w"> </span>at
<span class="gp">#</span>
<span class="gp">#       </span>http://www.apache.org/licenses/LICENSE-2.0
<span class="gp">#</span>
<span class="gp">#       </span>Unless<span class="w"> </span>required<span class="w"> </span>by<span class="w"> </span>applicable<span class="w"> </span>law<span class="w"> </span>or<span class="w"> </span>agreed<span class="w"> </span>to<span class="w"> </span><span class="k">in</span><span class="w"> </span>writing,<span class="w"> </span>software
<span class="gp">#       </span>distributed<span class="w"> </span>under<span class="w"> </span>the<span class="w"> </span>License<span class="w"> </span>is<span class="w"> </span>distributed<span class="w"> </span>on<span class="w"> </span>an<span class="w"> </span><span class="s2">"AS IS"</span><span class="w"> </span>BASIS,
<span class="gp">#       </span>WITHOUT<span class="w"> </span>WARRANTIES<span class="w"> </span>OR<span class="w"> </span>CONDITIONS<span class="w"> </span>OF<span class="w"> </span>ANY<span class="w"> </span>KIND,<span class="w"> </span>either<span class="w"> </span>express<span class="w"> </span>or<span class="w"> </span>implied.
<span class="gp">#       </span>See<span class="w"> </span>the<span class="w"> </span>License<span class="w"> </span><span class="k">for</span><span class="w"> </span>the<span class="w"> </span>specific<span class="w"> </span>language<span class="w"> </span>governing<span class="w"> </span>permissions<span class="w"> </span>and
<span class="gp">#       </span>limitations<span class="w"> </span>under<span class="w"> </span>the<span class="w"> </span>License.
<span class="gp">#</span>

<span class="gp"># </span><span class="nb">history</span><span class="w"> </span>enabled<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="go">history.enabled=false</span>
<span class="go">history.position.enabled=true</span>
<span class="go">history.zone.enabled=true</span>

<span class="gp"># </span>use<span class="w"> </span>node<span class="w"> </span>position<span class="w"> </span>message<span class="w"> </span>timestamp<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">true</span><span class="o">)</span>
<span class="go">history.use.position.timestamp=false</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>Export<span class="w"> </span><span class="nv">Options</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>

<span class="gp"># </span>add<span class="w"> </span>headers<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="go">history.export.headers=false</span>

<span class="gp"># </span>maximum<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>records<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">1000000</span><span class="o">)</span>
<span class="go">history.export.max.lines=1000000</span>

<span class="gp"># </span>compress<span class="w"> </span><span class="nb">export</span><span class="w"> </span>file<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">true</span><span class="o">)</span>
<span class="go">history.export.compress=true</span>

<span class="gp"># </span>number<span class="w"> </span>of<span class="w"> </span>decimal<span class="w"> </span>places<span class="w"> </span><span class="k">for</span><span class="w"> </span>x,<span class="w"> </span>y,<span class="w"> </span>z<span class="w"> </span>values<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">4</span><span class="o">)</span>
<span class="go">history.export.position.decimal.places=2</span>

<span class="gp"># </span>format<span class="w"> </span>network<span class="w"> </span>id<span class="w"> </span>to<span class="w"> </span>hex<span class="w"> </span>value<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">true</span><span class="o">)</span>
<span class="go">history.export.hex.network.id=true</span>

<span class="gp"># </span>format<span class="w"> </span>node<span class="w">  </span>ID<span class="w"> </span>to<span class="w"> </span>hex<span class="w"> </span>value<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">true</span><span class="o">)</span>
<span class="go">history.export.hex.node.id=true</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>Position<span class="w"> </span>History<span class="w"> </span><span class="nv">Options</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>

<span class="gp"># </span>interval<span class="w"> </span><span class="nb">time</span><span class="w"> </span>to<span class="w"> </span>add<span class="w"> </span>a<span class="w"> </span><span class="nb">history</span><span class="w"> </span>record<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">10000</span><span class="o">)</span>
<span class="go">history.node.position.interval.time=10000</span>

<span class="gp"># </span>minimun<span class="w"> </span>quality<span class="w"> </span>value<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">0</span><span class="o">)</span>
<span class="go">history.node.position.min.quality=0</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>Heatmap<span class="w"> </span><span class="nv">Options</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>maximum<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>records<span class="w"> </span><span class="k">for</span><span class="w"> </span>heatmap<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">100000</span><span class="o">)</span>
<span class="go">heatmap.max.results=100000</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>Purge<span class="w"> </span><span class="nv">Options</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>

<span class="gp"># </span><span class="nb">time</span><span class="w"> </span>to<span class="w"> </span>purge<span class="w"> </span>database<span class="w"> </span>records<span class="w"> </span><span class="k">in</span><span class="w"> </span>days<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">30</span><span class="w"> </span>days<span class="o">)</span>
<span class="go">history.purge.time=30</span>

<span class="gp"># </span>backup<span class="w"> </span>purged<span class="w"> </span>records<span class="w"> </span>to<span class="w"> </span>a<span class="w"> </span>file<span class="w"> </span><span class="k">in</span><span class="w"> </span>/history<span class="w"> </span>folder<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="go">history.purge.backup.records=true</span>

<span class="gp"># </span>max<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>backup<span class="w"> </span>files<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">10</span><span class="o">)</span>
<span class="go">history.purge.max.backup.files=5</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>DBMS<span class="w"> </span><span class="o">(</span>SQLITE,<span class="w"> </span>POSTGRESQL,<span class="w"> </span>MY_SQL,<span class="w"> </span>ORACLE,<span class="w"> </span>SQL_SERVER<span class="w"> </span>or<span class="w"> </span>CUSTOM<span class="o">)</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>SQLite<span class="w"> </span>Database<span class="w"> </span>Example<span class="w"> </span><span class="o">(</span>default<span class="o">)</span>.
<span class="gp"># </span>history.dbms<span class="o">=</span>SQLITE
<span class="gp"># </span>history.db.jdbc.url<span class="o">=</span>jdbc:sqlite:leaps-center-history.db
<span class="gp"># </span>history.db.username<span class="o">=</span>
<span class="gp"># </span>history.db.password<span class="o">=</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>PostgreSQL<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>history.dbms<span class="o">=</span>POSTGRESQL
<span class="gp"># </span>history.db.jdbc.url<span class="o">=</span>jdbc:postgresql://localhost:5432/leaps_center_history
<span class="gp"># </span>history.db.username<span class="o">=</span>leaps_center
<span class="gp"># </span>history.db.password<span class="o">=</span><span class="nb">pwd</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>Oracle<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>Important!<span class="w"> </span>To<span class="w"> </span>use<span class="w"> </span>Oracle<span class="w"> </span>DBMS<span class="w"> </span>is<span class="w"> </span>mandatory<span class="w"> </span>to<span class="w"> </span>change<span class="w"> </span>global.leaps.center.history.entity.NetworkNodeHistory.id<span class="w"> </span>@Id<span class="w"> </span>generation<span class="w"> </span>strategy<span class="w"> </span>to<span class="w"> </span>GenerationType.AUTO<span class="w"> </span>or<span class="w"> </span>GenerationType.SEQUENCE.<span class="w"> </span>Oracle<span class="w"> </span>does<span class="w"> </span>not<span class="w"> </span>support<span class="w"> </span>GenerationType.IDENTITY.
<span class="gp"># </span>history.dbms<span class="o">=</span>ORACLE
<span class="gp"># </span>history.db.hibernate.dialect<span class="o">=</span>org.hibernate.dialect.Oracle10gDialect
<span class="gp"># </span>history.db.jdbc.url<span class="o">=</span>jdbc:oracle:thin:@127.0.0.1:1521/XE
<span class="gp"># </span>history.db.username<span class="o">=</span>leaps_center
<span class="gp"># </span>history.db.password<span class="o">=</span><span class="nb">pwd</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>MySQL<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>history.dbms<span class="o">=</span>MY_SQL
<span class="gp"># </span>history.db.jdbc.url<span class="o">=</span>jdbc:mysql://localhost:3306/leaps_center
<span class="gp"># </span>history.db.username<span class="o">=</span>leaps_center
<span class="gp"># </span>history.db.password<span class="o">=</span><span class="nb">pwd</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>SQL<span class="w"> </span>Server<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>TODO:<span class="w"> </span>It<span class="w"> </span>needs<span class="w"> </span>to<span class="w"> </span>be<span class="w"> </span>tested.
<span class="gp"># </span>history.dbms<span class="o">=</span>SQL_SERVER
<span class="gp"># </span>history.db.jdbc.url<span class="o">=</span>jdbc:sqlserver://localhost:1433<span class="p">;</span><span class="nv">databaseName</span><span class="o">=</span>leaps_center_history<span class="p">;</span><span class="nv">integratedSecurity</span><span class="o">=</span><span class="nb">true</span>
<span class="gp"># </span>history.db.jdbc.url<span class="o">=</span>jdbc:jtds:sqlserver://localhost:1433/leaps_center_history<span class="p">;</span><span class="nv">instance</span><span class="o">=</span>SQLEXPRESS<span class="p">;</span>
<span class="gp"># </span>history.db.username<span class="o">=</span>leaps_center
<span class="gp"># </span>history.db.password<span class="o">=</span><span class="nb">pwd</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>Custom<span class="w"> </span>Database
<span class="gp"># </span>history.dbms<span class="o">=</span>CUSTOM

<span class="gp"># </span>Hibernate<span class="w"> </span>Dialect
<span class="gp"># </span>history.db.hibernate.dialect<span class="o">=</span>org.hibernate.dialect.PostgreSQLDialect

<span class="gp"># </span>JDBC<span class="w"> </span>driver<span class="w"> </span>class
<span class="gp"># </span>history.db.jdbc.driver.class<span class="o">=</span>org.postgresql.Driver
</pre></div>
</div>
</div>
<input id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
leaps-center-web.properties</label><div class="sd-tab-content docutils">
<p>This configuration file controls leaps_center application.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">#</span>
<span class="gp">#       </span>LEAPS<span class="w"> </span>-<span class="w"> </span>Low<span class="w"> </span>Energy<span class="w"> </span>Accurate<span class="w"> </span>Positioning<span class="w"> </span>System<span class="w"> </span>-<span class="w"> </span>LEAPS<span class="w"> </span>Center.
<span class="gp">#</span>
<span class="gp">#       </span>Copyright<span class="w"> </span><span class="o">(</span>c<span class="o">)</span><span class="w"> </span><span class="m">2016</span>-2021,<span class="w"> </span>LEAPS.
<span class="gp">#</span>
<span class="gp">#       </span>Licensed<span class="w"> </span>under<span class="w"> </span>the<span class="w"> </span>Apache<span class="w"> </span>License,<span class="w"> </span>Version<span class="w"> </span><span class="m">2</span>.0<span class="w"> </span><span class="o">(</span>the<span class="w"> </span><span class="s2">"License"</span><span class="o">)</span><span class="p">;</span>
<span class="gp">#       </span>you<span class="w"> </span>may<span class="w"> </span>not<span class="w"> </span>use<span class="w"> </span>this<span class="w"> </span>file<span class="w"> </span>except<span class="w"> </span><span class="k">in</span><span class="w"> </span>compliance<span class="w"> </span>with<span class="w"> </span>the<span class="w"> </span>License.
<span class="gp">#       </span>You<span class="w"> </span>may<span class="w"> </span>obtain<span class="w"> </span>a<span class="w"> </span>copy<span class="w"> </span>of<span class="w"> </span>the<span class="w"> </span>License<span class="w"> </span>at
<span class="gp">#</span>
<span class="gp">#       </span>http://www.apache.org/licenses/LICENSE-2.0
<span class="gp">#</span>
<span class="gp">#       </span>Unless<span class="w"> </span>required<span class="w"> </span>by<span class="w"> </span>applicable<span class="w"> </span>law<span class="w"> </span>or<span class="w"> </span>agreed<span class="w"> </span>to<span class="w"> </span><span class="k">in</span><span class="w"> </span>writing,<span class="w"> </span>software
<span class="gp">#       </span>distributed<span class="w"> </span>under<span class="w"> </span>the<span class="w"> </span>License<span class="w"> </span>is<span class="w"> </span>distributed<span class="w"> </span>on<span class="w"> </span>an<span class="w"> </span><span class="s2">"AS IS"</span><span class="w"> </span>BASIS,
<span class="gp">#       </span>WITHOUT<span class="w"> </span>WARRANTIES<span class="w"> </span>OR<span class="w"> </span>CONDITIONS<span class="w"> </span>OF<span class="w"> </span>ANY<span class="w"> </span>KIND,<span class="w"> </span>either<span class="w"> </span>express<span class="w"> </span>or<span class="w"> </span>implied.
<span class="gp">#       </span>See<span class="w"> </span>the<span class="w"> </span>License<span class="w"> </span><span class="k">for</span><span class="w"> </span>the<span class="w"> </span>specific<span class="w"> </span>language<span class="w"> </span>governing<span class="w"> </span>permissions<span class="w"> </span>and
<span class="gp">#       </span>limitations<span class="w"> </span>under<span class="w"> </span>the<span class="w"> </span>License.
<span class="gp">#</span>

<span class="gp"># </span>database<span class="w"> </span><span class="o">(</span>SQLITE,<span class="w"> </span>POSTGRESQL,<span class="w"> </span>MY_SQL,<span class="w"> </span>ORACLE,<span class="w"> </span>SQL_SERVER<span class="w"> </span>or<span class="w"> </span>CUSTOM<span class="o">)</span>
<span class="go">db.dbms=SQLITE</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>SQLite<span class="w"> </span>Database<span class="w"> </span>Example.
<span class="gp"># </span><span class="nv">dbms</span><span class="o">=</span>SQLITE
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:sqlite:leaps-center-db
<span class="gp"># </span>db.username<span class="o">=</span>
<span class="gp"># </span>db.password<span class="o">=</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>PostgreSQL<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>db.dbms<span class="o">=</span>POSTGRESQL
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:postgresql://localhost:5432/leaps_center
<span class="gp"># </span>db.username<span class="o">=</span>postgres
<span class="gp"># </span>db.password<span class="o">=</span>qwe123

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>Oracle<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>Important!<span class="w"> </span>To<span class="w"> </span>use<span class="w"> </span>Oracle<span class="w"> </span>DBMS<span class="w"> </span>is<span class="w"> </span>mandatory<span class="w"> </span>to<span class="w"> </span>change<span class="w"> </span>global.leaps.center.entity.NetworkNodeHistory.id<span class="w"> </span>@Id<span class="w"> </span>generation<span class="w"> </span>strategy<span class="w"> </span>to<span class="w"> </span>GenerationType.AUTO<span class="w"> </span>or<span class="w"> </span>GenerationType.SEQUENCE.<span class="w"> </span>Oracle<span class="w"> </span>does<span class="w"> </span>not<span class="w"> </span>support<span class="w"> </span>GenerationType.IDENTITY.
<span class="gp"># </span>db.dbms<span class="o">=</span>ORACLE
<span class="gp"># </span>db.hibernate.dialect<span class="o">=</span>org.hibernate.dialect.Oracle10gDialect
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:oracle:thin:@127.0.0.1:1521/XE
<span class="gp"># </span>db.username<span class="o">=</span>leaps_center
<span class="gp"># </span>db.password<span class="o">=</span>q1w2e3r4t5

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>MySQL<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>db.dbms<span class="o">=</span>MY_SQL
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:mysql://localhost:3306/leaps_center
<span class="gp"># </span>db.username<span class="o">=</span>root
<span class="gp"># </span>db.password<span class="o">=</span>qwe123

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>SQL<span class="w"> </span>Server<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>db.dbms<span class="o">=</span>SQL_SERVER
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:sqlserver://localhost:1433<span class="p">;</span><span class="nv">databaseName</span><span class="o">=</span>leaps_center_history<span class="p">;</span><span class="nv">integratedSecurity</span><span class="o">=</span><span class="nb">true</span>
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:jtds:sqlserver://localhost:1433/leaps_center_history<span class="p">;</span><span class="nv">instance</span><span class="o">=</span>SQLEXPRESS<span class="p">;</span>
<span class="gp"># </span>db.username<span class="o">=</span>leaps_center
<span class="gp"># </span>db.password<span class="o">=</span>qwe123

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>Custom<span class="w"> </span>Database
<span class="gp"># </span>db.dbms<span class="o">=</span>CUSTOM

<span class="gp"># </span>Hibernate<span class="w"> </span>Dialect
<span class="gp"># </span>db.hibernate.dialect<span class="o">=</span>org.hibernate.dialect.PostgreSQLDialect

<span class="gp"># </span>JDBC<span class="w"> </span>driver<span class="w"> </span>class
<span class="gp"># </span>history.db.jdbc.driver.class<span class="o">=</span>org.postgresql.Driver
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:postgresql://localhost:5432/leaps_center
<span class="gp"># </span>db.username<span class="o">=</span>postgres
<span class="gp"># </span>db.password<span class="o">=</span>qwe123
<span class="gp"># </span>db.jdbc.driver.class<span class="o">=</span>
<span class="gp"># </span>db.hibernate.dialect<span class="o">=</span>

<span class="gp"># </span>show<span class="w"> </span>sql<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="gp"># </span>db.jpa.show-sql<span class="o">=</span><span class="nb">false</span>

<span class="gp"># </span>format<span class="w"> </span>sql<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="gp"># </span>db.jpa.format-sql<span class="o">=</span><span class="nb">false</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span><span class="nv">network</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>

<span class="gp"># </span><span class="nb">enable</span><span class="w"> </span>the<span class="w"> </span>registration<span class="w"> </span>of<span class="w"> </span>networks<span class="w"> </span>with<span class="w"> </span>mqtt<span class="w"> </span>connection<span class="w"> </span><span class="nb">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>HOST.<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">true</span><span class="o">)</span>
<span class="go">network.mqtt.connection.by.host.enabled=true</span>

<span class="gp"># </span><span class="nb">enable</span><span class="w"> </span>the<span class="w"> </span>registration<span class="w"> </span>of<span class="w"> </span>networks<span class="w"> </span>with<span class="w"> </span>mqtt<span class="w"> </span>connection<span class="w"> </span><span class="nb">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>PAN_ID.<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="go">network.mqtt.connection.by.network.id.enable=false</span>

<span class="gp"># </span><span class="nb">enable</span><span class="w"> </span>the<span class="w"> </span>registration<span class="w"> </span>of<span class="w"> </span>networks<span class="w"> </span>with<span class="w"> </span>web<span class="w"> </span>client<span class="w"> </span>connection<span class="w"> </span>by<span class="w"> </span>websocket.<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="go">network.web.client.connection.by.web.socket=false</span>

<span class="gp"># </span>create<span class="w"> </span>the<span class="w"> </span>default<span class="w"> </span>network<span class="w"> </span><span class="k">if</span><span class="w"> </span>it<span class="w"> </span>does<span class="w"> </span>not<span class="w"> </span>exist<span class="w"> </span>when<span class="w"> </span>starting.<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">true</span><span class="o">)</span>
<span class="go">network.create.default.network=true</span>
<span class="gp"># </span>network.create.default.floor.plan<span class="o">=</span><span class="nb">true</span>

<span class="go">network.default.id=</span>
<span class="go">network.default.name=Default</span>

<span class="gp"># </span>PAN_ID<span class="w"> </span>or<span class="w"> </span>HOST
<span class="go">network.default.mqtt.connection.type=HOST</span>

<span class="gp"># </span>WS<span class="w"> </span>or<span class="w"> </span>SSE
<span class="go">network.default.web.client.connection.type=SSE</span>

<span class="gp"># </span>MQTT
<span class="go">mqtt.host=</span>
<span class="go">mqtt.ws.port=15675</span>
<span class="go">mqtt.tcp.port=1883</span>
<span class="go">mqtt.username=dwmuser</span>
<span class="go">mqtt.password=dwmuser</span>
<span class="gp"># </span>Enable/Disable<span class="w"> </span>TLS
<span class="gp">#</span>mqtt.tls<span class="o">=</span>
<span class="gp"># </span>CA_SIGNED_CERTIFICATE<span class="w"> </span><span class="o">(</span>signed<span class="w"> </span>by<span class="w"> </span>a<span class="w"> </span>publicly<span class="w"> </span>trusted<span class="w"> </span>CA<span class="o">)</span>,<span class="w"> </span>CA_FILE_CERTIFICATE<span class="w"> </span><span class="o">(</span>file<span class="w"> </span>certificate<span class="o">)</span><span class="p">;</span>
<span class="gp">#</span>mqtt.tls.certificate.type<span class="o">=</span>CA_SIGNED_CERTIFICATE
<span class="gp"># </span>TLS<span class="w"> </span>Protocol:<span class="w"> </span>TLS_V1<span class="w"> </span><span class="o">(</span>TLSv1<span class="o">)</span>,<span class="w"> </span>TLS_V1_1<span class="w"> </span><span class="o">(</span>TLSv1.1<span class="o">)</span>,<span class="w"> </span>TLS_V1_2<span class="w"> </span><span class="o">(</span>TLSv1.2<span class="o">)</span>,<span class="w"> </span>TLS_V1_3<span class="o">(</span>TLSv1.3<span class="o">)</span><span class="p">;</span>
<span class="gp">#</span>mqtt.tls.protocol<span class="o">=</span>TLS_V1_2
<span class="gp">#</span>mqtt.tls.certificate.file<span class="o">=</span>/user/.../leaps-center.crt
<span class="go">mqtt.topic.prefix=dwm</span>
<span class="go">mqtt.tag.topic.prefix=node</span>
<span class="go">mqtt.anchor.topic.prefix=node</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>floorplan<span class="w"> </span><span class="nv">settings</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>size<span class="w"> </span><span class="k">in</span><span class="w"> </span>pixels<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">2048</span><span class="o">)</span>
<span class="go">floorplan.max.image.dimension.size=2048</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>scene<span class="w"> </span><span class="nv">settings</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>size<span class="w"> </span><span class="k">in</span><span class="w"> </span>cm<span class="w"> </span><span class="o">(</span>default<span class="w"> </span>50cm<span class="o">)</span>
<span class="go">scene.grid.size=50</span>
<span class="gp"># </span>color<span class="w"> </span><span class="k">in</span><span class="w"> </span>int<span class="w"> </span><span class="o">(</span>default<span class="w"> </span>0xD8D8D8<span class="o">)</span>
<span class="go">scene.grid.color=0xD8D8D8</span>
<span class="gp"># </span>max<span class="w"> </span>grid<span class="w"> </span>visibility<span class="w"> </span>distance<span class="w"> </span><span class="k">in</span><span class="w"> </span>meters<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">100</span><span class="o">)</span>
<span class="go">scene.grid.max.visibility.distance=100</span>
<span class="gp"># </span>zoom<span class="w"> </span>min<span class="w"> </span><span class="k">in</span><span class="w"> </span>meters<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">2</span><span class="o">)</span>
<span class="go">scene.zoom.min=2</span>
<span class="gp"># </span>zoom<span class="w"> </span>max<span class="w"> </span><span class="k">in</span><span class="w"> </span>meters<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">100</span><span class="o">)</span>
<span class="go">scene.zoom.max=100</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>web<span class="w"> </span>server<span class="w"> </span><span class="nv">settings</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>

<span class="gp"># </span>http<span class="w"> </span>session<span class="w"> </span>timeout
<span class="go">server.servlet.session.timeout=120m</span>

<span class="gp"># </span>maximum<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>http<span class="w"> </span>sessions<span class="w"> </span>per<span class="w"> </span>user<span class="w"> </span><span class="o">(</span>-1<span class="w"> </span>is<span class="w"> </span>unlimited<span class="o">)</span>
<span class="go">server.max.sessions.per.user=-1</span>

<span class="gp"># </span>mod-jk/ajp<span class="w"> </span>connector<span class="w"> </span>configuration
<span class="go">tomcat.ajp.enabled=false</span>
<span class="gp"># </span>tomcat.ajp.port<span class="o">=</span><span class="m">8009</span>
<span class="gp"># </span>tomcat.ajp.secret.required<span class="o">=</span><span class="nb">false</span>
<span class="gp"># </span>tomcat.apr.enabled<span class="o">=</span><span class="nb">false</span>

<span class="gp"># </span>server<span class="w"> </span>port<span class="w"> </span><span class="o">(</span><span class="m">2</span>-65535<span class="o">)</span>
<span class="go">server.port=8080</span>

<span class="gp"># </span><span class="nb">enable</span><span class="w"> </span>/<span class="w"> </span>disable<span class="w"> </span>https
<span class="go">server.ssl.enabled=false</span>
<span class="gp"># </span>keystore<span class="w"> </span>format
<span class="gp"># </span>server.ssl.key-store-type<span class="o">=</span>PKCS12
<span class="gp"># </span>keystore<span class="w"> </span>location
<span class="gp"># </span>server.ssl.key-store<span class="o">=</span>D:<span class="se">\\</span>Leaps<span class="se">\\</span>tls<span class="se">\\</span>springboot.p12
<span class="gp"># </span>keystore<span class="w"> </span><span class="nb">alias</span>
<span class="gp"># </span>server.ssl.key-alias<span class="o">=</span>springboot
<span class="gp"># </span>keystore<span class="w"> </span>password
<span class="gp"># </span>server.ssl.key-store-password<span class="o">=</span>password
<span class="gp"># </span>SSL<span class="w"> </span>protocol<span class="w"> </span>to<span class="w"> </span>use
<span class="gp"># </span>server.ssl.protocol<span class="o">=</span>TLS
<span class="gp"># </span>Enabled<span class="w"> </span>SSL<span class="w"> </span>protocols
<span class="gp"># </span>server.ssl.enabled-protocols<span class="o">=</span>TLSv1.2
</pre></div>
</div>
</div>
</div>
</li>
</ul>
</div>
<div class="section" id="getting-started">
<h2>Getting Started</h2>
<blockquote>
<div><p>By default, a login account with the user name is <span class="red-text">admin</span> and password is <span class="red-text">admin</span>.</p>
</div></blockquote>
<div class="section" id="leaps-server-docker">
<h3>LEAPS Server Docker</h3>
<ul class="simple">
<li><p>Start LEAPS Center, run: <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">start</span> <span class="pre">leaps_center</span></code></p></li>
<li><p>Stop LEAPS Center, run: <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">stop</span> <span class="pre">leaps_center</span></code></p></li>
<li><p>Restart LEAPS Center, run: <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_center</span></code></p></li>
<li><p>Remove LEAPS Center, run <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">rm</span> <span class="pre">--force</span> <span class="pre">leaps_center</span></code></p></li>
</ul>
</div>
<div class="section" id="network-configurations">
<h3>Network Configurations</h3>
<blockquote>
<div><p>To configure the network, go to the menu and select  the <span class="red-text">Networks</span>.</p>
<a class="reference internal image-reference" href="../../../_images/lc_select_networks.png"><img alt="../../../_images/lc_select_networks.png" class="align-center" src="/docs-assets/_images/lc_select_networks.png" style="width: 720.0px; height: 564.3000000000001px;"></a>
<p>The Network management dialog will pop up. A localhost network will  already be  set up by default with network ID 0x1234.</p>
<a class="reference internal image-reference" href="../../../_images/lc_list_networks.png"><img alt="../../../_images/lc_list_networks.png" class="align-center" src="/docs-assets/_images/lc_list_networks.png" style="width: 1023.3000000000001px; height: 333.0px;"></a>
<p>To create a new network, click  the <span class="red-text">Add</span> button in the bottom right.</p>
<p>Now, fill in the required configuration parameters:</p>
<blockquote>
<div><blockquote>
<div><ul class="simple">
<li><p>Name</p></li>
<li><p>Network Type</p></li>
<li><p>Host</p></li>
<li><p>TCP Port</p></li>
<li><p>Username</p></li>
<li><p>Topic Prefix</p></li>
</ul>
</div></blockquote>
<p>Once you’ve filled in everything, click the <span class="red-text">Save</span> button to connect and receive the network ID.</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/lc_config_networks_1234.png"><img alt="../../../_images/lc_config_networks_1234.png" class="align-center" src="/docs-assets/_images/lc_config_networks_1234.png" style="width: 704.7px; height: 763.2px;"></a>
</div></blockquote>
</div></blockquote>
<p>If you don’t know the network ID, you can use <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> or Shell to find it.</p>
<p>Finally, you can click the <span class="red-text">Test</span> button to check the connection and then click the <span class="red-text">Save</span> button to save your configuration.</p>
</div></blockquote>
</div>
<div class="section" id="node-configurations">
<h3>Node Configurations</h3>
<p>To configure a node, you need to assign the node to a specific network in advance.</p>
<p>Select the network with the specified node to view network details. Then, you can start configure the node.</p>
<p>For a node that can be configured as a gateway, anchor, or tag node, please refer to the details below</p>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-6" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
Gateway</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_config_gateway.png"><img alt="../../../_images/lc_config_gateway.png" class="align-center" src="/docs-assets/_images/lc_config_gateway.png" style="width: 702.0px; height: 738.9px;"></a>
</div>
<input id="sd-tab-item-7" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
Anchor</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_config_anchor.png"><img alt="../../../_images/lc_config_anchor.png" class="align-center" src="/docs-assets/_images/lc_config_anchor.png" style="width: 712.8000000000001px; height: 512.1px;"></a>
</div>
<input id="sd-tab-item-8" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-8">
Tag</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_config_tag.png"><img alt="../../../_images/lc_config_tag.png" class="align-center" src="/docs-assets/_images/lc_config_tag.png" style="width: 712.8000000000001px; height: 540.9px;"></a>
</div>
</div>
</div></blockquote>
</div>
<div class="section" id="floor-plans">
<h3>Floor Plans</h3>
<blockquote>
<div><p>To configure the floor plans, go to the menu and select the <span class="red-text">Floor Plans</span>.</p>
<a class="reference internal image-reference" href="../../../_images/lc_menu.png"><img alt="../../../_images/lc_menu.png" class="align-center" src="/docs-assets/_images/lc_menu.png" style="width: 218.70000000000002px; height: 392.40000000000003px;"></a>
<p>Click the <span class="red-text">Add</span> button in the bottom right.</p>
<a class="reference internal image-reference" href="../../../_images/lc_floor_plans_add.png"><img alt="../../../_images/lc_floor_plans_add.png" class="align-center" src="/docs-assets/_images/lc_floor_plans_add.png" style="width: 1020.6px; height: 331.2px;"></a>
<p>Then, import the Floor Plans you want to configure and fill in the corresponding parameters.</p>
<a class="reference internal image-reference" href="../../../_images/lc_floor_plans_create.png"><img alt="../../../_images/lc_floor_plans_create.png" class="align-center" src="/docs-assets/_images/lc_floor_plans_create.png" style="width: 444.6px; height: 456.3px;"></a>
<p>Once you’ve filled it in, click the <span class="red-text">Save</span> button to save the configuration.  Use the <span class="red-text">Visible</span> checkbox to enable visibility on the map.</p>
<a class="reference internal image-reference" href="../../../_images/lc_floor_plans_udk.png"><img alt="../../../_images/lc_floor_plans_udk.png" class="align-center" src="/docs-assets/_images/lc_floor_plans_udk.png" style="width: 1020.6px; height: 331.2px;"></a>
</div></blockquote>
</div>
<div class="section" id="zones">
<h3>Zones</h3>
<blockquote>
<div><p>To configure the zones, go to the menu and select the <span class="red-text">Zones</span>.</p>
<a class="reference internal image-reference" href="../../../_images/lc_menu.png"><img alt="../../../_images/lc_menu.png" class="align-center" src="/docs-assets/_images/lc_menu.png" style="width: 218.70000000000002px; height: 392.40000000000003px;"></a>
<p>Click the <span class="red-text">Add</span> button in the bottom right.</p>
<a class="reference internal image-reference" href="../../../_images/lc_floor_plans_add.png"><img alt="../../../_images/lc_floor_plans_add.png" class="align-center" src="/docs-assets/_images/lc_floor_plans_add.png" style="width: 1020.6px; height: 331.2px;"></a>
<p>Then, fill in the corresponding parameters and add the configuration for <span class="red-text">Save</span>.</p>
</div></blockquote>
</div>
<div class="section" id="users">
<h3>Users</h3>
<blockquote>
<div><p>To configure the users, go to the menu and select the <span class="red-text">Users</span>.</p>
<a class="reference internal image-reference" href="../../../_images/lc_menu.png"><img alt="../../../_images/lc_menu.png" class="align-center" src="/docs-assets/_images/lc_menu.png" style="width: 218.70000000000002px; height: 392.40000000000003px;"></a>
<p>By default, the application has pre-configured an Admin account and a common account.</p>
<a class="reference internal image-reference" href="../../../_images/lc_user_list.png"><img alt="../../../_images/lc_user_list.png" class="align-center" src="/docs-assets/_images/lc_user_list.png" style="width: 714.6px; height: 367.2px;"></a>
<p>For accounts that are admin or common.</p>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-9" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
Admin</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_user_admin.png"><img alt="../../../_images/lc_user_admin.png" class="align-center" src="/docs-assets/_images/lc_user_admin.png" style="width: 443.7px; height: 486.0px;"></a>
</div>
<input id="sd-tab-item-10" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-10">
Common</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_user_common.png"><img alt="../../../_images/lc_user_common.png" class="align-center" src="/docs-assets/_images/lc_user_common.png" style="width: 440.1px; height: 689.4px;"></a>
</div>
</div>
</div></blockquote>
</div></blockquote>
</div>
</div>
<hr class="docutils">
<div class="section" id="api-authorization">
<h2>API Authorization</h2>
<ol class="arabic">
<li><p>Users need to make a simple HTTP POST to /login passing the following parameters (using admin:admin as example).</p>
<ul class="simple">
<li><p>username: admin</p></li>
<li><p>password: admin</p></li>
<li><p>remember-me: on</p></li>
</ul>
</li>
<li><p>After login, the JSESSIONID cookie is generated and users need to use it in the subsequent requests.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ol class="arabic simple">
<li><p>This is not mandatory and if users use it another cookie is added (cookie REMEMBERME) in response and users can use it in the subsequent requests.</p></li>
<li><p>As the LEAPS Center performs a redirect after login and also when users are not authorized, it is necessary to properly set up the “follow redirects” parameter in user’s client. The response code after login is 302, but users need to handle it manually because if the user is not authorized the status code is also 302. Users can make any request to a REST service, for example, and if the response status code is not 200 the user will not be authorized.</p></li>
</ol>
</div>
</li>
</ol>
<p>Below is an example of code in Java to make the request and query the networks:</p>
<a class="reference internal image-reference" href="../../../_images/api-authorization.png"><img alt="../../../_images/api-authorization.png" class="align-center" src="/docs-assets/_images/api-authorization.png" style="width: 505.4px; height: 591.5px;"></a>
<p>For more detail, please refer two below videos, one using Postman and the other with Java code</p>
<div style="text-align: center; max-width: 100%;">
    <video controls="" src="../../../_static/video/postman.mp4" style="width: 100%; height: auto;"></video>
    <h2 style="margin-top: 0; margin-bottom: 10px; font-size: 1rem;">Postman</h2> <!-- Adjusted font-size -->
</div><hr class="docutils">
<div style="text-align: center; max-width: 100%;">
    <video controls="" src="../../../_static/video/java_client.mp4" style="width: 100%; height: auto;"></video>
    <h2 style="margin-top: 0; margin-bottom: 10px; font-size: 1rem;">Java Client</h2> <!-- Adjusted font-size -->
</div></div>
<hr class="docutils">
<div class="section" id="troubleshooting">
<h2>Troubleshooting</h2>
<ul class="simple">
<li><p>Use the following command <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_center</span></code> to restart LEAPS Center.</p></li>
<li><p>Check the logs when LEAPS Center is running, open the docker desktop and select the leaps_center container.</p></li>
<li><p>Open via Safari: If the interactive floor plan fails to load when you open the app, a Safari experimental feature is likely causing a conflict. Go to Settings &gt; Safari &gt; Advanced &gt; Experimental Features and disable ‘requestIdleCallback’.</p></li>
</ul>
</div>
</div>


           </div>
