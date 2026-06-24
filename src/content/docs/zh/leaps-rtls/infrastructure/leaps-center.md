---
title: "LEAPS Center"
lang: zh
slug: "leaps-rtls/infrastructure/leaps-center"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/infrastructure/leaps-center/"
order: 32
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-center">
<span id="leapscenter"></span><h1>LEAPS Center</h1>
<p><a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 是一个网络应用程序，提供设备管理, 网络管理以及整个网络的位置和遥测数据的可视化。</p>
<div class="section" id="key-features">
<h2>主要功能</h2>
<ul class="simple">
<li><p>2D和3D网格提供实时位置更新，并将网络中的设备可视化。</p></li>
<li><p>其他有用的功能包括用户管理, 区域管理, 区域历史, 平面图管理, 位置历史和位置热图。</p></li>
<li><p>The <a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 通过 <a class="reference external" href="https://mosquitto.org/">MQTT Broker</a> 与 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a> 互联. 它作为一项服务在 Linux 和 Windows 上运行</p></li>
</ul>
</div>
<div class="section" id="installation">
<h2>安装</h2>
<div class="section" id="system-requirements">
<h3>系统要求</h3>
<p>Docker的系统要求因操作系统而异。</p>
<ul class="simple">
<li><p>对于 Linux，您需要 64 位架构, 兼容的内核版本和特定的内核功能。</p></li>
<li><p>在 Windows 上，在启用虚拟化的 Windows 10上使用 Docker Desktop</p></li>
<li><p>在 macOS 上，请使用配备 macOS 10.13 或更新版本的Docker Desktop. 在硬件方面，建议至少配备 2GB 内存以及足够的 CPU 和磁盘空间。</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>有关最新详情，请参阅 <a class="reference external" href="https://docs.docker.com/">Docker</a> 官方文档。</p>
</div>
</div>
<div class="section" id="instructions">
<h3>说明</h3>
<ol class="arabic simple">
<li><p>在电脑上安装 Docker</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
在 Linux 上</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/linux-install/">在 Linux 上安装 Docker Desktop</a></p>
<p>此外，您还可以参考以下命令进行安装：</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">curl -fsSL https://get.docker.com -o get-docker.sh</span>
<span class="go">sudo sh ./get-docker.sh</span>
<span class="go">sudo usermod -aG docker $USER</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
在Windows上</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/">在 Windows 上安装 Docker Desktop</a></p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
在 macOS 上</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/mac-install/">在macOS上安装Docker桌面</a></p>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>准备配置软件包</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>创建包含 <a class="reference internal" href="#configuration-files"><span class="std std-ref">配置文件</span></a> 的 leaps_center 目录</p>
<ul>
<li><p>leaps-center-web.conf</p></li>
<li><p>应用程序。属性</p></li>
<li><p>leaps-center-history.properties</p></li>
<li><p>leaps-center-web.properties</p></li>
</ul>
</li>
<li><p>或者下载 <a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 配置包 (<a class="reference external" href="https://drive.google.com/file/d/1T-TECozBs9O87w4sCUHM1bXtLkd6jvHM/view?usp=drive_link">LEAPS_CENTER_DOCKER.zip</a>)。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>在电脑上打开命令提示符或终端窗口。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>导航至从 <a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 配置包中提取的目录。</p></li>
</ul>
<p>例如，在 Ubuntu (Linux) 上：</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd LEAPS_CENTER_DOCKER/</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>安装 <a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a> Docker 软件包并运行：</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 80:8080/tcp --name some_name -v /path/to/data/data/:/app/data/ -e LEAPS_CENTER_HOME=/app/data/ leapslabs/leaps_center:tag sh -c "cd /app &amp;&amp;  java -jar leaps-center-web.jar"</span>
</pre></div>
</div>
<p>其中 <code class="docutils literal notranslate"><span class="pre">some_name</span></code> 是要分配给容器的名称，<code class="docutils literal notranslate"><span class="pre">tag</span></code> 是指定要使用的 <code class="docutils literal notranslate"><span class="pre">leaps-center-web</span></code> 版本的标记。</p>
<p>leaps_center 映像必须与外部挂载的文件夹一起运行，该文件夹包含配置文件以及应用程序日志和配置/节点历史数据库的空间。</p>
<p>选项 <code class="docutils literal notranslate"><span class="pre">-v</span> <span class="pre">/path/to/data/:/app/data/</span></code> 将位于 <code class="docutils literal notranslate"><span class="pre">/path/to/data/</span></code> 的文件夹挂载到内部的 <code class="docutils literal notranslate"><span class="pre">/app/data</span></code> 文件夹. 数据文件夹必须包含以下文件。</p>
<ul class="simple">
<li><p>推荐的运行选项</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--user</span> <span class="pre">$(id</span> <span class="pre">-u):$(id</span> <span class="pre">-g)</span></code> 在特定用户和组下运行实例。</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">--restart</span> <span class="pre">unless-stopped</span></code> 在服务器崩溃时自动重启实例。</p></li>
</ul>
</li>
<li><p>可选运行选项</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--security-opt</span> <span class="pre">seccomp=unconfined</span></code> 在 32 位 Raspberry Pi 镜像（Raspbian）上需要这个选项，因为它包含一个过时的 seccomp 库，其中的一个错误会对 Docker 镜像产生负面影响（无法连接到 MQTT 服务器）. 该选项允许我们覆盖这一问题。</p></li>
</ul>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p><a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 安装过程将开始。</p></li>
</ol>
<blockquote>
<div><p>例如，在 Ubuntu (Linux) 上：</p>
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
<li><p>确认安装成功，运行：</p></li>
</ol>
<blockquote>
<div><p>例如，在 Ubuntu (Linux) 上：</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker ps</span>

