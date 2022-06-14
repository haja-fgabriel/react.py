from react import use_state, use_effect

def app():
    is_welcome, set_is_welcome = use_state(False)

    def on_loaded():
        set_is_welcome(True)

    counter, set_count = use_state(0)

    use_effect(on_loaded, [])
    
    return f'''
        {is_welcome and '<p>Hello World!</p>'}
        <p>You clicked {counter} times</p>
    '''