---
title: "UDK-SDK Getting Started"
lang: en
slug: "udk/development-guide/udk-sdk-getting-started"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/development-guide/udk-sdk-getting-started/"
order: 45
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="udk-sdk-getting-started">
<span id="udksdk"></span><h1>UDK-SDK Getting Started</h1>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Please note, that development of the third-party application is out of scope of
the UDK offering and hence is not a part of the pre-paid UDK support.</p>
</div>
<p>This section offers comprehensive guidance on selecting and launching LEAPS example project, designed for the Zephyr RTOS platform. These examples facilitate a deeper understanding of <strong>UWB (Ultra-Wideband) technology</strong> and the UDK kit’s <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">Hardware Interfaces</span></a>.</p>
<p>Armed with this knowledge, users can confidently develop custom applications on the UDK kit.</p>
<p><strong>The guidance follows these steps:</strong></p>
<ol class="arabic simple">
<li><p>Set up development environment for <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> RTOS on Linux, macOS, or Windows.</p></li>
<li><p>Acquire the UDK’s SDK which is <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> based example application package.</p></li>
<li><p>Connecting devices to host PC and required tools.</p></li>
<li><p>Select the example, build, flash, and run an example application.</p></li>
</ol>
<hr class="docutils">
<div class="section" id="zephyr-s-getting-started-guide">
<h2>Zephyr’s Getting Started Guide</h2>
<p>Follow this guide to:</p>
<ul class="simple">
<li><p>Set up a command-line Zephyr development environment on Ubuntu, macOS, or Windows (instructions for other Linux distributions are discussed in <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/getting_started/installation_linux.html#installation-linux">installation_linux</a>)</p></li>
<li><p>Install the Zephyr’s SDK package (including required tool chains)</p></li>
</ul>
<div class="section" id="select-and-update-os">
<h3>Select and Update OS</h3>
<p>Click the operating system you are using.</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-0">
Ubuntu</label><div class="sd-tab-content docutils">
<p>This guide covers Ubuntu version 20.04 LTS and later.</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>apt<span class="w"> </span>update
sudo<span class="w"> </span>apt<span class="w"> </span>upgrade
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-1">
macOS</label><div class="sd-tab-content docutils">
<p>On macOS Mojave or later, select <em>System Preferences</em> &gt;*Software Update*. Click <em>Update Now</em> if necessary.</p>
<p>On other versions, see <a class="reference external" href="https://support.apple.com/en-us/HT201541">this Apple support topic</a>.</p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-2">
Windows</label><div class="sd-tab-content docutils">
<p>Select <em>Start</em> &gt; <em>Settings</em> &gt; <em>Update &amp; Security</em> &gt; <em>Windows Update</em>.
Click <em>Check for updates</em> and install any that are available.</p>
</div>
</div>
</div>
<div class="section" id="install-dependencies">
<h3>Install dependencies</h3>
<p>Next, you’ll install some host dependencies using your package manager.</p>
<p>The current minimum required version for the main dependencies are:</p>
<table class="docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Tool</p></th>
<th class="head"><p>Min. Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference external" href="https://cmake.org/">CMake</a></p></td>
<td><p>3.20.5</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference external" href="https://www.python.org/">Python</a></p></td>
<td><p>3.10</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference external" href="https://www.devicetree.org/">Devicetree compiler</a></p></td>
<td><p>1.4.6</p></td>
</tr>
</tbody>
</table>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-3">
Ubuntu</label><div class="sd-tab-content docutils">
<ol class="arabic" id="install-dependencies-ubuntu">
<li><p>If using an Ubuntu version older than 22.04, it is necessary to add extra repositories to meet the minimum required versions for the main
dependencies listed above. In that case, download, inspect and execute the Kitware archive script to add the Kitware APT repository to your
sources list. A detailed explanation of <code class="docutils literal notranslate"><span class="pre">kitware-archive.sh</span></code> can be found here <a class="reference external" href="https://apt.kitware.com/">kitware third-party apt repository</a>:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>wget<span class="w"> </span>https://apt.kitware.com/kitware-archive.sh
sudo<span class="w"> </span>bash<span class="w"> </span>kitware-archive.sh
</pre></div>
</div>
</li>
<li><p>Use <code class="docutils literal notranslate"><span class="pre">apt</span></code> to install the required dependencies:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>apt<span class="w"> </span>install<span class="w"> </span>--no-install-recommends<span class="w"> </span>git<span class="w"> </span>cmake<span class="w"> </span>ninja-build<span class="w"> </span>gperf<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>ccache<span class="w"> </span>dfu-util<span class="w"> </span>device-tree-compiler<span class="w"> </span>wget<span class="w"> </span>minicom<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>python3-dev<span class="w"> </span>python3-pip<span class="w"> </span>python3-setuptools<span class="w"> </span>python3-tk<span class="w"> </span>python3-wheel<span class="w"> </span>xz-utils<span class="w"> </span>file<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>make<span class="w"> </span>gcc<span class="w"> </span>gcc-multilib<span class="w"> </span>g++-multilib<span class="w"> </span>libsdl2-dev<span class="w"> </span>libmagic1
</pre></div>
</div>
</li>
<li><p>Verify the versions of the main dependencies installed on your system by entering:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>--version
python3<span class="w"> </span>--version
dtc<span class="w"> </span>--version
</pre></div>
</div>
<p>Check those against the versions in the table in the beginning of this section. Refer to the <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/getting_started/installation_linux.html#installation-linux">installation_linux</a> page for additional information on updating the dependencies manually.</p>
</li>
</ol>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-4">
macOS</label><div class="sd-tab-content docutils">
<ol class="arabic" id="install-dependencies-macos">
<li><p>Install <a class="reference external" href="https://brew.sh/">Homebrew</a>:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>/bin/bash<span class="w"> </span>-c<span class="w"> </span><span class="s2">"</span><span class="k">$(</span>curl<span class="w"> </span>-fsSL<span class="w"> </span>https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh<span class="k">)</span><span class="s2">"</span>
</pre></div>
</div>
</li>
<li><p>After the Homebrew installation script completes, follow the on-screen
instructions to add the Homebrew installation to the path.</p>
<ul>
<li><p>On macOS running on Apple Silicon, this is achieved with:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="o">(</span>echo<span class="p">;</span><span class="w"> </span><span class="nb">echo</span><span class="w"> </span><span class="s1">'eval "$(/opt/homebrew/bin/brew shellenv)"'</span><span class="o">)</span><span class="w"> </span>&gt;&gt;<span class="w"> </span>~/.zprofile
<span class="nb">source</span><span class="w"> </span>~/.zprofile
</pre></div>
</div>
</li>
<li><p>On macOS running on Intel, use the command for Apple Silicon, but replace <code class="docutils literal notranslate"><span class="pre">/opt/homebrew/</span></code> with <code class="docutils literal notranslate"><span class="pre">/usr/local/</span></code>.</p></li>
</ul>
</li>
<li><p>Use <code class="docutils literal notranslate"><span class="pre">brew</span></code> to install the required dependencies:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>brew<span class="w"> </span>install<span class="w"> </span>cmake<span class="w"> </span>ninja<span class="w"> </span>gperf<span class="w"> </span>python3<span class="w"> </span>ccache<span class="w"> </span>qemu<span class="w"> </span>dtc<span class="w"> </span>libmagic<span class="w"> </span>wget<span class="w"> </span>openocd<span class="w"> </span>minicom
</pre></div>
</div>
</li>
<li><p>Add the Homebrew Python folder to the path, in order to be able to
execute <code class="docutils literal notranslate"><span class="pre">python</span></code> and <code class="docutils literal notranslate"><span class="pre">pip</span></code> as well <code class="docutils literal notranslate"><span class="pre">python3</span></code> and <code class="docutils literal notranslate"><span class="pre">pip3</span></code>.</p>
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
<p class="admonition-title">Note</p>
<p>Due to issues finding executables, the Zephyr Project doesn’t currently support application flashing using the <a class="reference external" href="https://msdn.microsoft.com/en-us/commandline/wsl/install_guide">Windows Subsystem for Linux (WSL)</a> (WSL).</p>
<p>Therefore, we don’t recommend using WSL when getting started.</p>
</div>
<p>These instructions must be run in a <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> command prompt terminal window.
In modern version of Windows (10 and later) it is recommended to install the Windows Terminal application from the Microsoft Store. The required commands differ on PowerShell.</p>
<p>These instructions rely on <a class="reference external" href="https://chocolatey.org/">Chocolatey</a>. If Chocolatey isn’t an option, you can install dependencies from their respective websites and ensure
the command line tools are on your <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/env_vars.html#envvar-PATH">PATH</a> <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/env_vars.html#env-vars">environment variable</a>.</p>
<ol class="arabic" id="install-dependencies-windows">
<li><p><a class="reference external" href="https://chocolatey.org/install">Install chocolatey</a>.</p></li>
<li><p>Open a <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> terminal window as <strong>Administrator</strong>. To do so, press the Windows key,
type <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code>, right-click the <span class="guilabel">Command Prompt</span> search result, and choose
<span class="guilabel">Run as Administrator</span>.</p></li>
<li><p>Disable global confirmation to avoid having to confirm the
installation of individual programs:</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>choco feature enable -n allowGlobalConfirmation
</pre></div>
</div>
</li>
<li><p>Use <code class="docutils literal notranslate"><span class="pre">choco</span></code> to install the required dependencies:</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>choco install cmake --installargs 'ADD_CMAKE_TO_PATH=System'
choco install ninja gperf python311 git dtc-msys2 wget 7zip unzip
</pre></div>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>As of November 2023, Python 3.12 is not recommended for Zephyr development on Windows,
as some required Python dependencies may be difficult to install.</p>
</div>
</li>
<li><p>Close the terminal window.</p></li>
</ol>
</div>
</div>
</div>
<div class="section" id="install-west">
<h3>Install West</h3>
<p><a class="reference external" href="https://docs.zephyrproject.org/latest/develop/west/index.html">West</a> is a swiss-army knife command line tool for <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a>, to install it, please execute following commands:</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-6" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-6">
Ubuntu</label><div class="sd-tab-content docutils">
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-9" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
Install within virtual environment</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>Use <code class="docutils literal notranslate"><span class="pre">apt</span></code> to install Python <code class="docutils literal notranslate"><span class="pre">venv</span></code> package:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>apt<span class="w"> </span>install<span class="w"> </span>python3-venv
</pre></div>
</div>
</li>
<li><p>Create a new virtual environment:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>python3<span class="w"> </span>-m<span class="w"> </span>venv<span class="w"> </span>~/udk-sdk/.venv
</pre></div>
</div>
</li>
<li><p>Activate the virtual environment:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">source</span><span class="w"> </span>~/udk-sdk/.venv/bin/activate
</pre></div>
</div>
<p>Once activated your shell will be prefixed with <code class="docutils literal notranslate"><span class="pre">(.venv)</span></code>. The
virtual environment can be deactivated at any time by running
<code class="docutils literal notranslate"><span class="pre">deactivate</span></code>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Remember to activate the virtual environment every time you
start working.</p>
</div>
</li>
<li><p>Install west</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>west
</pre></div>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-10" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-10">
Install globally</label><div class="sd-tab-content docutils">
<p>Install west, and make sure <code class="file docutils literal notranslate"><span class="pre">~/.local/bin</span></code> is on your <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/env_vars.html#envvar-PATH">PATH</a> <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/env_vars.html#env-vars">environment variable</a>:</p>
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
Install within virtual environment</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>Create a new virtual environment:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>python3<span class="w"> </span>-m<span class="w"> </span>venv<span class="w"> </span>~/udk-sdk/.venv
</pre></div>
</div>
</li>
<li><p>Activate the virtual environment:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">source</span><span class="w"> </span>~/udk-sdk/.venv/bin/activate
</pre></div>
</div>
<p>Once activated your shell will be prefixed with <code class="docutils literal notranslate"><span class="pre">(.venv)</span></code>. The
virtual environment can be deactivated at any time by running
<code class="docutils literal notranslate"><span class="pre">deactivate</span></code>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Remember to activate the virtual environment every time you
start working.</p>
</div>
</li>
<li><p>Install west</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>west
</pre></div>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-12" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-12">
Install globally</label><div class="sd-tab-content docutils">
<p>Install west</p>
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
Install within virtual environment</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>Open a <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> terminal window <strong>as a regular user</strong></p></li>
<li><p>Create a new virtual environment:</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span><span class="k">cd</span> <span class="nv">%HOMEPATH%</span>
python -m venv udk-sdk\.venv
</pre></div>
</div>
</li>
<li><p>Activate the virtual environment:</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>udk-sdk\.venv\Scripts\activate.bat
</pre></div>
</div>
<p>Once activated your shell will be prefixed with <code class="docutils literal notranslate"><span class="pre">(.venv)</span></code>. The
virtual environment can be deactivated at any time by running
<code class="docutils literal notranslate"><span class="pre">deactivate</span></code>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Remember to activate the virtual environment every time you
start working.</p>
</div>
</li>
<li><p>Install west</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>pip install west
</pre></div>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-14" name="sd-tab-set-5" type="radio">
<label class="sd-tab-label" for="sd-tab-item-14">
Install globally</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>Open a <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> terminal window <strong>as a regular user</strong></p></li>
<li><p>Install west</p>
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
<span id="installthezephyrsdk"></span><h3>Install the Zephyr SDK</h3>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If you want to uninstall the SDK, you may simply remove the directory where you installed it.</p>
</div>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-15" name="sd-tab-set-6" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-15">
Ubuntu</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>Download and verify the <a class="reference external" href="https://github.com/zephyrproject-rtos/sdk-ng/tree/v0.14.2">Zephyr SDK bundle</a>:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="o">~</span>
<span class="n">wget</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_linux</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">tar</span><span class="o">.</span><span class="n">gz</span>
<span class="n">wget</span> <span class="o">-</span><span class="n">O</span> <span class="o">-</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">sha256</span><span class="o">.</span><span class="n">sum</span> <span class="o">|</span> <span class="n">shasum</span> <span class="o">--</span><span class="n">check</span> <span class="o">--</span><span class="n">ignore</span><span class="o">-</span><span class="n">missing</span>
</pre></div>
</div>
<p>If your host architecture is 64-bit ARM (for example, Raspberry Pi), replace <code class="docutils literal notranslate"><span class="pre">x86_64</span></code> with <code class="docutils literal notranslate"><span class="pre">aarch64</span></code> in order to download the 64-bit ARM Linux SDK.</p>
</li>
<li><p>Extract the Zephyr SDK bundle archive:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">tar</span> <span class="n">xvf</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_linux</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">tar</span><span class="o">.</span><span class="n">gz</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>It is recommended to extract the Zephyr SDK bundle at one of the following locations:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/.local</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/.local/opt</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/bin</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">/opt</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">/usr/local</span></code></p></li>
</ul>
<p>The Zephyr SDK bundle archive contains the <code class="docutils literal notranslate"><span class="pre">zephyr-sdk-&lt;version&gt;</span></code> directory and, when extracted under <code class="docutils literal notranslate"><span class="pre">$HOME</span></code>, the resulting installation path will be <code class="docutils literal notranslate"><span class="pre">$HOME/zephyr-sdk-&lt;version&gt;</span></code>.</p>
</div>
</li>
<li><p>Run the Zephyr SDK bundle setup script:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span>
<span class="o">./</span><span class="n">setup</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>You only need to run the setup script once after extracting the Zephyr SDK bundle.</p>
<p>You must rerun the setup script if you relocate the Zephyr SDK bundle directory after the initial setup.</p>
</div>
</li>
<li><p>Install <a class="reference external" href="https://en.wikipedia.org/wiki/Udev">udev</a> rules, which allow you to flash most Zephyr boards as a regular user:</p>
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
<li><p>Download and verify the <a class="reference external" href="https://github.com/zephyrproject-rtos/sdk-ng/tree/v0.14.2">Zephyr SDK bundle</a>:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="o">~</span>
<span class="n">curl</span> <span class="o">-</span><span class="n">L</span> <span class="o">-</span><span class="n">O</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_macos</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">tar</span><span class="o">.</span><span class="n">gz</span>
<span class="n">curl</span> <span class="o">-</span><span class="n">L</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">sha256</span><span class="o">.</span><span class="n">sum</span> <span class="o">|</span> <span class="n">shasum</span> <span class="o">--</span><span class="n">check</span> <span class="o">--</span><span class="n">ignore</span><span class="o">-</span><span class="n">missing</span>
</pre></div>
</div>
<p>If your host architecture is 64-bit ARM (Apple Silicon, also known as M1), replace <code class="docutils literal notranslate"><span class="pre">x86_64</span></code> with <code class="docutils literal notranslate"><span class="pre">aarch64</span></code> in order to download the 64-bit ARM macOS SDK.</p>
</li>
<li><p>Extract the Zephyr SDK bundle archive:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">tar</span> <span class="n">xvf</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_macos</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">tar</span><span class="o">.</span><span class="n">gz</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>It is recommended to extract the Zephyr SDK bundle at one of the following locations:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/.local</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/.local/opt</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/bin</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">/opt</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">/usr/local</span></code></p></li>
</ul>
<p>The Zephyr SDK bundle archive contains the <code class="docutils literal notranslate"><span class="pre">zephyr-sdk-&lt;version&gt;</span></code> directory and, when extracted under <code class="docutils literal notranslate"><span class="pre">$HOME</span></code>, the resulting installation path will be <code class="docutils literal notranslate"><span class="pre">$HOME/zephyr-sdk-&lt;version&gt;</span></code>.</p>
</div>
</li>
<li><p>Run the Zephyr SDK bundle setup script:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span>
<span class="o">./</span><span class="n">setup</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>You only need to run the setup script once after extracting the Zephyr SDK bundle.</p>
<p>You must rerun the setup script if you relocate the Zephyr SDK bundle directory after the initial setup.</p>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-17" name="sd-tab-set-6" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-17">
Windows</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>Open a <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> terminal window <strong>as a regular user</strong></p></li>
<li><p>Download the <a class="reference external" href="https://github.com/zephyrproject-rtos/sdk-ng/tree/v0.14.2">Zephyr SDK bundle</a>:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="o">%</span><span class="n">HOMEPATH</span><span class="o">%</span>
<span class="n">wget</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_windows</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">zip</span>
</pre></div>
</div>
</li>
<li><p>Extract the Zephyr SDK bundle archive:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">unzip</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_windows</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">zip</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>It is recommended to extract the Zephyr SDK bundle at one of the following locations:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">%HOMEPATH%</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">%PROGRAMFILES%</span></code></p></li>
</ul>
<p>The Zephyr SDK bundle archive contains the <code class="docutils literal notranslate"><span class="pre">zephyr-sdk-&lt;version&gt;</span></code>
directory and, when extracted under <code class="docutils literal notranslate"><span class="pre">%HOMEPATH%</span></code>, the resulting
installation path will be <code class="docutils literal notranslate"><span class="pre">%HOMEPATH%\zephyr-sdk-&lt;version&gt;</span></code>.</p>
</div>
</li>
<li><p>Run the Zephyr SDK bundle setup script:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span>
<span class="n">setup</span><span class="o">.</span><span class="n">cmd</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>You only need to run the setup script once after extracting the Zephyr SDK bundle.</p>
<p>You must rerun the setup script if you relocate the Zephyr SDK bundle directory after
the initial setup.</p>
</div>
</li>
</ol>
</div>
</div>
</div>
</div>
<div class="section" id="install-udk-sdk-package">
<h2>Install UDK-SDK package</h2>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The UDK SDK is also a Zephyr-based example application. For a deeper understanding, please refer to this <a class="reference external" href="https://github.com/zephyrproject-rtos/example-application">example-application</a> page.</p>
</div>
<p>The first step is to initialize the workspace folder <code class="docutils literal notranslate"><span class="pre">udk-sdk</span></code> where the <code class="docutils literal notranslate"><span class="pre">leaps-udk-examples</span></code> and all Zephyr modules will be cloned.
Please follow these instructions:</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-18" name="sd-tab-set-7" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-18">
Ubuntu</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>Open the Terminal</p></li>
<li><p>Initialize <code class="docutils literal notranslate"><span class="pre">udk-sdk</span></code> workspace for the <code class="docutils literal notranslate"><span class="pre">leaps-udk-examples</span></code> with main revision.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">init</span> <span class="o">-</span><span class="n">m</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">leapslabs</span><span class="o">/</span><span class="n">udk</span><span class="o">-</span><span class="n">sdk</span><span class="o">.</span><span class="n">git</span> <span class="o">--</span><span class="n">mr</span> <span class="n">main</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
</pre></div>
</div>
</li>
<li><p>Clone the <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> source (version 3.1.0) and its modules.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
<span class="n">west</span> <span class="n">update</span>
</pre></div>
</div>
</li>
<li><p>Export a <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> CMake package. This allows CMake to automatically load boilerplate code required for building Zephyr applications.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">export</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a>’s scripts/requirements.txt file declares additional Python dependencies. Install them with pip.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="o">./</span><span class="n">zephyr</span><span class="o">/</span><span class="n">scripts</span><span class="o">/</span><span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div>
</div>
</li>
<li><p>Set up $ZEPHYR_BASE environment..</p>
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
<li><p>Open the Terminal</p></li>
<li><p>Initialize <code class="docutils literal notranslate"><span class="pre">udk-sdk</span></code> workspace for the <code class="docutils literal notranslate"><span class="pre">leaps-udk-examples</span></code> with main revision.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">init</span> <span class="o">-</span><span class="n">m</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">leapslabs</span><span class="o">/</span><span class="n">udk</span><span class="o">-</span><span class="n">sdk</span><span class="o">.</span><span class="n">git</span> <span class="o">--</span><span class="n">mr</span> <span class="n">main</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
</pre></div>
</div>
<div class="admonition caution">
<p class="admonition-title">Caution</p>
<p>The published <code class="docutils literal notranslate"><span class="pre">udk-sdk</span> <span class="pre">repository</span></code> will be provided soon. Please stay tuned!</p>
</div>
</li>
<li><p>Clone the <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> source (version 3.1.0) and its modules.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
<span class="n">west</span> <span class="n">update</span>
</pre></div>
</div>
</li>
<li><p>Export a <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> CMake package. This allows CMake to automatically load boilerplate code required for building Zephyr applications.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">export</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a>’s scripts/requirements.txt file declares additional Python dependencies. Install them with pip.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="o">./</span><span class="n">zephyr</span><span class="o">/</span><span class="n">scripts</span><span class="o">/</span><span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div>
</div>
</li>
<li><p>Set up $ZEPHYR_BASE environment..</p>
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
<li><p>Open a <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> terminal window as a regular user</p></li>
<li><p>Initialize <code class="docutils literal notranslate"><span class="pre">udk-sdk</span></code> workspace for the <code class="docutils literal notranslate"><span class="pre">leaps-udk-examples</span></code> with main revision.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">init</span> <span class="o">-</span><span class="n">m</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">leapslabs</span><span class="o">/</span><span class="n">udk</span><span class="o">-</span><span class="n">sdk</span><span class="o">.</span><span class="n">git</span> <span class="o">--</span><span class="n">mr</span> <span class="n">main</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
</pre></div>
</div>
</li>
<li><p>Clone the <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> source (version 3.1.0) and its modules.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
<span class="n">west</span> <span class="n">update</span>
</pre></div>
</div>
</li>
<li><p>Export a <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> CMake package. This allows CMake to automatically load boilerplate code required for building Zephyr applications.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">export</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a>’s scripts/requirements.txt file declares additional Python dependencies. Install them with pip.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="n">zephyr</span><span class="o">/</span><span class="n">scripts</span><span class="o">/</span><span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div>
</div>
</li>
<li><p>Set up $ZEPHYR_BASE environment..</p>
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
<span id="devicesetup"></span><h2>Device Setup</h2>
<p>Before executing the example application, ensure that the devices are connected and open the Console window by following these steps:</p>
<ol class="arabic">
<li><p>Use a USB-C data cable to connect the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> of devices to host PC.</p>
<img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/_images/leaps-connect-usb-port2.gif">
</li>
<li><p>Install the OpenOCD tool by referring to the OpenOCD tab in the <a class="reference internal" href="/docs/en/udk/development-guide/firmware-reflashing#flashingfirmware"><span class="std std-ref">Programming/Upgrading firmware</span></a> section. This section also includes other solutions for flashing the firmware.</p></li>
<li><p>Execute the following commands to open minicom (on Linux and macOs), or <a class="reference external" href="https://teratermproject.github.io/index-en.html">Tera Term</a> (on Windows) to access the connected serial port and ready to view the printed messages from the examples.</p></li>
</ol>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-21" name="sd-tab-set-8" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-21">
Ubuntu</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>Open the Terminal</p></li>
<li><p>Execute the command below with ttyACM&lt;X&gt; (0 is default port for 1st connected device)</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">minicom -b 115200 -D /dev/ttyACM0</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Please verify all the connected device (ttyACM&lt;X&gt;) that you intend to re-flash by using the following command</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">ls ../../dev/</span>
</pre></div>
</div>
</div></blockquote>
</div>
</li>
<li><p>When successfully connected to device</p>
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
<li><p>Open the Terminal</p></li>
<li><p>Execute the command below with /dev/tty.usb&lt;xxx&gt; (modem1410 is example)</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">minicom -b 115200 -D /dev/tty.usbmodem1410</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Please verify the connected device (tty.usb&lt;xxx&gt;) that you intend to re-flash by using the following command</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">ls ../../dev/</span>
</pre></div>
</div>
</div>
</li>
<li><p>When successfully connected to device</p>
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
<li><p>Open the <a class="reference external" href="https://teratermproject.github.io/index-en.html">Tera Term</a> tool</p></li>
<li><p>Goto Setup &gt; Serial Port</p>
<a class="reference internal image-reference" href="../../../_images/setup.png"><img alt="../../../_images/setup.png" src="/docs-assets/_images/setup.png" style="width: 523.2px; height: 268.0px;"></a>
</li>
<li><p>Select connected port of device (e.g. Port 5 is connecting to device)</p>
<a class="reference internal image-reference" href="../../../_images/port.png"><img alt="../../../_images/port.png" src="/docs-assets/_images/port.png" style="width: 373.6px; height: 359.20000000000005px;"></a>
</li>
<li><p>Select the Speed as 115200</p>
<a class="reference internal image-reference" href="../../../_images/speed.png"><img alt="../../../_images/speed.png" src="/docs-assets/_images/speed.png" style="width: 372.0px; height: 361.6px;"></a>
</li>
<li><p>Select Close and New Open (or New Open)</p></li>
</ol>
</div></blockquote>
</div>
</div>
</div>
<div class="section" id="coordinated-examples-execution">
<h2>Coordinated Examples Execution</h2>
<p>In the UDK-SDK package, at <span class="sd-sphinx-override sd-badge sd-outline-info sd-text-info">@yourdir/udk-sdk/leaps-udk-examples/app/006_ex_uwb</span>
location, various examples are available. Achieving collaborative Ultra-Wideband
operation requires pairing two examples as outlined in the table below.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 51%">
<col style="width: 49%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Example 1</p></th>
<th class="head"><p>Example 2</p></th>
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
<p>For detailed instructions, please refer to the description provided in each example’s source *.c file.</p>
<p><strong>For example:</strong> ex_01h_simple_tx_pdoa/simple_tx_pdoa.c</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">*  @file    simple_tx_pdoa.c</span>
<span class="go">*  @brief   Simple TX PDOA example code, companion to Simple RX PDOA example.</span>
<span class="go">*           See note 7 regarding information on calibrating the system</span>
</pre></div>
</div>
</div>
<hr class="docutils">
<div class="section" id="build-and-run-the-example">
<h2>Build and run the example</h2>
<p>This section guide you on how to build and re-flash the software.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If any issues occur within the <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> environment, please refer to the <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/getting_started/index.html#troubleshooting-installation">Troubleshooting Installation</a> section.</p>
</div>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-24" name="sd-tab-set-9" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-24">
Ubuntu</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>Ensure complete <a class="reference internal" href="#devicesetup"><span class="std std-ref">Device Setup</span></a> guideline.</p></li>
<li><p>Go into the examples directory</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd leaps-udk-examples</span>
</pre></div>
</div>
</li>
<li><p>(Optional) Clean the old build directory</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">rm -rf build/</span>
</pre></div>
</div>
</li>
<li><p>Build the example</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-27" name="sd-tab-set-10" type="radio">
<label class="sd-tab-label" for="sd-tab-item-27">
With Selection Menu</label><div class="sd-tab-content docutils">
<p>This section guides you on how to build the example by selecting one expected example</p>
<ol class="arabic">
<li><p>Execute the below command to show the menu, with $BOARD is leaps_lc14 or leaps_lc13</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -t menuconfig -b $BOARD -s app</span>
</pre></div>
</div>
</li>
<li><p>Select the <strong>Sample Application</strong> and press Enter</p>
<a class="reference internal image-reference" href="../../../_images/main_menu.png"><img alt="../../../_images/main_menu.png" class="align-center" src="/docs-assets/_images/main_menu.png" style="width: 758.5px; height: 396.0px;"></a>
</li>
<li><p>You will see the default <strong>Example</strong>, press enter if you want to select another example</p>
<a class="reference internal image-reference" href="../../../_images/menu_default_example.png"><img alt="../../../_images/menu_default_example.png" class="align-center" src="/docs-assets/_images/menu_default_example.png" style="width: 688.5px; height: 385.5px;"></a>
</li>
<li><p>Select the <strong>Example</strong> by scrolling up or down then press Enter</p>
<a class="reference internal image-reference" href="../../../_images/menu_example_list.png"><img alt="../../../_images/menu_example_list.png" class="align-center" src="/docs-assets/_images/menu_example_list.png" style="width: 688.5px; height: 385.5px;"></a>
</li>
<li><p>Press ESC and Y to save the selection</p>
<a class="reference internal image-reference" href="../../../_images/menu_exit_andsave.png"><img alt="../../../_images/menu_exit_andsave.png" class="align-center" src="/docs-assets/_images/menu_exit_andsave.png" style="width: 688.5px; height: 385.5px;"></a>
</li>
<li><p>Build the example</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build</span>
</pre></div>
</div>
</li>
<li><p>Build the example Successfully</p>
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
Without Selection Menu</label><div class="sd-tab-content docutils">
<p>This section guides you on how to build the example with default example</p>
<ol class="arabic">
<li><p>Execute the below command, with $BOARD is leaps_lc14 or leaps_lc13</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -b $BOARD -s app</span>
</pre></div>
</div>
</li>
<li><p>Build the example Successfully</p>
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
<li><p>And then re-flash the hex file to the device:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west flash</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Successfully, re-flashed Firmware</p>
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
<li><p>Example output when running the TEST_BUTTONS example by pressing the button C, B and A, respectively.</p>
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
<li><p>Ensure complete <a class="reference internal" href="#devicesetup"><span class="std std-ref">Device Setup</span></a> guideline.</p></li>
<li><p>Go into the examples directory</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd leaps-udk-examples</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>(Optional) Clean the old build directory</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">rm -rf build/</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Build the example</p>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-29" name="sd-tab-set-11" type="radio">
<label class="sd-tab-label" for="sd-tab-item-29">
With Selection Menu</label><div class="sd-tab-content docutils">
<p>This section guides you on how to build the example with selecting one expect example</p>
<ol class="arabic">
<li><p>Execute the below command to show the menu, with $BOARD is leaps_lc14 or leaps_lc13</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -t menuconfig -b $BOARD -s app</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Select the <strong>Sample Application</strong> and press Enter</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/main_menu.png"><img alt="../../../_images/main_menu.png" class="align-center" src="/docs-assets/_images/main_menu.png" style="width: 758.5px; height: 396.0px;"></a>
</div></blockquote>
</li>
<li><p>You will see the default <strong>Example</strong>, press enter if you want to select another example</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_default_example.png"><img alt="../../../_images/menu_default_example.png" class="align-center" src="/docs-assets/_images/menu_default_example.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
</li>
<li><p>Select the <strong>Example</strong> by croll up/down then press Enter</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_example_list.png"><img alt="../../../_images/menu_example_list.png" class="align-center" src="/docs-assets/_images/menu_example_list.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
</li>
<li><p>Press ESC and Y to save the selection</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_exit_andsave.png"><img alt="../../../_images/menu_exit_andsave.png" class="align-center" src="/docs-assets/_images/menu_exit_andsave.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
</li>
<li><p>Build the example</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Build the example Successfully</p>
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
Without Selection Menu</label><div class="sd-tab-content docutils">
<p>This section guides you on how to build the example with default example</p>
<ol class="arabic">
<li><p>Execute the below command, with $BOARD is leaps_lc14 or leaps_lc13</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -b $BOARD</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Build the example Successfully</p>
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
<li><p>And then re-flash the hex file to the device:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west flash</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Successfully, re-flashed Firmware</p>
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
<li><p>Example output when running the TEST_BUTTONS example by pressing the button C, B and A, respectively.</p>
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
<li><p>Ensure complete <a class="reference internal" href="#devicesetup"><span class="std std-ref">Device Setup</span></a> guideline.</p></li>
<li><p>Go into the examples directory</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd leaps-udk-examples</span>
</pre></div>
</div>
</li>
<li><p>(Optional) Clean the old build directory and press Y</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">rd /s build</span>
</pre></div>
</div>
</li>
<li><p>Build the example</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-31" name="sd-tab-set-12" type="radio">
<label class="sd-tab-label" for="sd-tab-item-31">
With Selection Menu</label><div class="sd-tab-content docutils">
<p>This section guides you on how to build the example by selecting one expected example</p>
<ol class="arabic simple">
<li><p>Execute the below command to show the menu, with $BOARD is leaps_lc14 or leaps_lc13</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -t menuconfig -b $BOARD -s app</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple">
<li><p>Select the <strong>Sample Application</strong> and press Enter</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/main_menu.png"><img alt="../../../_images/main_menu.png" class="align-center" src="/docs-assets/_images/main_menu.png" style="width: 758.5px; height: 396.0px;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>You will see the default <strong>Example</strong>, press enter if you want to select another example</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_default_example.png"><img alt="../../../_images/menu_default_example.png" class="align-center" src="/docs-assets/_images/menu_default_example.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>Select the <strong>Example</strong> by scrolling up or down then press Enter</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_example_list.png"><img alt="../../../_images/menu_example_list.png" class="align-center" src="/docs-assets/_images/menu_example_list.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>Press ESC and Y to save the selection</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_exit_andsave.png"><img alt="../../../_images/menu_exit_andsave.png" class="align-center" src="/docs-assets/_images/menu_exit_andsave.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>Build the example</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple">
<li><p>Build the example Successfully</p></li>
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
Without Selection Menu</label><div class="sd-tab-content docutils">
<p>This section guides you on how to build the example with default example</p>
<ol class="arabic">
<li><p>Execute the below command, with $BOARD is leaps_lc14 or leaps_lc13</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -b $BOARD -s app</span>
</pre></div>
</div>
</li>
<li><p>Build the example Successfully</p>
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
<li><p>And then re-flash the hex file to the device:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west flash</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Successfully, re-flashed Firmware</p>
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
<li><p>Example output when running the TEST_BUTTONS example by pressing the button C, B and A, respectively.</p>
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