<span class="go">CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS                          PORTS     NAMES</span>
<span class="go">b1145b72db35   leapslabs/leaps_center:latest   "sh -c 'cd /app &amp;&amp;  …"   37 seconds ago   11 seconds ago                            leaps_center</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>打开web浏览器并输入以下内容 <a class="reference external" href="http://localhost:80">http://localhost:80</a>； 将在web浏览器中加载 <a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 应用程序。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/lc_login.png"><img alt="../../../_images/lc_login.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_login.png" style="width: 716.4px; height: 520.2px;"></a>
</div></blockquote>
<p>因此，您已在PC上成功安装并启动 <a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a>。</p>
</div>
</div>
<div class="section" id="configuration-files">
<span id="id1"></span><h2>配置文件</h2>
<ul>
<li><p>leaps-center-web.conf</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">JAVA_OPTS="-Xms256m -Xmx512m -Xss256k"</span>
</pre></div>
</div>
</li>
<li><p>应用程序。属性</p></li>
<li><p>leaps-center-history.properties</p></li>
<li><p>leaps-center-web.properties</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
应用程序。属性</label><div class="sd-tab-content docutils">
<p>该配置文件控制应用程序日志记录。</p>
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
<p>该配置文件控制节点位置历史记录。</p>
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
<p>该配置文件控制 leaps_center 应用程序。</p>
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
<h2>开始</h2>
<blockquote>
<div><p>默认情况下，登录账户的用户名为 <span class="red-text">admin</span>，密码为 <span class="red-text">admin</span>。</p>
</div></blockquote>
<div class="section" id="leaps-server-docker">
<h3>LEAPS Server Docker</h3>
<ul class="simple">
<li><p>开始 <a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a>，运行: <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">Start</span> <span class="pre">leaps_center</span></code></p></li>
<li><p>停止 <a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a>，运行: <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">Stop</span> <span class="pre">leaps_center</span></code></p></li>
<li><p>重启 <a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a>，运行: <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">Restart</span> <span class="pre">leaps_center</span></code></p></li>
<li><p>删除 <a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a>，运行 <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">rm--force</span> <span class="pre">leaps_center</span></code></p></li>
</ul>
</div>
<div class="section" id="network-configurations">
<h3>网络配置</h3>
<blockquote>
<div><p>要配置网络，请进入菜单并选择 <span class="red-text">Networks</span>。</p>
<a class="reference internal image-reference" href="../../../_images/lc_select_networks.png"><img alt="../../../_images/lc_select_networks.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_select_networks.png" style="width: 720.0px; height: 564.3000000000001px;"></a>
<p>网络管理对话框将弹出。 默认情况下已经设置了本地主机网络，网络 ID 为 0x1234。</p>
<a class="reference internal image-reference" href="../../../_images/lc_list_networks.png"><img alt="../../../_images/lc_list_networks.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_list_networks.png" style="width: 1023.3000000000001px; height: 333.0px;"></a>
<p>要创建新网络，请单击右下角的 <span class="red-text">Add</span> 按钮。</p>
<p>现在，填写所需的配置参数：</p>
<blockquote>
<div><blockquote>
<div><ul class="simple">
<li><p>名称</p></li>
<li><p>网络类型</p></li>
<li><p>主机</p></li>
<li><p>TCP 端口</p></li>
<li><p>用户名</p></li>
<li><p>主题前缀</p></li>
</ul>
</div></blockquote>
<p>填写完毕后，点击 <span class="red-text">Save</span> 按钮连接并接收网络 ID。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/lc_config_networks_1234.png"><img alt="../../../_images/lc_config_networks_1234.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_config_networks_1234.png" style="width: 704.7px; height: 763.2px;"></a>
</div></blockquote>
</div></blockquote>
<p>如果不知道网络 ID，可以使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 或 Shell 查找。</p>
<p>最后，您可以单击 <span class="red-text">Test</span> 按钮检查连接情况，然后单击 <span class="red-text">Save</span> 按钮保存配置。</p>
</div></blockquote>
</div>
<div class="section" id="node-configurations">
<h3>节点配置</h3>
<p>要配置节点，需要事先将节点分配到特定网络。</p>
<p>选择指定节点的网络，查看网络详细信息。 然后，您就可以开始配置节点了。</p>
<p>有关可配置为网关, 锚点或标记节点的节点，请参阅以下详细信息</p>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-6" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
网关</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_config_gateway.png"><img alt="../../../_images/lc_config_gateway.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_config_gateway.png" style="width: 702.0px; height: 738.9px;"></a>
</div>
<input id="sd-tab-item-7" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
锚机</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_config_anchor.png"><img alt="../../../_images/lc_config_anchor.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_config_anchor.png" style="width: 712.8000000000001px; height: 512.1px;"></a>
</div>
<input id="sd-tab-item-8" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-8">
标签</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_config_tag.png"><img alt="../../../_images/lc_config_tag.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_config_tag.png" style="width: 712.8000000000001px; height: 540.9px;"></a>
</div>
</div>
</div></blockquote>
</div>
<div class="section" id="floor-plans">
<h3>平面图</h3>
<blockquote>
<div><p>要配置平面图，请进入菜单并选择 <span class="red-text">Floor Plans</span>。</p>
<a class="reference internal image-reference" href="../../../_images/lc_menu.png"><img alt="../../../_images/lc_menu.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_menu.png" style="width: 218.70000000000002px; height: 392.40000000000003px;"></a>
<p>点击右下角的 <span class="red-text">Add</span> 按钮。</p>
<a class="reference internal image-reference" href="../../../_images/lc_floor_plans_add.png"><img alt="../../../_images/lc_floor_plans_add.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_floor_plans_add.png" style="width: 1020.6px; height: 331.2px;"></a>
<p>然后，导入要配置的平面图并填写相应参数。</p>
<a class="reference internal image-reference" href="../../../_images/lc_floor_plans_create.png"><img alt="../../../_images/lc_floor_plans_create.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_floor_plans_create.png" style="width: 444.6px; height: 456.3px;"></a>
<p>填写完毕后，点击 <span class="red-text">Save</span> 按钮保存配置.  使用 <span class="red-text">Visible</span> 复选框启用地图上的可见性。</p>
<a class="reference internal image-reference" href="../../../_images/lc_floor_plans_udk.png"><img alt="../../../_images/lc_floor_plans_udk.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_floor_plans_udk.png" style="width: 1020.6px; height: 331.2px;"></a>
</div></blockquote>
</div>
<div class="section" id="zones">
<h3>区域</h3>
<blockquote>
<div><p>要配置区段，请进入菜单并选择 <span class="red-text">Zones</span>。</p>
<a class="reference internal image-reference" href="../../../_images/lc_menu.png"><img alt="../../../_images/lc_menu.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_menu.png" style="width: 218.70000000000002px; height: 392.40000000000003px;"></a>
<p>点击右下角的 <span class="red-text">Add</span> 按钮。</p>
<a class="reference internal image-reference" href="../../../_images/lc_floor_plans_add.png"><img alt="../../../_images/lc_floor_plans_add.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_floor_plans_add.png" style="width: 1020.6px; height: 331.2px;"></a>
<p>然后，填写相应参数，并为 <span class="red-text">Save</span> 添加配置。</p>
</div></blockquote>
</div>
<div class="section" id="users">
<h3>用户</h3>
<blockquote>
<div><p>要配置用户，请进入菜单并选择 <span class="red-text">Users</span>。</p>
<a class="reference internal image-reference" href="../../../_images/lc_menu.png"><img alt="../../../_images/lc_menu.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_menu.png" style="width: 218.70000000000002px; height: 392.40000000000003px;"></a>
<p>默认情况下，应用程序已预先配置了一个管理员账户和一个普通账户。</p>
<a class="reference internal image-reference" href="../../../_images/lc_user_list.png"><img alt="../../../_images/lc_user_list.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_user_list.png" style="width: 714.6px; height: 367.2px;"></a>
<p>适用于管理员账户或普通账户。</p>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-9" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
管理</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_user_admin.png"><img alt="../../../_images/lc_user_admin.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_user_admin.png" style="width: 443.7px; height: 486.0px;"></a>
</div>
<input id="sd-tab-item-10" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-10">
常见</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_user_common.png"><img alt="../../../_images/lc_user_common.png" class="align-center" src="/docs-assets/zh-cn/_images/lc_user_common.png" style="width: 440.1px; height: 689.4px;"></a>
</div>
</div>
</div></blockquote>
</div></blockquote>
</div>
</div>
<hr class="docutils">
<div class="section" id="api-authorization">
<h2>应用程序接口授权</h2>
<ol class="arabic">
<li><p>用户需要向/login发送一个简单的HTTP POST，并传递以下参数（以admin:admin为例）。</p>
<ul class="simple">
<li><p>用户名: admin</p></li>
<li><p>密码：admin</p></li>
<li><p>记住我：开启</p></li>
</ul>
</li>
<li><p>登录后会生成 JSESSIONID cookie，用户需要在后续请求中使用它。</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ol class="arabic simple">
<li><p>这不是强制性的，如果用户使用了它，会在响应中添加另一个 cookie（cookie REMEMBERME），用户可以在后续请求中使用它。</p></li>
<li><p>由于 <a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 在登录后以及用户未经授权时执行重定向，因此有必要在用户的客户端中正确设置”跟随重定向” 参数。登录后的响应码为302，但用户需要手动处理，因为如果用户未获得授权，状态码也为302。例如，用户可以向REST服务发出任何请求，如果响应状态代码不是200，则用户将不会被授权。</p></li>
</ol>
</div>
</li>
</ol>
<p>下面是一个用 Java 编写的请求和查询网络的代码示例：</p>
<a class="reference internal image-reference" href="../../../_images/api-authorization.png"><img alt="../../../_images/api-authorization.png" class="align-center" src="/docs-assets/zh-cn/_images/api-authorization.png" style="width: 505.4px; height: 591.5px;"></a>
<p>更多详情，请参阅以下两段视频，一段使用 Postman，另一段使用 Java 代码</p>
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
<h2>故障排除</h2>
<ul class="simple">
<li><p>使用以下命令 <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_center</span></code> 重启 <a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a>。</p></li>
<li><p>当 <a class="reference internal" href="#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 正在运行时检查日志，打开docker桌面并选择leaps_center容器。</p></li>
<li><p>Open via Safari: If the interactive floor plan fails to load when you open the app, a Safari experimental feature is likely causing a conflict. Go to Settings &gt; Safari &gt; Advanced &gt; Experimental Features and disable ‘requestIdleCallback’.</p></li>
</ul>
</div>
</div>


           </div>
