---
title: "固件更新"
lang: zh
slug: "pans-pro-rtls/integration-guide/firmware-update"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/firmware-update/"
order: 94
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="firmware-update">
<span id="pans-pro-fw-update"></span><h1>固件更新</h1>
<p>RTLS网络组建时，启动锚会指定网络所需的固件版本。 启用固件自动更新后，任何希望参与（加入）网络的设备都必须拥有相同的固件（版本号和校验和）。 如果新设备没有正确的固件，将按照下面的小节进行更新。</p>
<div class="section" id="firmware-update-via-bluetooth">
<h2>通过Bluetooth更新固件</h2>
<p>如果想要在网络运行时，将整个网络更新为新的固件镜像，只需通过Bluetooth更新启动器即可。 然后，启动器会通过 UWB 无线电链路自动将新固件传播给所有其他设备。 需要注意的是，当启动器首先更新时，它将重新启动网络，当每个设备重新加入网络时，其固件也将更新。 因此，在固件更新期间，执行更新的节点将处于“离线”状态。</p>
</div>
<div class="section" id="firmware-update-via-uwb">
<h2>通过 UWB 更新固件</h2>
<p>正如 DWM1001 系统概述[4]中所介绍的，节点会将自己的固件版本与想要加入的网络进行比较。 如果固件版本不同，节点会尝试在加入前更新固件。 固件更新功能可在配置中启用/禁用。 这里列出了节点将遵循的功能规则。</p>
<p><strong>标签:</strong></p>
<ul class="simple">
<li><p>启用后，标签将始终检查固件版本，并尝试在开始测距前，通过向网络中附近的锚节点发送更新请求，使其固件版本与网络同步。</p></li>
<li><p>如果禁用，标签会在不检查固件版本的情况下开始测距。 这可能会导致版本兼容性问题，必须非常小心处理。</p></li>
</ul>
<p><strong>锚点:</strong></p>
<ul class="simple">
<li><p>启用后，在加入网络之前，锚节点将检查固件版本，并尝试通过向附近的锚节点发送更新请求，使其固件版本与网络同步。 加入网络后，锚点将响应附近节点的更新固件请求。</p></li>
<li><p>如果禁用，在加入网络之前，锚节点会直接发送加入请求，而不会检查固件版本。 这可能会导致版本兼容性问题，必须非常小心处理。 加入网络后，锚点会忽略附近节点的固件更新请求。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="firmware-update-via-uart">
<h2>通过 UART 更新固件</h2>
<p><strong>准备设置</strong></p>
<ul class="simple">
<li><p>至少一个设备。</p></li>
<li><p>一个软件包包含一个脚本和一个二进制文件，用于更新。</p></li>
<li><p>已安装 <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">OpenOCD</a>。</p></li>
</ul>
<p><strong>关于如何通过OpenOCD（片上开放调试器）进行更新的分步说明</strong></p>
<ol class="arabic simple">
<li><p>安装 OpenOCD 调试器。</p></li>
</ol>
<blockquote>
<div><ol class="upperalpha simple">
<li><p>在 Windows 上安装 OpenOCD</p></li>
</ol>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>下载适用于 Windows 的二进制压缩文件。</p></li>
<li><p>解压缩到 <code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1</span></code> 文件夹中。</p></li>
<li><p>将路径: <code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1\bin</span></code> 添加到Windows用户路径环境变量中。</p></li>
</ol>
</div></blockquote>
<ol class="upperalpha simple" start="2">
<li><p>在 Linux 或 macOS 上安装 OpenOCD。</p></li>
</ol>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>下载用于 <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">Linux 的二进制压缩包</a> 。</p></li>
<li><p>解开tarball并安装到本地。</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>mkdir -p ~/.local/xPacks/openocd
cd ~/.local/xPacks/openocd
tar -zxvf ~/Downloads/xpack-openocd-0.11.0-1-linux-arm.tar.gz (with PC’s AMD core, using … linux-x64.tar.gz with PC’s Intel core)
....
sudo chmod -R -w xpack-openocd-0.11.0-1/
~/.local/xPacks/openocd/xpack-openocd-0.11.0-1/bin/openocd --version
export PATH="~/.local/xPacks/openocd/xpack-openocd-0.11.0-1/bin/:$PATH"
cd ~
source .bashrc
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>检查 OpenOCD 版本。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">openocd</span> <span class="o">--</span><span class="n">version</span>
<span class="n">xPack</span> <span class="n">OpenOCD</span><span class="p">,</span> <span class="n">x86_64</span> <span class="n">Open</span> <span class="n">On</span><span class="o">-</span><span class="n">Chip</span> <span class="n">Debugger</span> <span class="mf">0.11.0</span><span class="o">-</span><span class="mi">00155</span><span class="o">-</span><span class="n">ge392e485e</span> <span class="p">(</span><span class="mi">2021</span><span class="o">-</span><span class="mi">03</span><span class="o">-</span><span class="mi">15</span><span class="o">-</span><span class="mi">16</span><span class="p">:</span><span class="mi">43</span><span class="p">)</span>
<span class="n">Licensed</span> <span class="n">under</span> <span class="n">GNU</span> <span class="n">GPL</span> <span class="n">v2</span>
<span class="n">For</span> <span class="n">bug</span> <span class="n">reports</span><span class="p">,</span> <span class="n">read</span>
  <span class="n">http</span><span class="p">:</span><span class="o">//</span><span class="n">openocd</span><span class="o">.</span><span class="n">org</span><span class="o">/</span><span class="n">doc</span><span class="o">/</span><span class="n">doxygen</span><span class="o">/</span><span class="n">bugs</span><span class="o">.</span><span class="n">html</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>下载软件包并将其解压缩到PC. 使用WinZip或7-Zip等程序解压缩下载的文件。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请联系我们获取下载包，网址为 <a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>打开您最喜欢的终端应用程序。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>在linux或macOS上，如 <span class="red-text">终端</span> 应用程序。</p></li>
<li><p>在Windows上，比如 <span class="red-text">Powershell</span>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>导航到包含提取包的文件夹。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><span class="red-text">cd</span> 到 <span class="red-text">/path/to/PANSPRO固件OpenOCD</span></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>使用Micro USB数据线将设备的 <code class="docutils literal notranslate"><span class="pre">Micro</span> <span class="pre">USB数据端口</span></code> 连接到您的PC。</p></li>
<li><p>执行脚本以自动更新固件。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>在linux或macOS上，使用 <span class="red-text">reflash-panspro-rtls-2ab.sh</span> 命令。</p></li>
<li><p>在Windows上，使用 <span class="red-text">reflash-panspro-rtls-2ab.bat</span> 命令。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>更新完成后，设备将发出蜂鸣声，表示更新成功。 作为该过程的一部分，该板将自动重置。</p></li>
</ol>
<p>设备已成功更新固件. 享受最新的功能和改进。</p>
</div>
</div>


           </div>
