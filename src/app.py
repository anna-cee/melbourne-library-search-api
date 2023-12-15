from main import app
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp
from blueprints.councils_bp import councils_bp
from blueprints.memberships_bp import memberships_bp
from blueprints.librarys_bp import librarys_bp


app.register_blueprint(db_commands)
app.register_blueprint(users_bp)
app.register_blueprint(councils_bp)
app.register_blueprint(memberships_bp)
app.register_blueprint(libraries_bp)

