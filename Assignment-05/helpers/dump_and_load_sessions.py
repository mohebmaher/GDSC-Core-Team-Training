def dump_session(name="session", file_path="./assets"):
    from datetime import datetime as dt
    import dill
    current_time = dt.now().strftime('%Y.%m.%d.pkl')
    filename = f"{file_path}/{name}_{current_time}"
    dill.dump_module(filename=filename)
    return filename
    
    
def load_session(filename):
    import dill
    dill.load_module(filename)
    
    