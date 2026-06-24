---
title: "TLV API"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/tlv-api"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/tlv-api/"
order: 114
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="tlv-api">
<span id="leaps-tlv-api"></span><h1>TLV API</h1>
<p>API 経由で通信する TLV API は、以下の形式のシンプルな TLV フレームを使用します。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 27%">
<col style="width: 31%">
<col style="width: 26%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p><strong>TLV フレーム</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
<td><p>チェックサム</p></td>
</tr>
<tr class="row-odd"><td><p>第 1 バイト</p></td>
<td><p>第 2 バイト</p>
<ul class="simple">
<li><p>チェックサムなしのペイロード長</p></li>
</ul>
</td>
<td><p>第 3 バイトから最大ペイロードバイト数</p>
<ul class="simple">
<li><p>SPI の場合最大 252 バイト</p></li>
<li><p>UART の場合最大 255 バイト</p></li>
</ul>
</td>
<td><p>最終バイト</p></td>
</tr>
</tbody>
</table>
<ul>
<li><p>タイプ255は予約済みタイプであり、モジュールはこれを無視します。</p></li>
<li><p>不明なTLVタイプは拒否されます。</p></li>
<li><p>TLV応答は、各TLV要求に確認応答します。</p></li>
<li><p>チェックサムアルゴリズムは、<a class="reference external" href="https://github.com/lammertb/libcrc/blob/master/src/crc8.c">crc8</a> を参照するCRC8です（多項式コンストラクタは x<sup>8</sup> + x<sup>5</sup> + x<sup>4</sup> +1）。これはパッケージ全体のチェックサムの計算に使用されます。TLVの長さにはこのチェックサムは含まれません。</p>
<blockquote>
<div><ul class="simple">
<li><p>コード例：</p></li>
</ul>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
C</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="c1">#include &lt;stdlib.h&gt;</span>
<span class="c1">#include "checksum.h"</span>

