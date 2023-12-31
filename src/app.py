

from setup import app
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp
from blueprints.councils_bp import councils_bp
from blueprints.libraries_bp import libraries_bp
from blueprints.memberships_bp import memberships_bp
from blueprints.holdings_bp import holdings_bp



app.register_blueprint(db_commands)
app.register_blueprint(users_bp)
app.register_blueprint(councils_bp)
app.register_blueprint(memberships_bp)
app.register_blueprint(libraries_bp)
app.register_blueprint(holdings_bp)

print(app.url_map)

