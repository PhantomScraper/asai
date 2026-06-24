---
title: "LE"
lang: ja
slug: "leaps-rtls/integration-guide/shell-api/le"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/shell-api/le/"
order: 137
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="le">
<h1>LE</h1>
<hr class="docutils">
<div class="section" id="les">
<span id="id1"></span><h2>les</h2>
<p>測距アンカーまでの距離と、ロケーション・エンジンが有効な場合の位置を表示します。</p>
<p>例1:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; les</span>
<span class="go">leaps&gt; POS[-1.21,2.23,-0.60,84] 0810[0.06,0.18,2.47,100]=3.90 8431[0.06,6.77,2.47,100]=5.62 919D[3.30,0.22,2.47,100]=5.81 5517[3.30,6.94,2.47,100]=6.80</span>
<span class="go">POS[-1.22,2.22,-0.59,84] 0810[0.06,0.18,2.47,100]=3.90 8431[0.06,6.77,2.47,100]=5.63 919D[3.30,0.22,2.47,100]=5.82 5517[3.30,6.94,2.47,100]=6.89</span>
<span class="go">POS[-1.28,2.20,-0.58,85] 0810[0.06,0.18,2.47,100]=3.89 8431[0.06,6.77,2.47,100]=5.65 919D[3.30,0.22,2.47,100]=5.85 5517[3.30,6.94,2.47,100]=6.94</span>
<span class="go">POS[-1.24,2.30,-0.51,85] 0810[0.06,0.18,2.47,100]=3.88 8431[0.06,6.77,2.47,100]=5.52 919D[3.30,0.22,2.47,100]=5.82 5517[3.30,6.94,2.47,100]=6.81</span>
</pre></div>
</div>
<p>例2:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; les 1</span>
<span class="go">leaps&gt; TS=176262990 DIFF=98310 SEAT=0 LE=1 MOV=0 POS[-1.27,2.11,-0.60,85] 0810[0.06,0.18,2.47,100]=3.86 8431[0.06,6.77,2.47,100]=5.74 919D[3.30,0.22,2.47,100]=5.82 5517[3.30,6.94,2.47,100]=6.90</span>
<span class="go">TS=176361300 DIFF=98310 SEAT=0 LE=1 MOV=0 POS[-1.29,2.66,-0.17,85] 0810[0.06,0.18,2.47,100]=3.87 8431[0.06,6.77,2.47,100]=5.73 919D[3.30,0.22,2.47,100]=5.83 5517[3.30,6.94,2.47,100]=6.81</span>
<span class="go">TS=176459610 DIFF=98310 SEAT=0 LE=1 MOV=0 POS[-1.23,2.11,-0.62,84] 0810[0.06,0.18,2.47,100]=3.87 8431[0.06,6.77,2.47,100]=5.74 919D[3.30,0.22,2.47,100]=5.80 5517[3.30,6.94,2.47,100]=6.86</span>
</pre></div>
</div>
<p><strong>どこで</strong></p>
<ul class="simple">
<li><p>TS = タイムスタンプ</p></li>
<li><p>DIFF = 前回の測定との時間差</p></li>
<li><p>SEAT = データシート</p></li>
<li><p>LE = 1 ロケーションエンジンが有効</p></li>
<li><p>MOV = 1 タグが移動中（アクセルセンサーによって示される）。</p></li>
</ul>
<p>例3:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; les 1 &lt;window size(1-20)&gt;</span>
<span class="go">leaps&gt; TS=165350940 DIFF=98310 SEAT=0 LE=1 MOV=0 POS[-0.11,2.14,-0.88,77]{0.25,0.01,0.06,R95=0.11} 0810[0.06,0.18,2.47,100]=3.89{0.01} 8431[0.06,6.77,2.47,100]=5.72{0.01} 919D[3.30,0.22,2.47,100]=5.85{0.02} 5517[3.30,6.94,2.47,100]=6.77{0.09}</span>
<span class="go">TS=165449250 DIFF=98310 SEAT=0 LE=1 MOV=0 POS[-1.25,2.11,-0.61,85]{0.25,0.01,0.06,R95=1.09} 0810[0.06,0.18,2.47,100]=3.86{0.01} 8431[0.06,6.77,2.47,100]=5.74{0.01} 919D[3.30,0.22,2.47,100]=5.81{0.02} 5517[3.30,6.94,2.47,100]=6.83{0.09}</span>
<span class="go">TS=165547560 DIFF=98310 SEAT=0 LE=1 MOV=0 POS[-1.24,2.13,-0.63,85]{0.25,0.01,0.06,R95=1.09} 0810[0.06,0.18,2.47,100]=3.89{0.01} 8431[0.06,6.77,2.47,100]=5.73{0.01} 919D[3.30,0.22,2.47,100]=5.82{0.02} 5517[3.30,6.94,2.47,100]=6.83{0.09}</span>
<span class="go">TS=165645870 DIFF=98310 SEAT=0 LE=1 MOV=0 POS[-1.30,2.12,-0.60,85]{0.25,0.01,0.06,R95=1.09} 0810[0.06,0.18,2.47,100]=3.88{0.01} 8431[0.06,6.77,2.47,100]=5.73{0.01} 919D[3.30,0.22,2.47,100]=5.85{0.02} 5517[3.30,6.94,2.47,100]=6.92{0.09}</span>
</pre></div>
</div>
<p><strong>どこで</strong></p>
<ul class="simple">
<li><p>{0.25,0.01,0.06,R95=1.09} -&gt; X,Y,Zの標準偏差と位置のR95値</p></li>
<li><p>{0.01}の各アンカーでの標準偏差 -&gt; 距離測定の標準偏差。</p></li>
</ul>
<hr class="docutils">
</div>
<div class="section" id="lec">
<span id="id2"></span><h2>lec</h2>
<p>測距アンカーまでの距離と、ロケーションエンジンが有効な場合の位置をCSV形式で表示します。</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; lec</span>
<span class="go">leaps&gt; POS,4.09,-2.80,0.57,73,MEAS,4,AN0,8EAA,5.14,-2.16,0.00,100,1.44,AN1,5886,5.30,-4.57,0.00,100,2.08,AN2,4F2E,2.12,-1.90,0.00,100,2.21,AN3,468D,2.07,-4.68,0.00,100,2.76</span>
<span class="go">POS,4.09,-2.82,0.62,72,MEAS,4,AN0,8EAA,5.14,-2.16,0.00,100,1.43,AN1,5886,5.30,-4.57,0.00,100,2.08,AN2,4F2E,2.12,-1.90,0.00,100,2.22,AN3,468D,2.07,-4.68,0.00,100,2.76</span>
<span class="go">POS,4.09,-2.84,0.62,73,MEAS,4,AN0,8EAA,5.14,-2.16,0.00,100,1.43,AN1,5886,5.30,-4.57,0.00,100,2.07,AN2,4F2E,2.12,-1.90,0.00,100,2.22,AN3,468D,2.07,-4.68,0.00,100,2.74</span>
<span class="go">POS,4.04,-2.96,-0.39,85,MEAS,4,AN0,8EAA,5.14,-2.16,0.00,100,1.41,AN1,5886,5.30,-4.57,0.00,100,2.08,AN2,4F2E,2.12,-1.90,0.00,100,2.24,AN3,468D,2.07,-4.68,0.00,100,2.74</span>
<span class="go">POS,4.04,-2.96,-0.39,85,MEAS,4,AN0,8EAA,5.14,-2.16,0.00,100,1.42,AN1,5886,5.30,-4.57,0.00,100,2.08,AN2,4F2E,2.12,-1.90,0.00,100,2.23,AN3,468D,2.07,-4.68,0.00,100,2.74</span>
<span class="go">POS,4.04,-2.97,-0.38,86,MEAS,4,AN0,8EAA,5.14,-2.16,0.00,100,1.42,AN1,5886,5.30,-4.57,0.00,100,2.08,AN2,4F2E,2.12,-1.90,0.00,100,2.23,AN3,468D,2.07,-4.68,0.00,100,2.73</span>
<span class="go">POS,4.03,-2.96,-0.36,86,MEAS,4,AN0,8EAA,5.14,-2.16,0.00,100,1.41,AN1,5886,5.30,-4.57,0.00,100,2.09,AN2,4F2E,2.12,-1.90,0.00,100,2.22,AN3,468D,2.07,-4.68,0.00,100,2.74</span>
<span class="go">POS,4.07,-2.85,0.59,74,MEAS,4,AN0,8EAA,5.14,-2.16,0.00,100,1.41,AN1,5886,5.30,-4.57,0.00,100,2.07,AN2,4F2E,2.12,-1.90,0.00,100,2.20,AN3,468D,2.07,-4.68,0.00,100,2.71</span>
<span class="go">POS,4.08,-2.83,0.61,73,MEAS,4,AN0,8EAA,5.14,-2.16,0.00,100,1.42,AN1,5886,5.30,-4.57,0.00,100,2.08,AN2,4F2E,2.12,-1.90,0.00,100,2.20,AN3,468D,2.07,-4.68,0.00,100,2.73</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="lep">
<span id="id3"></span><h2>lep</h2>
<p>CSV形式で位置を表示。</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; lep</span>
<span class="go">leaps&gt; POS,4.06,-2.95,-0.46,82</span>
<span class="go">POS,4.06,-2.95,-0.46,82</span>
<span class="go">POS,4.08,-2.96,-0.48,81</span>
<span class="go">POS,4.09,-2.96,-0.51,80</span>
<span class="go">POS,4.09,-2.98,-0.51,80</span>
<span class="go">POS,4.04,-2.98,-0.46,84</span>
<span class="go">POS,4.06,-2.99,-0.46,83</span>
<span class="go">POS,4.06,-2.98,-0.46,83</span>
<span class="go">POS,4.06,-2.98,-0.44,84</span>
<span class="go">POS,4.05,-2.99,-0.44,84</span>
<span class="go">POS,4.04,-2.99,-0.40,86</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="lej">
<span id="id4"></span><h2>lej</h2>
<p>JSON形式で位置を表示。</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; lej</span>
<span class="go">leaps&gt; {"position":{"x":4.036338,"y":-2.990612,"z":-0.439725,"quality":84},"superFrameNumber":0}</span>
<span class="go">{"position":{"x":4.026520,"y":-2.990608,"z":-0.387953,"quality":86},"superFrameNumber":1}</span>
<span class="go">{"position":{"x":4.088943,"y":-2.986658,"z":-0.425675,"quality":84},"superFrameNumber":2}</span>
<span class="go">{"position":{"x":4.030442,"y":-2.999600,"z":-0.371072,"quality":87},"superFrameNumber":3}</span>
<span class="go">{"position":{"x":4.026428,"y":-3.000456,"z":-0.392067,"quality":86},"superFrameNumber":4}</span>
<span class="go">{"position":{"x":4.042718,"y":-3.000376,"z":-0.367999,"quality":87},"superFrameNumber":5}</span>
<span class="go">{"position":{"x":4.045533,"y":-2.997239,"z":-0.412224,"quality":85},"superFrameNumber":6}</span>
<span class="go">{"position":{"x":4.050518,"y":-3.015047,"z":-0.445795,"quality":85},"superFrameNumber":7}</span>
<span class="go">{"position":{"x":4.091267,"y":-3.020544,"z":-0.423068,"quality":85},"superFrameNumber":8}</span>
<span class="go">{"position":{"x":4.093882,"y":-3.013582,"z":-0.471020,"quality":83},"superFrameNumber":9}</span>
<span class="go">{"position":{"x":4.080563,"y":-2.995730,"z":-0.463593,"quality":83},"superFrameNumber":10}</span>
<span class="go">{"position":{"x":4.098993,"y":-2.989659,"z":-0.494520,"quality":81},"superFrameNumber":11}</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="lea">
<span id="id5"></span><h2>lea</h2>
<p>meas.、pos.、pdoaを表示</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; lea</span>
<span class="go">leaps&gt; POS[4.11,-2.97,-0.49,81] 8EAA[5.14,-2.16,0.00,100]=1.41 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 5886[5.30,-4.57,0.00,100]=2.07 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 4F2E[2.12,-1.90,0.00,100]=2.30 l0</span>
<span class="go">POS[4.10,-2.97,-0.45,82] 8EAA[5.14,-2.16,0.00,100]=1.41 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 5886[5.30,-4.57,0.00,100]=2.07 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 4F2E[2.12,-1.90,0.00,100]=2.28 loc_az_p0</span>
<span class="go">POS[4.11,-2.97,-0.45,82] 8EAA[5.14,-2.16,0.00,100]=1.41 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 5886[5.30,-4.57,0.00,100]=2.07 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 4F2E[2.12,-1.90,0.00,100]=2.28 loc_az_p0</span>
<span class="go">POS[4.12,-2.96,-0.48,81] 8EAA[5.14,-2.16,0.00,100]=1.40 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 5886[5.30,-4.57,0.00,100]=2.07 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 4F2E[2.12,-1.90,0.00,100]=2.30 loc_az_p0</span>
<span class="go">POS[4.07,-3.00,-0.40,85] 8EAA[5.14,-2.16,0.00,100]=1.41 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 5886[5.30,-4.57,0.00,100]=2.04 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 4F2E[2.12,-1.90,0.00,100]=2.27 loc_az_p0</span>
<span class="go">POS[4.08,-2.99,-0.38,85] 8EAA[5.14,-2.16,0.00,100]=1.40 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 5886[5.30,-4.57,0.00,100]=2.03 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 4F2E[2.12,-1.90,0.00,100]=2.28 loc_az_p0</span>
<span class="go">POS[4.07,-3.00,-0.35,87] 8EAA[5.14,-2.16,0.00,100]=1.40 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 5886[5.30,-4.57,0.00,100]=2.03 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 4F2E[2.12,-1.90,0.00,100]=2.27 loc_az_p0</span>
<span class="go">POS[4.06,-2.98,-0.35,86] 8EAA[5.14,-2.16,0.00,100]=1.40 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 5886[5.30,-4.57,0.00,100]=2.04 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 4F2E[2.12,-1.90,0.00,100]=2.26 loc_az_p0</span>
<span class="go">POS[4.05,-2.98,-0.37,86] 8EAA[5.14,-2.16,0.00,100]=1.41 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 5886[5.30,-4.57,0.00,100]=2.05 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 4F2E[2.12,-1.90,0.00,100]=2.25 loc_az_p0</span>
<span class="go">POS[4.06,-2.99,-0.42,85] 8EAA[5.14,-2.16,0.00,100]=1.42 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 5886[5.30,-4.57,0.00,100]=2.06 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 4F2E[2.12,-1.90,0.00,100]=2.27 loc_az_p0</span>
<span class="go">POS[4.06,-2.98,-0.47,82] 8EAA[5.14,-2.16,0.00,100]=1.43 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 5886[5.30,-4.57,0.00,100]=2.07 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 4F2E[2.12,-1.90,0.00,100]=2.28 loc_az_p0</span>
<span class="go">POS[4.09,-2.97,-0.50,80] 8EAA[5.14,-2.16,0.00,100]=1.42 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 5886[5.30,-4.57,0.00,100]=2.08 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 4F2E[2.12,-1.90,0.00,100]=2.29 loc_az_p0</span>
<span class="go">POS[4.07,-2.97,-0.46,83] 8EAA[5.14,-2.16,0.00,100]=1.41 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 5886[5.30,-4.57,0.00,100]=2.07 loc_az_pdoa:0.00 loc_az:0.00 cfo_ppm:0.00 4F2E[2.12,-1.90,0.00,100]=2.28 loc_az_p0</span>
</pre></div>
</div>
</div>
</div>


           </div>
