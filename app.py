from flask import Flask, request, jsonify
import time, os, json

app = Flask(__name__)

# ---- REAL DATABASE (saves on Render) ----
DB_FILE = "ciphersyn_db.json"
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({"users":[], "ciphLore":[], "syntra":[]}, f)

def load_db():
    with open(DB_FILE) as f: return json.load(f)
def save_db(db):
    with open(DB_FILE, "w") as f: json.dump(db,f)

@app.route('/api/syntra', methods=['GET','POST'])
def syntra_api():
    db = load_db()
    if request.method == 'POST':
        data = request.json
        msg = {"cipher": data.get("cipher","Cipher"), "lore": data.get("lore",""), "ts": int(time.time()), "synlit": "● SynLit"}
        db["syntra"].append(msg)
        save_db(db)
        return jsonify({"ok": True})
    return jsonify(db["syntra"][-100:])

@app.route('/api/ciphlore', methods=['GET','POST'])
def lore_api():
    db = load_db()
    if request.method == 'POST':
        data = request.json
        post = {"cipher": data.get("cipher","Cipher"), "lore": data.get("lore",""), "syners": 0, "synacs": 0, "ts": int(time.time())}
        db["ciphLore"].insert(0, post)
        save_db(db)
        return jsonify({"ok": True})
    return jsonify(db["ciphLore"][:50])

@app.route('/api/forge', methods=['POST'])
def forge():
    db = load_db()
    data = request.json
    db["users"].append(data)
    save_db(db)
    return jsonify({"ok": True, "cipher": data.get("cipher")})

