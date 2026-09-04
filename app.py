from flask import Flask
app = Flask(__name__)

@app.route('/')
def os():
    return """
<!DOCTYPE html>
<html>
<head>
<title>CipherSyn OS v13</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box;font-family:'JetBrains Mono',monospace}
body{background:#050507;color:#00ff88;overflow:hidden;height:100vh}
.bg{position:fixed;inset:0;background:radial-gradient(ellipse at top,#0a1f14 0%,#050507 60%);z-index:-1}
.grid{position:fixed;inset:0;background-image:linear-gradient(rgba(0,255,136,0.05) 1px,transparent 1px),linear-gradient(90deg,rgba(0,255,136,0.05) 1px,transparent 1px);background-size:40px 40px;animation:move 20s linear infinite}
@keyframes move{0%{transform:translateY(0)}100%{transform:translateY(40px)}}
.topbar{height:40px;background:rgba(0,0,0,0.8);border-bottom:1px solid #00ff8844;display:flex;align-items:center;justify-content:space-between;padding:0 20px;backdrop-filter:blur(10px)}
.logo{font-weight:700;letter-spacing:2px;text-shadow:0 0 10px #00ff88}
.status{display:flex;gap:15px;font-size:12px}
.dot{width:8px;height:8px;background:#00ff88;border-radius:50%;display:inline-block;box-shadow:0 0 8px #00ff88;animation:pulse 1s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.5}}
.desktop{padding:30px;display:grid;grid-template-columns:repeat(auto-fill,80px);gap:30px;place-content:start}
.icon{width:80px;text-align:center;cursor:pointer;transition:0.2s}
.icon:hover{transform:translateY(-5px) scale(1.05)}
.icon-box{width:60px;height:60px;margin:0 auto 8px;background:linear-gradient(135deg,#0a2a1a,#001a0f);border:1px solid #00ff8866;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:28px;box-shadow:0 0 15px rgba(0,255,136,0.2)}
.icon span{font-size:10px;letter-spacing:1px}
.dock{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:rgba(0,0,0,0.8);border:1px solid #00ff8844;border-radius:20px;padding:10px 20px;display:flex;gap:15px;backdrop-filter:blur(15px)}
.dock-item{width:45px;height:45px;background:#0a1f14;border:1px solid #00ff8855;border-radius:10px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:0.2s}
.dock-item:hover{background:#00ff8822;box-shadow:0 0 15px #00ff88}
.terminal{position:fixed;bottom:90px;right:20px;width:380px;background:rgba(0,0,0,0.9);border:1px solid #00ff8866;border-radius:12px;padding:15px;font-size:11px;max-height:200px;overflow:hidden}
.terminal-bar{display:flex;gap:6px;margin-bottom:10px}
.terminal-bar div{width:10px;height:10px;border-radius:50%}
.red{background:#ff5f56}.yellow{background:#ffbd2e}.green{background:#27c93f}
.line{opacity:0;animation:type 0.5s forwards}
.line:nth-child(2){animation-delay:0.3s}.line:nth-child(3){animation-delay:0.6s}.line:nth-child(4){animation-delay:0.9s}
@keyframes type{from{opacity:0;transform:translateY(5px)}to{opacity:1;transform:translateY(0)}}
.center-title{position:fixed;top:45%;left:50%;transform:translate(-50%,-50%);text-align:center;pointer-events:none}
.center-title h1{font-size:48px;font-weight:700;letter-spacing:8px;text-shadow:0 0 30px #00ff88;animation:glow 2s ease-in-out infinite}
.center-title p{margin-top:10px;letter-spacing:4px;opacity:0.6;font-size:12px}
@keyframes glow{0%,100%{text-shadow:0 0 30px #00ff88}50%{text-shadow:0 0 50px #00ff88,0 0 80px #00ff88}}
@media(max-width:600px){.center-title h1{font-size:28px}.terminal{width:90%;left:5%;right:5%}}
</style>
</head>
<body>
<div class="bg"></div><div class="grid"></div>
<div class="topbar">
<div class="logo">CIPHER_SYN // OS v13</div>
<div class="status"><span><span class="dot"></span> ONLINE</span><span id="time"></span><span>LAGOS, NG</span></div>
</div>
<div class="desktop">
<div class="icon"><div class="icon-box">💻</div><span>TERMINAL</span></div>
<div class="icon"><div class="icon-box">📁</div><span>FILES</span></div>
<div class="icon"><div class="icon-box">🧠</div><span>NEURAL</span></div>
<div class="icon"><div class="icon-box">🔐</div><span>VAULT</span></div>
<div class="icon"><div class="icon-box">🌐</div><span>NETWORK</span></div>
<div class="icon"><div class="icon-box">⚙️</div><span>SYSTEM</span></div>
</div>
<div class="center-title">
<h1>CIPHERSYN</h1>
<p>OPERATING SYSTEM v13.0 • DEPLOYED</p>
<p style="margin-top:20px;font-size:10px;opacity:0.4">BUILT IN LAGOS • LIVE ON RENDER</p>
</div>
<div class="terminal">
<div class="terminal-bar"><div class="red"></div><div class="yellow"></div><div class="green"></div></div>
<div class="line">> Initializing CipherSyn Kernel...</div>
<div class="line">> Quantum encryption: ACTIVE [✓]</div>
<div class="line">> Neural link: ESTABLISHED [✓]</div>
<div class="line">> System status: <span style="color:#00ff88">LIVE ON https://ciphersyn-os-v13-1.onrender.com</span></div>
</div>
<div class="dock">
<div class="dock-item">🚀</div>
<div class="dock-item">💾</div>
<div class="dock-item">🔍</div>
<div class="dock-item">📊</div>
<div class="dock-item">🔋</div>
</div>
<script>
setInterval(()=>{document.getElementById('time').innerText=new Date().toLocaleTimeString()},1000)
</script>
</body>
</html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