<span class="n">static</span> <span class="n">uint8_t</span> <span class="n">crc_table</span><span class="p">[]</span> <span class="o">=</span> <span class="p">{</span>

   <span class="mi">0</span><span class="p">,</span>   <span class="mi">49</span><span class="p">,</span>  <span class="mi">98</span><span class="p">,</span>  <span class="mi">83</span><span class="p">,</span>  <span class="mi">196</span><span class="p">,</span> <span class="mi">245</span><span class="p">,</span> <span class="mi">166</span><span class="p">,</span> <span class="mi">151</span><span class="p">,</span> <span class="mi">185</span><span class="p">,</span> <span class="mi">136</span><span class="p">,</span> <span class="mi">219</span><span class="p">,</span> <span class="mi">234</span><span class="p">,</span> <span class="mi">125</span><span class="p">,</span> <span class="mi">76</span><span class="p">,</span>  <span class="mi">31</span><span class="p">,</span>  <span class="mi">46</span><span class="p">,</span>
   <span class="mi">67</span><span class="p">,</span>  <span class="mi">114</span><span class="p">,</span> <span class="mi">33</span><span class="p">,</span>  <span class="mi">16</span><span class="p">,</span>  <span class="mi">135</span><span class="p">,</span> <span class="mi">182</span><span class="p">,</span> <span class="mi">229</span><span class="p">,</span> <span class="mi">212</span><span class="p">,</span> <span class="mi">250</span><span class="p">,</span> <span class="mi">203</span><span class="p">,</span> <span class="mi">152</span><span class="p">,</span> <span class="mi">169</span><span class="p">,</span> <span class="mi">62</span><span class="p">,</span>  <span class="mi">15</span><span class="p">,</span>  <span class="mi">92</span><span class="p">,</span>  <span class="mi">109</span><span class="p">,</span>
   <span class="mi">134</span><span class="p">,</span> <span class="mi">183</span><span class="p">,</span> <span class="mi">228</span><span class="p">,</span> <span class="mi">213</span><span class="p">,</span> <span class="mi">66</span><span class="p">,</span>  <span class="mi">115</span><span class="p">,</span> <span class="mi">32</span><span class="p">,</span>  <span class="mi">17</span><span class="p">,</span>  <span class="mi">63</span><span class="p">,</span>  <span class="mi">14</span><span class="p">,</span>  <span class="mi">93</span><span class="p">,</span>  <span class="mi">108</span><span class="p">,</span> <span class="mi">251</span><span class="p">,</span> <span class="mi">202</span><span class="p">,</span> <span class="mi">153</span><span class="p">,</span> <span class="mi">168</span><span class="p">,</span>
   <span class="mi">197</span><span class="p">,</span> <span class="mi">244</span><span class="p">,</span> <span class="mi">167</span><span class="p">,</span> <span class="mi">150</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span>   <span class="mi">48</span><span class="p">,</span>  <span class="mi">99</span><span class="p">,</span>  <span class="mi">82</span><span class="p">,</span>  <span class="mi">124</span><span class="p">,</span> <span class="mi">77</span><span class="p">,</span>  <span class="mi">30</span><span class="p">,</span>  <span class="mi">47</span><span class="p">,</span>  <span class="mi">184</span><span class="p">,</span> <span class="mi">137</span><span class="p">,</span> <span class="mi">218</span><span class="p">,</span> <span class="mi">235</span><span class="p">,</span>
   <span class="mi">61</span><span class="p">,</span>  <span class="mi">12</span><span class="p">,</span>  <span class="mi">95</span><span class="p">,</span>  <span class="mi">110</span><span class="p">,</span> <span class="mi">249</span><span class="p">,</span> <span class="mi">200</span><span class="p">,</span> <span class="mi">155</span><span class="p">,</span> <span class="mi">170</span><span class="p">,</span> <span class="mi">132</span><span class="p">,</span> <span class="mi">181</span><span class="p">,</span> <span class="mi">230</span><span class="p">,</span> <span class="mi">215</span><span class="p">,</span> <span class="mi">64</span><span class="p">,</span>  <span class="mi">113</span><span class="p">,</span> <span class="mi">34</span><span class="p">,</span>  <span class="mi">19</span><span class="p">,</span>
   <span class="mi">126</span><span class="p">,</span> <span class="mi">79</span><span class="p">,</span>  <span class="mi">28</span><span class="p">,</span>  <span class="mi">45</span><span class="p">,</span>  <span class="mi">186</span><span class="p">,</span> <span class="mi">139</span><span class="p">,</span> <span class="mi">216</span><span class="p">,</span> <span class="mi">233</span><span class="p">,</span> <span class="mi">199</span><span class="p">,</span> <span class="mi">246</span><span class="p">,</span> <span class="mi">165</span><span class="p">,</span> <span class="mi">148</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span>   <span class="mi">50</span><span class="p">,</span>  <span class="mi">97</span><span class="p">,</span>  <span class="mi">80</span><span class="p">,</span>
   <span class="mi">187</span><span class="p">,</span> <span class="mi">138</span><span class="p">,</span> <span class="mi">217</span><span class="p">,</span> <span class="mi">232</span><span class="p">,</span> <span class="mi">127</span><span class="p">,</span> <span class="mi">78</span><span class="p">,</span>  <span class="mi">29</span><span class="p">,</span>  <span class="mi">44</span><span class="p">,</span>  <span class="mi">2</span><span class="p">,</span>   <span class="mi">51</span><span class="p">,</span>  <span class="mi">96</span><span class="p">,</span>  <span class="mi">81</span><span class="p">,</span>  <span class="mi">198</span><span class="p">,</span> <span class="mi">247</span><span class="p">,</span> <span class="mi">164</span><span class="p">,</span> <span class="mi">149</span><span class="p">,</span>
   <span class="mi">248</span><span class="p">,</span> <span class="mi">201</span><span class="p">,</span> <span class="mi">154</span><span class="p">,</span> <span class="mi">171</span><span class="p">,</span> <span class="mi">60</span><span class="p">,</span>  <span class="mi">13</span><span class="p">,</span>  <span class="mi">94</span><span class="p">,</span>  <span class="mi">111</span><span class="p">,</span> <span class="mi">65</span><span class="p">,</span>  <span class="mi">112</span><span class="p">,</span> <span class="mi">35</span><span class="p">,</span>  <span class="mi">18</span><span class="p">,</span>  <span class="mi">133</span><span class="p">,</span> <span class="mi">180</span><span class="p">,</span> <span class="mi">231</span><span class="p">,</span> <span class="mi">214</span><span class="p">,</span>
   <span class="mi">122</span><span class="p">,</span> <span class="mi">75</span><span class="p">,</span>  <span class="mi">24</span><span class="p">,</span>  <span class="mi">41</span><span class="p">,</span>  <span class="mi">190</span><span class="p">,</span> <span class="mi">143</span><span class="p">,</span> <span class="mi">220</span><span class="p">,</span> <span class="mi">237</span><span class="p">,</span> <span class="mi">195</span><span class="p">,</span> <span class="mi">242</span><span class="p">,</span> <span class="mi">161</span><span class="p">,</span> <span class="mi">144</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span>   <span class="mi">54</span><span class="p">,</span>  <span class="mi">101</span><span class="p">,</span> <span class="mi">84</span><span class="p">,</span>
   <span class="mi">57</span><span class="p">,</span>  <span class="mi">8</span><span class="p">,</span>   <span class="mi">91</span><span class="p">,</span>  <span class="mi">106</span><span class="p">,</span> <span class="mi">253</span><span class="p">,</span> <span class="mi">204</span><span class="p">,</span> <span class="mi">159</span><span class="p">,</span> <span class="mi">174</span><span class="p">,</span> <span class="mi">128</span><span class="p">,</span> <span class="mi">177</span><span class="p">,</span> <span class="mi">226</span><span class="p">,</span> <span class="mi">211</span><span class="p">,</span> <span class="mi">68</span><span class="p">,</span>  <span class="mi">117</span><span class="p">,</span> <span class="mi">38</span><span class="p">,</span>  <span class="mi">23</span><span class="p">,</span>
   <span class="mi">252</span><span class="p">,</span> <span class="mi">205</span><span class="p">,</span> <span class="mi">158</span><span class="p">,</span> <span class="mi">175</span><span class="p">,</span> <span class="mi">56</span><span class="p">,</span>  <span class="mi">9</span><span class="p">,</span>   <span class="mi">90</span><span class="p">,</span>  <span class="mi">107</span><span class="p">,</span> <span class="mi">69</span><span class="p">,</span>  <span class="mi">116</span><span class="p">,</span> <span class="mi">39</span><span class="p">,</span>  <span class="mi">22</span><span class="p">,</span>  <span class="mi">129</span><span class="p">,</span> <span class="mi">176</span><span class="p">,</span> <span class="mi">227</span><span class="p">,</span> <span class="mi">210</span><span class="p">,</span>
   <span class="mi">191</span><span class="p">,</span> <span class="mi">142</span><span class="p">,</span> <span class="mi">221</span><span class="p">,</span> <span class="mi">236</span><span class="p">,</span> <span class="mi">123</span><span class="p">,</span> <span class="mi">74</span><span class="p">,</span>  <span class="mi">25</span><span class="p">,</span>  <span class="mi">40</span><span class="p">,</span>  <span class="mi">6</span><span class="p">,</span>   <span class="mi">55</span><span class="p">,</span>  <span class="mi">100</span><span class="p">,</span> <span class="mi">85</span><span class="p">,</span>  <span class="mi">194</span><span class="p">,</span> <span class="mi">243</span><span class="p">,</span> <span class="mi">160</span><span class="p">,</span> <span class="mi">145</span><span class="p">,</span>
   <span class="mi">71</span><span class="p">,</span>  <span class="mi">118</span><span class="p">,</span> <span class="mi">37</span><span class="p">,</span>  <span class="mi">20</span><span class="p">,</span>  <span class="mi">131</span><span class="p">,</span> <span class="mi">178</span><span class="p">,</span> <span class="mi">225</span><span class="p">,</span> <span class="mi">208</span><span class="p">,</span> <span class="mi">254</span><span class="p">,</span> <span class="mi">207</span><span class="p">,</span> <span class="mi">156</span><span class="p">,</span> <span class="mi">173</span><span class="p">,</span> <span class="mi">58</span><span class="p">,</span>  <span class="mi">11</span><span class="p">,</span>  <span class="mi">88</span><span class="p">,</span>  <span class="mi">105</span><span class="p">,</span>
   <span class="mi">4</span><span class="p">,</span>   <span class="mi">53</span><span class="p">,</span>  <span class="mi">102</span><span class="p">,</span> <span class="mi">87</span><span class="p">,</span>  <span class="mi">192</span><span class="p">,</span> <span class="mi">241</span><span class="p">,</span> <span class="mi">162</span><span class="p">,</span> <span class="mi">147</span><span class="p">,</span> <span class="mi">189</span><span class="p">,</span> <span class="mi">140</span><span class="p">,</span> <span class="mi">223</span><span class="p">,</span> <span class="mi">238</span><span class="p">,</span> <span class="mi">121</span><span class="p">,</span> <span class="mi">72</span><span class="p">,</span>  <span class="mi">27</span><span class="p">,</span>  <span class="mi">42</span><span class="p">,</span>
   <span class="mi">193</span><span class="p">,</span> <span class="mi">240</span><span class="p">,</span> <span class="mi">163</span><span class="p">,</span> <span class="mi">146</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span>   <span class="mi">52</span><span class="p">,</span>  <span class="mi">103</span><span class="p">,</span> <span class="mi">86</span><span class="p">,</span>  <span class="mi">120</span><span class="p">,</span> <span class="mi">73</span><span class="p">,</span>  <span class="mi">26</span><span class="p">,</span>  <span class="mi">43</span><span class="p">,</span>  <span class="mi">188</span><span class="p">,</span> <span class="mi">141</span><span class="p">,</span> <span class="mi">222</span><span class="p">,</span> <span class="mi">239</span><span class="p">,</span>
   <span class="mi">130</span><span class="p">,</span> <span class="mi">179</span><span class="p">,</span> <span class="mi">224</span><span class="p">,</span> <span class="mi">209</span><span class="p">,</span> <span class="mi">70</span><span class="p">,</span>  <span class="mi">119</span><span class="p">,</span> <span class="mi">36</span><span class="p">,</span>  <span class="mi">21</span><span class="p">,</span>  <span class="mi">59</span><span class="p">,</span>  <span class="mi">10</span><span class="p">,</span>  <span class="mi">89</span><span class="p">,</span>  <span class="mi">104</span><span class="p">,</span> <span class="mi">255</span><span class="p">,</span> <span class="mi">206</span><span class="p">,</span> <span class="mi">157</span><span class="p">,</span> <span class="mi">172</span>
<span class="p">};</span>