@app.route('/')
def os():
 return """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>CipherSyn V13.3 LIVE</title><style>@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@700&display=swap');*{margin:0;padding:0;box-sizing:border-box;font-family:'Space Grotesk'}body{background:#0a0614;color:#fff;height:100vh;overflow:hidden}.bg{position:fixed;inset:0;background:radial-gradient(at 50% 0%,#3a1d6d,#0a0614 70%)}.app{width:100%;max-width:420px;height:100vh;margin:0 auto;background:rgba(18,10,35,0.92);border-left:1px solid #a855ff33;border-right:1px solid #a855ff33;display:flex;flex-direction:column;position:relative}.header{padding:12px 16px;display:flex;justify-content:space-between;border-bottom:1px solid #a855ff22;font-size:11px;letter-spacing:2px;color:#c084fc}.screen{display:none;flex:1;overflow-y:auto;padding:14px;padding-bottom:90px}.screen.active{display:flex;flex-direction:column}.card{background:rgba(0,0,0,0.45);border:1px solid #a855ff33;border-radius:16px;padding:14px;margin-bottom:10px}.t{font-size:18px;font-weight:700;color:#e9d5ff}.s{font-size:10px;color:#a78bfa;margin:5px 0 10px}.input{width:100%;background:#0f0a1f;border:1px solid #a855ff33;border-radius:12px;padding:13px;color:#fff;margin-bottom:8px;outline:none}.btn{width:100%;background:linear-gradient(90deg,#9333ea,#a855ff);border:none;border-radius:12px;padding:13px;font-weight:700;color:#fff}.pill{background:#a855ff22;border:1px solid #a855ff33;padding:4px 9px;border-radius:20px;font-size:9px;color:#d8b4fe;margin:2px;display:inline-block}.nav{position:absolute;bottom:0;left:0;right:0;height:70px;background:rgba(10,6,20,0.98);border-top:1px solid #a855ff33;display:flex;justify-content:space-around;align-items:center}.nav-item{opacity:0.5;text-align:center;cursor:pointer}.nav-item.active{opacity:1;color:#c084fc}.center{width:54px;height:54px;background:linear-gradient(135deg,#9333ea,#c084fc);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24px;margin-top:-16px;box-shadow:0 0 18px #a855ff88}.msg{padding:8px 0;border-bottom:1px solid #ffffff08}.chatbox{position:absolute;bottom:70px;left:0;right:0;display:flex;gap:6px;padding:8px;background:#0f0a1f;border-top:1px solid #a855ff33}</style></head><body><div class="bg"></div><div class="app"><div class="header"><div>CIPHERSYN // V13.3 LIVE</div><div id="myCipher">SynLit</div></div>

<div id="s1" class="screen active"><div class="card" style="margin-top:20px"><div class="t">CiphIn | Forge Cipher</div><div class="s">Forge once • Use am to Ciphing people you invite</div><input class="input" id="cipherName" placeholder="Cipher • Your Handle (e.g Tega Cipher)"><input class="input" id="ciphAdra" placeholder="CiphAdra | CiphDigit"><input class="input" type="password" placeholder="Synkra"><button class="btn" onclick="forgeCipher()">Forge Cipher & CiphIn</button><div id="inviteBox" style="display:none;margin-top:12px" class="card"><div style="font-size:11px">Your Synvite Link • Share to people to Ciphing:</div><input class="input" id="inviteLink" readonly style="margin-top:8px;font-size:10px"><button class="btn" style="background:#1e1435;border:1px solid #a855ff44" onclick="navigator.clipboard.writeText(document.getElementById('inviteLink').value);alert('Synvite Copied!')">Splay Synvite • Copy Link</button></div></div></div>

<div id="s4" class="screen"><div style="margin-bottom:8px"><span class="pill">Sync</span><span class="pill">SynLeg</span><span class="pill">SynHot</span></div><input class="input" id="loreInput" placeholder="Ciphering... Write CiphLore"><button class="btn" onclick="postLore()">Ciphering • Post CiphLore</button><div id="feed" style="margin-top:10px"></div></div>

<div id="s5" class="screen"><div class="t" style="font-size:15px">Syntra • Ciphing • LIVE TEXTING</div><div class="s">SynVox • SynVid • SynGather • Real people you invite go appear here</div><div id="chatList" style="flex:1;overflow-y:auto"></div><div class="chatbox"><input class="input" id="chatInput" placeholder="Ciphing... Type Syntra" style="margin:0"><button class="btn" style="width:70px" onclick="sendTra()">Splay</button></div></div>

<div id="s6" class="screen"><div class="card"><div class="t">SynKeg</div><div class="s">4,700 SynCoin • Forge • Splay • SynCord Pay</div><div style="text-align:center;font-size:40px;font-weight:700">4,700 <span style="color:#a855ff">SynCoin</span></div></div></div>
<div id="s7" class="screen"><div class="card"><div class="t">SynFort • CiphGuard</div><div class="s">CiphSeal Active • SynFace • SynProof • SynLit</div><div style="font-size:11px;opacity:0.6">No SynCut • No CiphFlag • All Synced</div></div></div>
<div id="s8" class="screen"><div class="card"><div class="t">Invite • Splay Cipher</div><div class="s">How to invite people now</div><div style="font-size:12px;line-height:1.6">1. Forge Cipher for top<br>2. Copy your Synvite Link<br>3. Splay am for WhatsApp / X<br>4. When dem open link, dem go CiphIn & dem go see you for Syntra<br>5. Start Ciphing live!<br><br><span class="pill">CiphAdra = Email</span> <span class="pill">Syntra = Chat</span> <span class="pill">Splay = Send</span></div><input class="input" id="inviteLink2" readonly style="margin-top:10px;font-size:10px"><button class="btn" onclick="document.getElementById('inviteLink2').value=document.getElementById('inviteLink').value">Show My Synvite</button></div></div>

<div class="nav"><div class="nav-item active" onclick="go('s4')"><div>◉</div><div style="font-size:8px">Sync</div></div><div class="nav-item" onclick="go('s5')"><div>◍</div><div style="font-size:8px">Ciphing</div></div><div onclick="go('s4')"><div class="center">+</div></div><div class="nav-item" onclick="go('s6')"><div>◎</div><div style="font-size:8px">SynKeg</div></div><div class="nav-item" onclick="go('s8')"><div>🛡</div><div style="font-size:8px">Cipher</div></div></div>
</div>
<script>
let myCipher = localStorage.getItem('cipher') || '';
let invite = new URLSearchParams(window.location.search).get('synvite') || '';
if(myCipher) document.getElementById('myCipher').innerText = myCipher + ' ● SynLit';
function go(id){document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));document.getElementById(id).classList.add('active');document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));}

async function forgeCipher(){
 let c = document.getElementById('cipherName').value || 'Cipher'+Math.floor(Math.random()*100);
 let a = document.getElementById('ciphAdra').value || 'anon';
 if(!c) return alert('Enter Cipher');
 localStorage.setItem('cipher', c);
 myCipher = c;
 document.getElementById('myCipher').innerText = c + ' ● SynLit';
 let link = window.location.origin + '/?synvite=' + encodeURIComponent(c);
 document.getElementById('inviteLink').value = link;
 document.getElementById('inviteLink2').value = link;
 document.getElementById('inviteBox').style.display='block';
 await fetch('/api/forge',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({cipher:c, ciphAdra:a})});
 alert('Cipher Forged! Now you fit invite people. Go to Ciphing!');
 go('s5');
}

async function loadChat(){
 let res = await fetch('/api/syntra'); let data = await res.json();
 let html = data.map(m=>`<div class=msg><div style=font-size:12px;font-weight:700>${m.cipher} <span style=font-size:9px;color:#22c55e>${m.synlit}</span></div><div style=font-size:12px;opacity:0.9>${m.lore}</div></div>`).join('');
 document.getElementById('chatList').innerHTML = html || '<div style=opacity:0.4;font-size:11px;padding:20px;text-align:center>No Syntra yet • Be first to Ciphering</div>';
 let feedRes = await fetch('/api/ciphlore'); let feed = await feedRes.json();
 document.getElementById('feed').innerHTML = feed.map(p=>`<div class=card><div style=font-size:12px;font-weight:700>${p.cipher}</div><div style=font-size:12px;margin-top:4px>${p.lore}</div><div style=margin-top:6px><span class=pill>${p.syners||0} Syners</span><span class=pill>${p.synacs||0} Synacs</span><span class=pill>CiphSee</span></div></div>`).join('');
}
async function sendTra(){
 let input = document.getElementById('chatInput'); let lore = input.value; if(!lore) return;
 let cipher = localStorage.getItem('cipher') || 'Anon Cipher';
 await fetch('/api/syntra',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({cipher, lore})});
 input.value=''; loadChat();
}
async function postLore(){
 let input = document.getElementById('loreInput'); let lore = input.value; if(!lore) return;
 let cipher = localStorage.getItem('cipher') || 'Anon Cipher';
 await fetch('/api/ciphlore',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({cipher, lore})});
 input.value=''; loadChat();
}
setInterval(loadChat,2000);
loadChat();
if(invite){ document.getElementById('cipherName').placeholder = 'Invited by '+invite+' • Forge your Cipher'; go('s1');}
</script></body></html>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
