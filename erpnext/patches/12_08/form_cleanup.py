import webnotes

def execute():
	update_comment()
	update_todo()

def update_comment():
	webnotes.conn.sql("""update tabComment set parenttype = comment_doctype,
		parent = comment_docname""")
		
def update_todo():
	webnotes.conn.sql("""update tabToDo set parenttype = reference_type,
		parent = reference_name""")		