<span class="o">/*</span>
<span class="o">*</span> <span class="n">The</span> <span class="n">function</span> <span class="n">crc_8</span><span class="p">()</span> <span class="n">calculates</span> <span class="n">the</span> <span class="mi">8</span> <span class="n">bit</span> <span class="n">wide</span> <span class="n">CRC</span> <span class="n">of</span> <span class="n">an</span> <span class="nb">input</span> <span class="n">string</span> <span class="n">of</span> <span class="n">a</span>
<span class="o">*</span> <span class="n">given</span> <span class="n">length</span><span class="o">.</span>
<span class="o">*/</span>

<span class="n">uint8_t</span> <span class="n">crc_8</span><span class="p">(</span> <span class="n">const</span> <span class="n">unsigned</span> <span class="n">char</span> <span class="o">*</span><span class="n">input_str</span><span class="p">,</span> <span class="n">size_t</span> <span class="n">num_bytes</span> <span class="p">)</span> <span class="p">{</span>

   <span class="n">size_t</span> <span class="n">a</span><span class="p">;</span>
   <span class="n">uint8_t</span> <span class="n">crc</span><span class="p">;</span>
   <span class="n">const</span> <span class="n">unsigned</span> <span class="n">char</span> <span class="o">*</span><span class="n">ptr</span><span class="p">;</span>

   <span class="n">crc</span> <span class="o">=</span> <span class="n">CRC_START_8</span><span class="p">;</span>
   <span class="n">ptr</span> <span class="o">=</span> <span class="n">input_str</span><span class="p">;</span>

   <span class="k">if</span> <span class="p">(</span> <span class="n">ptr</span> <span class="o">!=</span> <span class="n">NULL</span> <span class="p">)</span> <span class="k">for</span> <span class="p">(</span><span class="n">a</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span> <span class="n">a</span><span class="o">&lt;</span><span class="n">num_bytes</span><span class="p">;</span> <span class="n">a</span><span class="o">++</span><span class="p">)</span> <span class="p">{</span>

      <span class="n">crc</span> <span class="o">=</span> <span class="n">crc_table</span><span class="p">[(</span><span class="o">*</span><span class="n">ptr</span><span class="o">++</span><span class="p">)</span> <span class="o">^</span> <span class="n">crc</span><span class="p">];</span>
   <span class="p">}</span>

   <span class="k">return</span> <span class="n">crc</span><span class="p">;</span>

<span class="p">}</span>

