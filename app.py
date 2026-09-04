from flask import Flask
app = Flask(__name__)

@app.route('/')
def v132():
 return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
<title>CipherSyn OS V13.2</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box;font-family:'Space Grotesk',sans-serif}
body{background:#0a0614;color:#fff;overflow:hidden;height:100vh}
.bg{position:fixed;inset:0;background:radial-gradient(at 50% 0%,#3a1d6d 0%,#0a0614 70%);z-index:-2}
.grid{position:fixed;inset:0;opacity:0.15;background-image:linear-gradient(rgba(168,85,255,0.3) 1px,transparent 1px),linear-gradient(90deg,rgba(168,85,255,0.3) 1px,transparent 1px);background-size:40px 40px}
.app{width:100%;max-width:420px;height:100vh;margin:0 auto;background:rgba(18,10,35,0.85);backdrop-filter:blur(20px);border-left:1px solid #a855ff33;border-right:1px solid #a855ff33;display:flex;flex-direction:column;position:relative}
.header{padding:14px 18px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #a855ff22}
.logo{color:#c084fc;font-weight:700;letter-spacing:2px;font-size:14px}
.badge{font-size:10px;background:#a855ff22;border:1px solid #a855ff44;padding:4px 8px;border-radius:20px;color:#d8b4fe}
.screen{display:none;flex:1;overflow-y:auto;padding:18px;padding-bottom:90px;animation:fade 0.3s}
.screen.active{display:block}
@keyframes fade{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
.card{background:rgba(0,0,0,0.4);border:1px solid #a855ff33;border-radius:16px;padding:16px;margin-bottom:14px}
.title{font-size:22px;font-weight:700;color:#e9d5ff;margin-bottom:6px}
.sub{font-size:12px;color:#a78bfa;opacity:0.8;margin-bottom:14px}
.input{width:100%;background:#0f0a1f;border:1px solid #a855ff33;border-radius:12px;padding:14px;color:#fff;margin-bottom:10px;outline:none}
.input:focus{border-color:#a855ff;box-shadow:0 0 15px #a855ff44}
.btn{width:100%;background:linear-gradient(90deg,#9333ea,#a855ff);border:none;border-radius:12px;padding:14px;font-weight:700;color:#fff;cursor:pointer;letter-spacing:1px;margin-top:6px}
.btn:active{transform:scale(0.98)}
.link{font-size:11px;color:#c084fc;text-align:center;margin-top:12px;display:block;cursor:pointer}
.row{display:flex;gap:10px}
.pill{display:inline-block;background:#a855ff22;border:1px solid #a855ff33;padding:4px 10px;border-radius:20px;font-size:10px;color:#d8b4fe;margin:2px}
.post{border-bottom:1px solid #ffffff0f;padding:14px 0}
.avatar{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,#9333ea,#4f46e5);display:flex;align-items:center;justify-content:center;font-weight:700}
.dot{width:8px;height:8px;background:#22c55e;border-radius:50%;box-shadow:0 0 8px #22c55e;display:inline-block}
.nav{position:absolute;bottom:0;left:0;right:0;height:72px;background:rgba(10,6,20,0.95);border-top:1px solid #a855ff33;display:flex;justify-content:space-around;align-items:center;backdrop-filter:blur(20px)}
.nav-item{text-align:center;cursor:pointer;opacity:0.5;transition:0.2s}
.nav-item.active{opacity:1;color:#c084fc}
.nav-item div:first-child{font-size:20px}
.nav-item span{font-size:9px;letter-spacing:1px;display:block;margin-top:2px}
.center-btn{width:56px;height:56px;background:linear-gradient(135deg,#9333ea,#c084fc);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:26px;margin-top:-20px;box-shadow:0 0 20px #a855ff88;border:2px solid #0a0614}
.chat-item{display:flex;gap:12px;padding:12px 0;border-bottom:1px solid #ffffff0a;cursor:pointer}
.wallet-big{font-size:42px;font-weight:700;text-align:center;color:#fff}
.wallet-big span{color:#a855ff}
.toggle{width:40px;height:22px;background:#2a1f3f;border-radius:20px;position:relative;cursor:pointer}
.toggle.on{background:#a855ff}
.toggle::after{content:'';position:absolute;top:2px;left:2px;width:18px;height:18px;background:#fff;border-radius:50%;transition:0.2s}
.toggle.on::after{left:20px}
</style>
</head>
<body>
<div class="bg"></div><div class="grid"></div>
<div class="app">
<div class="header">
<div class="logo">CIPHERSYN // V13.2</div>
<div class="badge"><span class="dot"></span> SynLit • LAGOS</div>
</div>

<!-- 1 CIPHERIN AUTH -->
<div id="s1" class="screen active">
<div class="card" style="margin-top:30px">
<div class="title">CipherIn</div>
<div class="sub">Enter your CiphAdra or CiphDigit + Synkra to CipherIn. If you are lost, hit ReSynkra.</div>
<input class="input" placeholder="CiphAdra (Email) or CiphDigit (Phone)" id="loginUser">
<input class="input" type="password" placeholder="Synkra (Your Secret Sync)" id="loginPass">
<button class="btn" onclick="goTo('s4')">CipherIn • Login</button>
<span class="link" onclick="goTo('s2')">Forget Cipher? = Forge New Cipher (Sign Up)</span>
<span class="link" onclick="goTo('s3')">Lost Synkra? ReSynkra = Reset</span>
<div style="margin-top:16px;font-size:10px;color:#ffffff55">DICTIONARY: Ciphor=He/Male • Ciphra=She/Female • Cipher=They/Non-binary</div>
</div>
</div>

<!-- 2 FORGE CIPHER SIGN UP -->
<div id="s2" class="screen">
<div class="card">
<div class="title">Forge Cipher</div>
<div class="sub">Create your Synced Identity</div>
<input class="input" placeholder="Username • Your Cipher">
<input class="input" placeholder="CiphAdra • Email">
<input class="input" placeholder="CiphDigit • Phone">
<div class="row"><div class="pill" onclick="this.style.background='#a855ff'">Ciphor ♂ Male</div><div class="pill">Ciphra ♀ Female</div><div class="pill">Cipher ⚧ They</div></div>
<input class="input" type="password" placeholder="Synkra • Password" style="margin-top:10px">
<input class="input" type="password" placeholder="Confirm Synkra">
<input class="input" placeholder="Ciphacore • Bio (e.g. Port Harcourt to the World)">
<button class="btn" onclick="goTo('s4')">Forge Your Cipher • Sign Up</button>
<span class="link" onclick="goTo('s1')">Already Synced? CipherIn</span>
</div>
</div>

<!-- 3 SYNKRA REFORGE PASSWORD -->
<div id="s3" class="screen">
<div class="card">
<div class="title">Synkra ReForge</div>
<div class="sub">Choose new Syncode & ReSynkra</div>
<input class="input" placeholder="Enter CiphAdra / CiphDigit">
<button class="btn" style="background:#2a1f3f;border:1px solid #a855ff44">Send Syncode • OTP</button>
<input class="input" placeholder="Syncode • Verification Code" style="margin-top:14px">
<input class="input" type="password" placeholder="New Synkra">
<input class="input" type="password" placeholder="Confirm Synkra">
<button class="btn" onclick="goTo('s1')">ReForge Password • Save</button>
</div>
</div>

<!-- 4 SYNC FEED -->
<div id="s4" class="screen">
<div class="row" style="margin-bottom:10px"><span class="pill" style="background:#a855ff;color:#fff">Sync • Home Feed</span><span class="pill">SynLeg • Following</span><span class="pill">SynHot 🔥 Trending</span></div>
<div class="card">
<div style="display:flex;gap:10px;align-items:center"><div class="avatar">TC</div><div><div style="font-weight:700;font-size:13px">Tega Cipher <span style="font-size:10px;color:#22c55e">● SynLit</span></div><div style="font-size:10px;opacity:0.5">Cipher • CiphLore • 1k Syners</div></div></div>
<div style="margin-top:10px;font-size:13px">Just forged a new Cipher! The protocol update is 🔥 <span style="color:#a855ff">#Ciphering</span></div>
<div class="row" style="margin-top:10px"><span class="pill">💜 1k Syners (Likes)</span><span class="pill">💬 80 Synacs (Comments)</span><span class="pill">🔁 500 CiphSee (Views)</span></div>
</div>
<div class="card">
<div style="display:flex;gap:10px"><div class="avatar" style="background:linear-gradient(135deg,#ec4899,#8b5cf6)">C</div><div><div style="font-weight:700;font-size:13px">Ciphor <span style="font-size:9px;background:#22c55e;color:#000;padding:2px 6px;border-radius:10px">CiphSeal ✓ Verified</span></div><div style="font-size:11px;opacity:0.7;margin-top:4px">Exploring CiphLore: The lost data fragment recovered at sector 70</div><div style="font-size:9px;opacity:0.4;margin-top:6px">Protected by CiphGuard encryption • 12m ago</div></div></div>
</div>
<button class="btn" onclick="goTo('s5')">Go to Syntra Chat →</button>
</div>

<!-- 5 SYNTRA CHAT -->
<div id="s5" class="screen">
<div class="title" style="font-size:18px">Syntra • Chat & SynVox</div>
<input class="input" placeholder="Search Syntra..." style="padding:10px">
<div class="chat-item"><div class="avatar">SV</div><div style="flex:1"><div style="font-size:13px;font-weight:700">SynVox <span style="font-size:10px;color:#22c55e">● Voice room: Designing Cipher — 8 active</span></div><div style="font-size:11px;opacity:0.6">SynVox = Voice call • SynVid = Video call</div></div><div style="font-size:9px;opacity:0.4">now</div></div>
<div class="chat-item"><div class="avatar">VS</div><div style="flex:1"><div style="font-size:13px">SynVerse</div><div style="font-size:11px;opacity:0.6">Visual call with CiphLore — 3 participants • SynGather = Group call</div></div><div style="font-size:9px;opacity:0.4">2m ago</div></div>
<div class="chat-item"><div class="avatar">TC</div><div style="flex:1"><div style="font-size:13px">Tega Cipher <span class="dot"></span></div><div style="font-size:11px;opacity:0.6">Sent: Check the new synk you forged 🟢 • SynShow = Screen share</div></div><div style="font-size:9px;opacity:0.4">15m ago</div></div>
<div class="card" style="margin-top:10px"><div style="font-size:11px;opacity:0.7">DICTIONARY: SynBurst = Live • Burst Cipher = Go Live • SynSers = Live viewers • CiphPlace = Story/status</div></div>
</div>

<!-- 6 SYNK EG WALLET -->
<div id="s6" class="screen">
<div class="card">
<div class="title">SynKeg Wallet</div>
<div class="sub">Balance SynCoins • +230 this week</div>
<div class="wallet-big">4,700 <span>SynCoins</span></div>
<div style="text-align:center;font-size:11px;color:#22c55e;margin-top:6px">+230 SynCoins this week • SynLit</div>
<div class="row" style="margin-top:16px"><button class="btn" style="flex:1" onclick="alert('Forge SynCoin = Add Money')">Forge • Add</button><button class="btn" style="flex:1;background:#1e1533;border:1px solid #a855ff44" onclick="alert('Splay SynCoin = Send')">Splay • Send</button></div>
<div class="card" style="margin-top:14px;background:rgba(168,85,255,0.1)"><div style="font-size:11px">SynCord Pay = Location Pay • Chime = Notification • SynTag = Tag/Mention</div></div>
</div>
</div>

<!-- 7 SYNFORT -->
<div id="s7" class="screen">
<div class="card">
<div class="title">SynFort CiphGuard</div>
<div class="sub">Secure - All systems protected</div>
<div style="display:flex;justify-content:space-between;margin:12px 0"><div><div style="font-size:13px">SynFace • Facial Auth</div><div style="font-size:10px;opacity:0.5">Enabled</div></div><div class="toggle on"></div></div>
<div style="display:flex;justify-content:space-between;margin:12px 0"><div><div style="font-size:13px">SynProof • Identity Proof</div><div style="font-size:10px;opacity:0.5">Identity Proof</div></div><div class="toggle on"></div></div>
<div style="display:flex;justify-content:space-between;margin:12px 0"><div><div style="font-size:13px">CiphSeal • End-to-End Encryption</div><div style="font-size:10px;opacity:0.5">Active</div></div><div class="toggle on"></div></div>
<div style="font-size:10px;opacity:0.5;margin-top:14px">Security Logs: New login from Device SynPad • 10:32 AM • Allowed</div>
<button class="btn" style="margin-top:14px">Run Security Scan</button>
<div class="card" style="margin-top:10px"><div style="font-size:11px">SynKeep = Bookmark/Save • SynCut/CipherCut = Block/Mute • CiphFlag = Report • CiphSeal = Verification</div></div>
</div>
</div>

<!-- 8 WHITEPAPER / PROFILE -->
<div id="s8" class="screen">
<div class="card">
<div style="text-align:center"><div style="font-size:28px">🛡️</div><div style="font-weight:700;color:#c084fc;letter-spacing:2px">CIPHERSYN LABS</div><div class="title" style="text-align:center;margin-top:10px">CipherSyn OS V12 Whitepaper</div><div class="sub" style="text-align:center">The First OS With Its Own Language — From Port Harcourt to the World</div></div>
<div class="row" style="margin-top:10px;flex-wrap:wrap"><span class="pill">🔒 ENCRYPTED</span><span class="pill">🔄 SYNCED</span><span class="pill">🛡️ PRIVACY FIRST</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:14px">
<div class="card" style="padding:10px;text-align:center"><div>📄</div><div style="font-size:10px">Manifesto</div></div>
<div class="card" style="padding:10px;text-align:center"><div>📖</div><div style="font-size:10px">Dictionary</div></div>
<div class="card" style="padding:10px;text-align:center"><div>🪙</div><div style="font-size:10px">Tokenomics SynKeg</div></div>
<div class="card" style="padding:10px;text-align:center"><div>🏗️</div><div style="font-size:10px">Architecture SynFort</div></div>
</div>
<div style="font-size:10px;text-align:center;opacity:0.5;margin-top:10px">v12.0.4 • Released • Secure • Decentralized • Open • Port Harcourt, Nigeria • 2024</div>
</div>
</div>

<div class="nav">
<div class="nav-item active" onclick="goTo('s4')" id="n-sync"><div>◉</div><span>Sync</span></div>
<div class="nav-item" onclick="goTo('s1')" id="n-decipher"><div>🔍</div><span>DeCipher</span></div>
<div class="nav-item" onclick="goTo('s2')"><div class="center-btn">+</div><span>Ciphering</span></div>
<div class="nav-item" onclick="goTo('s5')" id="n-ciphing"><div>💬</div><span>Ciphing</span></div>
<div class="nav-item" onclick="goTo('s8')" id="n-cipher"><div>🛡️</div><span>Cipher</span></div>
</div>

</div>
<script>
function goTo(id){
 document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));
 document.getElementById(id).classList.add('active');
 document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
 if(id=='s4')document.getElementById('n-sync').classList.add('active');
 if(id=='s1')document.getElementById('n-decipher').classList.add('active');
 if(id=='s5')document.getElementById('n-ciphing').classList.add('active');
 if(id=='s8' || id=='s6' || id=='s7')document.getElementById('n-cipher').classList.add('active');
 window.scrollTo(0,0);
}
</script>
</body>
</html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
