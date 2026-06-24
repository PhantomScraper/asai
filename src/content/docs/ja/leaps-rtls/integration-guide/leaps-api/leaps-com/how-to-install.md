---
title: "How to install ?"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/leaps-com/how-to-install"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/leaps-com/how-to-install/"
order: 117
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="how-to-install">
<span id="install-leapscom"></span><h1>How to install ?</h1>
<ol class="arabic">
<li><p>Install <a class="reference external" href="https://www.python.org/downloads/">python</a> .</p>
<p>Verify installation: <code class="docutils literal notranslate"><span class="pre">python3</span> <span class="pre">--version</span></code> in the terminal.</p>
</li>
<li><p>Create a virtual environment.</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>venv<span class="w"> </span>.venv
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Activate the environment.</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Linux</label><div class="sd-tab-content docutils">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span><span class="nb">source</span><span class="w"> </span>.venv/bin/activate
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
macOS</label><div class="sd-tab-content docutils">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span><span class="nb">source</span><span class="w"> </span>.venv/bin/activate
</pre></div>
</div>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
Windows</label><div class="sd-tab-content docutils">
<ul>
<li><p>On Command Prompt:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>.venv<span class="se">\S</span>cripts<span class="se">\a</span>ctivate.bat
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>On PowerShell:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>.venv<span class="se">\S</span>cripts<span class="se">\A</span>ctivate.ps1
</pre></div>
</div>
</div></blockquote>
</li>
</ul>
</div>
</div>
</li>
<li><p>Download <a class="reference external" href="/_static/leaps_api/leapscom-1.1.1-py3-none-any.whl">leapscom-1.1.1-py3-none-any.whl</a>.</p>
</li>
</ol>
<ol class="arabic" start="5">
<li><p>Install <code class="docutils literal notranslate"><span class="pre">leapscom</span></code>.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>pip3<span class="w"> </span>install<span class="w"> </span>leapscom-1.1.1-py3-none-any.whl
</pre></div>
</div>
<p>or</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>pip3<span class="w"> </span>install<span class="w"> </span>--no-user<span class="w"> </span>--target<span class="w"> </span>leapscom-1.1.1-py3-none-any.whl
</pre></div>
</div>
<p>Make sure you have the installation folder in your system path!</p>
</li>
</ol>
<ol class="arabic simple" start="5">
<li><p>Verify that the installed tool works.</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--help
</pre></div>
</div>
<ol class="arabic simple" start="6">
<li><p>Optionally, you can uninstall the previously installed tool.</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>pip3<span class="w"> </span>uninstall<span class="w"> </span>leapscom
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>Need to activate the environment every time open a new terminal to work on this tool.</p></li>
</ul>
</div>
</div>


           </div>