<span class="n">void</span> <span class="n">main</span><span class="p">(</span><span class="n">void</span><span class="p">)</span> <span class="p">{</span>
   <span class="n">uint8_t</span> <span class="n">data</span><span class="p">[]</span> <span class="o">=</span> <span class="p">{</span><span class="mh">0x01</span><span class="p">,</span> <span class="mh">0x02</span><span class="p">,</span> <span class="mh">0x03</span><span class="p">,</span> <span class="mh">0x04</span><span class="p">,</span> <span class="mh">0x05</span><span class="p">};</span>
   <span class="n">uint8_t</span> <span class="n">crc</span><span class="p">;</span>

   <span class="n">crc</span> <span class="o">=</span> <span class="n">crc_8</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">sizeof</span><span class="p">(</span><span class="n">data</span><span class="p">));</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Python</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">crc_table</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">([</span>
   <span class="mi">0</span><span class="p">,</span>   <span class="mi">49</span><span class="p">,</span>  <span class="mi">98</span><span class="p">,</span>  <span class="mi">83</span><span class="p">,</span>  <span class="mi">196</span><span class="p">,</span> <span class="mi">245</span><span class="p">,</span> <span class="mi">166</span><span class="p">,</span> <span class="mi">151</span><span class="p">,</span> <span class="mi">185</span><span class="p">,</span> <span class="mi">136</span><span class="p">,</span> <span class="mi">219</span><span class="p">,</span> <span class="mi">234</span><span class="p">,</span> <span class="mi">125</span><span class="p">,</span> <span class="mi">76</span><span class="p">,</span>  <span class="mi">31</span><span class="p">,</span>  <span class="mi">46</span><span class="p">,</span>
   <span class="mi">67</span><span class="p">,</span>  <span class="mi">114</span><span class="p">,</span> <span class="mi">33</span><span class="p">,</span>  <span class="mi">16</span><span class="p">,</span>  <span class="mi">135</span><span class="p">,</span> <span class="mi">182</span><span class="p">,</span> <span class="mi">229</span><span class="p">,</span> <span class="mi">212</span><span class="p">,</span> <span class="mi">250</span><span class="p">,</span> <span class="mi">203</span><span class="p">,</span> <span class="mi">152</span><span class="p">,</span> <span class="mi">169</span><span class="p">,</span> <span class="mi">62</span><span class="p">,</span>  <span class="mi">15</span><span class="p">,</span>  <span class="mi">92</span><span class="p">,</span>  <span class="mi">109</span><span class="p">,</span>
   <span class="mi">134</span><span class="p">,</span> <span class="mi">183</span><span class="p">,</span> <span class="mi">228</span><span class="p">,</span> <span class="mi">213</span><span class="p">,</span> <span class="mi">66</span><span class="p">,</span>  <span class="mi">115</span><span class="p">,</span> <span class="mi">32</span><span class="p">,</span>  <span class="mi">17</span><span class="p">,</span>  <span class="mi">63</span><span class="p">,</span>  <span class="mi">14</span><span class="p">,</span>  <span class="mi">93</span><span class="p">,</span>  <span class="mi">108</span><span class="p">,</span> <span class="mi">251</span><span class="p">,</span> <span class="mi">202</span><span class="p">,</span> <span class="mi">153</span><span class="p">,</span> <span class="mi">168</span><span class="p">,</span>
   <span class="mi">197</span><span class="p">,</span> <span class="mi">244</span><span class="p">,</span> <span class="mi">167</span><span class="p">,</span> <span class="mi">150</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span>   <span class="mi">48</span><span class="p">,</span>  <span class="mi">99</span><span class="p">,</span>  <span class="mi">82</span><span class="p">,</span>  <span class="mi">124</span><span class="p">,</span> <span class="mi">77</span><span class="p">,</span>  <span class="mi">30</span><span class="p">,</span>  <span class="mi">47</span><span class="p">,</span>  <span class="mi">184</span><span class="p">,</span> <span class="mi">137</span><span class="p">,</span> <span class="mi">218</span><span class="p">,</span> <span class="mi">235</span><span class="p">,</span>
   <span class="mi">61</span><span class="p">,</span>  <span class="mi">12</span><span class="p">,</span>  <span class="mi">95</span><span class="p">,</span>  <span class="mi">110</span><span class="p">,</span> <span class="mi">249</span><span class="p">,</span> <span class="mi">200</span><span class="p">,</span> <span class="mi">155</span><span class="p">,</span> <span class="mi">170</span><span class="p">,</span> <span class="mi">132</span><span class="p">,</span> <span class="mi">181</span><span class="p">,</span> <span class="mi">230</span><span class="p">,</span> <span class="mi">215</span><span class="p">,</span> <span class="mi">64</span><span class="p">,</span>  <span class="mi">113</span><span class="p">,</span> <span class="mi">34</span><span class="p">,</span>  <span class="mi">19</span><span class="p">,</span>
   <span class="mi">126</span><span class="p">,</span> <span class="mi">79</span><span class="p">,</span>  <span class="mi">28</span><span class="p">,</span>  <span class="mi">45</span><span class="p">,</span>  <span class="mi">186</span><span class="p">,</span> <span class="mi">139</span><span class="p">,</span> <span class="mi">216</span><span class="p">,</span> <span class="mi">233</span><span class="p">,</span> <span class="mi">199</span><span class="p">,</span> <span class="mi">246</span><span class="p">,</span> <span class="mi">165</span><span class="p">,</span> <span class="mi">148</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span>   <span class="mi">50</span><span class="p">,</span>  <span class="mi">97</span><span class="p">,</span>  <span class="mi">80</span><span class="p">,</span>
   <span class="mi">187</span><span class="p">,</span> <span class="mi">138</span><span class="p">,</span> <span class="mi">217</span><span class="p">,</span> <span class="mi">232</span><span class="p">,</span> <span class="mi">127</span><span class="p">,</span> <span class="mi">78</span><span class="p">,</span>  <span class="mi">29</span><span class="p">,</span>  <span class="mi">44</span><span class="p">,</span>  <span class="mi">2</span><span class="p">,</span>   <span class="mi">51</span><span class="p">,</span>  <span class="mi">96</span><span class="p">,</span>  <span class="mi">81</span><span class="p">,</span>  <span class="mi">198</span><span class="p">,</span> <span class="mi">247</span><span class="p">,</span> <span class="mi">164</span><span class="p">,</span> <span class="mi">149</span><span class="p">,</span>
   <span class="mi">248</span><span class="p">,</span> <span class="mi">201</span><span class="p">,</span> <span class="mi">154</span><span class="p">,</span> <span class="mi">171</span><span class="p">,</span> <span class="mi">60</span><span class="p">,</span>  <span class="mi">13</span><span class="p">,</span>  <span class="mi">94</span><span class="p">,</span>  <span class="mi">111</span><span class="p">,</span> <span class="mi">65</span><span class="p">,</span>  <span class="mi">112</span><span class="p">,</span> <span class="mi">35</span><span class="p">,</span>  <span class="mi">18</span><span class="p">,</span>  <span class="mi">133</span><span class="p">,</span> <span class="mi">180</span><span class="p">,</span> <span class="mi">231</span><span class="p">,</span> <span class="mi">214</span><span class="p">,</span>
   <span class="mi">122</span><span class="p">,</span> <span class="mi">75</span><span class="p">,</span>  <span class="mi">24</span><span class="p">,</span>  <span class="mi">41</span><span class="p">,</span>  <span class="mi">190</span><span class="p">,</span> <span class="mi">143</span><span class="p">,</span> <span class="mi">220</span><span class="p">,</span> <span class="mi">237</span><span class="p">,</span> <span class="mi">195</span><span class="p">,</span> <span class="mi">242</span><span class="p">,</span> <span class="mi">161</span><span class="p">,</span> <span class="mi">144</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span>   <span class="mi">54</span><span class="p">,</span>  <span class="mi">101</span><span class="p">,</span> <span class="mi">84</span><span class="p">,</span>
   <span class="mi">57</span><span class="p">,</span>  <span class="mi">8</span><span class="p">,</span>   <span class="mi">91</span><span class="p">,</span>  <span class="mi">106</span><span class="p">,</span> <span class="mi">253</span><span class="p">,</span> <span class="mi">204</span><span class="p">,</span> <span class="mi">159</span><span class="p">,</span> <span class="mi">174</span><span class="p">,</span> <span class="mi">128</span><span class="p">,</span> <span class="mi">177</span><span class="p">,</span> <span class="mi">226</span><span class="p">,</span> <span class="mi">211</span><span class="p">,</span> <span class="mi">68</span><span class="p">,</span>  <span class="mi">117</span><span class="p">,</span> <span class="mi">38</span><span class="p">,</span>  <span class="mi">23</span><span class="p">,</span>
   <span class="mi">252</span><span class="p">,</span> <span class="mi">205</span><span class="p">,</span> <span class="mi">158</span><span class="p">,</span> <span class="mi">175</span><span class="p">,</span> <span class="mi">56</span><span class="p">,</span>  <span class="mi">9</span><span class="p">,</span>   <span class="mi">90</span><span class="p">,</span>  <span class="mi">107</span><span class="p">,</span> <span class="mi">69</span><span class="p">,</span>  <span class="mi">116</span><span class="p">,</span> <span class="mi">39</span><span class="p">,</span>  <span class="mi">22</span><span class="p">,</span>  <span class="mi">129</span><span class="p">,</span> <span class="mi">176</span><span class="p">,</span> <span class="mi">227</span><span class="p">,</span> <span class="mi">210</span><span class="p">,</span>
   <span class="mi">191</span><span class="p">,</span> <span class="mi">142</span><span class="p">,</span> <span class="mi">221</span><span class="p">,</span> <span class="mi">236</span><span class="p">,</span> <span class="mi">123</span><span class="p">,</span> <span class="mi">74</span><span class="p">,</span>  <span class="mi">25</span><span class="p">,</span>  <span class="mi">40</span><span class="p">,</span>  <span class="mi">6</span><span class="p">,</span>   <span class="mi">55</span><span class="p">,</span>  <span class="mi">100</span><span class="p">,</span> <span class="mi">85</span><span class="p">,</span>  <span class="mi">194</span><span class="p">,</span> <span class="mi">243</span><span class="p">,</span> <span class="mi">160</span><span class="p">,</span> <span class="mi">145</span><span class="p">,</span>
   <span class="mi">71</span><span class="p">,</span>  <span class="mi">118</span><span class="p">,</span> <span class="mi">37</span><span class="p">,</span>  <span class="mi">20</span><span class="p">,</span>  <span class="mi">131</span><span class="p">,</span> <span class="mi">178</span><span class="p">,</span> <span class="mi">225</span><span class="p">,</span> <span class="mi">208</span><span class="p">,</span> <span class="mi">254</span><span class="p">,</span> <span class="mi">207</span><span class="p">,</span> <span class="mi">156</span><span class="p">,</span> <span class="mi">173</span><span class="p">,</span> <span class="mi">58</span><span class="p">,</span>  <span class="mi">11</span><span class="p">,</span>  <span class="mi">88</span><span class="p">,</span>  <span class="mi">105</span><span class="p">,</span>
   <span class="mi">4</span><span class="p">,</span>   <span class="mi">53</span><span class="p">,</span>  <span class="mi">102</span><span class="p">,</span> <span class="mi">87</span><span class="p">,</span>  <span class="mi">192</span><span class="p">,</span> <span class="mi">241</span><span class="p">,</span> <span class="mi">162</span><span class="p">,</span> <span class="mi">147</span><span class="p">,</span> <span class="mi">189</span><span class="p">,</span> <span class="mi">140</span><span class="p">,</span> <span class="mi">223</span><span class="p">,</span> <span class="mi">238</span><span class="p">,</span> <span class="mi">121</span><span class="p">,</span> <span class="mi">72</span><span class="p">,</span>  <span class="mi">27</span><span class="p">,</span>  <span class="mi">42</span><span class="p">,</span>
   <span class="mi">193</span><span class="p">,</span> <span class="mi">240</span><span class="p">,</span> <span class="mi">163</span><span class="p">,</span> <span class="mi">146</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span>   <span class="mi">52</span><span class="p">,</span>  <span class="mi">103</span><span class="p">,</span> <span class="mi">86</span><span class="p">,</span>  <span class="mi">120</span><span class="p">,</span> <span class="mi">73</span><span class="p">,</span>  <span class="mi">26</span><span class="p">,</span>  <span class="mi">43</span><span class="p">,</span>  <span class="mi">188</span><span class="p">,</span> <span class="mi">141</span><span class="p">,</span> <span class="mi">222</span><span class="p">,</span> <span class="mi">239</span><span class="p">,</span>
   <span class="mi">130</span><span class="p">,</span> <span class="mi">179</span><span class="p">,</span> <span class="mi">224</span><span class="p">,</span> <span class="mi">209</span><span class="p">,</span> <span class="mi">70</span><span class="p">,</span>  <span class="mi">119</span><span class="p">,</span> <span class="mi">36</span><span class="p">,</span>  <span class="mi">21</span><span class="p">,</span>  <span class="mi">59</span><span class="p">,</span>  <span class="mi">10</span><span class="p">,</span>  <span class="mi">89</span><span class="p">,</span>  <span class="mi">104</span><span class="p">,</span> <span class="mi">255</span><span class="p">,</span> <span class="mi">206</span><span class="p">,</span> <span class="mi">157</span><span class="p">,</span> <span class="mi">172</span>
<span class="p">])</span>

