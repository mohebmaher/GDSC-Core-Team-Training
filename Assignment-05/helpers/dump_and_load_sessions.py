def dump_session(name="session", file_path="./assets"):
    from datetime import datetime as dt
    import dill
    current_time = dt.now().strftime('%Y.%m.%d.pkl')
    filename = f"{file_path}/{name}_{current_time}"
    dill.dump_module(filename=filename)
    return filename
    
    
def load_session(filename=None):
    import dill
    if filename is not None:
	try:
    	    dill.load_module(filename)
	except Exception as e:
	    print(e)
    
    