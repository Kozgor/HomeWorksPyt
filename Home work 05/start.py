from lib.person import db_manager
from lib.settings import *

test = db_manager(HOST, USERNAME, PASSWORD)
test.menu()