<span class="k">def</span> <span class="nf">crc_8</span><span class="p">(</span><span class="n">input_str</span><span class="p">):</span>
   <span class="n">crc</span> <span class="o">=</span> <span class="mi">0</span>

   <span class="k">for</span> <span class="n">data</span> <span class="ow">in</span> <span class="n">input_str</span><span class="p">:</span>
      <span class="n">crc</span> <span class="o">=</span> <span class="n">crc_table</span><span class="p">[</span><span class="n">data</span> <span class="o">^</span> <span class="n">crc</span><span class="p">]</span>

   <span class="k">return</span> <span class="n">crc</span>

<span class="n">data</span> <span class="o">=</span> <span class="p">[]</span>

<span class="n">data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mh">0x85</span><span class="p">)</span>
<span class="n">data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mh">0x04</span><span class="p">)</span>
<span class="n">data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mh">0x07</span><span class="p">)</span>
<span class="n">data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mh">0x00</span><span class="p">)</span>
<span class="n">data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mh">0x05</span><span class="p">)</span>
<span class="n">data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mh">0xff</span><span class="p">)</span>

<span class="nb">print</span> <span class="p">(</span><span class="nb">hex</span><span class="p">(</span><span class="n">crc_8</span><span class="p">(</span><span class="n">data</span><span class="p">)))</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
C#</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">byte</span><span class="p">[]</span> <span class="n">crc_table</span> <span class="o">=</span> <span class="n">new</span> <span class="n">byte</span><span class="p">[]</span> <span class="p">{</span>
   <span class="mi">0</span><span class="p">,</span>   <span class="mi">49</span><span class="p">,</span>  <span class="mi">98</span><span class="p">,</span>  <span class="mi">83</span><span class="p">,</span>  <span class="mi">196</span><span class="p">,</span> <span class="mi">245</span><span class="p">,</span> <span class="mi">166</span><span class="p">,</span> <span class="mi">151</span><span class="p">,</span> <span class="mi">185</span><span class="p">,</span> <span class="mi">136</span><span class="p">,</span> <span class="mi">219</span><span class="p">,</span> <span class="mi">234</span><span class="p">,</span> <span class="mi">125</span><span class="p">,</span> <span class="mi">76</span><span class="p">,</span>  <span class="mi">31</span><span class="p">,</span>  <span class="mi">46</span><span class="p">,</span>
   <span class="mi">67</span><span class="p">,</span>  <span class="mi">114</span><span class="p">,</span> <span class="mi">33</span><span class="p">,</span>  <span class="mi">16</span><span class="p">,</span>  <span class="mi">135</span><span class="p">,</span> <span class="mi">182</span><span class="p">,</span> <span class="mi">229</span><span class="p">,</span> <span class="mi">212</span><span class="p">,</span> <span class="mi">250</span><span class="p">,</span> <span class="mi">203</span><span class="p">,</span> <span class="mi">152</span><span class="p">,</span> <span class="mi">169</span><span class="p">,</span> <span class="mi">62</span><span class="p">,</span>  <span class="mi">15</span><span class="p">,</span>  <span class="mi">92</span><span class="p">,</span>  <span class="mi">109</span><span class="p">,</span>
   <span class="mi">134</span><span class="p">,</span> <span class="mi">183</span><span class="p">,</span> <span class="mi">228</span><span class="p">,</span> <span class="mi">213</span><span class="p">,</span> <span class="mi">66</span><span class="p">,</span>  <span class="mi">115</span><span class="p">,</span> <span class="mi">32</span><span class="p">,</span>  <span class="mi">17</span><span class="p">,</span>  <span class="mi">63</span><span class="p">,</span>  <span class="mi">14</span><span class="p">,</span>  <span class="mi">93</span><span class="p">,</span>  <span class="mi">108</span><span class="p">,</span> <span class="mi">251</span><span class="p">,</span> <span class="mi">202</span><span class="p">,</span> <span class="mi">153</span><span class="p">,</span> <span class="mi">168</span><span class="p">,</span>
   <span class="mi">197</span><span class="p">,</span> <span class="mi">244</span><span class="p">,</span> <span class="mi">167</span><span class="p">,</span> <span class="mi">150</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span>   <span class="mi">48</span><span class="p">,</span>  <span class="mi">99</span><span class="p">,</span>  <span class="mi">82</span><span class="p">,</span>  <span class="mi">124</span><span class="p">,</span> <span class="mi">77</span><span class="p">,</span>  <span class="mi">30</span><span class="p">,</span>  <span class="mi">47</span><span class="p">,</span>  <span class="mi">184</span><span class="p">,</span> <span class="mi">137</span><span class="p">,</span> <span class="mi">218</span><span class="p">,</span> <span class="mi">235</span><span class="p">,</span>
   <span class="mi">61</span><span class="p">,</span>  <span class="mi">12</span><span class="p">,</span>  <span class="mi">95</span><span class="p">,</span>  <span class="mi">110</span><span class="p">,</span> <span class="mi">249</span><span class="p">,</span> <span class="mi">200</span><span class="p">,</span> <span class="mi">155</span><span class="p">,</span> <span class="mi">170</span><span class="p">,</span> <span class="mi">132</span><span class="p">,</span> <span class="mi">181</span><span class="p">,</span> <span class="mi">230</span><span class="p">,</span> <span class="mi">215</span><span class="p">,</span> <span class="mi">64</span><span class="p">,</span>  <span class="mi">113</span><span class="p">,</span> <span class="mi">34</span><span class="p">,</span>  <span class="mi">19</span><span class="p">,</span>
   <span class="mi">126</span><span class="p">,</span> <span class="mi">79</span><span class="p">,</span>  <span class="mi">28</span><span class="p">,</span>  <span class="mi">45</span><span class="p">,</span>  <span class="mi">186</span><span class="p">,</span> <span class="mi">139</span><span class="p">,</span> <span class="mi">216</span><span class="p">,</span> <span class="mi">233</span><span class="p">,</span> <span class="mi">199</span><span class="p">,</span> <span class="mi">246</span><span class="p">,</span> <span class="mi">165</span><span class="p">,</span> <span class="mi">148</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span>   <span class="mi">50</span><span class="p">,</span>  <span class="mi">97</span><span class="p">,</span>  <span class="mi">80</span><span class="p">,</span>
   <span class="mi">187</span><span class="p">,</span> <span class="mi">138</span><span class="p">,</span> <span class="mi">217</span><span class="p">,</span> <span class="mi">232</span><span class="p">,</span> <span class="mi">127</span><span class="p">,</span> <span class="mi">78</span><span class="p">,</span>  <span class="mi">29</span><span class="p">,</span>  <span class="mi">44</span><span class="p">,</span>  <span class="mi">2</span><span class="p">,</span>   <span class="mi">51</span><span class="p">,</span>  <span class="mi">96</span><span class="p">,</span>  <span class="mi">81</span><span class="p">,</span>  <span class="mi">198</span><span class="p">,</span> <span class="mi">247</span><span class="p">,</span> <span class="mi">164</span><span class="p">,</span> <span class="mi">149</span><span class="p">,</span>
   <span class="mi">248</span><span class="p">,</span> <span class="mi">201</span><span class="p">,</span> <span class="mi">154</span><span class="p">,</span> <span class="mi">171</span><span class="p">,</span> <span class="mi">60</span><span class="p">,</span>  <span class="mi">13</span><span class="p">,</span>  <span class="mi">94</span><span class="p">,</span>  <span class="mi">111</span><span class="p">,</span> <span class="mi">65</span><span class="p">,</span>  <span class="mi">112</span><span class="p">,</span> <span class="mi">35</span><span class="p">,</span>  <span class="mi">18</span><span class="p">,</span>  <span class="mi">133</span><span class="p">,</span> <span class="mi">180</span><span class="p">,</span> <span class="mi">231</span><span class="p">,</span> <span class="mi">214</span><span class="p">,</span>
   <span class="mi">122</span><span class="p">,</span> <span class="mi">75</span><span class="p">,</span>  <span class="mi">24</span><span class="p">,</span>  <span class="mi">41</span><span class="p">,</span>  <span class="mi">190</span><span class="p">,</span> <span class="mi">143</span><span class="p">,</span> <span class="mi">220</span><span class="p">,</span> <span class="mi">237</span><span class="p">,</span> <span class="mi">195</span><span class="p">,</span> <span class="mi">242</span><span class="p">,</span> <span class="mi">161</span><span class="p">,</span> <span class="mi">144</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span>   <span class="mi">54</span><span class="p">,</span>  <span class="mi">101</span><span class="p">,</span> <span class="mi">84</span><span class="p">,</span>
   <span class="mi">57</span><span class="p">,</span>  <span class="mi">8</span><span class="p">,</span>   <span class="mi">91</span><span class="p">,</span>  <span class="mi">106</span><span class="p">,</span> <span class="mi">253</span><span class="p">,</span> <span class="mi">204</span><span class="p">,</span> <span class="mi">159</span><span class="p">,</span> <span class="mi">174</span><span class="p">,</span> <span class="mi">128</span><span class="p">,</span> <span class="mi">177</span><span class="p">,</span> <span class="mi">226</span><span class="p">,</span> <span class="mi">211</span><span class="p">,</span> <span class="mi">68</span><span class="p">,</span>  <span class="mi">117</span><span class="p">,</span> <span class="mi">38</span><span class="p">,</span>  <span class="mi">23</span><span class="p">,</span>
   <span class="mi">252</span><span class="p">,</span> <span class="mi">205</span><span class="p">,</span> <span class="mi">158</span><span class="p">,</span> <span class="mi">175</span><span class="p">,</span> <span class="mi">56</span><span class="p">,</span>  <span class="mi">9</span><span class="p">,</span>   <span class="mi">90</span><span class="p">,</span>  <span class="mi">107</span><span class="p">,</span> <span class="mi">69</span><span class="p">,</span>  <span class="mi">116</span><span class="p">,</span> <span class="mi">39</span><span class="p">,</span>  <span class="mi">22</span><span class="p">,</span>  <span class="mi">129</span><span class="p">,</span> <span class="mi">176</span><span class="p">,</span> <span class="mi">227</span><span class="p">,</span> <span class="mi">210</span><span class="p">,</span>
   <span class="mi">191</span><span class="p">,</span> <span class="mi">142</span><span class="p">,</span> <span class="mi">221</span><span class="p">,</span> <span class="mi">236</span><span class="p">,</span> <span class="mi">123</span><span class="p">,</span> <span class="mi">74</span><span class="p">,</span>  <span class="mi">25</span><span class="p">,</span>  <span class="mi">40</span><span class="p">,</span>  <span class="mi">6</span><span class="p">,</span>   <span class="mi">55</span><span class="p">,</span>  <span class="mi">100</span><span class="p">,</span> <span class="mi">85</span><span class="p">,</span>  <span class="mi">194</span><span class="p">,</span> <span class="mi">243</span><span class="p">,</span> <span class="mi">160</span><span class="p">,</span> <span class="mi">145</span><span class="p">,</span>
   <span class="mi">71</span><span class="p">,</span>  <span class="mi">118</span><span class="p">,</span> <span class="mi">37</span><span class="p">,</span>  <span class="mi">20</span><span class="p">,</span>  <span class="mi">131</span><span class="p">,</span> <span class="mi">178</span><span class="p">,</span> <span class="mi">225</span><span class="p">,</span> <span class="mi">208</span><span class="p">,</span> <span class="mi">254</span><span class="p">,</span> <span class="mi">207</span><span class="p">,</span> <span class="mi">156</span><span class="p">,</span> <span class="mi">173</span><span class="p">,</span> <span class="mi">58</span><span class="p">,</span>  <span class="mi">11</span><span class="p">,</span>  <span class="mi">88</span><span class="p">,</span>  <span class="mi">105</span><span class="p">,</span>
   <span class="mi">4</span><span class="p">,</span>   <span class="mi">53</span><span class="p">,</span>  <span class="mi">102</span><span class="p">,</span> <span class="mi">87</span><span class="p">,</span>  <span class="mi">192</span><span class="p">,</span> <span class="mi">241</span><span class="p">,</span> <span class="mi">162</span><span class="p">,</span> <span class="mi">147</span><span class="p">,</span> <span class="mi">189</span><span class="p">,</span> <span class="mi">140</span><span class="p">,</span> <span class="mi">223</span><span class="p">,</span> <span class="mi">238</span><span class="p">,</span> <span class="mi">121</span><span class="p">,</span> <span class="mi">72</span><span class="p">,</span>  <span class="mi">27</span><span class="p">,</span>  <span class="mi">42</span><span class="p">,</span>
   <span class="mi">193</span><span class="p">,</span> <span class="mi">240</span><span class="p">,</span> <span class="mi">163</span><span class="p">,</span> <span class="mi">146</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span>   <span class="mi">52</span><span class="p">,</span>  <span class="mi">103</span><span class="p">,</span> <span class="mi">86</span><span class="p">,</span>  <span class="mi">120</span><span class="p">,</span> <span class="mi">73</span><span class="p">,</span>  <span class="mi">26</span><span class="p">,</span>  <span class="mi">43</span><span class="p">,</span>  <span class="mi">188</span><span class="p">,</span> <span class="mi">141</span><span class="p">,</span> <span class="mi">222</span><span class="p">,</span> <span class="mi">239</span><span class="p">,</span>
   <span class="mi">130</span><span class="p">,</span> <span class="mi">179</span><span class="p">,</span> <span class="mi">224</span><span class="p">,</span> <span class="mi">209</span><span class="p">,</span> <span class="mi">70</span><span class="p">,</span>  <span class="mi">119</span><span class="p">,</span> <span class="mi">36</span><span class="p">,</span>  <span class="mi">21</span><span class="p">,</span>  <span class="mi">59</span><span class="p">,</span>  <span class="mi">10</span><span class="p">,</span>  <span class="mi">89</span><span class="p">,</span>  <span class="mi">104</span><span class="p">,</span> <span class="mi">255</span><span class="p">,</span> <span class="mi">206</span><span class="p">,</span> <span class="mi">157</span><span class="p">,</span> <span class="mi">172</span>
