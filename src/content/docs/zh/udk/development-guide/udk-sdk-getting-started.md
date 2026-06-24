---
title: "从 SDK 开始"
lang: zh
slug: "udk/development-guide/udk-sdk-getting-started"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/development-guide/udk-sdk-getting-started/"
order: 45
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="udk-sdk-getting-started">
<span id="udksdk"></span><h1>从 SDK 开始</h1>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>请注意，第三方应用程序的开发不在 UDK 的服务范围内，因此不属于预付费 UDK 支持的一部分。</p>
</div>
<p>本节为选择和启动 LEAPS 示例项目提供全面指导，这些示例项目专为 Zephyr 实时操作系统平台设计. 这些示例有助于加深对 <strong>UWB（超宽带）技术</strong> 和 UDK 工具包的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">硬件接口</span></a> 的理解。</p>
<p>有了这些知识，用户就可以放心地在 UDK 套件上开发自定义应用程序。</p>
<p><strong>指导遵循以下步骤:</strong></p>
<ol class="arabic simple">
<li><p>在Linux, macOS或Windows上为 <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> 实时操作系统设置开发环境。</p></li>
<li><p>获取UDK的SDK，它是基于 <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> 的示例应用程序包。</p></li>
<li><p>将设备连接到主机和所需的工具。</p></li>
<li><p>选择示例, 构建, 闪存并运行一个示例程序。</p></li>
</ol>
<hr class="docutils">
<div class="section" id="zephyr-s-getting-started-guide">
<h2>Zephyr 入门指南</h2>
<p>按照本指南进行操作:</p>
<ul class="simple">
<li><p>在 Ubuntu, macOS 或 Windows 上设置命令行 Zephyr 开发环境（有关其他 Linux 发行版的说明，请参阅 <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/getting_started/installation_linux.html#installation-linux">installation_linux</a>）。</p></li>
<li><p>安装Zephyr的SDK软件包（包括所需的工具链）</p></li>
</ul>
<div class="section" id="select-and-update-os">
<h3>选择并更新操作系统</h3>
<p>点击你正在使用的操作系统。</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-0">
Ubuntu</label><div class="sd-tab-content docutils">
<p>本指南涵盖 Ubuntu 20.04 LTS 及更高版本。</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>apt<span class="w"> </span>update
sudo<span class="w"> </span>apt<span class="w"> </span>upgrade
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-1">
macOS</label><div class="sd-tab-content docutils">
<p>在macOS Mojave或更新版本中，选择 <em>系统偏好设置</em> &gt; <em>软件更新</em>。 如有必要，点击 <em>立即更新</em>。</p>
<p>关于其他版本，请参阅 <a class="reference external" href="https://support.apple.com/en-us/HT201541">此Apple支持主题</a></p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-2">
Windows</label><div class="sd-tab-content docutils">
<p>选择 <em>启动</em> &gt; <em>设置</em> &gt; <em>更新与安全</em> &gt; <em>Windows更新</em>。点击 <em>检查更新</em> 并安装任何可用的更新。</p>
</div>
</div>
</div>
<div class="section" id="install-dependencies">
<h3>安装依赖项</h3>
<p>接下来，你将使用软件包管理器安装一些主机依赖包。</p>
<p>当前主要依赖项所需的最低版本是:</p>
<table class="docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>工具</p></th>
<th class="head"><p>最小. 版本</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference external" href="https://cmake.org/">CMake</a></p></td>
<td><p>3.20.5</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference external" href="https://www.python.org/">Python</a></p></td>
<td><p>3.10</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference external" href="https://www.devicetree.org/">Devicetree编译器</a></p></td>
<td><p>1.4.6</p></td>
</tr>
</tbody>
</table>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-3">
Ubuntu</label><div class="sd-tab-content docutils">
<ol class="arabic" id="install-dependencies-ubuntu">
<li><p>如果使用的Ubuntu版本早于22.04，则有必要添加额外的软件源，以满足上述主要依赖项的最低版本要求. 在这种情况下，请下载, 检查并执行 Kitware 存档脚本，将 Kitware APT 仓库添加到源代码列表中. 关于 <code class="docutils literal notranslate"><span class="pre">kitware-archive.sh</span></code> 的详细解释，请参阅 <a class="reference external" href="https://apt.kitware.com/">kitware第三方apt仓库</a>:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>wget<span class="w"> </span>https://apt.kitware.com/kitware-archive.sh
sudo<span class="w"> </span>bash<span class="w"> </span>kitware-archive.sh
</pre></div>
</div>
</li>
<li><p>使用 <code class="docutils literal notranslate"><span class="pre">apt</span></code> 安装所需的依赖项:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>apt<span class="w"> </span>install<span class="w"> </span>--no-install-recommends<span class="w"> </span>git<span class="w"> </span>cmake<span class="w"> </span>ninja-build<span class="w"> </span>gperf<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>ccache<span class="w"> </span>dfu-util<span class="w"> </span>device-tree-compiler<span class="w"> </span>wget<span class="w"> </span>minicom<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>python3-dev<span class="w"> </span>python3-pip<span class="w"> </span>python3-setuptools<span class="w"> </span>python3-tk<span class="w"> </span>python3-wheel<span class="w"> </span>xz-utils<span class="w"> </span>file<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>make<span class="w"> </span>gcc<span class="w"> </span>gcc-multilib<span class="w"> </span>g++-multilib<span class="w"> </span>libsdl2-dev<span class="w"> </span>libmagic1
</pre></div>
</div>
</li>
<li><p>输入验证系统上安装的主要依赖版本:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>--version
python3<span class="w"> </span>--version
dtc<span class="w"> </span>--version
</pre></div>
</div>
<p>与本节开头的表格中的版本进行核对. 请参阅 <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/getting_started/installation_linux.html#installation-linux">installation_linux</a> 页面，了解手动更新依赖项的更多信息。</p>
</li>
</ol>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-4">
macOS</label><div class="sd-tab-content docutils">
<ol class="arabic" id="install-dependencies-macos">
<li><p>安装 <a class="reference external" href="https://brew.sh/">Homebrew</a>：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>/bin/bash<span class="w"> </span>-c<span class="w"> </span><span class="s2">"</span><span class="k">$(</span>curl<span class="w"> </span>-fsSL<span class="w"> </span>https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh<span class="k">)</span><span class="s2">"</span>
</pre></div>
</div>
</li>
<li><p>在 Homebrew 安装脚本完成后，按照屏幕上的指示，将 Homebrew 安装程序添加到路径中。</p>
<ul>
<li><p>在苹果硅上运行的 macOS 上，可以通过以下方法实现：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="o">(</span>echo<span class="p">;</span><span class="w"> </span><span class="nb">echo</span><span class="w"> </span><span class="s1">'eval "$(/opt/homebrew/bin/brew shellenv)"'</span><span class="o">)</span><span class="w"> </span>&gt;&gt;<span class="w"> </span>~/.zprofile
<span class="nb">source</span><span class="w"> </span>~/.zprofile
</pre></div>
</div>
</li>
<li><p>在 Intel 上运行的 macOS，使用 Apple Silicon 的命令，但将 <code class="docutils literal notranslate"><span class="pre">/opt/homebrew/</span></code> 替换为 <code class="docutils literal notranslate"><span class="pre">/usr/local/</span></code>。</p></li>
</ul>
</li>
<li><p>使用 <code class="docutils literal notranslate"><span class="pre">brew</span></code> 安装所需的依赖项：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>brew<span class="w"> </span>install<span class="w"> </span>cmake<span class="w"> </span>ninja<span class="w"> </span>gperf<span class="w"> </span>python3<span class="w"> </span>ccache<span class="w"> </span>qemu<span class="w"> </span>dtc<span class="w"> </span>libmagic<span class="w"> </span>wget<span class="w"> </span>openocd<span class="w"> </span>minicom
</pre></div>
</div>
</li>
<li><p>在路径中添加 Homebrew Python 文件夹，以便能够执行 <code class="docutils literal notranslate"><span class="pre">python`</span> <span class="pre">和</span> <span class="pre">``pip</span></code> 以及 <code class="docutils literal notranslate"><span class="pre">python3</span></code> 和 <code class="docutils literal notranslate"><span class="pre">pip3</span></code>。</p>
<blockquote>
<div><div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="o">(</span>echo<span class="p">;</span><span class="w"> </span><span class="nb">echo</span><span class="w"> </span><span class="s1">'export PATH="'</span><span class="k">$(</span>brew<span class="w"> </span>--prefix<span class="k">)</span><span class="s1">'/opt/python/libexec/bin:$PATH"'</span><span class="o">)</span><span class="w"> </span>&gt;&gt;<span class="w"> </span>~/.zprofile
<span class="nb">source</span><span class="w"> </span>~/.zprofile
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
</div>
<input id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-5">
Windows</label><div class="sd-tab-content docutils">
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>由于寻找可执行文件的问题，Zephyr 项目目前不支持使用 <a class="reference external" href="https://msdn.microsoft.com/en-us/commandline/wsl/install_guide">Windows Subsystem for Linux(WSL)</a> (WSL)闪存应用程序。</p>
<p>因此，我们不建议在入门时使用 WSL。</p>
</div>
<p>这些说明必须在 <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> 命令提示符终端窗口中运行. 在现代版本的 Windows 中（10 及更高版本），建议从微软商店安装 Windows 终端应用程序. PowerShell 所需的指令有所不同。</p>
<p>这些说明依赖于 <a class="reference external" href="https://chocolatey.org/">Chocolatey</a>. 如果没有 Chocolatey，你可以从它们各自的网站上安装依赖项，并确保命令行工具位于你的 <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/env_vars.html#envvar-PATH">PATH</a> <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/env_vars.html#env-vars">环境变量</a> 上。</p>
<ol class="arabic" id="install-dependencies-windows">
<li><p><a class="reference external" href="https://chocolatey.org/install">安装chocolatey</a>。</p></li>
<li><p>以 <strong>管理员</strong> 身份打开 <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> 终端窗口。为此，按下Windows键，输入 <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code>，右键单击 <span class="guilabel">命令提示符</span> 搜索结果，并选择 <span class="guilabel">Run as管理员</span></p></li>
<li><p>禁用全局确认，以避免必须确认单个程序的安装：</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>choco feature enable -n allowGlobalConfirmation
</pre></div>
</div>
</li>
<li><p>使用 <code class="docutils literal notranslate"><span class="pre">choco</span></code> 安装所需的依赖项：</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>choco install cmake --installargs 'ADD_CMAKE_TO_PATH=System'
choco install ninja gperf python311 git dtc-msys2 wget 7zip unzip
</pre></div>
</div>
<div class="admonition warning">
<p class="admonition-title">警告</p>
<p>截至2023年11月，不建议将Python 3.12用于Windows上的Zephyr开发，因为一些必需的Python依赖项可能难以安装。</p>
</div>
</li>
<li><p>关闭终端窗口。</p></li>
</ol>
</div>
</div>
</div>
<div class="section" id="install-west">
<h3>安装West</h3>
<p><a class="reference external" href="https://docs.zephyrproject.org/latest/develop/west/index.html">West</a> 是 <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> 的瑞士军刀命令行工具，要安装它，请执行以下命令：</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-6" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-6">
Ubuntu</label><div class="sd-tab-content docutils">
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-9" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
在虚拟环境中安装</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>使用 <code class="docutils literal notranslate"><span class="pre">apt</span></code> 安装Python <code class="docutils literal notranslate"><span class="pre">venv</span></code> 包：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>apt<span class="w"> </span>install<span class="w"> </span>python3-venv
</pre></div>
</div>
</li>
<li><p>创建新的虚拟环境：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>python3<span class="w"> </span>-m<span class="w"> </span>venv<span class="w"> </span>~/udk-sdk/.venv
</pre></div>
</div>
</li>
<li><p>激活虚拟环境：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">source</span><span class="w"> </span>~/udk-sdk/.venv/bin/activate
</pre></div>
</div>
<p>激活后，您的shell将以 <code class="docutils literal notranslate"><span class="pre">(.venv)</span></code> 作为前缀. 通过运行 <code class="docutils literal notranslate"><span class="pre">deactivate</span></code>，可以随时停用虚拟环境。</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>每次开始工作时，记得激活虚拟环境。</p>
</div>
</li>
<li><p>安装west</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>west
</pre></div>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-10" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-10">
全局安装</label><div class="sd-tab-content docutils">
<p>安装west，并确保 <code class="file docutils literal notranslate"><span class="pre">~/.local/bin</span></code> 在您的 <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/env_vars.html#envvar-PATH">PATH</a> <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/env_vars.html#env-vars">环境变量</a> 上：</p>
<blockquote>
<div><div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>pip3<span class="w"> </span>install<span class="w"> </span>--user<span class="w"> </span>-U<span class="w"> </span>west
<span class="nb">echo</span><span class="w"> </span><span class="s1">'export PATH=~/.local/bin:"$PATH"'</span><span class="w"> </span>&gt;&gt;<span class="w"> </span>~/.bashrc
<span class="nb">source</span><span class="w"> </span>~/.bashrc
</pre></div>
</div>
</div></blockquote>
</div>
</div>
</div>
<input id="sd-tab-item-7" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-7">
macOS</label><div class="sd-tab-content docutils">
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-11" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-11">
在虚拟环境中安装</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>创建新的虚拟环境：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>python3<span class="w"> </span>-m<span class="w"> </span>venv<span class="w"> </span>~/udk-sdk/.venv
</pre></div>
</div>
</li>
<li><p>激活虚拟环境：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">source</span><span class="w"> </span>~/udk-sdk/.venv/bin/activate
</pre></div>
</div>
<p>激活后，您的shell将以 <code class="docutils literal notranslate"><span class="pre">(.venv)</span></code> 作为前缀. 通过运行 <code class="docutils literal notranslate"><span class="pre">deactivate</span></code>，可以随时停用虚拟环境。</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>每次开始工作时，记得激活虚拟环境。</p>
</div>
</li>
<li><p>安装west</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>west
</pre></div>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-12" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-12">
全局安装</label><div class="sd-tab-content docutils">
<p>安装west</p>
<blockquote>
<div><div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>pip3<span class="w"> </span>install<span class="w"> </span>-U<span class="w"> </span>west
</pre></div>
</div>
</div></blockquote>
</div>
</div>
</div>
<input id="sd-tab-item-8" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-8">
Windows</label><div class="sd-tab-content docutils">
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-13" name="sd-tab-set-5" type="radio">
<label class="sd-tab-label" for="sd-tab-item-13">
在虚拟环境中安装</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>以普通用户身份打开 <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> <strong>终端窗口</strong></p></li>
<li><p>创建新的虚拟环境：</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span><span class="k">cd</span> <span class="nv">%HOMEPATH%</span>
python -m venv udk-sdk\.venv
</pre></div>
</div>
</li>
<li><p>激活虚拟环境：</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>udk-sdk\.venv\Scripts\activate.bat
</pre></div>
</div>
<p>激活后，您的shell将以 <code class="docutils literal notranslate"><span class="pre">(.venv)</span></code> 作为前缀. 通过运行 <code class="docutils literal notranslate"><span class="pre">deactivate</span></code>，可以随时停用虚拟环境。</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>每次开始工作时，记得激活虚拟环境。</p>
</div>
</li>
<li><p>安装west</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>pip install west
</pre></div>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-14" name="sd-tab-set-5" type="radio">
<label class="sd-tab-label" for="sd-tab-item-14">
全局安装</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>以普通用户身份打开 <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> <strong>终端窗口</strong></p></li>
<li><p>安装west</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>pip3 install -U west
</pre></div>
</div>
</li>
</ol>
</div>
</div>
</div>
</div>
</div>
<div class="section" id="install-the-zephyr-sdk">
<span id="installthezephyrsdk"></span><h3>安装 Zephyr SDK</h3>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>如果你想卸载 SDK，你可以直接移除安装它的目录。</p>
</div>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-15" name="sd-tab-set-6" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-15">
Ubuntu</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>下载并验证 <a class="reference external" href="https://github.com/zephyrproject-rtos/sdk-ng/tree/v0.14.2">Zephyr SDK bundle</a>:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="o">~</span>
<span class="n">wget</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_linux</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">tar</span><span class="o">.</span><span class="n">gz</span>
<span class="n">wget</span> <span class="o">-</span><span class="n">O</span> <span class="o">-</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">sha256</span><span class="o">.</span><span class="n">sum</span> <span class="o">|</span> <span class="n">shasum</span> <span class="o">--</span><span class="n">check</span> <span class="o">--</span><span class="n">ignore</span><span class="o">-</span><span class="n">missing</span>
</pre></div>
</div>
<p>如果你的主机架构是 64 位 ARM (例如 Raspberry Pi)，请将 <code class="docutils literal notranslate"><span class="pre">x86_64</span></code> 替换为 <code class="docutils literal notranslate"><span class="pre">aarch64</span></code> 以下载 64 位 ARM Linux SDK。</p>
</li>
<li><p>解压缩 Zephyr SDK 捆绑包：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">tar</span> <span class="n">xvf</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_linux</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">tar</span><span class="o">.</span><span class="n">gz</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>建议在下列其中一个位置解压缩 Zephyr SDK 套件：</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/.local</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/.local/opt</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/bin</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">/opt</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">/usr/local</span></code></p></li>
</ul>
<p>Zephyr SDK 捆绑包中包含 <code class="docutils literal notranslate"><span class="pre">zephyr-sdk-&lt;version&gt;</span></code> 目录，在 <code class="docutils literal notranslate"><span class="pre">$HOME</span></code> 下解压缩后，安装路径为 <code class="docutils literal notranslate"><span class="pre">$HOME/zephyr-sdk-&lt;version&gt;</span></code>。</p>
</div>
</li>
<li><p>运行 Zephyr SDK bundle 安装脚本：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span>
<span class="o">./</span><span class="n">setup</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>在解压缩 Zephyr SDK 软件包后，您只需要运行一次设置脚本。</p>
<p>如果您在初始设置后重新定位Zephyr SDK bundle目录，您必须重新运行设置脚本。</p>
</div>
</li>
<li><p>安装 <a class="reference external" href="https://en.wikipedia.org/wiki/Udev">udev</a> 规则，它允许你以普通用户的身份闪存大多数 Zephyr 主板：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">cp</span> <span class="o">~/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="o">/</span><span class="n">sysroots</span><span class="o">/</span><span class="n">x86_64</span><span class="o">-</span><span class="n">pokysdk</span><span class="o">-</span><span class="n">linux</span><span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="n">share</span><span class="o">/</span><span class="n">openocd</span><span class="o">/</span><span class="n">contrib</span><span class="o">/</span><span class="mi">60</span><span class="o">-</span><span class="n">openocd</span><span class="o">.</span><span class="n">rules</span> <span class="o">/</span><span class="n">etc</span><span class="o">/</span><span class="n">udev</span><span class="o">/</span><span class="n">rules</span><span class="o">.</span><span class="n">d</span>
<span class="n">sudo</span> <span class="n">udevadm</span> <span class="n">control</span> <span class="o">--</span><span class="n">reload</span>
</pre></div>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-16" name="sd-tab-set-6" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-16">
macOS</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>下载并验证 <a class="reference external" href="https://github.com/zephyrproject-rtos/sdk-ng/tree/v0.14.2">Zephyr SDK bundle</a>:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="o">~</span>
<span class="n">curl</span> <span class="o">-</span><span class="n">L</span> <span class="o">-</span><span class="n">O</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_macos</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">tar</span><span class="o">.</span><span class="n">gz</span>
<span class="n">curl</span> <span class="o">-</span><span class="n">L</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">sha256</span><span class="o">.</span><span class="n">sum</span> <span class="o">|</span> <span class="n">shasum</span> <span class="o">--</span><span class="n">check</span> <span class="o">--</span><span class="n">ignore</span><span class="o">-</span><span class="n">missing</span>
</pre></div>
</div>
<p>如果您的主机架构是 64 位 ARM (Apple Silicon，也称为 M1)，请将 <code class="docutils literal notranslate"><span class="pre">x86_64</span></code> 替换为 <code class="docutils literal notranslate"><span class="pre">aarch64</span></code>，以便下载 64 位 ARM macOS SDK。</p>
</li>
<li><p>解压缩 Zephyr SDK 捆绑包：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">tar</span> <span class="n">xvf</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_macos</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">tar</span><span class="o">.</span><span class="n">gz</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>建议在下列其中一个位置解压缩 Zephyr SDK 套件：</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/.local</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/.local/opt</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/bin</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">/opt</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">/usr/local</span></code></p></li>
</ul>
<p>Zephyr SDK 捆绑包中包含 <code class="docutils literal notranslate"><span class="pre">zephyr-sdk-&lt;version&gt;</span></code> 目录，在 <code class="docutils literal notranslate"><span class="pre">$HOME</span></code> 下解压缩后，安装路径为 <code class="docutils literal notranslate"><span class="pre">$HOME/zephyr-sdk-&lt;version&gt;</span></code>。</p>
</div>
</li>
<li><p>运行 Zephyr SDK bundle 安装脚本：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span>
<span class="o">./</span><span class="n">setup</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>在解压缩 Zephyr SDK 软件包后，您只需要运行一次设置脚本。</p>
<p>如果您在初始设置后重新定位Zephyr SDK bundle目录，您必须重新运行设置脚本。</p>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-17" name="sd-tab-set-6" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-17">
Windows</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>以普通用户身份打开 <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> <strong>终端窗口</strong></p></li>
<li><p>下载 <a class="reference external" href="https://github.com/zephyrproject-rtos/sdk-ng/tree/v0.14.2">Zephyr SDK bundle</a>：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="o">%</span><span class="n">HOMEPATH</span><span class="o">%</span>
<span class="n">wget</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_windows</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">zip</span>
</pre></div>
</div>
</li>
<li><p>解压缩 Zephyr SDK 捆绑包：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">unzip</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_windows</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">zip</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>建议在下列其中一个位置解压缩 Zephyr SDK 套件：</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">%HOMEPATH%</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">%PROGRAMFILES%</span></code>.</p></li>
</ul>
<p>Zephyr SDK 捆绑包中包含 <code class="docutils literal notranslate"><span class="pre">zephyr-sdk-&lt;version&gt;</span></code> 目录，在 <code class="docutils literal notranslate"><span class="pre">%HOMEPATH%</span></code> 下解压缩时，生成的安装路径将是 <code class="docutils literal notranslate"><span class="pre">%HOMEPATH%\zephyr-sdk-&lt;version&gt;</span></code>。</p>
</div>
</li>
<li><p>运行 Zephyr SDK bundle 安装脚本：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span>
<span class="n">setup</span><span class="o">.</span><span class="n">cmd</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>在解压缩 Zephyr SDK 软件包后，您只需要运行一次设置脚本。</p>
<p>如果您在初始设置后重新定位Zephyr SDK bundle目录，您必须重新运行设置脚本。</p>
</div>
</li>
</ol>
</div>
</div>
</div>
</div>
<div class="section" id="install-udk-sdk-package">
<h2>安装 UDK-SDK 软件包</h2>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>UDK SDK 也是一个基于 Zephyr 的示例应用程序。 若要深入了解，请参阅此 <a class="reference external" href="https://github.com/zephyrproject-rtos/example-application">示例应用程式</a> 页面。</p>
</div>
<p>第一步是初始化工作区文件夹 <code class="docutils literal notranslate"><span class="pre">udk-sdk</span></code>，<code class="docutils literal notranslate"><span class="pre">leaps-udk-examples</span></code> 和所有 Zephyr 模块都会被克隆到这里. 请遵循以下说明</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-18" name="sd-tab-set-7" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-18">
Ubuntu</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>打开终端</p></li>
<li><p>使用主版本初始化 <cite>leaps-udk-examples</cite> 的 <cite>udk-sdk</cite> 工作区。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">init</span> <span class="o">-</span><span class="n">m</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">leapslabs</span><span class="o">/</span><span class="n">udk</span><span class="o">-</span><span class="n">sdk</span><span class="o">.</span><span class="n">git</span> <span class="o">--</span><span class="n">mr</span> <span class="n">main</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
</pre></div>
</div>
</li>
<li><p>克隆 <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> 源代码（版本 3.1.0）及其模块。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
<span class="n">west</span> <span class="n">update</span>
</pre></div>
</div>
</li>
<li><p>导出一个 <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> CMake软件包. 这将允许CMake自动加载构建 Zephyr 应用程序所需的模板代码。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">export</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> 的scripts/requirements.txt文件声明了额外的Python依赖项. 使用pip安装它们。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="o">./</span><span class="n">zephyr</span><span class="o">/</span><span class="n">scripts</span><span class="o">/</span><span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div>
</div>
</li>
<li><p>设置 $ZEPHYR_BASE 环境。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">zephyr</span><span class="o">/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">env</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</li>
</ol>
</div></blockquote>
</div>
<input id="sd-tab-item-19" name="sd-tab-set-7" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-19">
macOS</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>打开终端</p></li>
<li><p>使用主版本初始化 <cite>leaps-udk-examples</cite> 的 <cite>udk-sdk</cite> 工作区。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">init</span> <span class="o">-</span><span class="n">m</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">leapslabs</span><span class="o">/</span><span class="n">udk</span><span class="o">-</span><span class="n">sdk</span><span class="o">.</span><span class="n">git</span> <span class="o">--</span><span class="n">mr</span> <span class="n">main</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
</pre></div>
</div>
<div class="admonition caution">
<p class="admonition-title">小心</p>
<p>我们将很快提供已发布的 <code class="docutils literal notranslate"><span class="pre">udk-sdk资源库</span></code>. 请继续关注！</p>
</div>
</li>
<li><p>克隆 <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> 源代码（版本 3.1.0）及其模块。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
<span class="n">west</span> <span class="n">update</span>
</pre></div>
</div>
</li>
<li><p>导出一个 <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> CMake软件包. 这将允许CMake自动加载构建 Zephyr 应用程序所需的模板代码。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">export</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> 的scripts/requirements.txt文件声明了额外的Python依赖项. 使用pip安装它们。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="o">./</span><span class="n">zephyr</span><span class="o">/</span><span class="n">scripts</span><span class="o">/</span><span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div>
</div>
</li>
<li><p>设置 $ZEPHYR_BASE 环境。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">zephyr</span><span class="o">/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">env</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</li>
</ol>
</div></blockquote>
</div>
<input id="sd-tab-item-20" name="sd-tab-set-7" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-20">
Windows</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>以普通用户身份打开 <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> 终端窗口</p></li>
<li><p>使用主版本初始化 <cite>leaps-udk-examples</cite> 的 <cite>udk-sdk</cite> 工作区。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">init</span> <span class="o">-</span><span class="n">m</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">leapslabs</span><span class="o">/</span><span class="n">udk</span><span class="o">-</span><span class="n">sdk</span><span class="o">.</span><span class="n">git</span> <span class="o">--</span><span class="n">mr</span> <span class="n">main</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
</pre></div>
</div>
</li>
<li><p>克隆 <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> 源代码（版本 3.1.0）及其模块。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
<span class="n">west</span> <span class="n">update</span>
</pre></div>
</div>
</li>
<li><p>导出一个 <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> CMake软件包. 这将允许CMake自动加载构建 Zephyr 应用程序所需的模板代码。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">export</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> 的scripts/requirements.txt文件声明了额外的Python依赖项. 使用pip安装它们。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="n">zephyr</span><span class="o">/</span><span class="n">scripts</span><span class="o">/</span><span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div>
</div>
</li>
<li><p>设置 $ZEPHYR_BASE 环境。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">zephyr</span>
<span class="n">zephyr</span><span class="o">-</span><span class="n">env</span><span class="o">.</span><span class="n">cmd</span>
</pre></div>
</div>
</li>
</ol>
</div></blockquote>
</div>
</div>
</div>
<div class="section" id="device-setup">
<span id="devicesetup"></span><h2>设备设置</h2>
<p>在执行范例程序之前，请确保设备已经连接，并按照以下步骤打开控制台窗口：</p>
<ol class="arabic">
<li><p>使用 USB-C 数据线将设备的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> 连接到主机 PC。</p>
<img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port2.gif">
</li>
<li><p>参考 <a class="reference internal" href="/docs/zh/udk/development-guide/firmware-reflashing#flashingfirmware"><span class="std std-ref">编程/升级固件</span></a> 部分的 OpenOCD 选项卡，安装 OpenOCD 工具. 本节还包括闪存固件的其他解决方案。</p></li>
<li><p>执行以下命令，打开minicom (Linux和macOs)或 <a class="reference external" href="https://teratermproject.github.io/index-en.html">Tera Term</a> (Windows) 访问已连接的串口，并准备好查看示例中打印的信息。</p></li>
</ol>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-21" name="sd-tab-set-8" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-21">
Ubuntu</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>打开终端</p></li>
<li><p>使用ttyACM&lt;X&gt;执行下面的命令（0是第一个连接设备的默认端口）</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">minicom -b 115200 -D /dev/ttyACM0</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>请使用以下命令验证所有连接的设备(ttyACM&lt;X&gt;)，您打算重新刷新这些设备</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">ls ../../dev/</span>
</pre></div>
</div>
</div></blockquote>
</div>
</li>
<li><p>成功连接设备后</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">Welcome to minicom 2.8</span>

<span class="go">OPTIONS: I18n</span>
<span class="go">Port /dev/ttyACM0, 04:49:57</span>

<span class="go">Press CTRL-A Z for help on special keys</span>
</pre></div>
</div>
</li>
</ol>
</div></blockquote>
</div>
<input id="sd-tab-item-22" name="sd-tab-set-8" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-22">
macOS</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>打开终端</p></li>
<li><p>使用/dev/tty.usb&lt;xxx&gt;执行以下命令（以modem1410为例）</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">minicom -b 115200 -D /dev/tty.usbmodem1410</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>请使用以下命令验证您打算重新刷新的连接设备 (tty.usb&lt;xxx&gt;)</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">ls ../../dev/</span>
</pre></div>
</div>
</div>
</li>
<li><p>成功连接设备后</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">Welcome to minicom 2.8</span>

<span class="go">OPTIONS:</span>
<span class="go">Compiled on Jan  4 2021, 00:04:46.</span>
<span class="go">Port /dev/tty.usbmodem1410, 19:42:45</span>

<span class="go">Press Meta-Z for help on special keys</span>
</pre></div>
</div>
</li>
</ol>
</div></blockquote>
</div>
<input id="sd-tab-item-23" name="sd-tab-set-8" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-23">
Windows</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>打开 <a class="reference external" href="https://teratermproject.github.io/index-en.html">Tera Term</a> 工具</p></li>
<li><p>转到设置&gt;串行端口</p>
<a class="reference internal image-reference" href="../../../_images/setup.png"><img alt="../../../_images/setup.png" src="/docs-assets/zh-cn/_images/setup.png" style="width: 523.2px; height: 268.0px;"></a>
</li>
<li><p>选择设备的连接端口 (例如：端口5正在连接设备)</p>
<a class="reference internal image-reference" href="../../../_images/port.png"><img alt="../../../_images/port.png" src="/docs-assets/zh-cn/_images/port.png" style="width: 373.6px; height: 359.20000000000005px;"></a>
</li>
<li><p>选择速度为 115200</p>
<a class="reference internal image-reference" href="../../../_images/speed.png"><img alt="../../../_images/speed.png" src="/docs-assets/zh-cn/_images/speed.png" style="width: 372.0px; height: 361.6px;"></a>
</li>
<li><p>选择关闭和新打开（或新打开）</p></li>
</ol>
</div></blockquote>
</div>
</div>
</div>
<div class="section" id="coordinated-examples-execution">
<h2>协调示例执行</h2>
<p>在 UDK-SDK 软件包的 <span class="sd-sphinx-override sd-badge sd-outline-info sd-text-info">@yourdir/udk-sdk/leaps-udk-examples/app/006_ex_uwb</span> 位置，提供了各种范例. 要实现协作式超宽带操作，需要如下表所示，将两个示例配对使用。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 51%">
<col style="width: 49%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>实例1</p></th>
<th class="head"><p>实例2</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ex_01a_simple_tx/simple_tx.c</p></td>
<td><p>ex_02a_simple_rx/simple_rx.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_01b_tx_sleep/tx_sleep_idleRC.c</p></td>
<td><p>ex_02a_simple_rx/simple_rx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_01b_tx_sleep/tx_sleep.c</p></td>
<td><p>ex_02a_simple_rx/simple_rx.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_01c_tx_sleep_auto/tx_sleep_auto.c</p></td>
<td><p>ex_02a_simple_rx/simple_rx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_01d_tx_timed_sleep/tx_timed_sleep.c</p></td>
<td><p>ex_02a_simple_rx/simple_rx.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_01e_tx_with_cca/tx_with_cca.c</p></td>
<td><p>ex_02a_simple_rx/simple_rx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_01g_simple_tx_sts_sdc/simple_tx_sts_sdc.c</p></td>
<td><p>ex_02g_simple_rx_sts_sdc/simple_rx_sts_sdc.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_01h_simple_tx_pdoa/simple_tx_pdoa.c</p></td>
<td><p>ex_02h_simple_rx_pdoa/simple_rx_pdoa.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_01i_simple_tx_aes/simple_tx_aes.c</p></td>
<td><p>ex_02i_simple_rx_aes/simple_rx_aes.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_02a_simple_rx/simple_rx_nlos.c</p></td>
<td><p>ex_01a_simple_tx/simple_tx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_02c_rx_diagnostics/rx_diagnostics.c</p></td>
<td><p>ex_01a_simple_tx/simple_tx.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_02d_rx_sniff/rx_sniff.c</p></td>
<td><p>ex_01a_simple_tx/simple_tx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_02e_rx_dbl_buff/double_buffer_rx.c</p></td>
<td><p>ex_01a_simple_tx/simple_tx.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_02f_rx_with_crystal_trim/rx_with_xtal_trim.c</p></td>
<td><p>ex_01a_simple_tx/simple_tx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_03a_tx_wait_resp/tx_wait_resp.c</p></td>
<td><p>ex_03b_rx_send_resp/rx_send_resp.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_03d_tx_wait_resp_interrupts/tx_wait_resp_int.c</p></td>
<td><p>ex_03b_rx_send_resp/rx_send_resp.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_05a_ds_twr_init/ds_twr_initiator.c</p></td>
<td><p>ex_05b_ds_twr_resp/ds_twr_responder.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_05a_ds_twr_init/ds_twr_initiator_sts.c</p></td>
<td><p>ex_05b_ds_twr_resp/ds_twr_responder_sts.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_05c_ds_twr_init_sts_sdc/ds_twr_sts_sdc_initiator.c</p></td>
<td><p>ex_05d_ds_twr_resp_sts_sdc/ds_twr_sts_sdc_responder.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_06a_ss_twr_initiator/ss_twr_initiator_sts_no_data.c</p></td>
<td><p>ex_06b_ss_twr_responder/ss_twr_responder_sts_no_data.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_06a_ss_twr_initiator/ss_twr_initiator_sts.c</p></td>
<td><p>ex_06b_ss_twr_responder/ss_twr_responder_sts.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_06a_ss_twr_initiator/ss_twr_initiator.c</p></td>
<td><p>ex_06b_ss_twr_responder/ss_twr_responder.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_06e_AES_ss_twr_initiator/ss_aes_twr_initiator.c</p></td>
<td><p>ex_06f_AES_ss_twr_responder/ss_aes_twr_responder.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_07a_ack_data_tx/ack_data_tx.c</p></td>
<td><p>ex_07b_ack_data_rx/ack_data_rx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_15_le_pend/le_pend_rx.c</p></td>
<td><p>ex_15_le_pend/le_pend_tx.c</p></td>
</tr>
</tbody>
</table>
<p>有关详细说明，请参阅每个示例的源文件*.c文件中提供的说明。</p>
<p><strong>例如:</strong> ex_01h_simple_tx_pdoa/simple_tx_pdoa.c</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">*  @file    simple_tx_pdoa.c</span>
<span class="go">*  @brief   Simple TX PDOA example code, companion to Simple RX PDOA example.</span>
<span class="go">*           See note 7 regarding information on calibrating the system</span>
</pre></div>
</div>
</div>
<hr class="docutils">
<div class="section" id="build-and-run-the-example">
<h2>构建并运行示例</h2>
<p>本节将指导您如何构建和重新刷新软件。</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>如果在 <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> 环境中出现任何问题，请参阅 <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/getting_started/index。html#troubleshooting-installation">安装</a> 故障排除 部分。</p>
</div>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-24" name="sd-tab-set-9" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-24">
Ubuntu</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>确保完整的 <a class="reference internal" href="#devicesetup"><span class="std std-ref">设备设置</span></a> 指南。</p></li>
<li><p>进入示例目录</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd leaps-udk-examples</span>
</pre></div>
</div>
</li>
<li><p>(可选) 清理旧的联编目录</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">rm -rf build/</span>
</pre></div>
</div>
</li>
<li><p>建立范例</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-27" name="sd-tab-set-10" type="radio">
<label class="sd-tab-label" for="sd-tab-item-27">
使用选择菜单</label><div class="sd-tab-content docutils">
<p>本节将指导你如何通过选择一个预期的示例来构建示例。</p>
<ol class="arabic">
<li><p>当 $BOARD 为 leaps_lc14 或 leaps_lc13 时，执行以下命令来显示菜单</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -t menuconfig -b $BOARD -s app</span>
</pre></div>
</div>
</li>
<li><p>选择 <strong>示例应用程序</strong>，然后按 Enter</p>
<a class="reference internal image-reference" href="../../../_images/main_menu.png"><img alt="../../../_images/main_menu.png" class="align-center" src="/docs-assets/zh-cn/_images/main_menu.png" style="width: 758.5px; height: 396.0px;"></a>
</li>
<li><p>你将看到默认的**示例**，如果你想选择其他示例，请按回车键</p>
<a class="reference internal image-reference" href="../../../_images/menu_default_example.png"><img alt="../../../_images/menu_default_example.png" class="align-center" src="/docs-assets/zh-cn/_images/menu_default_example.png" style="width: 688.5px; height: 385.5px;"></a>
</li>
<li><p>向上或向下滚动，选择**示例**，然后按回车键</p>
<a class="reference internal image-reference" href="../../../_images/menu_example_list.png"><img alt="../../../_images/menu_example_list.png" class="align-center" src="/docs-assets/zh-cn/_images/menu_example_list.png" style="width: 688.5px; height: 385.5px;"></a>
</li>
<li><p>按 ESC 和 Y 保存选择</p>
<a class="reference internal image-reference" href="../../../_images/menu_exit_andsave.png"><img alt="../../../_images/menu_exit_andsave.png" class="align-center" src="/docs-assets/zh-cn/_images/menu_exit_andsave.png" style="width: 688.5px; height: 385.5px;"></a>
</li>
<li><p>建立范例</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build</span>
</pre></div>
</div>
</li>
<li><p>成功建立范例</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[169/179] Linking C executable zephyr/zephyr_pre0.elf</span>

<span class="go">[173/179] Linking C executable zephyr/zephyr_pre1.elf</span>

<span class="go">[179/179] Linking C executable zephyr/zephyr.elf</span>
<span class="go">Memory region         Used Size  Region Size  %age Used</span>
<span class="go">           FLASH:       31268 B         1 MB      2.98%</span>
<span class="go">            SRAM:        8568 B       256 KB      3.27%</span>
<span class="go">        IDT_LIST:          0 GB         2 KB      0.00%</span>
</pre></div>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-28" name="sd-tab-set-10" type="radio">
<label class="sd-tab-label" for="sd-tab-item-28">
无选择菜单</label><div class="sd-tab-content docutils">
<p>本节将指导您如何使用默认示例构建示例。</p>
<ol class="arabic">
<li><p>执行以下命令，$BOARD 为 leaps_lc14 或 leaps_lc13</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -b $BOARD -s app</span>
</pre></div>
</div>
</li>
<li><p>成功建立范例</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[169/179] Linking C executable zephyr/zephyr_pre0.elf</span>

<span class="go">[173/179] Linking C executable zephyr/zephyr_pre1.elf</span>

<span class="go">[179/179] Linking C executable zephyr/zephyr.elf</span>
<span class="go">Memory region         Used Size  Region Size  %age Used</span>
<span class="go">           FLASH:       31268 B         1 MB      2.98%</span>
<span class="go">            SRAM:        8568 B       256 KB      3.27%</span>
<span class="go">        IDT_LIST:          0 GB         2 KB      0.00%</span>
</pre></div>
</div>
</li>
</ol>
</div>
</div>
</li>
<li><p>然后将十六进制文件重新刷新到设备上：</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west flash</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>成功，重新刷新固件</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">Open On-Chip Debugger 0.11.0+dev-00245-gaf169e805 (2022-05-14-14:24)</span>
<span class="go">Licensed under GNU GPL v2</span>
<span class="go">For bug reports, read</span>
<span class="go">        http://openocd.org/doc/doxygen/bugs.html</span>
<span class="go">DEPRECATED! use 'adapter speed' not 'adapter_khz'</span>
<span class="go">exit_debug_mode</span>
<span class="go">Info : Using CMSIS-DAPv2 interface with VID:PID=0x0d28:0x0204, serial=01100E003602002e00354146570120313238</span>
<span class="go">Info : CMSIS-DAP: SWD  Supported</span>
<span class="go">Info : CMSIS-DAP: FW Version = 2.1.0</span>
<span class="go">Info : CMSIS-DAP: Serial# = 01100E003602002e00354146570120313238</span>
<span class="go">Info : CMSIS-DAP: Interface Initialised (SWD)</span>
<span class="go">Info : SWCLK/TCK = 1 SWDIO/TMS = 1 TDI = 0 TDO = 0 nTRST = 0 nRESET = 1</span>
<span class="go">Info : CMSIS-DAP: Interface ready</span>
<span class="go">Info : clock speed 10000 kHz</span>
<span class="go">Info : SWD DPIDR 0x2ba01477</span>
<span class="go">Info : nrf52.cpu: hardware has 6 breakpoints, 4 watchpoints</span>
<span class="go">Info : starting gdb server for nrf52.cpu on 3333</span>
<span class="go">Info : Listening on port 3333 for gdb connections</span>
<span class="go">    TargetName         Type       Endian TapName            State</span>
<span class="go">--  ------------------ ---------- ------ ------------------ ------------</span>
<span class="go"> 0* nrf52.cpu          cortex_m   little nrf52.cpu          running</span>

<span class="go">target halted due to debug-request, current mode: Thread</span>
<span class="go">xPSR: 0x01000000 pc: 0x0000243c msp: 0x20001838</span>
<span class="go">Info : nRF52840-CKAA(build code: D0) 1024kB Flash, 256kB RAM</span>
<span class="go">Warn : Adding extra erase range, 0x00007a24 .. 0x00007fff</span>
<span class="go">auto erase enabled</span>
<span class="go">wrote 31268 bytes from file @/udk-sdk/zephyr/zephyr.hex in     1.151423s             (26.519 KiB/s)</span>

<span class="go">target halted due to debug-request, current mode: Thread</span>
<span class="go">xPSR: 0x01000000 pc: 0x0000243c msp: 0x20001838</span>
<span class="go">verified 31268 bytes in 0.092640s (329.611 KiB/s)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>分别按下C, B和A按钮运行TEST_BUTTONS示例时的输出。</p>
<blockquote>
<div><div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>***<span class="w"> </span>Booting<span class="w"> </span>Zephyr<span class="w"> </span>OS<span class="w"> </span>build<span class="w"> </span>5db7528340ec<span class="w">  </span>***
PRESS<span class="w"> </span>BUTTON<span class="w"> </span>EXAMPLE
Button<span class="w"> </span>C<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">24778</span>
Button<span class="w"> </span>C<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">28996</span>
Button<span class="w"> </span>B<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">76012</span>
Button<span class="w"> </span>B<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">81454</span>
Button<span class="w"> </span>A<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">104172</span>
Button<span class="w"> </span>A<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">109917</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
</div></blockquote>
</div>
<input id="sd-tab-item-25" name="sd-tab-set-9" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-25">
macOS</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>确保完整的 <a class="reference internal" href="#devicesetup"><span class="std std-ref">设备设置</span></a> 指南。</p></li>
<li><p>进入示例目录</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd leaps-udk-examples</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>(可选) 清理旧的联编目录</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">rm -rf build/</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>建立范例</p>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-29" name="sd-tab-set-11" type="radio">
<label class="sd-tab-label" for="sd-tab-item-29">
使用选择菜单</label><div class="sd-tab-content docutils">
<p>本节将指导您如何通过选择一个预期示例来构建示例。</p>
<ol class="arabic">
<li><p>当 $BOARD 为 leaps_lc14 或 leaps_lc13 时，执行以下命令来显示菜单</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -t menuconfig -b $BOARD -s app</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>选择 <strong>示例应用程序</strong>，然后按 Enter</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/main_menu.png"><img alt="../../../_images/main_menu.png" class="align-center" src="/docs-assets/zh-cn/_images/main_menu.png" style="width: 758.5px; height: 396.0px;"></a>
</div></blockquote>
</li>
<li><p>你将看到默认的**示例**，如果你想选择其他示例，请按回车键</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_default_example.png"><img alt="../../../_images/menu_default_example.png" class="align-center" src="/docs-assets/zh-cn/_images/menu_default_example.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
</li>
<li><p>通过向上/向下滚动选择**示例**，然后按 Enter</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_example_list.png"><img alt="../../../_images/menu_example_list.png" class="align-center" src="/docs-assets/zh-cn/_images/menu_example_list.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
</li>
<li><p>按 ESC 和 Y 保存选择</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_exit_andsave.png"><img alt="../../../_images/menu_exit_andsave.png" class="align-center" src="/docs-assets/zh-cn/_images/menu_exit_andsave.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
</li>
<li><p>建立范例</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>成功建立范例</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[169/179] Linking C executable zephyr/zephyr_pre0.elf</span>

<span class="go">[173/179] Linking C executable zephyr/zephyr_pre1.elf</span>

<span class="go">[179/179] Linking C executable zephyr/zephyr.elf</span>
<span class="go">Memory region         Used Size  Region Size  %age Used</span>
<span class="go">           FLASH:       31268 B         1 MB      2.98%</span>
<span class="go">            SRAM:        8568 B       256 KB      3.27%</span>
<span class="go">        IDT_LIST:          0 GB         2 KB      0.00%</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
</div>
<input id="sd-tab-item-30" name="sd-tab-set-11" type="radio">
<label class="sd-tab-label" for="sd-tab-item-30">
无选择菜单</label><div class="sd-tab-content docutils">
<p>本节将指导您如何使用默认示例构建示例。</p>
<ol class="arabic">
<li><p>执行以下命令，$BOARD 为 leaps_lc14 或 leaps_lc13</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -b $BOARD</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>成功建立范例</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[169/179] Linking C executable zephyr/zephyr_pre0.elf</span>

<span class="go">[173/179] Linking C executable zephyr/zephyr_pre1.elf</span>

<span class="go">[179/179] Linking C executable zephyr/zephyr.elf</span>
<span class="go">Memory region         Used Size  Region Size  %age Used</span>
<span class="go">           FLASH:       31268 B         1 MB      2.98%</span>
<span class="go">            SRAM:        8568 B       256 KB      3.27%</span>
<span class="go">        IDT_LIST:          0 GB         2 KB      0.00%</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
</div>
</div>
</div></blockquote>
</li>
<li><p>然后将十六进制文件重新刷新到设备上：</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west flash</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>成功，重新刷新固件</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">Open On-Chip Debugger 0.11.0+dev-00245-gaf169e805 (2022-05-14-14:24)</span>
<span class="go">Licensed under GNU GPL v2</span>
<span class="go">For bug reports, read</span>
<span class="go">        http://openocd.org/doc/doxygen/bugs.html</span>
<span class="go">DEPRECATED! use 'adapter speed' not 'adapter_khz'</span>
<span class="go">exit_debug_mode</span>
<span class="go">Info : Using CMSIS-DAPv2 interface with VID:PID=0x0d28:0x0204, serial=01100E003602002e00354146570120313238</span>
<span class="go">Info : CMSIS-DAP: SWD  Supported</span>
<span class="go">Info : CMSIS-DAP: FW Version = 2.1.0</span>
<span class="go">Info : CMSIS-DAP: Serial# = 01100E003602002e00354146570120313238</span>
<span class="go">Info : CMSIS-DAP: Interface Initialised (SWD)</span>
<span class="go">Info : SWCLK/TCK = 1 SWDIO/TMS = 1 TDI = 0 TDO = 0 nTRST = 0 nRESET = 1</span>
<span class="go">Info : CMSIS-DAP: Interface ready</span>
<span class="go">Info : clock speed 10000 kHz</span>
<span class="go">Info : SWD DPIDR 0x2ba01477</span>
<span class="go">Info : nrf52.cpu: hardware has 6 breakpoints, 4 watchpoints</span>
<span class="go">Info : starting gdb server for nrf52.cpu on 3333</span>
<span class="go">Info : Listening on port 3333 for gdb connections</span>
<span class="go">    TargetName         Type       Endian TapName            State</span>
<span class="go">--  ------------------ ---------- ------ ------------------ ------------</span>
<span class="go"> 0* nrf52.cpu          cortex_m   little nrf52.cpu          running</span>

<span class="go">target halted due to debug-request, current mode: Thread</span>
<span class="go">xPSR: 0x01000000 pc: 0x0000243c msp: 0x20001838</span>
<span class="go">Info : nRF52840-CKAA(build code: D0) 1024kB Flash, 256kB RAM</span>
<span class="go">Warn : Adding extra erase range, 0x00007a24 .. 0x00007fff</span>
<span class="go">auto erase enabled</span>
<span class="go">wrote 31268 bytes from file @/udk-sdk/zephyr/zephyr.hex in     1.151423s             (26.519 KiB/s)</span>

<span class="go">target halted due to debug-request, current mode: Thread</span>
<span class="go">xPSR: 0x01000000 pc: 0x0000243c msp: 0x20001838</span>
<span class="go">verified 31268 bytes in 0.092640s (329.611 KiB/s)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>分别按下C, B和A按钮运行TEST_BUTTONS示例时的输出。</p>
<blockquote>
<div><div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>***<span class="w"> </span>Booting<span class="w"> </span>Zephyr<span class="w"> </span>OS<span class="w"> </span>build<span class="w"> </span>5db7528340ec<span class="w">  </span>***
PRESS<span class="w"> </span>BUTTON<span class="w"> </span>EXAMPLE
Button<span class="w"> </span>C<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">24778</span>
Button<span class="w"> </span>C<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">28996</span>
Button<span class="w"> </span>B<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">76012</span>
Button<span class="w"> </span>B<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">81454</span>
Button<span class="w"> </span>A<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">104172</span>
Button<span class="w"> </span>A<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">109917</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
</div></blockquote>
</div>
<input id="sd-tab-item-26" name="sd-tab-set-9" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-26">
Windows</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>确保完整的 <a class="reference internal" href="#devicesetup"><span class="std std-ref">设备设置</span></a> 指南。</p></li>
<li><p>进入示例目录</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd leaps-udk-examples</span>
</pre></div>
</div>
</li>
<li><p>（可选）清理旧的联编目录，然后按 Y</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">rd /s build</span>
</pre></div>
</div>
</li>
<li><p>建立范例</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-31" name="sd-tab-set-12" type="radio">
<label class="sd-tab-label" for="sd-tab-item-31">
使用选择菜单</label><div class="sd-tab-content docutils">
<p>本节将指导你如何通过选择一个预期的示例来构建示例。</p>
<ol class="arabic simple">
<li><p>当 $BOARD 为 leaps_lc14 或 leaps_lc13 时，执行以下命令来显示菜单</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -t menuconfig -b $BOARD -s app</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple">
<li><p>选择 <strong>示例应用程序</strong>，然后按 Enter</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/main_menu.png"><img alt="../../../_images/main_menu.png" class="align-center" src="/docs-assets/zh-cn/_images/main_menu.png" style="width: 758.5px; height: 396.0px;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>你将看到默认的**示例**，如果你想选择其他示例，请按回车键</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_default_example.png"><img alt="../../../_images/menu_default_example.png" class="align-center" src="/docs-assets/zh-cn/_images/menu_default_example.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>向上或向下滚动，选择**示例**，然后按回车键</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_example_list.png"><img alt="../../../_images/menu_example_list.png" class="align-center" src="/docs-assets/zh-cn/_images/menu_example_list.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>按 ESC 和 Y 保存选择</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_exit_andsave.png"><img alt="../../../_images/menu_exit_andsave.png" class="align-center" src="/docs-assets/zh-cn/_images/menu_exit_andsave.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>建立范例</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple">
<li><p>成功建立范例</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[152/158] Linking C executable zephyr\zephyr_pre1.elf←[K1.dir/dev_handles.c.obj←[Kj←[K</span>

<span class="go">[158/158] Linking C executable zephyr\zephyr.elf←[Kr_final.dir/dev_handles.c.obj←[Kj←[K</span>
<span class="go">Memory region         Used Size  Region Size  %age Used</span>
<span class="go">           FLASH:       32668 B         1 MB      3.12%</span>
<span class="go">            SRAM:        4496 B       248 KB      1.77%</span>
<span class="go">        IDT_LIST:          0 GB         2 KB      0.00%</span>
</pre></div>
</div>
</div></blockquote>
</div>
<input id="sd-tab-item-32" name="sd-tab-set-12" type="radio">
<label class="sd-tab-label" for="sd-tab-item-32">
无选择菜单</label><div class="sd-tab-content docutils">
<p>本节将指导您如何使用默认示例构建示例。</p>
<ol class="arabic">
<li><p>执行以下命令，$BOARD 为 leaps_lc14 或 leaps_lc13</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -b $BOARD -s app</span>
</pre></div>
</div>
</li>
<li><p>成功建立范例</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[1/161] Generating include/generated/version.h</span>
<span class="go">-- Zephyr version: 3.1.0 (@/udk-sdk/zephyr), build: zephyr-v3.1.0</span>
<span class="go">[151/161] Linking C executable zephyr\zephyr_pre0.elf</span>

<span class="go">[155/161] Linking C executable zephyr\zephyr_pre1.elf</span>

<span class="go">[161/161] Linking C executable zephyr\zephyr.elf</span>
<span class="go">Memory region         Used Size  Region Size  %age Used</span>
<span class="go">           FLASH:       91160 B         1 MB      8.69%</span>
<span class="go">            SRAM:        5056 B       248 KB      1.99%</span>
<span class="go">        IDT_LIST:          0 GB         2 KB      0.00%</span>
</pre></div>
</div>
</li>
</ol>
</div>
</div>
</li>
<li><p>然后将十六进制文件重新刷新到设备上：</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west flash</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>成功，重新刷新固件</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">-- west flash: rebuilding</span>
<span class="go">ninja: no work to do.</span>
<span class="go">-- west flash: using runner openocd</span>
<span class="go">-- runners.openocd: Flashing file: D:/01_Work/udk-sdk/udk-sdk/leaps-udk-examples/build/zephyr/zephyr.hex</span>
<span class="go">xPack Open On-Chip Debugger 0.12.0-01004-g9ea7f3d64-dirty (2023-01-30-15:04)</span>
<span class="go">Licensed under GNU GPL v2</span>
<span class="go">For bug reports, read</span>
<span class="go">        http://openocd.org/doc/doxygen/bugs.html</span>
<span class="go">DEPRECATED! use 'adapter speed' not 'adapter_khz'</span>
<span class="go">exit_debug_mode</span>
<span class="go">Info : Using CMSIS-DAPv2 interface with VID:PID=0x0d28:0x0204, serial=01100E003602002d00184146570120313238</span>
<span class="go">Info : CMSIS-DAP: SWD supported</span>
<span class="go">Info : CMSIS-DAP: Atomic commands supported</span>
<span class="go">Info : CMSIS-DAP: Test domain timer supported</span>
<span class="go">Info : CMSIS-DAP: FW Version = 2.1.0</span>
<span class="go">Info : CMSIS-DAP: Serial# = 01100E003602002d00184146570120313238</span>
<span class="go">Info : CMSIS-DAP: Interface Initialised (SWD)</span>
<span class="go">Info : SWCLK/TCK = 1 SWDIO/TMS = 1 TDI = 0 TDO = 0 nTRST = 0 nRESET = 1</span>
<span class="go">Info : CMSIS-DAP: Interface ready</span>
<span class="go">Info : clock speed 10000 kHz</span>
<span class="go">Info : SWD DPIDR 0x2ba01477</span>
<span class="go">Info : [nrf52.cpu] Cortex-M4 r0p1 processor detected</span>
<span class="go">Info : [nrf52.cpu] target has 6 breakpoints, 4 watchpoints</span>
<span class="go">Info : starting gdb server for nrf52.cpu on 3333</span>
<span class="go">Info : Listening on port 3333 for gdb connections</span>
<span class="go">    TargetName         Type       Endian TapName            State</span>
<span class="go">--  ------------------ ---------- ------ ------------------ ------------</span>
<span class="go"> 0* nrf52.cpu          cortex_m   little nrf52.cpu          running</span>

<span class="go">[nrf52.cpu] halted due to debug-request, current mode: Thread</span>
<span class="go">xPSR: 0x01000000 pc: 0x00002e10 msp: 0x20002b10</span>
<span class="go">Info : nRF52840-CKAA(build code: D0) 1024kB Flash, 256kB RAM</span>
<span class="go">Warn : Adding extra erase range, 0x00007f9c .. 0x00007fff</span>
<span class="go">auto erase enabled</span>
<span class="go">wrote 32668 bytes from file D:/01_Work/udk-sdk/udk-sdk/leaps-udk-examples/build/zephyr/zephyr.hex in 1.178412s (27.072 KiB/s)</span>

<span class="go">[nrf52.cpu] halted due to debug-request, current mode: Thread</span>
<span class="go">xPSR: 0x01000000 pc: 0x00002a5c msp: 0x20002850</span>
<span class="go">verified 32668 bytes in 0.099523s (320.552 KiB/s)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>分别按下C, B和A按钮运行TEST_BUTTONS示例时的输出。</p>
<blockquote>
<div><div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>***<span class="w"> </span>Booting<span class="w"> </span>Zephyr<span class="w"> </span>OS<span class="w"> </span>build<span class="w"> </span>5db7528340ec<span class="w">  </span>***
PRESS<span class="w"> </span>BUTTON<span class="w"> </span>EXAMPLE
Button<span class="w"> </span>C<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">24778</span>
Button<span class="w"> </span>C<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">28996</span>
Button<span class="w"> </span>B<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">76012</span>
Button<span class="w"> </span>B<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">81454</span>
Button<span class="w"> </span>A<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">104172</span>
Button<span class="w"> </span>A<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">109917</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
</div></blockquote>
</div>
</div>
</div>
</div>


           </div>
