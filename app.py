from flask import Flask, render_template_string, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "v13-2-final"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ciphersyn.db'
db = SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), default="Olowoyotemidayodavid")
    handle=db.Column(db.String(50), default="ayo.sync")
    gender=db.Column(db.String(20), default="")
    location=db.Column(db.String(50), default="Lagos NG")

class Cipher(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.Text)
    syn=db.Column(db.Integer, default=0)
    disyn=db.Column(db.Integer, default=0)

with app.app_context():
    db.create_all()
    if not User.query.first():
        db.session.add(User())
        db.session.add(Cipher(content="CipherSyn V13.2 - SYN=Like DISYN=Dislike SYNHUSH=Mute Gender OPTIONAL!", syn=1))
        db.session.commit()

HTML="""
<body style="background:#0A0A0F;color:#fff;font-family:sans-serif;padding:20px">
<h1 style="color:#8B5CF6">CipherSyn OS V13.2 FOR USING</h1>
<div style="background:#15151F;padding:16px;border-radius:16px;border:1px solid #8B5CF6">
<b>{{ u.name }} @{{ u.handle }}</b><br>
Gender: {% if u.gender %}{{ u.gender }}{% else %}Prefer not to say (OPTIONAL){% endif %} | {{ u.location }} | SynLit 🟢
<br><br><a href="/forge" style="background:#8B5CF6;color:#fff;padding:8px 16px;border-radius:20px;text-decoration:none">Edit Forge - Gender OPTIONAL</a>
</div>
{% for c in cs %}
<div style="background:#15151F;padding:16px;border-radius:16px;margin-top:12px">
<p>{{ c.content }}</p><p style="color:#8B5CF6">#CIPHERSIGIL</p>
<a href="/syn/{{ c.id }}" style="background:#8B5CF6;color:#fff;padding:6px 12px;border-radius:20px;text-decoration:none">SYN 💜 {{ c.syn }}</a>
<a href="/disyn/{{ c.id }}" style="background:#2A2A3A;color:#fff;padding:6px 12px;border-radius:20px;text-decoration:none">DISYN {{ c.disyn }}</a> SYNERS | CIPHESEE 843 | SYNSPLAY | SYNTUG | SYNHUSH 🔇
</div>
{% endfor %}
</body>
"""

FORGE="""
<body style="background:#0A0A0F;color:#fff;font-family:sans-serif;padding:20px">
<h2 style="color:#8B5CF6">Forge Cipher - Gender OPTIONAL V13.2</h2>
<form method="POST" style="background:#15151F;padding:16px;border-radius:16px">
<input name="name" value="{{ u.name }}" style="width:100%;padding:12px;margin:6px 0;border-radius:10px;background:#1E1E2A;color:#fff;border:1px solid #8B5CF6">
<input name="handle" value="{{ u.handle }}" style="width:100%;padding:12px;margin:6px 0;border-radius:10px;background:#1E1E2A;color:#fff;border:1px solid #8B5CF6">
<label style="color:#8B5CF6">Cipher Form (Gender) - OPTIONAL</label>
<select name="gender" style="width:100%;padding:12px;margin:6px 0;border-radius:10px;background:#1E1E2A;color:#fff;border:1px solid #8B5CF6">
<option value="">Prefer not to say / Skip (OPTIONAL)</option>
<option value="Synor">Synor - He / Male</option>
<option value="Synra">Synra - She / Female</option>
<option value="Synhen">Synhen - They</option>
</select>
<button type="submit" style="background:#8B5CF6;color:#fff;padding:12px;width:100%;border-radius:20px;border:none">Save</button>
</form>
<a href="/" style="color:#8B5CF6">Back</a>
</body>
"""

@app.route("/")
def home():
    u=User.query.first(); cs=Cipher.query.all()
    return render_template_string(HTML, u=u, cs=cs)
@app.route("/syn/<int:id>")
def syn(id):
    c=Cipher.query.get(id); c.syn+=1; db.session.commit(); return redirect("/")
@app.route("/disyn/<int:id>")
def disyn(id):
    c=Cipher.query.get(id); c.disyn+=1; db.session.commit(); return redirect("/")
@app.route("/forge", methods=["GET","POST"])
def forge():
    u=User.query.first()
    if request.method=="POST":
        u.name=request.form.get("name"); u.handle=request.form.get("handle"); u.gender=request.form.get("gender") or ""; db.session.commit(); return redirect("/")
    return render_template_string(FORGE, u=u)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