<span class="p">};</span>

<span class="n">public</span> <span class="n">byte</span> <span class="n">crc_8</span><span class="p">(</span><span class="n">byte</span><span class="p">[]</span> <span class="n">data</span><span class="p">)</span> <span class="p">{</span>

   <span class="n">byte</span> <span class="n">crc</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span>

   <span class="n">foreach</span> <span class="p">(</span><span class="n">byte</span> <span class="n">b</span> <span class="ow">in</span> <span class="n">data</span><span class="p">)</span> <span class="p">{</span> <span class="n">crc</span> <span class="o">=</span> <span class="n">crc_table</span><span class="p">[</span><span class="n">b</span> <span class="o">^</span> <span class="n">crc</span><span class="p">];</span> <span class="p">}</span>

   <span class="k">return</span> <span class="n">crc</span><span class="p">;</span>
<span class="p">}</span>

<span class="n">public</span> <span class="n">void</span> <span class="n">calculateChecksum</span><span class="p">()</span> <span class="p">{</span>

   <span class="n">byte</span><span class="p">[]</span> <span class="n">data</span> <span class="o">=</span> <span class="n">new</span> <span class="n">byte</span><span class="p">[</span><span class="mi">6</span><span class="p">];</span>

   <span class="n">data</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="mh">0x85</span><span class="p">;</span>
   <span class="n">data</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="mh">0x04</span><span class="p">;</span>
   <span class="n">data</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">=</span> <span class="mh">0x07</span><span class="p">;</span>
   <span class="n">data</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span> <span class="o">=</span> <span class="mh">0x00</span><span class="p">;</span>
   <span class="n">data</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span> <span class="o">=</span> <span class="mh">0x5</span><span class="p">;</span>
   <span class="n">data</span><span class="p">[</span><span class="mi">5</span><span class="p">]</span> <span class="o">=</span> <span class="mh">0xff</span><span class="p">;</span>

   <span class="n">byte</span> <span class="n">crc</span> <span class="o">=</span> <span class="n">crc_8</span><span class="p">(</span><span class="n">data</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
</div>
<ul class="simple">
<li><p>API <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-alarm-start#leaps-alarm-start"><span class="std std-ref">leaps_alarm_start</span></a> の TLV リクエスト/レスポンスにおける CRC の例</p></li>
</ul>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 16%">
<col style="width: 46%">
<col style="width: 21%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
<td><p>チェックサム</p></td>
</tr>
<tr class="row-odd"><td><p>0x85</p></td>
<td><p>0x04</p></td>
<td><p>0x07 0x00 0x05 0xff</p></td>
<td><p>0x80</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 21%">
<col style="width: 21%">
<col style="width: 41%">
<col style="width: 17%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
<td><p>チェックサム</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x06</p></td>
</tr>
</tbody>
</table>
</div></blockquote>
</li>
</ul>
<p>一部のインターフェースでは、設定によって有効になっている場合（例：UART インターフェースまたは BLE インターフェース）、以前のリクエストがなくても内部イベントの結果として TLV フレームが生成されることがあります。CORE_INT GPIO ピンは、UART/SPI 上の内部イベントを通知するために使用されます。</p>
<p>イベントは <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-set#leaps-int-cfg-set"><span class="std std-ref">leaps_int_cfg_set</span></a> で設定できます。新しいイベントは CORE_INT ピンをセットします。CORE_INT ピンは、UART または SPI インターフェース上でユーザーが開始したアクティビティの後に自動的にクリアされます。マルチバイトデータ部分はリトルエンディアンで順序付けられます。</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types">API の汎用データ型</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-list">API コマンドリスト</a></li>
</ul>
</div>
</div>


           </div>
